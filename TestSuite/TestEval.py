import pandas as pd
import numpy as np
import re

def __init__(self, tracedf):
    self.tracedf = tracedf

def setTraceData(self, dataframe):
    self.tracedf = dataframe

def eval(self, inputdf, testdf):
    #Get row of test and column of input
    Tedata = self.tracedf.iloc[[testdf]]
    Trdata = self.tracedf.iloc[inputdf]

    #Use finditer?