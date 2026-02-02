weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in centimeters: "))
hm = height / 100
bmi = weight / (hm ** 2)
print("Your BMI is:", bmi)
if bmi < 18.5:
    print("You are underweight.")
elif bmi < 24.9:
    print("You have a normal weight.")
elif bmi <29.9:
    print("your are overweight.")
else:
    print("your are obese.")


