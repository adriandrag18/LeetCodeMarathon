# title: Modify Columns
# timestamp: 2025-06-08 02:29:46
# problemUrl: https://leetcode.com/problems/modify-columns/
# memory: 66.2 MB
# runtime: 232 ms

import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] *= 2
    return employees