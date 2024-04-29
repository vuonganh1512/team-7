import re
import math
import string
import random

class MatrixParser:
  def __init__(self, tracedf):
    self.tracedf = tracedf

  def setTraceData(self, dataframe):
    self.tracedf = dataframe


  

  # Calculates a boolean truth of the property for the trace data given at times T and Z.
  # Assumes that the "T" expression is always on the left side of the operator, and the "Z" expression is always
  # on the right side.
  def parse(self, property, T, Z):
    # Retrieve data rows in the trace file at times T and Z
    Tdata = self.tracedf.iloc[[T]] # iloc here: get row at index
    Zdata = self.tracedf.iloc[[Z]]

    # Convert these to dictionaries, with the keys being the column names, and the values being their values.
    # Assume that the iloc above returned only one dictionary
    Tdict = Tdata.to_dict(orient='records')[0] # https://stackoverflow.com/a/31324373
    Zdict = Zdata.to_dict(orient='records')[0]

    ### Find all the variable expressions, including their names and indexing variables
    vars_dict = {} # The scope dictionary for the variables, which we will fill with random variable names to their values
    
    # Create a dictionary of the entire match, mapped to the match object. This is only done to create a proper set
    # of the matches, without duplicates
    match_dict = {match.group(0): match for match in re.finditer(r'{([A-Za-z0-9|]+)}\[([A-Za-z0-9|])+\]', property)}
    
    # Iteratively replace each kind in the string with a random name, adding this and the actual value of the variable to the dictionary
    for fullmatch in set(match_dict.keys()):
      match = match_dict[fullmatch]
      # Note: match.group(0) is the entire match
      variable_name = match.group(1)
      indexing_variable = match.group(2)

      # https://stackoverflow.com/a/56398787
      alphabet = string.ascii_lowercase + string.ascii_uppercase
      random_name = ''.join(random.choices(alphabet, k=8))  # variable_name + "_" + # Some actual variable names may not be allowed variable names?
      property = property.replace(match.group(0), random_name)
      
      # Add to scope dictionary
      match indexing_variable:
        case 'T':
          vars_dict[random_name] = Tdata[variable_name].values[0] # .values[0]: A Series object with one item is returned, so get this value
        case 'Z':
          vars_dict[random_name] = Zdata[variable_name].values[0]
        case _:
          raise KeyError(f"No such indexing variable '{indexing_variable}' is supported!")
        
    return eval(property, vars_dict, vars_dict)