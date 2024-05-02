#!/usr/bin/env python3

from TestSuite.MatrixParser import MatrixParser
import pandas as pd
import os

PROJECT_ROOT = os.path.realpath(__file__).split('/')[:-2]
PROJECT_ROOT = '/'.join(PROJECT_ROOT)
DATAFILES_PATH = PROJECT_ROOT + "/" + "DataFiles"

def test_correct_time_lookup():
  # {Y}[T] == {X1}[Z] / 2
  # Property for ASE3: {Y}[T] == 0
  df = pd.read_csv(DATAFILES_PATH + "/csv/Tracefile/1.csv")
  test_matrix = pd.read_csv(DATAFILES_PATH + "/csv/TestMatrix/TestMatrix.csv")
  prop = test_matrix[test_matrix.TestName == "ASE3"]['Property'].array[0]

  parser = MatrixParser(tracedf = df)
  result = parser.parse(property = prop, T = 22, Z = 0)
  assert result == False
  result = parser.parse(property = prop, T = 5, Z = 0)
  assert result == True
  


def main():
  test_correct_time_lookup()


if __name__ == "__main__":
  main()