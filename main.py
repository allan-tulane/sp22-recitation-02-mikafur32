"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time


###

def simple_work_calc(n, a, b):
    """Compute the value of the recurrence $W(n) = aW(n/b) + n

    Params:
    n......input integer
    a......branching factor of recursion tree
    b......input split factor

    Returns: the value of W(n).
    """
    '''
    When w(1) , w(1) = value in question, then build back up.
        if n < 1:
        end
        return value  
        w(0) == return f(n)
        
    if n/b =\= integer, round down = floor,  === n // b 
    
    default f(n) = n
    
    a * (n // b) + n
    '''
    if n <= 1:
        return n
    return a * simple_work_calc(n // b, a, b) + n


def test_simple_work():
    """ done. """
    # Compute the value of the recurrence $W(n) = aW(n/b) + n
    assert simple_work_calc(10, 2, 2) == 36
    assert simple_work_calc(20, 3, 2) == 230
    assert simple_work_calc(30, 4, 2) == 650


def work_calc(n, a, b, f):
    """Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

    Params:
    n......input integer
    a......branching factor of recursion tree
    b......input split factor
    f......a function that takes an integer and returns
           the work done at each node

    Returns: the value of W(n).
    """
    if n <= 1:
        return n
    return a * simple_work_calc(n // b, a, b) + f(n)


def test_work():
    """ done. """

    assert work_calc(10, 2, 2, lambda n: 1) == 27
    assert work_calc(20, 1, 2, lambda n: n * n) == 418
    assert work_calc(30, 3, 2, lambda n: n) == 300


def span_calc(n, a, b, f):
    """Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

    Params:
    n......input integer
    a......branching factor of recursion tree
    b......input split factor
    f......a function that takes an integer and returns
           the work done at each node

    Returns: the value of S(n).

    get rid of a, branching factor
    """
    # TODO
    pass


def compare_work(work_fn1, work_fn2, sizes = [10, 20, 50, 100, 1000, 5000, 10000]):
    """
    Compare the values of different recurrences for
    given input sizes.

    Returns:
    A list of tuples of the form
    (n, work_fn1(n), work_fn2(n), ...)

    """
    result = []
    for n in sizes:
        # compute W(n) using current a, b, f
        result.append((
            n,
            work_fn1(n),
            work_fn2(n)
        ))
    return result


def print_results(results):
    """ done """
    print(tabulate.tabulate(results,
                            headers = ['n', 'W_1', 'W_2'],
                            floatfmt = ".3f",
                            tablefmt = "github"))


def test_compare_work():
    # curry work_calc to create multiple work
    # functions taht can be passed to compare_work

    work_fn1 = work_calc(30, 3, 2, lambda n: n)
    work_fn2 = work_calc(15, 2, 3, lambda n: n)
    res = (compare_work(work_fn1, work_fn2))
    print(res)
    assert 0
# def test_compare_span():
# TODO
