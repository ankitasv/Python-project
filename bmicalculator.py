print("This is a BMI calculator\n ")
name=input("Enter your Name: ")
height=float(input("Enter  your Height in meter  :"))
weight=float(input("Enter your  weight in kg :"))
bmi=weight/(height/100)**2
if (bmi<16):
 print(f"{name},You are  underweight.Your BMI is {bmi}")
elif (bmi >= 16 and bmi<18.5):
      print(f"{name},You are  underweight.Your BMI is {bmi}") 
elif(bmi >= 18.5 and bmi<25):
        print(f"{name},You are  Normal and Healthy.Your BMI is {bmi}")
        
elif(bmi >= 25 and bmi < 35):
       print(f"{name},You are  overweight.Your BMI is {bmi}")
        
elif(bmi >= 35):
        print(f"{name},You are  obase,please do exercise.Your BMI is {bmi}")
    
   