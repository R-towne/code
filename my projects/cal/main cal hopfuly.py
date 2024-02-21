
num1=float(input("enter a number:"))
num2=float(input("enter a number:"))

numerator=float(input("enter a numerator:"))
denominator=float(input("enter a denominator:"))

length=float(input("enter a length"))
height=float(input("enter a height"))
width=float(input("enter a width"))
base=float(input("enter a base"))

#addition

def addition(num1:float,num2:float)->float:
     """
     arithmtically subtract two number returning their quotient
     
     num1: float- 1st number of the problem 
     num2: float- 2nd number of the problem
     returns: float- num1+num2
     """
     return num1+num2

#subtraction

def subtraction(num1:float,num2:float)->float:
     """
     arithmtically subtract two number returning their quotient
     
     num1: float- 1st number of the problem 
     num2: float- 2nd number of the problem
     returns: float- num1-num2
     """
     return num1-num2

#divison

def division(numerator:float,denominator:float)-> float:
    """
    arithmtically divides two number returning their quotient

    numerator: float-the numerator of the division
    denominatior: float-the denomiatior of the division 
    returns: float the quotient of the two numbers 
    """
    return numerator/denominator

#multiplcation

def multiplcation(num1:float,num2:float)->float:
    """
     arithmtically subtract two number returning their quotient
     
     num1: float- 1st number of the problem 
     num2: float- 2nd number of the problem
     returns: float- num1*num2
     """
    return num1*num2


#area of a rectangle

def rectanglearea(length, width):
    area=length*width
    return area

#area of a triangle

def triangleArea(base, height):
    area= (base*height)/2
    return area

#area of a cube 

def cubeArea(length,width,height):
    area= length*width*height
    return area


#if number is a prime number
def isPrime(n: int)->bool:
    """
    determines if a number is prime or not

    parameters:
    m:int- the number to test for praimalty 

    returns: true if the number is prime otherwise false
    """
    

    if n < 2:
        return False 

    factor=2
    while factor<2:
        if n % factor==0:
            return False
    factor=factor+1
    return True




answer1=subtraction(num1,num2)
print('answer 1 subtraction',answer1)

answer2=division(numerator,denominator)
print('anwser 2 division',answer2)

answer3=multiplcation(num1,num2)
print('answer 3 multiplcation',answer3)

answer4=rectanglearea(length,width)
print("answer 4 rectangle area",answer4)

answer5=triangleArea(base,height)
print("answer 5 triangle area",answer5)

answer6=cubeArea(length,width,height)
print("answer 6 cube area",answer6)










