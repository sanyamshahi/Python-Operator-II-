height=float(input("enter your height in cm:  "))
weight=float(input("enter your weight in kh:  "))
BMI=weight/(height/100)**2
print(f"your bmi is {BMI}")

if BMI<=18.4:
    print("you are underweight")
elif BMI<24.9:
    print("you are healthy")
elif BMI<=29.9:
    print("you are over weight")
elif BMI<=34.9:
    print("you are severly overweight")
elif BMI<=39.9:
    print("you are obese")
else:
    print("you are severly obese")
    