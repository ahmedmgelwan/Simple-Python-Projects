# Calculator info
print('''Welcome to our Calculator
With us you can get alot result of a calculation''''')

## Functions ##

# Sum function
def sumition(x,y):
    print(f'The sumition of {x} and {y} is :',x+y) 
# sub function
def sub (x,y):
    print(f'The subtraction of {x} and {y} is :',x-y)
# product function
def prod(x,y):
    print(f'The product of {x} and {y} is: ',x*y)
# division function
def div(x,y):
    print(f'the divion of {x} by {y} is: ', x/y)
# power function
def power(x,y):
    print(f' {x} powered by  {y} is :',x**y)
def resdiv(x,y):
    print(f'the residual division of {x} by {y} is :',x//y)
while True:
  print('''  >> Plesse choose what you want then enter your numbers:
  1- Get sumition of two numbers.
  2- Get Subtraction of two numbers.
  3- Get The product of two numbers.
  4- Get the division of two numbers.
  5- Get the power of two numbers. 
  6- Get residual division of two numbers.
  ''')
  operation = int(input('Enter your choice:>  '))
  if operation > 6 :
    print('Please enter a valid operation!!')
    continue
  x = int(input('Enter your frist number: '))
  y = int(input('Enter your second number: '))
  ### Condtons ####
  if operation == 1:
      sumition(x,y)
  elif operation == 2:
      sub(x,y)
  elif operation == 3:
      prod(x,y)
  elif operation == 4:
      div(x,y)
  elif operation == 5:
      power(x,y)
  elif operation == 6:
      resdiv(x,y)
  ask = input('\n Do you want to do another opreation? ').strip().lower
  if (ask == "yes" or ask == 'y'):
    continue
    
  else:
    print('Good bye , We are happy to see you and we want to see you again')
    quit()