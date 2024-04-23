#!/usr/bin/env python3

from MatrixParser.MatrixParser import MatrixParser
import numpy as np
import pandas as pd
import csv
import sys
import os

def main(argv):
  

  input_matrix = pd.read_csv('TestSuite/InputMatrix.csv') # Based on the formulas at time t in the input matrix
  test_matrix = pd.read_csv('TestSuite/TestMatrix.csv') # Both T and Z are given by 
  

  cur_test = input("Enter Test: ")
  cur_input = input("Enter InputID: ")
  #time_t = input("Enter Time T: ")
  #time_z = input("Enter Time Z: ")

  df_test = test_matrix[test_matrix.TestName == cur_test].Property[0]
  
  trace_file = pd.read_csv('TestSuite/' + cur_input + '.csv') # IDs correspond to the input ids of InputMatrix Evaluate upon the trace filec

  matrix = MatrixParser(trace_file)
  print(matrix.parse(df_test, 0.0322235411435365, 0.122627636858503))
  

if __name__ == "__main__":
  main(sys.argv)