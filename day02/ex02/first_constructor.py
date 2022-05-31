import sys
import os


class Research:
	def __init__(self, f_path):
		self.f_path = f_path

	def file_reader(self):
		with open(self.f_path, 'r') as r_f:
			rows = r_f.readlines()
		if len(rows) < 2:
			raise Exception('file has to have at least 2 rows')
		header = rows[0].split(',')
		if len(header) != 2:
			raise Exception('header has to have precisely 2 strings')
		for row in rows[1:]:
			if row[0:3] != '0,1' and row[0:3] != '1,0':
				raise Exception('Incorrect file')
		return ''.join(rows)


if __name__ == '__main__':
	if len(sys.argv) == 2:
		print(Research(sys.argv[1]).file_reader())
