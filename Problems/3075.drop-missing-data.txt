# title: Drop Missing Data
# timestamp: 2025-06-08 02:29:00
# problemUrl: https://leetcode.com/problems/drop-missing-data/
# memory: 67.1 MB
# runtime: 290 ms

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=['name'])