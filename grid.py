

class Grid:
    def __init__(self, rows, columns):
        if rows < 1:
            raise ValueError('Invalid number of rows')
        if columns < 1:
            raise ValueError('Invalid number of columns')
        self.rows = rows
        self.columns = columns
        self.values = []
        for i in range(rows):
            self.values.append([])
            for j in range(columns):
                self.values[i].append(None)
    def setPosition(self, position, value):
        x, y = position
        if y > self.rows or y < 0:
            raise IndexError('Invalid row.')
        if x > self.columns or x < 0:
            raise IndexError('Invalid column.')
        self.values[x][y] = value
        return self
    def getPosition(self, position):
        x, y = position
        if y > self.rows or y < 0:
            raise IndexError('Invalid row.')
        if x > self.columns or x < 0:
            raise IndexError('Invalid column.')
        return self.values[x][y]
    def getRow(self, row):
        if row > self.rows or row < 0:
            raise IndexError('Invalid row.')
        return self.values[row]
    def setRow(self, row, values):
        if len(values) > self.columns:
            raise ValueError('Length mismatch for row.')
        if row > self.rows or row < 0:
            raise IndexError('Invalid row.')
        self.values[row] = values
        return self
    def getRows(self):
        return self.values
    def getColumn(self, column):
        if column > self.columns or column < 0:
            raise IndexError('Invalid column.')
        colValues = []
        for row in self.values:
            colValues.append(row[column])
        return colValues
    def setColumn(self, column, values):
        if column > self.columns or column < 0:
            raise IndexError('Invalid column.')
        if len(values) > self.rows:
            raise ValueError('Length mismatch for column.')
        for i in range(len(self.values)):
            self.values[i][column] = values[i]
        return self
    def getColumns(self):
        columns = []
        for i in range(self.columns):
            columns.append(self.getColumn(i))
        return columns
    def setIndex(self, index, value):
        if index > self.rows * self.columns or index < 0:
            raise IndexError('Invalid index.')
        y = int(index / self.columns)
        x = index % self.columns
        if y > self.rows or y < 0:
            raise IndexError('Invalid row.')
        if x > self.columns or x < 0:
            raise IndexError('Invalid column.')
        self.values[y][x] = value
        return self
    def getIndex(self, index):
        if index > self.rows * self.columns or index < 0:
            raise IndexError('Invalid index.')
        y = int(index / self.columns)
        x = index % self.columns
        if y > self.rows or y < 0:
            raise IndexError('Invalid row.')
        if x > self.columns or x < 0:
            raise IndexError('Invalid column.')
        return self.values[y][x]
    def fill(self, value):
        for i in range(self.rows):
            for j in range(self.columns):
                self.values[i][j] = value
        return self
    def info(self):
        return {
            'rows': self.rows,
            'columns': self.columns
        }
    def exportGrid(self):
        return self.values
    def importGrid(self, grid):
        if len(grid) != self.rows:
            raise ValueError('Length mismatch for rows.')
        for row in grid:
            if len(row) != self.columns:
                raise ValueError('Length mismatch for columns.')
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                self.setPosition((y, x), cell)
    def exportValues(self):
        values = []
        for row in self.values:
            values.extend(row)
        return values
    def importValues(self, values):
        if len(values) != self.rows * self.columns:
            raise ValueError('Length mismatch for grid')
        for i in range(self.rows):
            self.values[i] = values[i * self.rows:i * self.rows + self.columns]
    def map(self, fn):
        for y, row in enumerate(self.values):
            for x, cell in enumerate(row):
                self.setPosition((y, x), fn(cell, (y, x)))
        return self
    def forEach(self, fn):
        for y, row in enumerate(self.values):
            for x, cell in enumerate(row):
                fn(cell, (y, x))
    def duplicate(self):
        dupeGrid = Grid(self.rows, self.columns)
        dupeGrid.importValues(self.exportValues())
        return dupeGrid
    def contains(self, other, comparator = None):
        contains = True
        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                if comparator != None:
                    if not comparator(self.values[i][j], other.getPosition((i, j))):
                        contains = False
                else:
                    if other.getPosition((i, j)) != None and other.getPosition((i, j)) != self.values[i][j]:
                        contains = False
        return contains
    def reset(self):
        self.fill(None)
        return self


class Grid3x3(Grid):
    def __init__(self):
        super().__init__(3, 3)

