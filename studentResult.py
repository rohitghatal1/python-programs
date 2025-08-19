name = input("Enter your name: ")
marks = float(input("Enter your marks: "))

if marks >= 40:
    print(f"Congratulation {name}, your are passed")

    if marks >= 90:
        print(f"Excellent performance {name}! You nailed it")
    elif marks >= 80:
        print("Great job, that is awesome")
    elif marks >=60:
        print("Well done, you are doing good")
    elif marks >=50:
        print("Goood makrs but you can do better")
    else:
        print("Poors marks you should work hard")
else:
    print(f"Sorry to inform you that you failed the exam, better luck next time")