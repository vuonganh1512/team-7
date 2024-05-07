import pandas as pd


# Updates a save dictionary in the nested form: test_name --> trace_id --> 'result' (literal key; to allow flexibility with storing multiple possible attributes)
# "property" is optional at this point, and will be saved along with the result if specified
def update_results_dataframe(test_name: str, trace_id: str, result: bool, property = None, df: pd.DataFrame = None):
  if df is None:
    df = pd.DataFrame({'TestName': [], 'TraceId': [], 'Result': [], 'Property': []})
  data = {'TestName': test_name, 'TraceId': trace_id, 'Result': result, 'Property': property}
  df.append(data)
  return data
