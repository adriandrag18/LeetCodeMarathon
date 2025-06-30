# title: Reshape Data: Melt
# timestamp: 2025-06-08 02:44:05
# problemUrl: https://leetcode.com/problems/reshape-data-melt/
# memory: 66.8 MB
# runtime: 308 ms

import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame: 
    return pd.melt(report, id_vars=['product'], 
                 value_vars=['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'],
                 var_name='quarter', value_name='sales')