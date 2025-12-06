#!/usr/bin/python3
# test_square.py
"""Defines unittests for models/square.py.
Unittest classes:
    TestSquare_instantiation - line 24
    TestSquare_size - line 88
    TestSquare_x - line 166
    TestSquare_y - line 238
    TestSquare_order_of_initialization - line 306
    TestSquare_area - line 322
    TestSquare_stdout - line 343
    TestSquare_update_args - line 426
    TestSquare_update_kwargs - line 538
    TestSquare_to_dictionary - 640
"""
import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Square class."""

    def test_is_base(self):
        """test_is_base - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_is_base - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        self.assertIsInstance(Square(10), Base)

    def test_is_rectangle(self):
        """test_is_rectangle - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_is_rectangle - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        self.assertIsInstance(Square(10), Square)

    def test_no_args(self):
        """test_no_args - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_no_args - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        """test_one_arg - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_one_arg - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        """test_two_args - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_two_args - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        """test_three_args - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_three_args - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s1 = Square(10, 2, 2)
        s2 = Square(2, 2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        """test_four_args - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_four_args - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_more_than_four_args(self):
        """test_more_than_four_args - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_more_than_four_args - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size_private(self):
        """test_size_private - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_size_private - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def test_size_getter(self):
        """test_size_getter - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_size_getter - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def test_size_setter(self):
        """test_size_setter - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_size_setter - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.size)

    def test_width_getter(self):
        """test_width_getter - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_width_getter - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.width)

    def test_height_getter(self):
        """test_height_getter - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_height_getter - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.height)

    def test_x_getter(self):
        """test_x_getter - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_x_getter - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        self.assertEqual(0, Square(10).x)

    def test_y_getter(self):
        """test_y_getter - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_y_getter - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        self.assertEqual(0, Square(10).y)


class TestSquare_size(unittest.TestCase):
    """Unittests for testing size initialization of the Square class."""

    def test_None_size(self):
        """test_None_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_None_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_str_size(self):
        """test_str_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_str_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid")

    def test_float_size(self):
        """test_float_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_float_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5)

    def test_complex_size(self):
        """test_complex_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_complex_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(5))

    def test_dict_size(self):
        """test_dict_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_dict_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 1, "b": 2}, 2)

    def test_bool_size(self):
        """test_bool_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_bool_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True, 2, 3)

    def test_list_size(self):
        """test_list_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_list_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3])

    def test_set_size(self):
        """test_set_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_set_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3}, 2)

    def test_tuple_size(self):
        """test_tuple_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_tuple_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3), 2, 3)

    def test_frozenset_size(self):
        """test_frozenset_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_frozenset_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({1, 2, 3, 1}))

    def test_range_size(self):
        """test_range_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_range_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(5))

    def test_bytes_size(self):
        """test_bytes_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_bytes_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'Python')

    def test_bytearray_size(self):
        """test_bytearray_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_bytearray_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(b'abcdefg'))

    def test_memoryview_size(self):
        """test_memoryview_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_memoryview_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(b'abcdefg'))

    def test_inf_size(self):
        """test_inf_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_inf_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))

    def test_nan_size(self):
        """test_nan_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_nan_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    # Test size values
    def test_negative_size(self):
        """test_negative_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_negative_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)

    def test_zero_size(self):
        """test_zero_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_zero_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)


