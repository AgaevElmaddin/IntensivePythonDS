import timeit
import random
from collections import Counter


def generate_dct(lst):
	dct = {}
	for el in lst:
		if el in dct:
			dct[el] += 1
		else:
			dct[el] = 1
	return dct


def common_top_10(lst):
	dct = generate_dct(lst)
	return sorted(dct.items(), key=(lambda x: -x[1]))[:10]


if __name__ == '__main__':
	lst = [random.randint(0, 100) for x in range(1000000)]
	print('my function:', timeit.timeit(f'generate_dct({lst})', setup = 'from __main__ import generate_dct', number = 1))
	print('Counter:', timeit.timeit(f'Counter({lst})', setup = 'from __main__ import Counter', number = 1))
	print('my top:', timeit.timeit(f'common_top_10({lst})', setup = 'from __main__ import common_top_10', number = 1))
	print('Counter\'s top:', timeit.timeit(f'Counter({lst}).most_common(10)', setup = 'from __main__ import Counter', number = 1))
