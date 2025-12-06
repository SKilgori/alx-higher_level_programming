#!/usr/bin/python3
# test_rectangle.py
"""Defines unittests for models/rectangle.py.
Unittest classes:
    TestRectangle_instantiation - line 25
    TestRectangle_width - line 114
    TestRectangle_height - line 190
    TestRectangle_x - line 262
    TestRectangle_y - line 334
    TestRectangle_order_of_initialization - line 402
    TestRectangle_area - line 430
    TestRectangle_update_args - line 538
    TestRectangle_update_kwargs - line 676
    TestRectangle_to_dictionary - line 788
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""

    def test_rectangle_is_base(self):
        """test_rectangle_is_base - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_rectangle_is_base - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        self.assertIsInstance(Rectangle(10, 2), Base)

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
            Rectangle()

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
        with self.assertRaises(TypeError):
            Rectangle(1)

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
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

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
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

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
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        """test_five_args - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_five_args - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_more_than_five_args(self):
        """test_more_than_five_args - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_more_than_five_args - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        """test_width_private - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_width_private - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        """test_height_private - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_height_private - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        """test_x_private - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_x_private - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        """test_y_private - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_y_private - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

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
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)

    def test_width_setter(self):
        """test_width_setter - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_width_setter - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(5, 7, 7, 5, 1)
        r.width = 10
        self.assertEqual(10, r.width)

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
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.height)

    def test_height_setter(self):
        """test_height_setter - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_height_setter - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(5, 7, 7, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

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
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.x)

    def test_x_setter(self):
        """test_x_setter - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_x_setter - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(5, 7, 7, 5, 1)
        r.x = 10
        self.assertEqual(10, r.x)

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
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_y_setter(self):
        """test_y_setter - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_y_setter - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(5, 7, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)


class TestRectangle_width(unittest.TestCase):
    """Unittests for testing initialization of Rectangle width attribute."""

    def test_None_width(self):
        """test_None_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_None_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        """test_str_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_str_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 2)

    def test_float_width(self):
        """test_float_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_float_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 1)

    def test_complex_width(self):
        """test_complex_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_complex_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(5), 2)

    def test_dict_width(self):
        """test_dict_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_dict_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1, "b": 2}, 2)

    def test_bool_width(self):
        """test_bool_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_bool_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)

    def test_list_width(self):
        """test_list_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_list_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)

    def test_set_width(self):
        """test_set_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_set_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 2)

    def test_tuple_width(self):
        """test_tuple_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_tuple_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 2)

    def test_frozenset_width(self):
        """test_frozenset_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_frozenset_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 2, 3, 1}), 2)

    def test_range_width(self):
        """test_range_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_range_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(5), 2)

    def test_bytes_width(self):
        """test_bytes_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_bytes_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Python', 2)

    def test_bytearray_width(self):
        """test_bytearray_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_bytearray_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'abcdefg'), 2)

    def test_memoryview_width(self):
        """test_memoryview_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_memoryview_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'abcedfg'), 2)

    def test_inf_width(self):
        """test_inf_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_inf_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 2)

    def test_nan_width(self):
        """test_nan_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_nan_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 2)

    def test_negative_width(self):
        """test_negative_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_negative_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_zero_width(self):
        """test_zero_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_zero_width - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)


