import random

num1=random.randint(1,6)
num2=random.randint(1,6)
bet_amount=int(input("Please enter the amount you wish to bet: "))
bet_eo=(input("Please enter your bet - 'EVEN' or 'ODD': ")).upper()
while bet_eo!="EVEN" and bet_eo!="ODD":
    bet_eo=(input("Please enter either 'EVEN' or 'ODD'")).upper()
bet_total=num1+num2
even_or_odd=''
bet_win=2*bet_amount
house_fee=bet_amount/10
bet_right=''

if bet_total%2==0:
    even_or_odd="EVEN"
else:
    even_or_odd="ODD"

if even_or_odd==bet_eo:
    bet_right="won"
else:
    bet_right="lost"



print(f"You threw a {num1} and a {num2}, making a total of {bet_total}.  {bet_total} is {even_or_odd} so you {bet_right}.")
if bet_right=="won":
    print(f"You win {bet_win}, less a house fee of {house_fee}")


