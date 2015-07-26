import sys

print "Welcome to the Fizzbuzz Game!" 

# defining n. 
# first option command line argument. command line can have: 1 argument (no n), 2 arguments (n) or more than 2 arguments (mistake/error)
# In case of 2 arguments, the second argument is n. otherwise n will be equal to user's input. 
#possible problems: argument or input should be an integer in type string. If that is not the case than we have a problem.  
# we are instructed to handel error.  
# it will arise when we try to convert from type string to type integer. 
if len(sys.argv)==2:
    n=sys.argv[1]
else:                               #This will execute if the user provide n, or provided more than 2 arguments.  
    n=raw_input ("Please enter a number. We will play Fizzbuzz up to the number you choose.     ")
while True: 
    try:
        n=int(n)
        break
    except Exception, e:
        #while (type(n)==int)==False:
        n=raw_input ("Please enter a number. We will play Fizzbuzz up to the number you choose.     ")
            #try:
        #        n=int(n)
         #   except Exception, e:
          #      pass  

# printing fizzbuzz up to n
print "Fizz buzz counting up to {}".format (n)
for num in range (1,n+1):
    if (num%5==0) & (num%3==0):
        print("Fizzbuzz")
    elif num%5==0:
        print("Buzz")
    elif num%3==0:
        print("Fizz")
    else:
        print(num)
        

