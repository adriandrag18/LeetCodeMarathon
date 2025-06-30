# title: Display the First Three Rows
# timestamp: 2025-06-08 01:41:20
# problemUrl: https://leetcode.com/problems/display-the-first-three-rows/
# memory: 66.4 MB
# runtime: 288 ms

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)