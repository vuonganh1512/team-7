import pandas as pd
from pandas import DataFrame as df
import sys
import os

def main(argv):
  #Printing the file name and input_matrix
  input_matrix = pd.read_csv('TestSuite/InputMatrix.csv')
  print(os.getcwd())
  print(input_matrix)




if __name__ == "__main__":
  main(sys.argv)
