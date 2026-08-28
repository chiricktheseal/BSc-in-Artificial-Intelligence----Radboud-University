"""
@Author: Joris van Vugt, Moira Berens, Leonieke van den Bulk

Class for the implementation of the variable elimination algorithm.

"""
import pandas as pd
class VariableElimination():

    def __init__(self, network):
        """
        Initialize the variable elimination algorithm with the specified network.
        Add more initializations if necessary.

        """
        self.network = network

    #------------3a
    def factor_reduction(self, factor, evidence):
        """
        Input:
            factor:     table of probabilities
            evidence:   A dictionary of the observed variables {variable: value} #observed
        """
        for variable, value in evidence.items():
            if variable in factor.columns: # check if variable is in the df's columns
                factor = factor[ factor[variable] == value]  #save rows only corresponding to the evidence(when var==val)
                factor = factor.drop(columns=[variable])  # Remove variable column from factor
        return factor
        
    def factor_product(self, factor1, factor2):
        """
        Input:
            factor1, factor2: two factors that need to be combined
        """
        common_vars = list(set(factor1.columns) & set(factor2.columns))
        if common_vars:
            product_factor = pd.merge(factor1, factor2, on=common_vars, how='outer')#merge = common vars with all probabilites(vals)
        else:
            product_factor = pd.concat([factor1, factor2], axis=1)
        
        prob_columns = []
        for col in product_factor.columns:
            if 'prob' in col:
                prob_columns.append(col)

        product_factor['prob'] = product_factor[prob_columns].prod(axis=1) #multiply the probabilities of variables in each row = saves in column prob
        product_factor = product_factor.drop(columns=prob_columns) #delete old cols with probabilities
        return product_factor 

    def factor_marginalization(self, factor, variable):
        """
        Input:
            factor: the factor to exclude the variable from
            variable: a variable for marginalisation
        """
        groupby_columns = []
        for col in factor.columns:
            if col != variable:
                groupby_columns.append(col)
                print(factor.head()) #Why het NAN????????????
                print(factor.columns)
        grouped_factor = factor.groupby(groupby_columns)['prob'].sum()
        marginalized_factor = grouped_factor.reset_index()
        return marginalized_factor
        
    def normalize(self, factor):
        """Normalize probabilities"""
        total_prob = factor['prob'].sum()
        if total_prob != 0:
            factor['prob'] = factor['prob'] / total_prob
        else:
            print("Division by 0")
        return factor
    
    #------------3b
    def initialize_factors(self, observed):
        """Initialize factors considering observed variables"""
        factors = []
        for variable, df in self.network.probabilities.items(): #for each var and its prob
            if variable in observed:
                observed_value = observed[variable] 
                filtered_df = df[ df[variable] == observed_value ] #get rows where var value = observed val
                factors.append(filtered_df) #filtred df to factor list
            else:
                factors.append(df)
        
        return factors
    
    
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
        factors = self.initialize_factors(observed) #1) initialize factors considering observed variables

        for factor in factors:
            factor = self.factor_reduction(factor, observed) #2) factor reduction (filter factors based on evidence)

        if isinstance(elim_order, list):
            elim_order = elim_order #or pass
        else:
            elim_order = elim_order(self.network) #3) call function passed network to it
        
        #4) eliminate variables one by one as per elimination order
        for variable in elim_order:
            if variable == query:
                continue  #kkip  query var
                    
            relevant_factors = []
            for factor in factors:
                if variable in factor.columns:
                    relevant_factors.append(factor) #add factor to list if var is in its column = find all factors involving variable

            if relevant_factors: #if relevant_factors is non empty list
                combined_factor = relevant_factors[0] 
                for f in relevant_factors[1:]:  #each other factor = f
                    combined_factor = self.factor_product(combined_factor, f) #combine_factor = f *combine factor
                
                marginalized_factor = self.factor_marginalization(combined_factor, variable) #marginalize the combined factor over the variable
                
                for f in relevant_factors:
                    factors.remove(f)
                factors.append(marginalized_factor) #remove eliminated factors and add the marginalized factor
                
        #5) after elimination, combine all remaining factors that involve the query variable
        query_factors = []
        for factor in factor:
            if query in factor.columns:
                query_factors.append(factor) #add factor with query 
                
        if query_factors: # if nonempty list
            combined_query_factor = query_factors[0] 
            for f in query_factors[1:]: 
                combined_query_factor = self.factor_product(combined_query_factor, f)#combine_quer_f = f*combined_query
            
            # Normalize the factor to get the final probability distribution
            result_factor = self.normalize(combined_query_factor)
        
        return result_factor
    