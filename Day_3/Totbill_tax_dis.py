'''Print a programme to store 2 products cost 1000, 2000 into 2 variables these are p1,p2
 Calculate total bill, stock into one variable called total bill on total bill.
 Calculate 20% discount and store into one variable called discount after discount calculate 30% tax on total bill and
 display total bill with help of message and variable.'''
p1=1000
p2=2000
tot= p1+p2
dis=tot*.2
disbil=tot-dis
tax=disbil*.3
final=disbil+tax
print('Final bill=', final)
