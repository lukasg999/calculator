
#asking for mode
mode = input("Select your mode: a for addition, s for subtraction, m for multiplication, d for divison, c for temperature conversion")

#for a s m and d 
if mode in ["a", "s", "m", "d"]:
    number1 = float(input("Your first number:"))
    number2 = float(input("Your second number:"))
    if mode == "a":
         print(number1 + number2)
    elif mode == "s":
         print(number1 - number2)
    elif mode == "m":
         print(number1 * number2)
    elif mode == "d":
         print(number1 / number2)

#for c      
elif mode == "c":
    temperature = float(input("Temperature you want to convert in C"))
    print(temperature * 9/5 + 32)
#what happens else
else:
    print("please check you inputs again")
  
