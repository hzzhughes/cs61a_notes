HW_SOURCE_FILE = __file__


def composer(func=lambda x: x):
    """
    Returns two functions -
    one holding the composed function so far, and another
    that can create further composed problems.
    >>> add_one = lambda x: x + 1
    >>> mul_two = lambda x: x * 2
    >>> f, func_adder = composer()
    >>> f1, func_adder = func_adder(add_one)
    >>> f1(3)
    4
    >>> f2, func_adder = func_adder(mul_two)
    >>> f2(3) # should be 1 + (2*3) = 7
    7
    >>> f3, func_adder = func_adder(add_one)
    >>> f3(3) # should be 1 + (2 * (3 + 1)) = 9
    9
    """

    def func_adder(g):
        "*** YOUR CODE HERE ***"

        def new_func(y):
            return func(g(y))

        return composer(new_func)

    return func, func_adder


def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)


def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> # ban recursion
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    g_1, g_2, g_3, index = 3, 2, 1, 4
    while index <= n:
        g_1, g_2, g_3, index = g_1 + 2 * g_2 + 3 * g_3, g_1, g_2, index + 1
    return g_1


def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        return 0
    return max(n % 10 - n // 10 % 10 - 1, 0) + missing_digits(n // 10)


def count_change(total):
    """Return the number of ways to make change for total.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"

    def greatest_exp_of_2(num):
        if num < 2:
            return 1
        return greatest_exp_of_2(num / 2) * 2

    def count_change_up_to_m(total, m):
        if total < 0:
            return 0
        if m == 1:
            return 1
        return (
            count_change_up_to_m(total - m, m)
            + count_change_up_to_m(total, m // 2)
        )

    return count_change_up_to_m(total, greatest_exp_of_2(total))


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)


def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"


from operator import sub, mul


def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return "YOUR_EXPRESSION_HERE"
