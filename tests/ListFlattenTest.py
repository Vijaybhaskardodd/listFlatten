import unittest
import sys
sys.path.append('../src')
from ListFlatten import flatten

class TestListFlatten(unittest.TestCase):

    def setUp(self):
        pass

    def test_empty_list(self):
        '''Passing empty list and expecting an empty list without exception '''
        input_list=[]
        expected_value = []
        self.assertEqual(flatten(input_list), expected_value)

    def test_simple_list(self):
        ''' Passing simple one dimension list and expecting same list should be return'''
        input_list=[1,2,3]
        expected_value = [1, 2, 3]
        self.assertEqual(flatten(input_list), expected_value)

    def test_hierarchial_list(self):
        '''Passing hierarchical  list and expecting flatten list with same number of items'''
        input_list=[1, [2, 3], [4, 5, 6],6.5, [7], [[8, 9], 9], 10, [20, 30, [40, [50, [60, [70, 80]]]]]]
        expected_value = [1, 2, 3, 4, 5, 6,6.5, 7, 8, 9, 9, 10, 20, 30, 40, 50, 60, 70, 80]
        self.assertEqual(flatten(input_list), expected_value)

    def test_hierarchial_list_with_string(self):
        ''' Passing hierarchical  list with one string item as item
         expecting one dimensional list with same number of items including string item '''
        input_list=[1, [2, 3], [4, 5, 6],"s", [7], [[8, 9], 9], 10, [20, 30, [40, [50, ["60", [70, 80]]]]]]
        expected_value = [1, 2, 3, 4, 5, 6,"s", 7, 8, 9, 9, 10, 20, 30, 40, 50, "60", 70, 80]
        self.assertEqual(flatten(input_list), expected_value)

if __name__ == '__main__':
    unittest.main()
