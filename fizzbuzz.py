"""Write a program that prints numbers from 1 to 50. Apply the following rules  

If a number is divisible by both 3 and 5, print 'FizzBuzz'.   

If a number is divisible by 3 and is odd, print 'FizzOdd'.    

If a number is only divisible by 3, print 'Fizz'.   

If a number is only divisible by 5, print 'Buzz'.   

For all other numbers, print the number itself."""  

"""Function Fizzbuzz that displays numbers from 1 - 50 """
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"  # Divisble by 3 and 5
    if n % 3 == 0 and n % 2 != 0: # Checks for odd multiple of 3
        return "FizzOdd"
    if n % 3 == 0:
        return "Fizz" # Only Multiples of 3
    if n % 5 == 0:
        return "Buzz" # Only Multiples of 5
    return str(n) #Returns string number if it doesn't meet any criteria

for i in range(1, 51):
    print(fizzbuzz(i))