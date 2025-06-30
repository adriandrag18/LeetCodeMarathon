# title: Reshape Data: Concatenate
# timestamp: 2025-06-08 02:39:03
# problemUrl: https://leetcode.com/problems/reshape-data-concatenate/
# memory: 66.8 MB
# runtime: 300 ms

import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2], axis=0, ignore_index=True)