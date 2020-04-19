from nearest import nearest_square

def test_nearest_sqr_5():
	assert nearest_square(5) == 25

def test_nearest_sqr_3():
	assert nearest_square(7) == 4

def test_nearest_sqr_17():
	assert nearest_square(17) == 16
