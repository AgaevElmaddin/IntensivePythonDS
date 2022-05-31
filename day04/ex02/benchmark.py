import timeit
import sys

def list_comprehension():
	emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
	return [email for email in emails if email.endswith('@gmail.com')]


def loop_append():
	emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
	lst = []
	for email in emails:
		if email.endswith('@gmail.com'):
			lst.append(email)
	return lst


def map_():
	emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
	return list(map(lambda x: x if x.endswith('@gmail.com') else None, emails))

def filter_():
	emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
	return list(filter(lambda x: x.endswith('@gmail.com'), emails))

if __name__ == '__main__':
	dct =	{
				'loop': 'loop_append',
				'list_comprehension': 'list_comprehension',
				'map': 'map_',
				'filter': 'filter_'
			}
	if len(sys.argv) == 3:
		try:
			if sys.argv[1] in dct:
				print(timeit.timeit(dct[sys.argv[1]] + '()', setup = 'from __main__ import ' + dct[sys.argv[1]],
						number = int(sys.argv[2])))
			else:
				raise Exception('This function is not our topic in this task')
		except ValueError:
				raise Exception('Could not convert number to an integer')