class TestSquare_x(unittest.TestCase):
    """Unittests for testing initialization of Square x attribute."""

    def test_None_x(self):
        """test_None_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_None_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)

    def test_str_x(self):
        """test_str_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_str_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid")

    def test_float_x(self):
        """test_float_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_float_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 5.5)

    def test_complex_x(self):
        """test_complex_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_complex_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, complex(5))

    def test_dict_x(self):
        """test_dict_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_dict_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {"a": 1, "b": 2}, 2)

    def test_bool_x(self):
        """test_bool_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_bool_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, True)

    def test_list_x(self):
        """test_list_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_list_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [1, 2, 3])

    def test_set_x(self):
        """test_set_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_set_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {1, 2, 3})

    def test_tuple_x(self):
        """test_tuple_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_tuple_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, (1, 2, 3))

    def test_frozenset_x(self):
        """test_frozenset_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_frozenset_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, frozenset({1, 2, 3, 1}))

    def test_range_x(self):
        """test_range_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_range_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, range(5))

    def test_bytes_x(self):
        """test_bytes_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_bytes_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, b'Python')

    def test_bytearray_x(self):
        """test_bytearray_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_bytearray_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, bytearray(b'abcdefg'))

    def test_memoryview_x(self):
        """test_memoryview_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_memoryview_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, memoryview(b'abcedfg'))

    def test_inf_x(self):
        """test_inf_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_inf_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('inf'), 2)

    def test_nan_x(self):
        """test_nan_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_nan_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('nan'), 2)

    def test_negative_x(self):
        """test_negative_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_negative_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1, 0)


class TestSquare_y(unittest.TestCase):
    """Unittests for testing initialization of Square y attribute."""

    def test_None_y(self):
        """test_None_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_None_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, None)

    def test_str_y(self):
        """test_str_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_str_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, "invalid")

    def test_float_y(self):
        """test_float_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_float_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, 5.5)

    def test_complex_y(self):
        """test_complex_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_complex_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, complex(5))

    def test_dict_y(self):
        """test_dict_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_dict_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {"a": 1, "b": 2})

    def test_list_y(self):
        """test_list_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_list_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, [1, 2, 3])

    def test_set_y(self):
        """test_set_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_set_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {1, 2, 3})

    def test_tuple_y(self):
        """test_tuple_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_tuple_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, (1, 2, 3))

    def test_frozenset_y(self):
        """test_frozenset_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_frozenset_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, frozenset({1, 2, 3, 1}))

    def test_range_y(self):
        """test_range_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_range_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, range(5))

    def test_bytes_y(self):
        """test_bytes_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_bytes_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, b'Python')

    def test_bytearray_y(self):
        """test_bytearray_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_bytearray_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, bytearray(b'abcdefg'))

    def test_memoryview_y(self):
        """test_memoryview_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_memoryview_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, memoryview(b'abcedfg'))

    def test_inf_y(self):
        """test_inf_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_inf_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, float('inf'))

    def test_nan_y(self):
        """test_nan_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_nan_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, float('nan'))

    def test_negative_y(self):
        """test_negative_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_negative_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 0, -1)


class TestSquare_order_of_initialization(unittest.TestCase):
    """Unittests for testing order of Square attribute initialization."""

    def test_size_before_x(self):
        """test_size_before_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_size_before_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", "invalid x")

    def test_size_before_y(self):
        """test_size_before_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_size_before_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", 1, "invalid y")

    def test_x_before_y(self):
        """test_x_before_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_x_before_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid x", "invalid y")


class TestSquare_area(unittest.TestCase):
    """Unittests for testing the area method of the Square class."""

    def test_area_small(self):
        """test_area_small - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_area_small - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        self.assertEqual(100, Square(10, 0, 0, 1).area())

    def test_area_large(self):
        """test_area_large - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_area_large - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999999998000000000000000001, s.area())

    def test_area_changed_attributes(self):
        """test_area_changed_attributes - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_area_changed_attributes - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(2, 0, 0, 1)
        s.size = 7
        self.assertEqual(49, s.area())

    def test_area_one_arg(self):
        """test_area_one_arg - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_area_one_arg - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            s.area(1)


