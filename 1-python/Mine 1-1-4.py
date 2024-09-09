for i in range(10):
    print(" ")

grade = float(input("Input a grade: "))

if grade > 120 or grade < 0:
    print("Bad grade!")
elif grade < 120 and grade >= 95:
    print("You got an A")
elif grade < 95 and grade >= 75:
    print("You got a B")
elif grade < 75 and grade >= 50: 
    print("You got a C")
elif grade < 50 and grade >= 0:
    print("You got an F")
