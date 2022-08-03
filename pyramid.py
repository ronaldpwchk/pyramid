from time import sleep
import sys
def main():
	if len(sys.argv) != 2:
		raise Exception('usage: pyramid num.-of-layer-in-odd')
		exit()

	n = int(sys.argv[1])
	if n % 2 == 0:
		raise Exception('usage: pyramid num.-of-layer-in-odd')
		exit()

	mid = n // 2
	for i in range(mid+1):
		for j in range(n):
			if mid + i >= j >= mid - i:
				print('*', end="")
			else: 
				print(' ', end="")
		print()

	input('Press ANY key to quit')
	sleep(1)
	print('terminated')
	print()

if __name__ == '__main__':
	main()