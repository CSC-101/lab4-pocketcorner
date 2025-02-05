import data
import lab4
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)

    def test_first_element_2(self):
        # write a second test here
        input = [[], []]
        result = lab4.first_element(input)
        expected = []
        self.assertEqual(expected, result)

    # Part 2
    def test_x_coordinate_1(self):
        input = [data.Point(5,8)]
        result = lab4.x_coordinates(input)
        expected = [5]
        self.assertEqual(expected, result)

    def test_x_coordinate_2(self):
        input = [data.Point(6,4), data.Point(2,2049643), data.Point(4,43)]
        result = lab4.x_coordinates(input)
        expected = [6,2,4]
        self.assertEqual(expected, result)

    # Part 3


    # Part 4


    # Part 5


    # Part 6





if __name__ == '__main__':
    unittest.main()
