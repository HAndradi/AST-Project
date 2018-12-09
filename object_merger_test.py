import unittest
from object_merger import *

class TestStringMethods(unittest.TestCase):

    def test1_object_merger(self):
        sensor_1 = [('knife',1, 99), ('scissor', 2, 65), ('spoon', 3, 33), ('spoon', 4, 80), ('keys', 5, 95)]
        sensor_2 = [('knife',1, 55), ('scissor', 2, 95), ('fork', 3, 99), ('spoon', 4, 99), ('keys', 5, 95) ]

        expected = [('knife',1, 99), ('scissor', 2, 95), ('fork', 3, 99), ('spoon', 4, 99), ('keys', 5, 95)]
        actual = ObjectListMerger(sensor_1,sensor_2).combined_tuple_list()
        self.assertEqual(len(actual), len(expected))
        for i in actual:
            self.assertIn(i,expected)

    def test2_object_merger(self):
        sensor_1 = [('knife',1, 99), ('scissor', 2, 65), ('spoon', 3, 33), ('spoon', 4, 80), ('keys', 5, 95)]
        sensor_2 = [('keys', 5, 95), ('spoon', 4, 99), ('fork', 3, 99), ('scissor', 2, 95), ('knife',1, 55)]

        expected = [('knife',1, 99), ('scissor', 2, 95), ('fork', 3, 99), ('spoon', 4, 99), ('keys', 5, 95)]
        actual = ObjectListMerger(sensor_1,sensor_2).combined_tuple_list()
        self.assertEqual(len(actual), len(expected))
        for i in actual:
            self.assertIn(i,expected)

    def test3_object_merger(self):
        sensor_1 = []
        sensor_2 = []

        expected = []
        actual = ObjectListMerger(sensor_1,sensor_2).combined_tuple_list()
        self.assertEqual(len(actual), len(expected))
        for i in actual:
            self.assertIn(i,expected)

    def test4_object_merger(self):
        sensor_1 = [('knife',1, 99), ('scissor', 2, 65), ('spoon', 3, 33)]
        sensor_2 = []

        expected = [('knife',1, 99), ('scissor', 2, 65), ('spoon', 3, 33)]
        actual = ObjectListMerger(sensor_1,sensor_2).combined_tuple_list()
        self.assertEqual(len(actual), len(expected))
        for i in actual:
            self.assertIn(i,expected)

    def test5_object_merger(self):
        sensor_1 = [('knife',1, 99), ('scissor', 2, 65), ('spoon', 3, 33)]
        sensor_2 = [('KNIFE',1, 99), ('SCISSOR', 2, 65), ('SPOON', 3, 33)]

        expected = [('knife',1, 99), ('scissor', 2, 65), ('spoon', 3, 33)]
        actual = ObjectListMerger(sensor_1,sensor_2).combined_tuple_list()
        self.assertEqual(len(actual), len(expected))
        for i in actual:
            self.assertIn(i,expected)

    def test6_object_merger(self):
        sensor_1 = [('knife',1, 99), ('scissor', 2, 65)]
        sensor_2 = [('fork', 3, 99), ('spoon', 4, 99)]

        expected = [('knife',1, 99), ('scissor', 2, 65), ('fork', 3, 99), ('spoon', 4, 99)]
        actual = ObjectListMerger(sensor_1,sensor_2).combined_tuple_list()
        self.assertEqual(len(actual), len(expected))
        for i in actual:
            self.assertIn(i,expected)

    def test7_object_merger(self):
        sensor_1 = [('knife',1, 94),('knife',1, 69),('knife',1, 89)]
        sensor_2 = [('knife',1, 99),('fork', 3, 99)]

        expected = [('knife',1, 99), ('fork', 3, 99)]
        actual = ObjectListMerger(sensor_1,sensor_2).combined_tuple_list()
        self.assertEqual(len(actual), len(expected))
        for i in actual:
            self.assertIn(i,expected)

    def test8_object_merger(self):
        sensor_1 = [('knife',1, 89)]
        sensor_2 = [('knife',1, 35)]
        sensor_3 = [('knife',1, 69)]
        sensor_4 = [('knife',1, 80)]

        expected = [('knife',1, 89)]
        actual = ObjectListMerger(sensor_1,sensor_2,sensor_3,sensor_4).combined_tuple_list()
        self.assertEqual(len(actual), len(expected))
        for i in actual:
            self.assertIn(i,expected)

if __name__ == '__main__':
    unittest.main()
