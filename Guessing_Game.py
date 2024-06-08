import random

def guess_number():
    secret_number=random.randint(1,100)
    attempts=0
    
    while True:
        userguess=int(input("Guess the number between 1 to 100:"))
        attempts+=1
        
        if userguess<secret_number:
            print("Number is too low,try a higher number")
        elif userguess>secret_number:
            print("Numebr is too high,try a lower number")
        else:
            print(f"Success, You have cracked the Secret Number {secret_number} in {attempts} attempts")
            break
if __name__=="__main__":
    guess_number()
            