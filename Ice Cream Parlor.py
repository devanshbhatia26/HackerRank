from collections import defaultdict

def binSearch(arr, x, lo, hi):
	if lo < hi:
		mid = (lo + hi) / 2
		if x == arr[mid]:
			return arr[mid]
		if x > arr[mid]:
			return binSearch(arr, x, mid + 1, hi)
		return binSearch(arr, x, lo, mid)
	return -1

fin = open('ice_cream_parlor_inp1.txt', 'r')

t = int(raw_input().strip())
# t = int(fin.readline().strip())
for _ in xrange(t):
	d = defaultdict(list)
	money = int(raw_input().strip())
	# money = int(fin.readline().strip())
	n = int(raw_input().strip())
	# n = int(fin.readline().strip())
	arr = map(int, raw_input().strip().split())
	# arr = map(int, fin.readline().strip().split())
	for i, v in enumerate(arr):
		d[v].append(i+1)
	sorted_arr = sorted(arr)

	for i in xrange(n):
		tmp = binSearch(sorted_arr, money - sorted_arr[i], i+1, n)
		if tmp != -1:
			print ' '.join(map(str, sorted([d[sorted_arr[i]].pop(0), d[tmp].pop(0)])))
			break