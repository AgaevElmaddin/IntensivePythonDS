def data_types():
	a = 5
	b = 'hello'
	c = 4.3
	d = True
	my_list = [1, 2, 3]
	my_dictionary = {'first':1, 'second':2, 'third':3}
	my_tuple = (True, 3.14, 'text')
	my_set = {'hi', 'bye'}
	print('[', type(a).__name__, ', ', type(b).__name__, ', ', type(c).__name__, ', ', type(d).__name__,  ', ', type(my_list).__name__, ', ', type(my_dictionary).__name__, ', ', type(my_tuple).__name__, ', ', type(my_set).__name__, ']', sep='')


if __name__ == '__main__':
	data_types()
