# title: Drop Duplicate Rows
# timestamp: 2025-06-08 02:27:07
# problemUrl: https://leetcode.com/problems/drop-duplicate-rows/
# memory: 66.9 MB
# runtime: 255 ms

import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=['email'], keep='first')