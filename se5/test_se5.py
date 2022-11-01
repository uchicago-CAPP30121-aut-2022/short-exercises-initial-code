import sys
import os
import math

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

import se5
import numpy as np

MODULE = "se5"

# # #
#
# HELPER FUNCTIONS
#
# # #

def pretty_print_repr(x):
    """
    A version of repr with some special casing.
    """
    if isinstance(x, np.ndarray):
        return "np." + repr(x)
    return repr(x)

def gen_recreate_msg(module, function, *params, **kwparams):

    params_str = ", ".join([pretty_print_repr(p) for p in params])
    if len(kwparams) > 0:
        params_str += ", ".join(["{} = {}".format(k, repr(v)) for k, v in kwparams.items()])


    recreate_msg = "To recreate this test in ipython3 run:\n"
    recreate_msg += "  {}.{}({})".format(module, function, params_str)

    return recreate_msg

def check_equal(actual, expected, recreate_msg=None):
    msg = "Actual ({}) and expected ({}) values do not match.".format(actual, expected)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual == expected, msg

def check_float_equal(actual, expected, recreate_msg=None):
    msg = "Actual ({}) and expected ({}) values do not match.".format(actual, expected)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert abs(actual-expected) < 0.01, msg

def check_none(actual, recreate_msg=None):
    msg = "The function returned None."
    msg += " Did you forget to replace the placeholder value we provide?"
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual is not None, msg

def check_type(actual, expected, recreate_msg=None):
    actual_type = type(actual)
    expected_type = type(expected)

    msg = "The function returned a value of the wrong type.\n"
    msg += "  Expected return type: {}.\n".format(expected_type.__name__)
    msg += "  Actual return type: {}.".format(actual_type.__name__)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert isinstance(actual, expected_type), msg

def check_dtype(array, expected, recreate_msg=None):
    actual_dtype = array.dtype
    expected_dtype = expected

    msg = "The function returned an array of the wrong dtype.\n"
    msg += "  Expected return dtype: {}.\n".format(expected_dtype)
    msg += "  Actual return dtype: {}.".format(actual_dtype)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual_dtype == expected_dtype, msg

def check_is_ndarray(actual, recreate_msg=None):
    check_type(actual, np.zeros(1), recreate_msg)

def check_array_equal(actual, expected, recreate_msg):
    msg = "The function returned the wrong array"
    msg += " Expected array: {}\n".format(expected)
    msg += " Actual returned array: {}\n".format(actual)

    if recreate_msg is not None:
        msg += "\n" + recreate_msg
    
    np.testing.assert_allclose(actual, expected,
                               err_msg = msg, verbose=False)
    
    
    # # #
#
# TEST HELPERS
#
# # #

def do_test_reshape_array(x, new_dims, expected):

    recreate_msg = gen_recreate_msg(MODULE, 'reshape_array', x, new_dims)

    actual = se5.reshape_array(x, new_dims)

    check_none(actual, recreate_msg)
    check_is_ndarray(actual, recreate_msg)
    check_array_equal(actual, expected, recreate_msg)

def test_reshape_array_1():

    x = np.array([[1, 2, 3, 4, 5, 6]])
    new_dims = (2, 3)
    expected = np.array([[1, 2, 3],
                         [4, 5, 6]])

    do_test_reshape_array(x, new_dims, expected)
    
def test_reshape_array_2():

    x = np.array([[1, 2, 3, 4, 5, 6]])
    new_dims = (3, 2)
    expected = np.array([[1, 2],
                         [3, 4],
                         [5, 6]])

    do_test_reshape_array(x, new_dims, expected) 

def test_reshape_array_3():

    x = np.array([[1, 2, 3, 4, 5, 6]])
    new_dims = (3, 3)
    expected = np.array([[1, 2, 3, 4, 5, 6]])

    do_test_reshape_array(x, new_dims, expected) 

def test_reshape_array_4():

    x = np.array([[1, 2, 3, 4], 
                  [5, 6, 7, 8]])
    new_dims = (2, 4)
    expected = np.array([[1, 2, 3, 4], 
                         [5, 6, 7, 8]])

    do_test_reshape_array(x, new_dims, expected) 

def test_reshape_array_5():

    x = np.array([[1, 2, 3, 4], 
                  [5, 6, 7, 8]])
    new_dims = (4, 2)
    expected = np.array([[1, 2],
                         [3, 4],
                         [5, 6],
                         [7, 8]])

    do_test_reshape_array(x, new_dims, expected) 

def test_reshape_array_6():

    x = np.array([[1, 2, 3, 4], 
                  [5, 6, 7, 8]])
    new_dims = (1, 8)
    expected = np.array([[1, 2, 3, 4, 5, 6, 7, 8]])

    do_test_reshape_array(x, new_dims, expected) 

