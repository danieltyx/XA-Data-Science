import os

# Functions

def fizzbuzz(start=1, stop=100):
    ''' 
    >>> fizzbuzz(1, 5)
    1
    2
    Fizz
    4
    Buzz
    
    >>> fizzbuzz(12, 15)
    Fizz
    13
    14
    FizzBuzz
    '''
    # START CODE HERE
    for i in range(start,stop+1):
        if i%15==0:
            print("FizzBuss")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)


# Main Execution

if __name__ == '__main__':
    fizzbuzz()