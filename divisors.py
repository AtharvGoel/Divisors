#divisors

from timeit import default_timer as timer

list = []

num = int(input('Enter a number: '))

start = timer()

if num % 2 == 0:
	x = range(1, num//2+1)
else:
	x = range(1, (num + 1)//2, 2)
	
for a in x:
	if num % a == 0:
		list.append(a)
		
list.append(num)
		
if list == [1, num]:
	print('*' + str(num) + ' is a prime number.*')
else:
	print('Divisors of ' + str(num) + ' are: ')
	print(list)
		
print('\nProgram took ' + str(timer() - start) + ' seconds.')