class TestRectangle_height(unittest.TestCase):
    """Unittests for testing initialization of Rectangle height attribute."""

    def test_None_height(self):
        """test_None_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_None_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_str_height(self):
        """test_str_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_str_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid")

    def test_float_height(self):
        """test_float_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_float_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 5.5)

    def test_complex_height(self):
        """test_complex_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_complex_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, complex(5))

    def test_dict_height(self):
        """test_dict_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_dict_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"a": 1, "b": 2})

    def test_list_height(self):
        """test_list_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_list_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1, 2, 3])

    def test_set_height(self):
        """test_set_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_set_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {1, 2, 3})

    def test_tuple_height(self):
        """test_tuple_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_tuple_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1, 2, 3))

    def test_frozenset_height(self):
        """test_frozenset_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_frozenset_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, frozenset({1, 2, 3, 1}))

    def test_range_height(self):
        """test_range_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_range_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, range(5))

    def test_bytes_height(self):
        """test_bytes_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_bytes_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, b'Python')

    def test_bytearray_height(self):
        """test_bytearray_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_bytearray_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, bytearray(b'abcdefg'))

    def test_memoryview_height(self):
        """test_memoryview_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_memoryview_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, memoryview(b'abcedfg'))

    def test_inf_height(self):
        """test_inf_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_inf_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('inf'))

    def test_nan_height(self):
        """test_nan_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_nan_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('nan'))

    def test_negative_height(self):
        """test_negative_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_negative_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)

    def test_zero_height(self):
        """test_zero_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_zero_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)


class TestRectangle_x(unittest.TestCase):
    """Unittests for testing initialization of Rectangle x attribute."""

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
            Rectangle(1, 2, None)

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
            Rectangle(1, 2, "invalid", 2)

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
            Rectangle(1, 2, 5.5, 9)

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
            Rectangle(1, 2, complex(5))

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
            Rectangle(1, 2, {"a": 1, "b": 2}, 2)

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
            Rectangle(1, 2, True, 2)

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
            Rectangle(1, 2, [1, 2, 3], 2)

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
            Rectangle(1, 2, {1, 2, 3}, 2)

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
            Rectangle(1, 2, (1, 2, 3), 2)

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
            Rectangle(1, 2, frozenset({1, 2, 3, 1}))

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
            Rectangle(1, 2, range(5))

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
            Rectangle(1, 2, b'Python')

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
            Rectangle(1, 2, bytearray(b'abcdefg'))

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
            Rectangle(1, 2, memoryview(b'abcedfg'))

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
            Rectangle(1, 2, float('inf'), 2)

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
            Rectangle(1, 2, float('nan'), 2)

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
            Rectangle(5, 3, -1, 0)


class TestRectangle_y(unittest.TestCase):
    """Unittests for testing initialization of Rectangle y attribute."""

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
            Rectangle(1, 2, 3, None)

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
            Rectangle(1, 2, 1, "invalid")

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
            Rectangle(1, 2, 3, 5.5)

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
            Rectangle(1, 2, 3, complex(5))

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
            Rectangle(1, 2, 1, {"a": 1, "b": 2})

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
            Rectangle(1, 2, 1, [1, 2, 3])

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
            Rectangle(1, 2, 1, {1, 2, 3})

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
            Rectangle(1, 2, 1, (1, 2, 3))

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
            Rectangle(1, 2, 3, frozenset({1, 2, 3, 1}))

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
            Rectangle(1, 2, 3, range(5))

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
            Rectangle(1, 2, 3, b'Python')

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
            Rectangle(1, 2, 3, bytearray(b'abcdefg'))

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
            Rectangle(1, 2, 3, memoryview(b'abcedfg'))

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
            Rectangle(1, 2, 1, float('inf'))

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
            Rectangle(1, 2, 1, float('nan'))

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
            Rectangle(3, 5, 0, -1)


class TestRectangle_order_of_initialization(unittest.TestCase):
    """Unittests for testing Rectangle order of attribute initialization."""

    def test_width_before_height(self):
        """test_width_before_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_width_before_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", "invalid height")

    def test_width_before_x(self):
        """test_width_before_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_width_before_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, "invalid x")

    def test_width_before_y(self):
        """test_width_before_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_width_before_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, 3, "invalid y")

    def test_height_before_x(self):
        """test_height_before_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_height_before_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", "invalid x")

    def test_height_before_y(self):
        """test_height_before_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_height_before_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", 2, "invalid y")

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
            Rectangle(1, 2, "invalid x", "invalid y")


class TestRectangle_area(unittest.TestCase):
    """Unittests for testing the area method of the Rectangle class."""

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
        r = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, r.area())

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
        r = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, r.area())

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
        r = Rectangle(2, 10, 1, 1, 1)
        r.width = 7
        r.height = 14
        self.assertEqual(98, r.area())

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
        r = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.area(1)


