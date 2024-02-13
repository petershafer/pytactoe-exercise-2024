import unittest
from grid import Grid, Grid3x3

class TestGridClass(unittest.TestCase):
    def testInstance(self):
        myGrid = Grid(3,3)
        self.assertTrue(isinstance(myGrid, Grid), "Grid() should create a grid instance")
    def testInvalidArguments(self):
        msg = "Grid() should not allow invalid arguments in constructor"
        with self.assertRaises(TypeError, msg=msg):
            Grid()
        with self.assertRaises(TypeError, msg=msg):
            Grid(1)
        with self.assertRaises(TypeError, msg=msg):
            Grid(1, '2')
        with self.assertRaises(TypeError, msg=msg):
            Grid(None, None)
        with self.assertRaises(ValueError, msg=msg):
            Grid(-1, -1)
    def testSetPositionCoords(self):
        myGrid = Grid(3, 3)
        myGrid.setPosition((0, 0), 'x')
        self.assertEqual(myGrid.getPosition((0, 0)), 'x')
        self.assertEqual(myGrid.getIndex(0), 'x')
    def testSetPositionBounds(self):
        msg = "setPosition() should not set values outside of the grid"
        myGrid = Grid(3, 3)
        with self.assertRaises(IndexError, msg=msg):
            myGrid.setPosition((-1, -1), 'x')
        with self.assertRaises(TypeError, msg=msg):
            myGrid.setPosition((0), 'x')
        with self.assertRaises(IndexError, msg=msg):
            myGrid.setPosition((3, 3), 'x')
    def testGetPositionValue(self):
        myGrid = Grid(3, 3)
        myGrid.setPosition((0, 0), 'x')
        self.assertEqual(myGrid.getPosition((0, 0)), 'x', 'getPosition() should get the value at the given coordinates')
    def testGetPositionBounds(self):
        msg = 'getPosition() should not get values outside of the grid'
        myGrid = Grid(3, 3)
        with self.assertRaises(IndexError, msg=msg):
            myGrid.getPosition((-1, -1))
        with self.assertRaises(TypeError, msg=msg):
            myGrid.getPosition((0))
        with self.assertRaises(IndexError, msg=msg):
            myGrid.getPosition((3, 3))
    def testGetRowValues(self):
        myGrid = Grid(3, 3)
        myGrid.setRow(0, [1, 2, 3])
        self.assertEqual(myGrid.getRow(0), [1, 2, 3])
    def testGetRowBounds(self):
        msg = 'getRow() should not set values outside of the grid'
        myGrid = Grid(3, 3)
        with self.assertRaises(IndexError, msg=msg):
            myGrid.getRow(-1)
        with self.assertRaises(TypeError, msg=msg):
            myGrid.getRow('0')
        with self.assertRaises(IndexError, msg=msg):
            myGrid.getRow(3)
    def testSetRowValues(self):
        myGrid = Grid(3, 3)
        myGrid.setRow(0, [1, 2, 3])
        self.assertEqual(myGrid.getRow(0), [1, 2, 3], 'should set the values for the given row')
    def testSetRowBounds(self):
        msg = 'setRow() should not set values outside of the grid'
        myGrid = Grid(3, 3)
        with self.assertRaises(IndexError, msg=msg):
            myGrid.setRow(-1, [1, 2, 3])
        with self.assertRaises(TypeError, msg=msg):
            myGrid.setRow('0', [1, 2, 3])
        with self.assertRaises(IndexError, msg=msg):
            myGrid.setRow(3, [1, 2, 3])
    def testGetRows(self):
        myGrid = Grid(3, 3)
        myGrid.setRow(0, [1, 2, 3])
        myGrid.setRow(1, [4, 5, 6])
        myGrid.setRow(2, [7, 8, 9])
        self.assertEqual(myGrid.getRows(), [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ], 'getRows() should get all values by row')
    def testGetColumnValues(self):
        myGrid = Grid(3, 3)
        myGrid.setColumn(0, [1, 2, 3])
        self.assertEqual(myGrid.getColumn(0), [1, 2, 3], 'getColumn() should get the values for the given column')
    def testGetColumnBounds(self):
        msg = 'getColumn() should not set values outside of the grid'
        myGrid = Grid(3, 3)
        with self.assertRaises(IndexError, msg=msg):
            myGrid.getColumn(-1)
        with self.assertRaises(TypeError, msg=msg):
            myGrid.getColumn('0')
        with self.assertRaises(IndexError, msg=msg):
            myGrid.getColumn(3)
    def testSetColumnValues(self):
        myGrid = Grid(3, 3)
        myGrid.setColumn(0, [1, 2, 3])
        self.assertEqual(myGrid.getColumn(0), [1, 2, 3], 'setColumn() should set the values for the given row')
    def testColumnRowBounds(self):
        msg = 'setColumn() should not set values outside of the grid'
        myGrid = Grid(3, 3)
        with self.assertRaises(IndexError, msg=msg):
            myGrid.setColumn(-1, [1, 2, 3])
        with self.assertRaises(TypeError, msg=msg):
            myGrid.setColumn('0', [1, 2, 3])
        with self.assertRaises(IndexError, msg=msg):
            myGrid.setColumn(3, [1, 2, 3])
    def testGetColumns(self):
        myGrid = Grid(3, 3)
        myGrid.setColumn(0, [1, 2, 3])
        myGrid.setColumn(1, [4, 5, 6])
        myGrid.setColumn(2, [7, 8, 9])
        self.assertEqual(myGrid.getColumns(), [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ], 'getColumns() should get all values by column')
    def testSetIndexValue(self):
        myGrid = Grid(3, 3)
        myGrid.setIndex(0, 'x')
        self.assertEqual(myGrid.getPosition((0, 0)), 'x', 'setIndex() should set the value at the given index')
        self.assertEqual(myGrid.getIndex(0), 'x', 'setIndex() should set the value at the given index')
    def testSetIndexBounds(self):
        msg = 'setIndex() should not set values outside of the grid'
        myGrid = Grid(3, 3)
        with self.assertRaises(IndexError, msg=msg):
            myGrid.setIndex(-1, 'x')
        with self.assertRaises(TypeError, msg=msg):
            myGrid.setIndex('0', 'x')
        with self.assertRaises(IndexError, msg=msg):
            myGrid.setIndex(9, 'x')
    def testGetIndexValue(self):
        myGrid = Grid(3, 3)
        myGrid.setIndex(0, 'x')
        self.assertEqual(myGrid.getPosition((0, 0)), 'x', 'getIndex() should set the value at the given index')
        self.assertEqual(myGrid.getIndex(0), 'x', 'getIndex() should set the value at the given index')
    def testGetIndexBounds(self):
        msg = 'getIndex() should not set values outside of the grid'
        myGrid = Grid(3, 3)
        with self.assertRaises(IndexError, msg=msg):
            myGrid.getIndex(-1)
        with self.assertRaises(TypeError, msg=msg):
            myGrid.getIndex('0')
        with self.assertRaises(IndexError, msg=msg):
            myGrid.getIndex(9)
    def testFillValues(self):
        myGrid = Grid(3, 3)
        myGrid.fill('x')
        self.assertEqual(myGrid.getRows(), [
            ['x', 'x', 'x'],
            ['x', 'x', 'x'],
            ['x', 'x', 'x'],
        ], "fillValues() should apply a single value to every part of the grid.")
    def testGetInfo(self):
        myGrid = Grid(3, 3)
        self.assertEqual(myGrid.info(), {
            "rows": 3,
            "columns": 3
        }, "getInfo() should report the dimensions of the grid.")
    def testExportGrid(self):
        myGrid = Grid(3, 3)
        myGrid.setRow(0, [1, 2, 3])
        myGrid.setRow(1, [4, 5, 6])
        myGrid.setRow(2, [7, 8, 9])
        self.assertEqual(myGrid.exportGrid(), [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ], "exportGrid() should export a 2D list of values representing the grid")
    def testImportGrid(self):
        myGrid = Grid(3, 3)
        myGrid.importGrid([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ])
        self.assertEqual(myGrid.exportGrid(), [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ], "importGrid() should export a 2D list of values representing the grid")
    def testExportValues(self):
        myGrid = Grid(3, 3)
        myGrid.setRow(0, [1, 2, 3])
        myGrid.setRow(1, [4, 5, 6])
        myGrid.setRow(2, [7, 8, 9])
        self.assertEqual(myGrid.exportValues(), [1, 2, 3, 4, 5, 6, 7, 8, 9], "exportValues() should convert the grid into a list of values")
    def testImportValues(self):
        myGrid = Grid(3, 3)
        myGrid.importValues([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(myGrid.exportGrid(), [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ], "importValues() should create a grid from a list")
    def testMapValues(self):
        myGrid = Grid(3, 3)
        myGrid.importValues([1, 2, 3, 4, 5, 6, 7, 8, 9])
        myGrid.map(lambda value, position: 10 - value)
        self.assertEqual(myGrid.exportGrid(), [
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1],
        ], "map() should apply specified function to all values")
    def testMapCoords(self):
        myGrid = Grid(3, 3)
        myGrid.map(lambda value, position: position)
        self.assertEqual(myGrid.exportGrid(), [
            [(0, 0),(0, 1),(0, 2)],
            [(1, 0),(1, 1),(1, 2)],
            [(2, 0),(2, 1),(2, 2)],
        ], "map() should apply specified function with coorect row/col values.")
    def testForEachValues(self):
        myGrid = Grid(3, 3)
        myGrid.importValues([1, 2, 3, 4, 5, 6, 7, 8, 9])
        values = []
        myGrid.forEach(lambda value, position: values.append(value))
        self.assertEqual(values, [1, 2, 3, 4, 5, 6, 7, 8, 9], "forEach() should apply specified function to all values")
    def testForEachCoords(self):
        myGrid = Grid(3, 3)
        positions = []
        myGrid.forEach(lambda value, position: positions.append(position))
        self.assertEqual(positions, [
            (0, 0),(0, 1),(0, 2),
            (1, 0),(1, 1),(1, 2),
            (2, 0),(2, 1),(2, 2),
        ], "forEach() should apply specified function with coorect row/col values.")
    def testDuplicate(self):
        myGrid = Grid(3, 3)
        myGrid.importValues([1, 2, 3, 4, 5, 6, 7, 8, 9])
        newGrid = myGrid.duplicate()
        self.assertNotEqual(myGrid, newGrid, "duplicate() should return a new instance of Grid.")
        self.assertEqual(newGrid.exportGrid(), myGrid.exportGrid(), "duplicate() should create a new grid with the same values.")
    def testContainsSimple(self):
        myGrid = Grid(3, 3)
        myGrid.importValues([1, 2, 3, 4, 5, 6, 7, 8, 9])
        myOtherGrid = Grid(3, 3)
        myOtherGrid.setIndex(0, 1)
        self.assertTrue(myGrid.contains(myOtherGrid), "contains() should return true if a grid is contained")
    def testContainsComparator(self):
        myGrid = Grid(3, 3)
        myGrid.importValues([1, 2, 3, 4, 5, 6, 7, 8, 9])
        myOtherGrid = Grid(3, 3)
        myOtherGrid.fill(None)
        myOtherGrid.setIndex(0, 1)
        def comparator(value, otherValue):
            if otherValue != None:
                return otherValue == value
            return True
        self.assertTrue(myGrid.contains(myOtherGrid, comparator), "contains() should return true if a grid is contained")
    def testContainsMatching(self):
        myGrid = Grid(3, 3)
        myGrid.importValues([1, 2, 3, 4, 5, 6, 7, 8, 9])
        myOtherGrid = Grid(3, 3)
        myOtherGrid.importValues([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertTrue(myGrid.contains(myOtherGrid), "contains() should return true if grids match")
    def testContainsMatchingComparator(self):
        myGrid = Grid(3, 3)
        myGrid.importValues([1, 2, 3, 4, 5, 6, 7, 8, 9])
        myOtherGrid = Grid(3, 3)
        myOtherGrid.importValues(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
        comparator = lambda value, otherValue: int(value) == int(otherValue)
        self.assertTrue(myGrid.contains(myOtherGrid, comparator), "contains() should return true if grids match, using comparator")
    def testContainsNotMatching(self):
        myGrid = Grid(3, 3)
        myGrid.setIndex(0, 0)
        myOtherGrid = Grid(3, 3)
        myOtherGrid.setIndex(0, 0)
        myOtherGrid.setIndex(1, 1)
        self.assertFalse(myGrid.contains(myOtherGrid), "contains() should return false if other grid has more values than this one")
    def testContainsNotMatchingComparator(self):
        myGrid = Grid(3, 3)
        myGrid.setIndex(0, 0)
        myOtherGrid = Grid(3, 3)
        myOtherGrid.fill(None)
        myOtherGrid.setIndex(0, 0)
        myOtherGrid.setIndex(1, 1)
        def comparator(value, otherValue):
            if otherValue != None:
                return otherValue == value
            return True
        self.assertFalse(myGrid.contains(myOtherGrid, comparator), "contains() should return false if other grid has more values than this one, using comparator")
    def testContainsNotMatching2(self):
        myGrid = Grid(3, 3)
        myGrid.importValues([1, 2, 3, 4, 5, 6, 7, 8, 9])
        myOtherGrid = Grid(3, 3)
        myOtherGrid.importValues([9, 8, 7, 6, 5, 4, 3, 2, 1])
        self.assertFalse(myGrid.contains(myOtherGrid), "contains() should return false if grids don't match")
    def testContainsNotMatching2Comparator(self):
        myGrid = Grid(3, 3)
        myGrid.importValues([1, 2, 3, 4, 5, 6, 7, 8, 9])
        myOtherGrid = Grid(3, 3)
        myOtherGrid.fill(None)
        myOtherGrid.importValues([9, 8, 7, 6, 5, 4, 3, 2, 1])
        def comparator(value, otherValue):
            if otherValue != None:
                return otherValue == value
            return True
        self.assertFalse(myGrid.contains(myOtherGrid, comparator), "contains() should return false if grids don't match, using comparator")
    def testReset(self):
        myGrid = Grid(3, 3)
        myGrid.importValues([1, 2, 3, 4, 5, 6, 7, 8, 9])
        myGrid.reset()
        self.assertEqual(myGrid.exportValues(), [None, None, None, None, None, None, None, None, None], "reset() should remove all values from the grid.")

class TestGrid3x3Class(unittest.TestCase):
    def testInstance(self):
        myGrid = Grid3x3()
        myGrid.fill('x')
        self.assertEqual(myGrid.info(), {
            "rows": 3,
            "columns": 3
        }, "Grid3x3() should create a 3 by 3 grid")
        self.assertEqual(myGrid.exportGrid(), [
            ["x", "x", "x"],
            ["x", "x", "x"],
            ["x", "x", "x"]
        ], "Grid3x3() should populate with 9 values in rows of 3")

if __name__ == '__main__':
    unittest.main()
