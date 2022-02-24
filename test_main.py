from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650

def test_work():
	assert work_calc(10, 2, 2, lambda n: 1) == 14
	assert work_calc(20, 1, 2, lambda n: n * n) == 418
	assert work_calc(30, 3, 2, lambda n: n) == 120
	assert work_calc(30, 3, 2, lambda n: 1) == 91
	assert work_calc(50, 4, 2, lambda n: 1) == 618
	assert work_calc(40, 3, 2, lambda n: int(math.log2(n))) == 235



