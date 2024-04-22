#!/usr/bin/env python3

from MatrixParser import MatrixParser
import numpy as np
import pandas as pd
import csv
import sys
import os

def main(argv):
  input_matrix = pd.read_csv('TestSuite/InputMatrix.csv') # Based on the formulas at time t in the input matrix
  test_matrix = pd.read_csv('TestSuite/TestMatrix.csv') # Both T and Z are given by 
  df_test = test_matrix[test_matrix.TestName == "ASE1"].Property

  cur_test = input("Enter Test: ")
  cur_input = input("Enter InputID: ")
  time_t = input("Enter Time T: ")
  time_z = input("Enter Time Z: ")
  trace_file = pd.read_csv('TestSuite/' + cur_input + '.csv') # IDs correspond to the input ids of InputMatrix Evaluate upon the trace file

  
  print(trace_file.parse(time_t, time_z))
  parse(time_t, time_z)
  print(df_test)


if __name__ == "__main__":
  main(sys.argv)

def parse(T, Z):
  return 0