import random

class boom():
    def __init__(self):
        self.name = 'This is a bomb. You need to unlock your password as soon as possible。'
        
    def jiesuo(self):
        boom_key = random.randint(1,10)
        boom_stat = 1
        looptime = 1
        while looptime<=3:
            inkey = input('Bomb blast, please enter the password to remove the bomb! You still have a {} chance'.format(4 - looptime))
            if int(inkey) == boom_key:
                boom_stat = 0
                break
        
            if int(inkey) > boom_key:
                print('The password seems too big。')
    
            if int(inkey) < boom_key:
                print('The password seems too samll。')
        
            looptime = looptime +1

        if boom_stat == 0:
            print("Congratulations! Get rid of the bomb!")
        else:
            print("/done. The bomb explodes. You're dead! Game over...")