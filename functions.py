def greeting(name):
    print (f"Hello {name}")


add =  lambda x,y : x + y

userName = input("enter your name: ")

greeting(userName)
firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number:: "))

sum = add(firstNumber, secondNumber)

print(sum)