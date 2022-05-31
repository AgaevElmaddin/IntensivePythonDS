import timeit


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


if __name__ == '__main__':
	loop_append_time = timeit.timeit('loop_append()', setup='from __main__ import loop_append', number = 90000000)
	list_comprehension_time = timeit.timeit('list_comprehension()', setup='from __main__ import list_comprehension',
											number = 90000000)
	map_time = timeit.timeit('map_', setup = 'from __main__ import map_', number = 90000000)
	if loop_append_time < list_comprehension_time and loop_append_time < map_time:
		print('it is better to use a loop')
	elif list_comprehension_time < loop_append_time and list_comprehension_time < map_time:
		print('it is better to use a list comprehension')
	else:
		print('it is better to use a map')
	sorted_time = sorted([loop_append_time, list_comprehension_time, map_time])
	print(f'{sorted_time[0]} vs {sorted_time[1]} vs {sorted_time[2]}')


