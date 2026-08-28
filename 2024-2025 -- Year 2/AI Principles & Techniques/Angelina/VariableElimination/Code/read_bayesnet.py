"""
@Author: Joris van Vugt, Moira Berens, Leonieke van den Bulk

Representation of a Bayesian network read in from a .bif file.

"""

import pandas as pd

class BayesNet():
    """
    This class represents a Bayesian network.
    It can read files in a .bif format (if the formatting is
    along the lines of http://www.bnlearn.com/bnrepository/)

    Uses pandas DataFrames for representing conditional probability tables
    """

    # Possible values per variable
    values = {}

    # Probability distributions per variable
    probabilities = {}

    # Parents per variable
    parents = {}

    def __init__(self, filename):
        """
        Construct a bayesian network from a .bif file

        """
        with open(filename, 'r') as file: #open file
            line_number = 0 #start with 0
            for line in file:
                if line.startswith('network'): #if starts with network
                    self.name = ' '.join(line.split()[1:-1]) #save name of network
                elif line.startswith('variable'): 
                    self.parse_variable(line_number, filename) #parse_varible =finds info about variable and saves it
                elif line.startswith('probability'):
                    self.parse_probability(line_number, filename)  #parse_varible =analyse table of probaibilities 
                line_number = line_number + 1

    def parse_probability(self, line_number, filename):
        """
        Parse the probability distribution
        """

        # get line
        line = open(filename, 'r').readlines()[line_number] # get line -with index [line_number] ; this line = probability (Variable | Parent1, Parent2)

        # Find out what variable(s) we are talking about
        variable, parents = self.parse_parents(line) #save variable and parents
        next_line = open(filename, 'r').readlines()[line_number + 1].strip() #read next line to find - word "table" if no parents, -or prob distr (depends on parents)

        # If a variable has no parents, its probabilities start with table
        if next_line.startswith('table'): 
            comma_sep_probs = next_line.split('table')[1].split(';')[0].strip() # next_line.First part of line after table. delete everything after ;
            probs = [float(p) for p in comma_sep_probs.split(',')] #comma_sep_probs to probabilities (floats) ,separated by , 
            df = pd.DataFrame(columns=[variable, 'prob']) #empty df wit 2 cols 
            for value, p in zip(self.values[variable], probs): 
                df.loc[len(df)] = [value, p] #add every value and prob to table
                self.probabilities[variable] = df #probiblity table we get save to self.probabilities
        else:
            #create dataFrame to store the variables
            df = pd.DataFrame(columns=[variable] + parents + ['prob'])

            #loop over the lines until a line is the same as "}" 
            with open(filename, 'r') as file:
                for i in range(line_number + 1):
                    file.readline()
                for line in file:
                    if '}' in line:
                        # Done reading this probability distribution
                        break
                    
                    # Get the values for the parents
                    comma_sep_values = line.split('(')[1].split(')')[0] 
                    values = [v.strip() for v in comma_sep_values.split(',')] #save values of parents (e.g., "(True, False)")

                    # Get the probabilities for the variable
                    comma_sep_probs = line.split(')')[1].split(';')[0].strip()
                    probs = [float(p) for p in comma_sep_probs.split(',')]

                	# Create a row in the df for each value combination
                    for value, p in zip(self.values[variable], probs):
                        df.loc[len(df)] = [value] + values + [p] #for every (val, prob) add row in table df

            self.probabilities[variable] = df #save table or probabilities for current var

    def parse_variable(self, line_number, filename):
        """
        Parse the name of a variable and its possible values
        """
        variable = open(filename, 'r').readlines()[line_number].split()[1] #save variable name (second word of line [line_number])
        line = open(filename, 'r').readlines()[line_number+1] #
        start = line.find('{') + 1
        end = line.find('}')
        values = [value.strip() for value in line[start:end].split(',')] 
        self.values[variable] = values  #next line - distribution in {} and save values of variable in self.values

    def parse_parents(self, line):
        """
        Find out what variables are the parents
        Returns the variable and its parents
        """
        start = line.find('(') + 1
        end = line.find(')')
        variables = line[start:end].strip().split('|')
        variable = variables[0].strip()
        if len(variables) > 1:
            parents = variables[1] 
            self.parents[variable] = [v.strip() for v in parents.split(',')] #if has parents save to parents list [parent,parent] to self.parents
        else:
            self.parents[variable] = [] #if has no parents save []
        return variable, self.parents[variable] 

    @property
    def nodes(self):
        """Returns the names of the variables in the network"""
        return list(self.values.keys())
