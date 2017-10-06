  
day = 24 
h = int(input("type number of hours to wait: ")) 
now = int(input("type number of now: ")) 
b = (now + h) % day
print ("alarm:" +str(b)) 
if b < 12: 
    print (str(b)+" am") 
else:
    
    print(str(b-12) + " pm")
