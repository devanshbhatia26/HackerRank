s = int(raw_input().strip())
arr = [-1]*37
arr[0] = 0
arr[1] = 1
arr[2] = 2
arr[3] = 4

def getWays(x, arr):
	if arr[x] != -1:
		# print 'returning %d' % arr[x]
		return arr[x]
	if x - 3 >= 0:
		arr[x-3] = getWays(x-3, arr)
		arr[x-2] = getWays(x-2, arr)
		arr[x-1] = getWays(x-1, arr)
		return arr[x-3] + arr[x-2] + arr[x-1]
	if x - 2 >= 0:
		arr[x-2] = getWays(x-2, arr)
		arr[x-1] = getWays(x-1, arr)
		return arr[x-2] + arr[x-1]
	arr[x] = 1 + getWays(x-1, arr)
	return arr[x]

for a0 in xrange(s):
	n = int(raw_input().strip())
	print getWays(n, arr)
	# print arr