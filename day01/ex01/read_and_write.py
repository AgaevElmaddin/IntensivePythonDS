def read_and_write():
	with open('ds.csv', 'r') as r_f:
		with open('ds.tsv', 'w') as w_f:
			w_f.write(r_f.read().replace('",', '"\t',).replace('false,', 'false\t').replace('true,', 'true\t'))


if __name__ == '__main__':
	read_and_write()
	