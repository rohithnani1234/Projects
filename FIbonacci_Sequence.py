def fibonacci(n):
  if n<=0:
    return "Invalid input, Please enter a valid input!"
  elif n==1:
    return [0]
  elif n==2:
    return [0,1]
  else:
    sequence=[0,1]
    while len(sequence)<n:
      sequence.append(sequence[-1]+sequence[-2])
    return sequence

n=int(input("Enter number of terms:"))
print(fibonacci(n))