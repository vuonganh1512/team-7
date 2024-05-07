#!/usr/bin/env python3

import numpy as np
import pandas as pd
import sys
import os
from OutputFormatter import update_results_dataframe
from MatrixParser import MatrixParser

# Currently gets the path two levels above the test_suite.py
global PROJECT_ROOT
PROJECT_ROOT = os.path.realpath(__file__).split('/')[:-2]
PROJECT_ROOT = '/'.join(PROJECT_ROOT)
DATAFILES_PATH = PROJECT_ROOT + "/" + "DataFiles"

def process_test_cases(data):
  results = []
  
  # Iterate over each row in the data
  for index, row in data.iterrows():
    test_name = row['TestName']
    constraints = row['Constraints']
    property_test = row['Property']
    
     
    numerical_columns = row[3:]
    passed = evaluate_constraints(numerical_columns, constraints) and evaluate_property(numerical_columns, property_test)
    
    # Record the result of the test case
    results.append((test_name, passed))
  
  return results

def evaluate_constraints(numerical_columns, constraints):
  return True

def evaluate_property(numerical_columns, property_test):
  return True


test_matrix = pd.read_csv(f'{DATAFILES_PATH}/csv/TestMatrix/TestMatrix.csv')

test_results = process_test_cases(test_matrix)

# Display results
for test_name, passed in test_results:
  print(f"Test case '{test_name}': {'True' if passed else 'False'}")
#pd.read_parquet('1__101.parquet', engine='fastparquet')