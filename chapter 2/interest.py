  
p = 10000 
n = 12 
r = 0.08 
t = int(input("the number of years: ")) 
final_amount = p * ((1 + r / n ) ** (n * t)) 
print (final_amount)
 