# title: Get the Size of a DataFrame
# timestamp: 2025-06-08 01:40:44
# problemUrl: https://leetcode.com/problems/get-the-size-of-a-dataframe/
# memory: 66.4 MB
# runtime: 283 ms

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [players.shape[0], players.shape[1]]