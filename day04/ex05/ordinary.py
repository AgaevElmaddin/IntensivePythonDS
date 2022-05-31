import sys
import psutil


def ordinary(file_path):
	with open(file_path, 'r') as r_f:
		lst = r_f.readlines()
	return lst


if __name__ == '__main__':
	if len(sys.argv) == 2:
		for row in ordinary(sys.argv[1]):
			pass
	memory = psutil.Process().memory_info().vms / 2 ** 30
	cpu = psutil.Process().cpu_times()
	print(f'Peak Memory Usage = {memory:.3f} GB')
	print(f'User Mode Time + System Mode Time = {cpu.user + cpu.system:.2f}s')
