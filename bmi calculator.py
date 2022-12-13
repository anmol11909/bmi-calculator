print("Welcome to bmi calculator")
height = float(input("enter your height in m"))
weight = float(input("enter your weight in kg"))
bmi = float(weight)/float(height)**2
print(f"Your bmi is {bmi}")
if bmi<18:
  print("Your are underweight")
elif 25>bmi>18.5:
  print("You have a normal weight")
elif 30>bmi>25:
  print("You are overweight")
elif 35>bmi>30:
  print("You are obese")
else:
  print("You are clinically obese")
  