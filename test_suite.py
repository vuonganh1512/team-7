#!/usr/bin/env python3

import numpy as np
import pandas as pd
import sys
import os

def main(argv):
  print(os.getcwd())
  print(os.listdir('.'))
  input_matrix = pd.read_csv('CS322-SP2024-Core-main/FullSampleTestANDTrace/InputMatrix.csv') # Based on the formulas at time t in the input matrix
  trace_file = pd.read_csv('CS322-SP2024-Core-main/FullSampleTestANDTrace/1.csv') # IDs correspond to the input ids of InputMatrix Evaluate upon the trace file
  test_matrix = pd.read_csv('CS322-SP2024-Core-main/FullSampleTestANDTrace/TestMatrix.csv') # Both T and Z are given by 
  print(input_matrix)

  print(trace_file)


if __name__ == "__main__":
  main(sys.argv)

