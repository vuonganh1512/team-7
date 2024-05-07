#!/usr/bin/env python3
# CONSIDER PYTEST
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
  
  # For a given test, run each "trued" tracefile id. For each of these, given the input id from the input matrix (given by the trace files

  # Trace file and input id are given by the "trues" in the testmatrix.
  # In the trace files, we should look at the rows corresponding to the given times (not row #)

  # for each ct in the testmatrix, load the trace file, starting variable is the input matrix at given input ids, with the input id trace file. A0_1 -> test with input id 1
  # we are generating summary ex: AT and CT

  # test matrix is user input. run it all at t = 100 by default and z = 0
  # generate at, ct, and ts




  parser = MatrixParser(tracedf = df)
  result = parser.parse(property = prop, T = 22, Z = 0)
  assert result == False
  result = parser.parse(property = prop, T = 5, Z = 0)
  assert result == True
  


def main():
  test_correct_time_lookup()


if __name__ == "__main__":
  main()