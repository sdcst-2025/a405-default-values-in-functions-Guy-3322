#!python3
# Currency Conversion
"""
Most of the time, in Canada, we convert our money
into USD. But we could also travel to other places

Create a function that accepts:
required: 1 positional argument - amount of money to convert
optional:
1 argument: currency to convert from default CAD
1 argument: currency to covnert to default USD

Conversion rates to use:
1 USD = 1.35 CAD
1 BTC = 62000 USD
1 USD = 1.51 AUD
1 USD = 155 Yen
1 Eur = 1.07 USD

Units must be in ["USD","CAD","BTC","AUD","Yen","Eur"]
"""

def convert(a,b =" ",c=" "):
   t=0
   if b == " " and c==" ":
       t= round(a/1.35,2)
   
   if b == "USD" and c==" ":
       t= round(a,2)
    
   if b == "USD" and c=="CAD":
     t= round(a*1.35,2)
  
   if b == "BTC" and c==" ":
       t= round(a*62000,2)
    
   if b == "BTC" and c=="CAD":
       t= round(a*62000*1.35,2)
       
   if b == "BTC" and c=="Eur":
       t= round(a*62000/1.07,2)
       

   print(t)
   
   
   return t


if __name__ == "__main__":
    assert convert(1.35) == 1
    assert convert(1,"USD") == 1
    assert convert(1,"USD","CAD") == 1.35
    assert convert(1,"BTC") == 62000
    assert convert(1,"BTC","CAD") == 83700
    assert convert(1,"BTC","Eur") == 57943.93
    
    
