w1="all"
w2="work"
w3="and"
w4="no"
W5="play"
w6="makes"
w7="jack"
w8="a"
w9="dull"
w10="boy"
print(w1+w2+w3+w4+w5+W6+W7+W8+W9+W10)
 
  
  
  
  
  
  p = 10000 
 n = 12 
 r = 0.08 
 t = int(input("the number of years: ")) 
 final_amount = p * ((1 + r / n ) ** (n * t)) 
 print (final_amount) 
   day = 24 
 h = int(input("type number of hours to wait: ")) 
 now = int(input("type number of now: ")) 
 b = now + (h % day) 
 print ("alarm:" +str(b))
  
  
  
  day = 24 
 h = int(input("type number of hours to wait: ")) 
 now = int(input("type number of now: ")) 
 b = now + (h % day) 
 print ("alarm:" +str(b)) 
 if b < 12: 
 print (str(b)+" am") 
 else: 
 print(str(b-12) + " pm")
