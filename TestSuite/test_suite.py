#!/usr/bin/env python3

import numpy as np
import pandas as pd
import sys
import os

from MatrixParser.MatrixParser import MatrixParser

def main(argv):
  #print(os.getcwd())
  #print(os.listdir('.'))
  test_input = input("Test: ")
  trace_input = input("InputID: ")

  input_matrix = pd.read_csv('TestSuite/InputMatrix.csv') # Based on the formulas at time t in the input matrix
  trace_file = pd.read_csv('TestSuite/' + trace_input + '.csv') # IDs correspond to the input ids of InputMatrix Evaluate upon the trace file
  test_matrix = pd.read_csv('TestSuite/TestMatrix.csv') # Both T and Z are given by 
  
  #print(test_matrix[test_matrix.TestName == "ASE1"].Property.iloc[0])

  prop = test_matrix[test_matrix.TestName == test_input].Property.iloc[0]
  mparser = MatrixParser(tracedf = trace_file)
  r = mparser.parse(property = prop, T = 1.4, Z = 2.5)
  print("Parse result: " + str(r))
  #print(trace_file.iloc[[4]].to_dict(orient='records')[0]) # https://stackoverflow.com/a/31324373
  #prop = test_matrix[test_matrix.TestName == "ASE7"].Property
  #prop = str(prop[0])
  #print(prop)
  #expr = prop.replace('{','(').replace('}',')')
  #print(expr)
  
  #print(r)
  #print(prop)
  #print(input_matrix)

  #print(trace_file)


if __name__ == "__main__":
  main(sys.argv)

