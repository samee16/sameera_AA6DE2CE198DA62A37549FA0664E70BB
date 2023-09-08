# Implement a recursive function to calculate the factorial of a given number
def factorial(x):
  if x==0 or x==1:
    return 1
  else:
    return(x*factorial (x-1))

x=int(input("Enter number:"))
print("Factorial of given number is :",factorial(x))
            