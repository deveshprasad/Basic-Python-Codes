secretword='devesh'
guess=''
guesscount=0
guesslimit=3
outofguesses=False
while guess!=secretword and not outofguesses:
    if guesscount<guesslimit:
        guess=input('ENTER GUESS(small alphabets only):')
        guesscount+=1
    else:
        outofguesses=True
if outofguesses:
    print("YOU LOSE MOTHERFUCKER")
else:
    print("YOU WIN")