import re

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

    # Find the operator in the property string
    op = re.search(r'([<>]|==)', property)
    if op is None:
      raise Exception("No valid operator was present in the property string!")
    op = op.group(0)
    
    # Find expressions on either side of the operator
    Texpr, Zexpr = tuple(property.split(op))
    
    # Clean the expressions, by replacing "{SOMEVAR}[T]" with just "SOMEVAR"
    Texpr = re.sub(r'{([A-Za-z|]+)}\[[A-Za-z|]+\]', '\g<1>', Texpr)
    Zexpr = re.sub(r'{([A-Za-z|]+)}\[[A-Za-z|]+\]', '\g<1>', Zexpr)

    # Evaluate the T and Z parts of the expressions into numerical values,
    # given all the other input variables that we retrieved earlier at times T and Z

    Tresult = eval(Texpr, Tdict, Tdict)
    Zresult = eval(Zexpr, Zdict, Zdict)

    # Compare the resulting T and Z values with the operator we retrieved earlier
    return eval(str(Tresult) + op + str(Zresult))