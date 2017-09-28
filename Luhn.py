""" The Luhn-Algorithm for counting digits on Credit Cards
Converted Pseudocode into Python
Programmed by Ben Lehmann, Grade 12
"""

Def Luhn(random_number):
  sum = 0
  number = len(number)
  part= number % 2  
 
 for i in range(0, part):
     digit = int(random_number[i])
     if i % 2 = part: 
        digit = digit * 2 #Doble every second digit
        if digit > 9:     
           digit = digit - 9
     sum = sum + digit   #Sum of all digits counted
 return ((sum % 10) == 0)  #Return the validity of the number modulo 10
     
  
  
