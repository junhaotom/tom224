import random
password = random.randint(1,100)
#print(password)
print('------Time Bomb！-----')
guess = 0
while guess != password:
    temp = input('The time is running out：')
    guess = int(temp)
    if guess > password:
        print('Wrong number(Hint: too big)！')
    elif guess < password:
        print('Wrong number(Hint: too small)！')
if guess == password:
    print('Right！')
    print('Good game well play')