class TestRectangle_stdout(unittest.TestCase):
    """Unittests for testing __str__ and display methods of Rectangle class."""

    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns text printed to stdout.
        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on rect.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    # Test __str__ method
    def test_str_method_print_width_height(self):
        """test_str_method_print_width_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_str_method_print_width_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(4, 6)
        capture = TestRectangle_stdout.capture_stdout(r, "print")
        correct = "[Rectangle] ({}) 0/0 - 4/6\n".format(r.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_width_height_x(self):
        """test_str_method_width_height_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_str_method_width_height_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(5, 5, 1)
        correct = "[Rectangle] ({}) 1/0 - 5/5".format(r.id)
        self.assertEqual(correct, r.__str__())

    def test_str_method_width_height_x_y(self):
        """test_str_method_width_height_x_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_str_method_width_height_x_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(1, 8, 2, 4)
        correct = "[Rectangle] ({}) 2/4 - 1/8".format(r.id)
        self.assertEqual(correct, str(r))

    def test_str_method_width_height_x_y_id(self):
        """test_str_method_width_height_x_y_id - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_str_method_width_height_x_y_id - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(r))

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
        r = Rectangle(7, 7, 0, 0, [4])
        r.width = 15
        r.height = 1
        r.x = 8
        r.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(r))

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
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)

    # Test display method
    def test_display_width_height(self):
        """test_display_width_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_display_width_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(2, 3, 0, 0, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_display_width_height_x(self):
        """test_display_width_height_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_display_width_height_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(3, 2, 1, 0, 1)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

    def test_display_width_height_y(self):
        """test_display_width_height_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_display_width_height_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(4, 5, 0, 1, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_width_height_x_y(self):
        """test_display_width_height_x_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_display_width_height_x_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(2, 4, 3, 2, 0)
        capture = TestRectangle_stdout.capture_stdout(r, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
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
        r = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display(1)


class TestRectangle_update_args(unittest.TestCase):
    """Unittests for testing update args method of the Rectangle class."""

    # Test args
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
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

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
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))

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
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

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
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

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
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r))

    def test_update_args_five(self):
        """test_update_args_five - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_five - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_args_more_than_five(self):
        """test_update_args_more_than_five - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_more_than_five - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

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
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

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
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None, 4, 5, 2)
        correct = "[Rectangle] ({}) 2/10 - 4/5".format(r.id)
        self.assertEqual(correct, str(r))

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
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        r.update(6, 5, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(r))

    def test_update_args_invalid_width_type(self):
        """test_update_args_invalid_width_type - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_invalid_width_type - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid")

    def test_update_args_width_zero(self):
        """test_update_args_width_zero - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_width_zero - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, 0)

    def test_update_args_width_negative(self):
        """test_update_args_width_negative - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_width_negative - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, -5)

    def test_update_args_invalid_height_type(self):
        """test_update_args_invalid_height_type - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_invalid_height_type - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 2, "invalid")

    def test_update_args_height_zero(self):
        """test_update_args_height_zero - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_height_zero - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, 0)

    def test_update_args_height_negative(self):
        """test_update_args_height_negative - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_height_negative - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, -5)

    def test_update_args_invalid_x_type(self):
        """test_update_args_invalid_x_type - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_invalid_x_type - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 2, 3, "invalid")

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
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(89, 1, 2, -6)

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
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(89, 2, 3, 4, "invalid")

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
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(89, 1, 2, 3, -6)

    def test_update_args_width_before_height(self):
        """test_update_args_width_before_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_width_before_height - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", "invalid")

    def test_update_args_width_before_x(self):
        """test_update_args_width_before_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_width_before_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, "invalid")

    def test_update_args_width_before_y(self):
        """test_update_args_width_before_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_width_before_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, 2, "invalid")

    def test_update_args_height_before_x(self):
        """test_update_args_height_before_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_height_before_x - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", "invalid")

    def test_update_args_height_before_y(self):
        """test_update_args_height_before_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_args_height_before_y - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", 1, "invalid")

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
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 1, 2, "invalid", "invalid")


class TestRectangle_update_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of the Rectangle class."""

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
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))

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
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

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
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

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
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r))

    def test_update_kwargs_five(self):
        """test_update_kwargs_five - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_kwargs_five - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(r))

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
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

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
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None, height=7, y=9)
        correct = "[Rectangle] ({}) 10/9 - 10/7".format(r.id)
        self.assertEqual(correct, str(r))

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
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2)
        r.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(r))

    def test_update_kwargs_invalid_width_type(self):
        """test_update_kwargs_invalid_width_type - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_kwargs_invalid_width_type - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="invalid")

    def test_update_kwargs_width_zero(self):
        """test_update_kwargs_width_zero - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_kwargs_width_zero - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def test_update_kwargs_width_negative(self):
        """test_update_kwargs_width_negative - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_kwargs_width_negative - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-5)

    def test_update_kwargs_invalid_height_type(self):
        """test_update_kwargs_invalid_height_type - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_kwargs_invalid_height_type - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="invalid")

    def test_update_kwargs_height_zero(self):
        """test_update_kwargs_height_zero - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_kwargs_height_zero - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def test_update_kwargs_height_negative(self):
        """test_update_kwargs_height_negative - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_kwargs_height_negative - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-5)

    def test_update_kwargs_inavlid_x_type(self):
        """test_update_kwargs_inavlid_x_type - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_kwargs_inavlid_x_type - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid")

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
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        """test_update_kwargs_invalid_y_type - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        """test_update_kwargs_invalid_y_type - Function documentation.
        
        Args:
            self: Description of self.
        
        Returns:
            Description of the return value.
        """
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="invalid")

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
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-5)

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
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

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
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

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
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(r))


class TestRectangle_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Rectangle class."""

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
        r = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())

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
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

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
        r = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
