def sum(a,b):
	total = a + b
	return total
	
total = sum( 1, 2 );
print "sum is ", total


sum = lambda arg1, arg2: arg1 + arg2;

# Now you can call sum as a function
print "Value of total : ", sum( 10, 20 )
print "Value of total : ", sum( 20, 20 )

multiply = lambda arg1, arg2: arg1 * arg2;

print "Product is : ", multiply( 10, 20 )