#!/usr/bin/env python3

import numpy as np
import pandas as pd
import sys
import os

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


input_matrix = pd.read_csv('FullSampleTestANDTrace\TestMatrix.csv')

test_results = process_test_cases(input_matrix)

# Display results
for test_name, passed in test_results:
    print(f"Test case '{test_name}': {'True' if passed else 'False'}")
