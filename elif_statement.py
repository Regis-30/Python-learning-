# using elif statement
marks = int(input("How many marks did you get?: "))

if marks >= 70:
    print("Distinction")
elif marks >= 50 and marks < 70:
    print("Pass")
else:
    print("Fail")
    print("Sorry!...")
