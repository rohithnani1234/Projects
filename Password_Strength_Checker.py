import re
def evvaluate_password(password):
  strength=0
  if len(password)>=8:
    strength+=1
  if re.search(r"[A-Z]",password):
    strength+=1
  if re.search(r"[a-z]",password):
    strength+=1
  if re.search(r"\d",password):
    strength+=1
  if re.search(r"\W",password):
    strength+=1
  
  if strength==1:
    return "Weak"
  elif strength==2:
    return "Medium"
  elif strength==3:
    return "Strong"
  else:
    return "Very Strong"

password=input("Enter Password:")
print(f"The strength of your password is: {evvaluate_password(password)}")