def test_reshape_array_7():

    x = np.array([[1, 2, 3, 4], 
                  [5, 6, 7, 8]])
    new_dims = (8, 1)
    expected = np.array([[1],
                         [2],
                         [3],
                         [4],
                         [5],
                         [6],
                         [7],
                         [8]])

    do_test_reshape_array(x, new_dims, expected) 

def test_reshape_array_8():

    x = np.array([[1, 2, 3, 4], 
                  [5, 6, 7, 8]])
    new_dims = (2, 3)
    expected = np.array([[1, 2, 3, 4], 
                         [5, 6, 7, 8]])

    do_test_reshape_array(x, new_dims, expected) 


def do_test_harmonic_sequence(N, expected):

    recreate_msg = gen_recreate_msg(MODULE, 'harmonic_sequence', N)

    actual = se5.harmonic_sequence(N)

    check_none(actual, recreate_msg)
    check_float_equal(actual, expected, recreate_msg)

def test_harmonic_sequence():

    for N in range(1, 12):
        expected = sum([1/i for i in range(1, N+1)])
        do_test_harmonic_sequence(N, expected)

def do_test_clip_in_range(x, lb, ub, expected):

    recreate_msg = gen_recreate_msg(MODULE, 'clip_in_range', x, lb, ub)

    output = se5.clip_in_range(x, lb, ub)

    check_type(output, None, recreate_msg)
    check_is_ndarray(x, recreate_msg)
    check_array_equal(x, expected, recreate_msg)

def test_clip_in_range_1():

    x = np.array([1])
    lb, ub = 0, 2
    expected = np.array([1])

    do_test_clip_in_range(x, lb, ub, expected)

def test_clip_in_range_2():

    x = np.array([1])
    lb, ub = 0, 0
    expected = np.array([0])

    do_test_clip_in_range(x, lb, ub, expected)

def test_clip_in_range_3():

    x = np.array([0, 1, 2])
    lb, ub = 0, 2
    expected = np.array([0, 1, 2])

    do_test_clip_in_range(x, lb, ub, expected)

def test_clip_in_range_4():

    x = np.array([-1, 9, 0, 3, 3, 6])
    lb, ub = -2, 5
    expected = np.array([-1, 5, 0, 3, 3, 5])

    do_test_clip_in_range(x, lb, ub, expected)

def test_clip_in_range_5():

    x = np.array([-1, 9, 0, 3, 3, 6])
    lb, ub = 2, 9
    expected = np.array([2, 9, 2, 3, 3, 6])

    do_test_clip_in_range(x, lb, ub, expected)

def test_clip_in_range_6():

    x = np.array([5, -1, 3, 4, -5, 7, -3])
    lb, ub = 0, 2
    expected = np.array([2, 0, 2, 2, 0, 2, 0])

    do_test_clip_in_range(x, lb, ub, expected)


def do_test_fill_missing_data(x, expected):

    recreate_msg = gen_recreate_msg(MODULE, 'fill_missing_data', x)

    output = se5.fill_missing_data(x)

    check_type(output, None, recreate_msg)
    check_is_ndarray(x, recreate_msg)
    check_array_equal(x, expected, recreate_msg)

def test_fill_missing_data_1():

    x = np.array([-1, 0, 1, 5])
    expected = np.array([2, 0, 1, 5])

    do_test_fill_missing_data(x, expected)

def test_fill_missing_data_2():

    x = np.array([-1, 0, -1, 6])
    expected = np.array([3, 0, 3, 6])

    do_test_fill_missing_data(x, expected)

def test_fill_missing_data_3():

    x = np.array([-1, -1, -1, 6])
    expected = np.array([6, 6, 6, 6])

    do_test_fill_missing_data(x, expected)

def test_fill_missing_data_4():

    x = np.array([[1, 8],
                  [6, -1]])
    expected = np.array([[1, 8],
                         [6, 5]])

    do_test_fill_missing_data(x, expected)

def test_fill_missing_data_5():

    x = np.array([[2, -1],
                  [6, -1]])
    expected = np.array([[2, 4],
                         [6, 4]])

    do_test_fill_missing_data(x, expected)

def test_fill_missing_data_6():

    x = np.array([[1, -4, 3, 1],
                  [6, -1, 8, -1],
                  [2, 5, -1, 14]])
    expected = np.array([[1, -4, 3, 1],
                         [6, 4, 8, 4],
                         [2, 5, 4, 14]])

    do_test_fill_missing_data(x, expected)

