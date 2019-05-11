#divisors

from timeit import default_timer as timer

def original():
num = int(input('Enter a number: '))

start = timer()

print('Divisors of ' + str(num) + ' are: ')

x = range(0, num)
y = []
z = []
w = []
for a in x:
	if a == -1 or a ==0 or a ==1:
		z.append(a)
		w.append(a)
		continue
	if num%a == 0:
		y.append(a)
		w.append(a)
		
	else:
		z.append(a)
		w.append(a)

for b in y:
	print(b)
	
if z == w:
	print('*' + str(num) + ' is a prime number.*')
	
print('\nProgram took ' + str(timer() - start) + ' seconds.')
	
input('\nPress Enter to continue')