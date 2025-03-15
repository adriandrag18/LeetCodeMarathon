# title: Design Spreadsheet
# timestamp: 2025-03-15 16:43:11
# problemUrl: https://leetcode.com/problems/design-spreadsheet/
# memory: 23.7 MB
# runtime: 59 ms

class Spreadsheet:

    def __init__(self, rows: int):
        self.map = {}

    def setCell(self, cell: str, value: int) -> None:
        self.map[cell] = value        

    def resetCell(self, cell: str) -> None:
        self.map[cell] = 0

    def getValue(self, formula: str) -> int:
        x, y = formula[1:].split('+')
        # print(x, y, end=' ')
        if x[0].isalpha():
            x = self.map.get(x, 0)
        else:
            x = int(x)
            
        if y[0].isalpha():
            y = self.map.get(y, 0)
        else:
            y = int(y)

        # print(f' = {x + y}')
        return x + y


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)