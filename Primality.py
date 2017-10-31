from math import sqrt

# fin = open('primality_inp9.txt', 'r')

p = int(raw_input().strip())
# p = int(fin.readline().strip())
for _ in xrange(p):
	flag = False
	n = int(raw_input().strip())
	# n = int(fin.readline().strip())
	if n == 1:
		print 'Not prime'
		continue
	for i in range(2, int(sqrt(n))+1):
		if n % i == 0:
			print "Not Prime"
			flag = True
			break
	if not flag:
		print "Prime"