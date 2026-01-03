'''Write a programme to take 2 products that is p1,p2 with 1000,2000 on p1-10% of discount on p2-20% discount
print find bill to pay after discount'''
p1=1000
p2=2000
dp1=p1*.1
dp2=p2*.2
fp1=p1-dp1
fp2=p2-dp2
fb=fp1+fp2
print('Final bill=', fb)
