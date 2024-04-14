#!/usr/bin/env python3

import numpy as np
import pandas as pd
import sys
import os

def main(argv):
  input_matrix = pd.read_csv('TestSuite/InputMatrix.csv')
  print(os.getcwd())
  print(input_matrix)


if __name__ == "__main__":
  main(sys.argv)