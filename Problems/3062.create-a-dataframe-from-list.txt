# title: Create a DataFrame from List
# timestamp: 2025-06-08 01:38:44
# problemUrl: https://leetcode.com/problems/create-a-dataframe-from-list/
# memory: 65.9 MB
# runtime: 273 ms

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=['student_id', 'age'])