class TestSquare_stdout(unittest.TestCase):
    """Unittests for testing __str__ and display methods of Square class."""

    @staticmethod
    def capture_stdout(sq, method):
        """Captures and returns text printed to stdout.
        Args:
            sq (Square): The Square ot print to stdout.
            method (str): The method to run on sq.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_str_method_print_size(self):
        """test_str_method_print_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_str_method_print_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(4)
        capture = TestSquare_stdout.capture_stdout(s, "print")
        correct = "[Square] ({}) 0/0 - 4\n".format(s.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_size_x(self):
        """test_str_method_size_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_str_method_size_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(5, 5)
        correct = "[Square] ({}) 5/0 - 5".format(s.id)
        self.assertEqual(correct, s.__str__())

    def test_str_method_size_x_y(self):
        """test_str_method_size_x_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_str_method_size_x_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(7, 4, 22)
        correct = "[Square] ({}) 4/22 - 7".format(s.id)
        self.assertEqual(correct, str(s))

    def test_str_method_size_x_y_id(self):
        """test_str_method_size_x_y_id - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_str_method_size_x_y_id - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(2, 88, 4, 19)
        self.assertEqual("[Square] (19) 88/4 - 2", str(s))

    def test_str_method_changed_attributes(self):
        """test_str_method_changed_attributes - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_str_method_changed_attributes - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(7, 0, 0, [4])
        s.size = 15
        s.x = 8
        s.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15", str(s))

    def test_str_method_one_arg(self):
        """test_str_method_one_arg - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_str_method_one_arg - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.__str__(1)

    # Test display method
    def test_display_size(self):
        """test_display_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_display_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(2, 0, 0, 9)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        self.assertEqual("##\n##\n", capture.getvalue())

    def test_display_size_x(self):
        """test_display_size_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_display_size_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(3, 1, 0, 18)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        self.assertEqual(" ###\n ###\n ###\n", capture.getvalue())

    def test_display_size_y(self):
        """test_display_size_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_display_size_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(4, 0, 1, 9)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        display = "\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_size_x_y(self):
        """test_display_size_x_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_display_size_x_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(2, 3, 2, 1)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        display = "\n\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        """test_display_one_arg - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_display_one_arg - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(3, 4, 5, 2)
        with self.assertRaises(TypeError):
            s.display(1)


class TestSquare_update_args(unittest.TestCase):
    """Unittests for testing update args method of the Square class."""

    def test_update_args_zero(self):
        """test_update_args_zero - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_zero - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_update_args_one(self):
        """test_update_args_one - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_one - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        s.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(s))

    def test_update_args_two(self):
        """test_update_args_two - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_two - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))

    def test_update_args_three(self):
        """test_update_args_three - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_three - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(s))

    def test_update_args_four(self):
        """test_update_args_four - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_four - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_update_args_more_than_four(self):
        """test_update_args_more_than_four - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_more_than_four - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_update_args_width_setter(self):
        """test_update_args_width_setter - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_width_setter - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual(2, s.width)

    def test_update_args_height_setter(self):
        """test_update_args_height_setter - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_height_setter - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual(2, s.height)

    def test_update_args_None_id(self):
        """test_update_args_None_id - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_None_id - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        s.update(None)
        correct = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_args_None_id_and_more(self):
        """test_update_args_None_id_and_more - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_None_id_and_more - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        s.update(None, 4, 5)
        correct = "[Square] ({}) 5/10 - 4".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_args_twice(self):
        """test_update_args_twice - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_twice - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        s.update(4, 3, 2, 89)
        self.assertEqual("[Square] (4) 2/89 - 3", str(s))

    def test_update_args_invalid_size_type(self):
        """test_update_args_invalid_size_type - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_invalid_size_type - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid")

    def test_update_args_size_zero(self):
        """test_update_args_size_zero - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_size_zero - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, 0)

    def test_update_args_size_negative(self):
        """test_update_args_size_negative - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_size_negative - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, -4)

    def test_update_args_invalid_x(self):
        """test_update_args_invalid_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_invalid_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(89, 1, "invalid")

    def test_update_args_x_negative(self):
        """test_update_args_x_negative - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_x_negative - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(98, 1, -4)

    def test_update_args_invalid_y(self):
        """test_update_args_invalid_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_invalid_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(89, 1, 2, "invalid")

    def test_update_args_y_negative(self):
        """test_update_args_y_negative - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_y_negative - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(98, 1, 2, -4)

    def test_update_args_size_before_x(self):
        """test_update_args_size_before_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_size_before_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid", "invalid")

    def test_update_args_size_before_y(self):
        """test_update_args_size_before_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_size_before_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid", 2, "invalid")

    def test_update_args_x_before_y(self):
        """test_update_args_x_before_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_x_before_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(89, 1, "invalid", "invalid")


class TestSquare_update_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of Square class."""

    def test_update_kwargs_one(self):
        """test_update_kwargs_one - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_kwargs_one - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        s.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(s))

    def test_update_kwargs_two(self):
        """test_update_kwargs_two - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_kwargs_two - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        s.update(size=1, id=2)
        self.assertEqual("[Square] (2) 10/10 - 1", str(s))

    def test_update_kwargs_three(self):
        """test_update_kwargs_three - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_kwargs_three - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        s.update(y=1, size=3, id=89)
        self.assertEqual("[Square] (89) 10/1 - 3", str(s))

    def test_update_kwargs_four(self):
        """test_update_kwargs_four - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_kwargs_four - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        s.update(id=89, x=1, y=3, size=4)
        self.assertEqual("[Square] (89) 1/3 - 4", str(s))

    def test_update_kwargs_width_setter(self):
        """test_update_kwargs_width_setter - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_kwargs_width_setter - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=8)
        self.assertEqual(8, s.width)

    def test_update_kwargs_height_setter(self):
        """test_update_kwargs_height_setter - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_kwargs_height_setter - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=9)
        self.assertEqual(9, s.height)

    def test_update_kwargs_None_id(self):
        """test_update_kwargs_None_id - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_kwargs_None_id - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        s.update(id=None)
        correct = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_None_id_and_more(self):
        """test_update_kwargs_None_id_and_more - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_kwargs_None_id_and_more - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        s.update(id=None, size=7, x=18)
        correct = "[Square] ({}) 18/10 - 7".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_twice(self):
        """test_update_kwargs_twice - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_kwargs_twice - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        s.update(id=89, x=1)
        s.update(y=3, x=15, size=2)
        self.assertEqual("[Square] (89) 15/3 - 2", str(s))

    def test_update_kwargs_invalid_size(self):
        """test_update_kwargs_invalid_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_kwargs_invalid_size - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="invalid")

    def test_update_kwargs_size_zero(self):
        """test_update_kwargs_size_zero - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_kwargs_size_zero - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=0)

    def test_update_kwargs_size_negative(self):
        """test_update_kwargs_size_negative - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_kwargs_size_negative - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=-3)

    def test_update_kwargs_invalid_x(self):
        """test_update_kwargs_invalid_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_kwargs_invalid_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        """test_update_kwargs_x_negative - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_kwargs_x_negative - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-5)

    def test_update_kwargs_invalid_y(self):
        """test_update_kwargs_invalid_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_kwargs_invalid_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        """test_update_kwargs_y_negative - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_kwargs_y_negative - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(y=-5)

    def test_update_args_and_kwargs(self):
        """test_update_args_and_kwargs - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_and_kwargs - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        s.update(89, 2, y=6)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))

    def test_update_kwargs_wrong_keys(self):
        """test_update_kwargs_wrong_keys - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_kwargs_wrong_keys - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        s.update(a=5, b=10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_update_kwargs_some_wrong_keys(self):
        """test_update_kwargs_some_wrong_keys - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_kwargs_some_wrong_keys - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        s.update(size=5, id=89, a=1, b=54)
        self.assertEqual("[Square] (89) 10/10 - 5", str(s))


class TestSquare_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Square class."""

    def test_to_dictionary_output(self):
        """test_to_dictionary_output - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_to_dictionary_output - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, s.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        """test_to_dictionary_no_object_changes - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_to_dictionary_no_object_changes - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s1 = Square(10, 2, 1, 2)
        s2 = Square(1, 2, 10)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def test_to_dictionary_arg(self):
        """test_to_dictionary_arg - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_to_dictionary_arg - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        s = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
