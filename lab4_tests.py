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
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)

        # write a second test here
    def test_first_element_2(self):
        input = [[], []]
        result = lab4.first_element(input)
        expected = []
        self.assertEqual(expected, result)


    # Part 4
    def test_distance_1(self):
        input = (data.Point(-6,4),data.Point(2,7))
        result = lab4.distance(input)
        expected = 8.544
        self.assertEqual(expected, result)

    # write a second test here
    def test_distance_2(self):
        input = (data.Point(1,-1), data.Point(0,0))
        result = lab4.distance(input)
        expected = 1
        self.assertEqual(expected, result)


    # Part 5
    def test_manhattan_distance_1(self):
        input = (data.Point(-6,4), data.Point(2,7))
        result = lab4.manhattan_distance(input)
        expected = 11.0
        self.assertEqual(expected, result)

    def test_manhattan_distance_2(self):
        # write a second test here
        input = (data.Point(1,-1), data.Point(0,0))
        result = lab4.manhattan_distance(input)
        expected = 2
        self.assertEqual(expected, result)

    # Part 6
    def test_distance_all_1(self):
        input = [data.Point(-6,4), data.Point(2,-2049643), data.Point(4,43)]
        result = lab4.distance_all(input)
        expected = [7.211102550927978, 2049643.0000009758, 43.18564576337837]
        self.assertEqual(expected, result)

    def test_distance_all_2(self):
        # write a second test here
        input = [data.Point(0,0), data.Point(1,1), data.Point(0,0)]
        result = lab4.distance_all(input)
        expected = [0.0, 1.4142135623730951, 0.0]
        self.assertEqual(expected, result)




if __name__ == '__main__':
    unittest.main()

