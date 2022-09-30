import sys
import os

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

import se1

MODULE = "se1"

def test_add_one_and_multiply_1():
    do_test_add_one_and_multiply(a=0, x=0, expected=0)


def test_add_one_and_multiply_2():
    do_test_add_one_and_multiply(a=5, x=2, expected=12)


def test_add_one_and_multiply_3():
    do_test_add_one_and_multiply(a=5, x=0, expected=0)


def test_add_one_and_multiply_4():
    do_test_add_one_and_multiply(a=9, x=1, expected=10)


def test_add_one_and_multiply_5():
    do_test_add_one_and_multiply(a=9, x=-2, expected=-20)


def test_add_one_and_multiply_6():
    do_test_add_one_and_multiply(a=-11, x=2, expected=-20)


def test_fractional_part_1():
    do_test_fractional_part(n=2, d=3, expected=2/3)


def test_fractional_part_2():
    do_test_fractional_part(n=3, d=2, expected=1/2)


def test_fractional_part_3():
    do_test_fractional_part(n=50, d=7, expected=1/7)


def test_fractional_part_4():
    do_test_fractional_part(n=3, d=3, expected=float(0))


def test_out_of_unit_square_1():
    do_test_out_of_unit_square(x=0, y=0, expected=False)


def test_out_of_unit_square_2():
    do_test_out_of_unit_square(x=1, y=0, expected=False)


def test_out_of_unit_square_3():
    do_test_out_of_unit_square(x=0, y=1, expected=False)


def test_out_of_unit_square_4():
    do_test_out_of_unit_square(x=0.5, y=1, expected=False)


def test_out_of_unit_square_5():
    do_test_out_of_unit_square(x=0.5, y=0.5, expected=False)


def test_out_of_unit_square_6():
    do_test_out_of_unit_square(x=1.5, y=1.5, expected=True)


def test_out_of_unit_square_7():
    do_test_out_of_unit_square(x=-0.5, y=-0.5, expected=True)


def test_out_of_unit_square_8():
    do_test_out_of_unit_square(x=-0.5, y=0.5, expected=True)


def test_out_of_unit_square_9():
    do_test_out_of_unit_square(x=0.5, y=-0.5, expected=True)


def test_num_common_divisors_1():
    do_test_num_common_divisors(a=4, b=8, expected=3)


def test_num_common_divisors_2():
    do_test_num_common_divisors(a=4, b=5, expected=1)


def test_num_common_divisors_3():
    do_test_num_common_divisors(a=12, b=33, expected=2)


def test_num_common_divisors_4():
    do_test_num_common_divisors(a=1, b=1, expected=1)


def test_num_common_divisors_5():
    do_test_num_common_divisors(a=4, b=4, expected=3)

def test_num_common_divisors_6():
    do_test_num_common_divisors(a=20, b=30, expected=4)


def test_count_evens_odds_1():
    do_test_count_evens_odds(lst=[3, 3, 3, 5], expected="ODDS")


def test_count_evens_odds_2():
    do_test_count_evens_odds(lst=[1, 2, 1], expected="ODDS")


def test_count_evens_odds_3():
    do_test_count_evens_odds(lst=[2, 2, 1], expected="EVENS")


def test_count_evens_odds_4():
    do_test_count_evens_odds(lst=[3, 3, 3, 5], expected="ODDS")


def test_count_evens_odds_5():
    do_test_count_evens_odds(lst=[0, 1, 2, 3], expected="NEITHER")

def test_count_evens_odds_6():
    do_test_count_evens_odds(lst=[], expected="NEITHER")
    

def test_first_negative_1():
    do_test_first_negative(lst=[-1, 2, 3, 4], expected=-1)


def test_first_negative_2():
    do_test_first_negative(lst=[-1, -2, -3, -4], expected=-1)


def test_first_negative_3():
    do_test_first_negative(lst=[0, -1, 2, -3, 4], expected=-1)


def test_first_negative_4():
    do_test_first_negative(lst=[0, 1, 2, 3, -4], expected=-4)


# # #
#
# HELPER FUNCTIONS
#
# # #

def gen_recreate_msg(module, function, *params):
    params_str = ", ".join([str(p) for p in params])

    recreate_msg = "To recreate this test in ipython3 run:\n"
    recreate_msg += "  {}.{}({})".format(module, function, params_str)

    return recreate_msg


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


def check_equals(actual, expected, recreate_msg=None):
    msg = "Actual ({}) and expected ({}) values do not match.".format(actual, expected)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual == expected, msg


def check_float_equals(actual, expected, epsilon, recreate_msg=None):
    msg = "Actual ({}) and expected ({}) values do not match.".format(actual, expected)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert abs(actual - expected) < epsilon, msg


def check_list_unmodified(param_name, before, after, recreate_msg=None):
    msg = "You modified the contents of {} (this is not allowed).\n".format(param_name)
    msg += "  Value before your code: {}\n".format(before)
    msg += "  Value after your code:  {}".format(after)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert before == after, msg


# # #
#
# TEST HELPERS
#
# # #


def do_test_add_one_and_multiply(a, x, expected):
    recreate_msg = gen_recreate_msg(MODULE, "add_one_and_multiply", *(a, x))

    actual = se1.add_one_and_multiply(a, x)

    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)


def do_test_fractional_part(n, d, expected):
    recreate_msg = gen_recreate_msg(MODULE, "fractional_part", *(n, d))

    actual = se1.fractional_part(n, d)

    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_float_equals(actual, expected, 0.001, recreate_msg)


def do_test_out_of_unit_square(x, y, expected):
    recreate_msg = gen_recreate_msg(MODULE, "out_of_unit_square", *(x, y))

    actual = se1.out_of_unit_square(x, y)

    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)


def do_test_num_common_divisors(a, b, expected):
    recreate_msg = gen_recreate_msg(MODULE, "num_common_divisors", *(a, b))

    actual = se1.num_common_divisors(a, b)

    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)


def do_test_count_evens_odds(lst, expected):
    recreate_msg = gen_recreate_msg(MODULE, "count_evens_odds", *(lst,))

    actual = se1.count_evens_odds(lst)

    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)


def do_test_first_negative(lst, expected):
    recreate_msg = gen_recreate_msg(MODULE, "first_negative", *(lst,))

    actual = se1.first_negative(lst)

    check_none(actual, recreate_msg)
    check_type(actual, expected, recreate_msg)
    check_equals(actual, expected, recreate_msg)
