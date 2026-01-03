'''Write a programe to take 2 products p1,p2 1000, 2000 on p1-10% of discount on p2- 20% od discount and tax of 30%'''

p1=1000
p2=2000
dp1=p1*.1
dp2=p2*.2
fp1=p1-dp1
fp2=p2-dp2
tp1=fp1*.3
tp2=fp2*.3
fdp1=fp1+tp1
fdp2=fp2+tp2
fb=fdp1+fdp2
print('Final bill=',fb)