# title: Select Data
# timestamp: 2025-06-08 01:43:32
# problemUrl: https://leetcode.com/problems/select-data/
# memory: 66.9 MB
# runtime: 298 ms

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students['student_id'] == 101][['name', 'age']]