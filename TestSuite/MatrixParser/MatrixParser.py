class MatrixParser:
  def __init__(self, tracedf):
    self.tracedf = tracedf

  def setTraceData(self, dataframe):
    self.tracedf = dataframe

  def parse(self, T, Z):
    Tdata = self.tracedf[T]
    expr = prop.replace('{','(').replace('}',')')
    r = eval(expr, {}, {"T": T, "Z": Z})