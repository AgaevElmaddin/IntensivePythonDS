class Research:
	def file_reader(self):
		with open('data.csv', 'r') as r_f:
			return r_f.read()


if __name__ == '__main__':
	print(Research().file_reader())