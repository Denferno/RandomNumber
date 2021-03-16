import random

def randomfunc():
    num1 = int(input("Nummer 1: "))
    num2 = int(input("Nummer 2: "))
    if num1 > num2:
        res = random.randint(num2, num1)
    else:
        res = random.randint(num1, num2)
    if res >= 3:
        return res
    elif res == 1:
        return ("""
          _____
         / _  |
        /_/ | |
            | |
            | |
            | |
            |_|"""
      )
    elif res == 2:
        return ("""
            __________ 
            |_______ |   
            _______| | 
            | _______| 
            | |_______ 
            |________|  
    """)



print(randomfunc())