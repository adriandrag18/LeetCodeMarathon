# title: Change Data Type
# timestamp: 2025-06-08 02:34:30
# problemUrl: https://leetcode.com/problems/change-data-type/
# memory: 66.7 MB
# runtime: 258 ms

import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype('int')
    return students