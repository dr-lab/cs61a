def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """

    if k == 0:
        return 1

    falling = n
    while k>1:
        falling *= n - k +  1
        k -= 1
    return falling


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    sumx = 0
    while y > 0:
        curr_digit = int(y % 10)
        sumx += curr_digit
        y = int(y / 10)

    return sumx


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    to_compare = int(n % 10)
    is_same = False
    n = int(n / 10)

    while n > 0:
        curr_digit = int(n % 10)
        if to_compare == curr_digit:
            is_same = True
            break
        else:
            to_compare = curr_digit
        n = int(n / 10)
    return is_same
