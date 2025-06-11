# title: Reshape Data: Pivot
# timestamp: 2025-06-08 02:42:40
# problemUrl: https://leetcode.com/problems/reshape-data-pivot/
# memory: 67.4 MB
# runtime: 329 ms

import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index='month', values='temperature', columns='city')