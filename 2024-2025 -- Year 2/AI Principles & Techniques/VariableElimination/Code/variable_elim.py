"""
@Author: Joris van Vugt, Moira Berens, Leonieke van den Bulk

Class for the implementation of the variable elimination algorithm.

"""

import pandas as pd
from datetime import datetime

class VariableElimination():

    def __init__(self, network):
        """
        Initialize the variable elimination algorithm with the specified network.
        Add more initializations if necessary.

        """
        self.network = network

    def run(self, query, observed, elim_order):
        """
        Use the variable elimination algorithm to find out the probability
        distribution of the query variable given the observed variables

        Input:
            query:      The query variable #Q
            observed:   A dictionary of the observed variables {variable: value} #evidence #e
            elim_order: Either a list specifying the elimination ordering 
                        or a function that will determine an elimination ordering
                        given the network during the run

        Output: A variable holding the probability distribution
                for the query variable

        """
        
        # getting the current time to append to the log files name (to identify when the program was run)
        current_time = datetime.now()
        format_1 = current_time.strftime("%H-%M")
        format_2 = current_time.strftime("%H:%M:%S")
        
        file_name = "VariableEliminationLog_" + format_1
        
        # Writing the key data points in the log file
        f = open(file_name, "w")
        f.write("Variable Elimination - Log\n\n\n")
        f.write("Run at " + format_2 + "\n\n")
        f.write("Nodes: " + str(self.network.nodes) + "\n")
        f.write("Query: " + query + "\n")
        f.write("Evidence: " + str(observed) + "\n")
        f.write("Elimination order: " + str(elim_order) + "\n")
        f.write("\n\n\n")
        
        # Initialize the factors and add them to the log
        f.write("Initial Factors: \n\n")
        initialized_factors = list(self.network.probabilities.values())
        for i in initialized_factors:
            f.write(str(i) + "\n\n")
        
        
        ########## Reduce the factors based on the evidence and add it to the log ##########
        new_factors = {}
        for factor_key, factor_val in self.network.probabilities.items():
            new_factors[factor_key] = self.factor_reduction(factor_val, observed)
        
        f.write("\nUpdated Factors: \n\n")
        updated_factors = list(new_factors.values())
        for i in updated_factors:
            f.write(str(i) + "\n\n")
            
        
        ########## Multiply and marginalize the factors ##########
        f.write("Multiplying and marginalizing factors: \n\n")
        factors_after_multiplying = new_factors.copy()
        
        for var in elim_order:
            
            f.write("The variable considered is: " + str(var) + "\n")
            factors_to_multiply = []
            
            for factor_key in new_factors.keys():
                if var in new_factors[factor_key].columns:
                    factors_to_multiply.append(new_factors[factor_key])
                    del factors_after_multiplying[factor_key]
            
            # Check if there are factors to be multiplied
            if len(factors_to_multiply) == 0:
                f.write("No factors to multiply\n\n")
                continue
            elif len(factors_to_multiply) == 1:
                f.write("Only one factor to multiply -> factor does not change\n\n")
            else:
                product_factor = factors_to_multiply[0]
                for factor in factors_to_multiply[1:]:
                    product_factor = self.factor_product(product_factor, factor)
                
                # Apply marginalization
                product_factor = self.factor_marginalization(product_factor, var)
                
                factors_after_multiplying["Muliplied and Marginalized Factor"] = product_factor
                
                f.write("New factors: \n\n")
                for i in factors_after_multiplying.values():
                    f.write(str(i) + "\n\n")
        
        
        f.write("\nOverview of the factors after multiplying and marginalization is done: \n\n")
        for i in factors_after_multiplying.values():
            f.write(str(i) + "\n\n")
        
        
        ########## Calculate the final factor by multiplying the remaining ones ##########
        f.write("Final Factor: \n\n")
        
        final_factors = []
        for factor_val in factors_after_multiplying.values():
            final_factors.append(factor_val)
            
        final_factor = final_factors[0]
        for factor in final_factors[1:]:
            final_factor = self.factor_product(final_factor, factor)
        
        
        ########## Normalize the factor ##########
        final_factor['prob'] /= final_factor['prob'].sum()
        
        f.write(str(final_factor))
        print("\n\nFinal factor:")
        print(str(final_factor))
        
        f.close()
        
        
        
    
    def factor_reduction(self, factor, evidence):
        """
        Reduce a factor by applying evidence
        Every row in a dataframe that is not in accordance with the evidence is cut
        """
        for var, val in evidence.items():
            if var in factor.columns:
                factor = factor[factor[var] == val]
        return factor
    
    def factor_product(self, factor1, factor2):
        """
        Multiplies two dataframes and merges them into one dataframe
        """
        
        columns_in_both_factors = list(set(factor1.columns) & set(factor2.columns))
        
        if 'prob' in columns_in_both_factors:
            columns_in_both_factors.remove('prob')
        
        # Handle two dataframes with no common columns
        if not columns_in_both_factors:
            factor1['key'] = 1
            factor2['key'] = 1
            new_frame = pd.merge(factor1, factor2, on='key').drop('key', axis=1)
        else:
            new_frame = pd.merge(factor1, factor2, on=columns_in_both_factors, how='outer')
        
        new_frame['prob'] = new_frame['prob_x'] * new_frame['prob_y']
        new_frame.drop(['prob_x', 'prob_y'], axis=1, inplace=True)
        return new_frame
    

    
    def factor_marginalization(self, factor, variable):
        """
        Marginalizes two given dataframes into one
        """
        
        remaining_columns = []
        for col in factor.columns:
            if col != variable and col!= 'prob':
                remaining_columns.append(col)
        
        marginalized_factor = factor.groupby(remaining_columns, as_index = False)['prob'].sum()
        return marginalized_factor
        




