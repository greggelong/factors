'''
find factors of integer
'''

def factors(b):
	faclist=[]
	for i in range(1,b+1):
		if b%i == 0:
			faclist.append(i)
	return faclist
	
	
	
	
b= input('Your number please..')
b= float(b) #chang to float to use is_int
	
if b>0 and b.is_integer:
	myfacs = factors(int(b))
else:	
	print('Please enter a positive integer ')
	
print('   the factors {} are {}.'.format(b,myfacs))
if len(myfacs) == 2:
	print('       {} is prime'.format(b))	