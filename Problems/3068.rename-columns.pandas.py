# title: Rename Columns
# timestamp: 2025-06-08 02:33:17
# problemUrl: https://leetcode.com/problems/rename-columns/
# memory: 66.2 MB
# runtime: 301 ms

import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(columns={
        'id': 'student_id',
        'first': 'first_name',
        'last': 'last_name',
        'age': 'age_in_years'
    })