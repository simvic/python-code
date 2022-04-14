print("Hello welcome to my BMI calculator")

# this line of code converts the user input to a float
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

answer = weight / height ** 2

# this section rounds of the answer to 1 decimal place
bmi = round(answer)

if bmi > 0:
    if bmi <= 18.5:
        print(f"Your BMI is {bmi}, you are underweight.")
    elif bmi <= 24.9:
        print(f"Your BMI is {bmi}, you have a normal weight.")
    elif bmi <= 29.9:
        print(f"Your BMI is {bmi}, you are slightly overweight.")
    elif bmi <= 34.9:
        print(f"Your BMI is {bmi}, you are obese.")
    elif bmi > 35:
        print(f"Your BMI is {bmi}, you are clinically obese.")
    else:
        print("sorry try again")
else:
    print("Error! please try again")


# Finally click "Run" to execute the tests
