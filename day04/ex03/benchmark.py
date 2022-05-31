import timeit
import sys
from functools import reduce


def loop_(number):
	square = 0
	for el in range(1, int(number) + 1):
		square += el ** 2
	return square


def reduce_(number):
	lst = [a for a in range(1, int(number) + 1)]
	return reduce(lambda x, y: x + y ** 2, lst)


if __name__ == '__main__':
	dct =	{
				'loop': 'loop_',
				'reduce': 'reduce_'
			}
	if len(sys.argv) == 4:
		try:
			if sys.argv[1] in dct:
				print(timeit.timeit(dct[sys.argv[1]] + f'({int(sys.argv[3])})',
					setup = 'from __main__ import ' + dct[sys.argv[1]], number = int(sys.argv[2])))
			else:
				raise Exception('This function is not our topic in this task')
		except ValueError:
				raise Exception('Could not convert number to an integer')
