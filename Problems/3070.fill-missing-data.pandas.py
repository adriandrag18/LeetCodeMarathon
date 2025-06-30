# title: Fill Missing Data
# timestamp: 2025-06-08 02:36:02
# problemUrl: https://leetcode.com/problems/fill-missing-data/
# memory: 66.1 MB
# runtime: 251 ms

import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'].fillna(0, inplace=True)
    return products