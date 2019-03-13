import math
import sys
import time

primes = [2, 3] # Start the list with a few primes

def test(toTest):
	for i in primes:
		if(i > math.sqrt(toTest)):
			break
		if(toTest % i == 0):
			wasPrime = 0
			break
		else:
			wasPrime = 1
	return wasPrime
				

try:
	num = 4 # Starting number
	initial = num
	how_many_primes = 2
	while(1):
		result = test(num)
		if(result):
			primes.append(num)
			how_many_primes += 1
			sys.stdout.write("\r{} is the highest prime, found {} primes".format(primes[-1],how_many_primes))
			sys.stdout.flush()
			time.sleep(0.1)
			
		num += 1 # move on to the next number
except KeyboardInterrupt:
	print('\nUser forced stop -- writing primes to primes.txt...')
	file = open('primes.txt', 'w')
	for prime in primes:
		file.write(str(prime) + '\n')
	file.close
	print('Job Complete')
	
