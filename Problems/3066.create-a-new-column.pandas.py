# title: Create a New Column
# timestamp: 2025-06-08 01:44:48
# problemUrl: https://leetcode.com/problems/create-a-new-column/
# memory: 66.2 MB
# runtime: 283 ms

import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees