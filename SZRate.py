# Caculate SH Stock rate exchange

# Step

Delta = 0.025

CurBase  = 11961

MyBase = 12330

InvestBase = 780000

CurMarketValue = 360000

#

CurScore = (CurBase-MyBase)/MyBase*100
CurScore = round(CurScore, 2)

MatchGap = (MyBase-CurBase)/CurBase*100
MatchGap = round(MatchGap, 2)

CurRate = CurMarketValue/InvestBase*100
CurRate = round(CurRate, 2)


Step = 1/Delta

Step = int(Step)

Index = 1
IncValue = [0]
DecValue = [0]

temp = [0]

for Index in range(1,Step):
    temp[0] = CurBase*(1+Index*Delta)
    IncValue += temp
    temp[0] = CurBase*(1-Index*Delta)
    DecValue += temp
    Index+=1

print("Step =", Step)
print("CurBase = ", CurBase, "MyBase = ", MyBase, "CurScore =", CurScore,"%")
print("CurMaket =", CurMarketValue, "Total = ", InvestBase, "CurRate = ", CurRate, "%")

Index = 1

print("Increase way")
for Index in range(1,Step):
    print("step = ", round(Index*Delta*100,2),"%", " = ", int(IncValue[Index]));
    Index+=1

print("Decrease way")
for Index in range(1,Step):
    print("step = -", round(Index*Delta*100, 2),"%"," = ", int(DecValue[Index]));
    Index+=1
        
    


