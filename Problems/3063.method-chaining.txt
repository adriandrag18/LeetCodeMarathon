# title: Method Chaining
# timestamp: 2025-06-08 02:48:53
# problemUrl: https://leetcode.com/problems/method-chaining/
# memory: 67.4 MB
# runtime: 289 ms

import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals['weight'] > 100].sort_values(by='weight', ascending=False)[['name']]
    