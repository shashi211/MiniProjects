
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################
import random
def get_guess():
    return list(input("What is your guess? "))

def generate_code():
    digit=[str(num) for num in range(10)]
    random.shuffle(digit)
    return digit[:3]

def generate_clues(code,user_guess):
    if(code==user_guess):
        return 'code cracked!'
    clues=[]
    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("Match")
        elif num in code:
            clues.append("Close")
    if clues==[]:
        return['nope']
    else:
        return clues

print("Welcome CodeBreaker!")
secret_code = generate_code()
clue_report=[]
while clue_report != 'code cracked!':
    guess = get_guess()
    clue_report = generate_clues(guess,secret_code)
    print('here is the result of your guess')
    for clue in clue_report:
        print(clue)
