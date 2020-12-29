#1

mystring = "This is a DEVOPS ERA"
mylist = [letter for letter in mystring]
print(mylist)

#2 

mystring2 = [num**2 for num in range(0,20) if num%2==0]
print(mystring2)

#3

mystring3 = [x if x%2==0 else 'ODD' for x in range(0,11)]
print(mystring3)


#4

def func(*args):
  print(args)
func(1,2,3,4,5,6,7,8,9)

#5 **kwargs is an dictionary

def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I have {}  {} experience in {} technology'.format(args[0], kwargs['experience'],kwargs['profile']))

myfunc(10,20,30,book='python',profile='cloud',experience='years')