Deposit = input('Type your money: ')
one_year = int(Deposit)/100*105
two_year = int(one_year)/100*105
ten_year = int(two_year)/100**8*105**8
print(one_year)
print(ten_year)
