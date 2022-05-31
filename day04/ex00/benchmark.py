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


if __name__ == '__main__':
	loop_append_time = timeit.timeit('loop_append()', setup='from __main__ import loop_append', number = 90000000)
	list_comprehension_time = timeit.timeit('list_comprehension()', setup='from __main__ import list_comprehension',
											number = 90000000)
	if loop_append_time < list_comprehension_time:
		print('it is better to use a loop')
		print(str(loop_append_time) + ' vs ' + str(list_comprehension_time))
	else:
		print('it is better to use a list comprehension')
		print(str(list_comprehension_time) + ' vs ' + str(loop_append_time))