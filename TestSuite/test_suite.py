import pandas as pd
from pandas import DataFrame as df
import sys
import os

def main(argv):
  #Printing the file name and input_matrix
  trace_file1 = pd.read_csv('CS322-SP2024-Core-main/FullSampleTestANDTrace/101.csv')
  main_TFile = df(trace_file1)
  
  print(os.getcwd())
  print(main_TFile)



if __name__ == "__main__":
  main(sys.argv)
