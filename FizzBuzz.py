#Code by Ekta Kapase

print("Let's play FizzBuzz!")

for number in range(1,101):
  if number % 3 == 0:
    if number % 3 ==0 and number % 5 ==0:
      print("FizzBuzz")
    else:
      print("Fizz")
  elif number % 5 ==0:
    if number % 3 ==0 and number % 5 ==0:
     print("FizzBuzz")
    else:
      print("Buzz")
  else:
    print(number)