def do_test_smallest_span(x, expected):

    recreate_msg = gen_recreate_msg(MODULE, 'smallest_span', x)

    actual = se5.smallest_span(x)

    check_none(actual, recreate_msg)
    check_equal(actual, expected, recreate_msg)

def test_smallest_span_1():

    x = np.array([[1, 2]])
    expected = 0

    do_test_smallest_span(x, expected)

def test_smallest_span_2():

    x = np.array([[1, 8],
                  [6, 9]])
    expected = 1

    do_test_smallest_span(x, expected)

def test_smallest_span_3():

    x = np.array([[1, 2],
                  [6, 9]])
    expected = 0

    do_test_smallest_span(x, expected)

def test_smallest_span_4():

    x = np.array([[1, -4, 3, 1],
                  [6, 9, 8, 9],
                  [2, 5, 3, 7]])
    expected = 1

    do_test_smallest_span(x, expected)

def test_smallest_span_5():

    x = np.array([[1, -4, 3, 1],
                  [6, 9, 8, 16],
                  [2, 5, 3, 7]])
    expected = 2

    do_test_smallest_span(x, expected)

def test_smallest_span_6():

    x = np.array([[1, -4, 3, 1],
                  [6, 9, 8, 1],
                  [2, -5, 3, 7]])
    expected = 0

    do_test_smallest_span(x, expected)

def test_select_row_col():
    x = np.arange(20).reshape(4, 5)

    def custom_get_cols(x, cols):
        out = np.stack([x[:, r] for r in cols], -1)
        return out
    
    def custom_get_rows(x, rows):
        out = np.stack([x[r] for r in rows])
        return out
    
    def custom_get_rows_cols(x, rows, cols):
        row_out = np.stack([x[r] for r in rows])
        out = np.stack([row_out[:, r] for r in cols], -1)
        return out
    
        
    for tgt_cols in [[0], [1, 2, 3], [3, 2, 1], [2, 1, 3, 4, 0]]:

        recreate_msg = gen_recreate_msg(MODULE, 'select_row_col', x, None, tgt_cols)
        
        result = se5.select_row_col(x, None, tgt_cols)
    
        check_none(result, recreate_msg)
        check_is_ndarray(result, recreate_msg)

        expected_shape = (4, len(tgt_cols))
        assert result.shape == expected_shape, \
            "The shape of the returned array was {}, but".format(result.shape) \
            + " we expected {}\n\n".format(expected_shape) + recreate_msg

        expected_value = custom_get_cols(x, tgt_cols)

        check_array_equal(result, expected_value, 
                          recreate_msg)

        
    for tgt_rows in [[0], [1, 2, 3], [3, 2, 1], [2, 1, 3, 0]]:

        recreate_msg = gen_recreate_msg(MODULE, 'select_row_col', x, tgt_rows, None)
        
        result = se5.select_row_col(x, tgt_rows, None)
    
        check_none(result, recreate_msg)
        check_is_ndarray(result, recreate_msg)

        expected_shape = (len(tgt_rows), 5)
        assert result.shape == expected_shape, \
            "The shape of the returned array was {}, but".format(result.shape) \
            + " we expected {}\n\n".format(expected_shape) + recreate_msg

        expected_value = custom_get_rows(x, tgt_rows)

        check_array_equal(result, expected_value, 
                          recreate_msg)
    
    for tgt_rows, tgt_cols in [([0],[0]), ([1, 2, 3],[1, 3]), ([3, 1],[0,2])]:

        recreate_msg = gen_recreate_msg(MODULE, 'select_row_col', x, tgt_rows, tgt_cols)
        
        result = se5.select_row_col(x, tgt_rows, tgt_cols)
    
        check_none(result, recreate_msg)
        check_is_ndarray(result, recreate_msg)

        expected_shape = (len(tgt_rows), len(tgt_cols))
        assert result.shape == expected_shape, \
            "The shape of the returned array was {}, but".format(result.shape) \
            + " we expected {}\n\n".format(expected_shape) + recreate_msg

        expected_value = custom_get_rows_cols(x, tgt_rows, tgt_cols)

        check_array_equal(result, expected_value, 
                          recreate_msg)
    
    
    for tgt_rows, tgt_cols in [(None, None)]:

        recreate_msg = gen_recreate_msg(MODULE, 'select_row_col', x, None, None)
        
        result = se5.select_row_col(x, None, None)
    
        check_none(result, recreate_msg)
        check_is_ndarray(result, recreate_msg)

        expected_shape = (x.shape[0], x.shape[1])
        assert result.shape == expected_shape, \
            "The shape of the returned array was {}, but".format(result.shape) \
            + " we expected {}\n\n".format(expected_shape) + recreate_msg

        check_array_equal(result, x, recreate_msg)