import unittest
from object_merger import *

class TestStringMethods(unittest.TestCase):
    SENSOR_1 = [('knife',1, 99), ('scissor', 2, 65), ('spoon', 3, 33), ('spoon', 4, 80), ('keys', 5, 95)]
    SENSOR_2 = [('knife',1, 55), ('scissor', 2, 95), ('fork', 3, 99), ('spoon', 4, 99), ('keys', 5, 95) ]

    def test_object_merger(self):
        expected = [('knife',1, 99), ('scissor', 2, 95), ('fork', 3, 99), ('spoon', 4, 99), ('keys', 5, 95)]
        actual = ObjectListMerger(self.SENSOR_1,self.SENSOR_2).combined_tuple_list()
        self.assertEqual(len(actual), len(expected))
        for i in actual:
            self.assertIn(i,expected)

if __name__ == '__main__':
    unittest.main()
