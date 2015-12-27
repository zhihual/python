#计算分级A基金的隐含收益率

# Input area for calculate settings
# 150171 证券A 3-14日为结算日

# 输入参数
# 利率规则
#RatePolicy = 0.03 # 3%的约定收益率
# 当前价格
CurPrice = 0.957
# 当前净值
CurNetValue = 1.0607
# 距离到期时间
MonthToFicalYearEnd = 12
# 当年一年定期存款利率
CurYearRate = 0.05  
# 下一轮周期一年定期存款利率
NextYearRate = 0.05 
# 参考隐含收益率
CurMaxReturnRate = 0.0498





# 计算过程
Discount = (CurNetValue - CurPrice)/CurNetValue*100
Discount = round(Discount, 2)

print("CurPrice =", CurPrice,"CurNetValue =", CurNetValue)
print("CurYearRate =", CurYearRate*100, "%", "NextYearRate=", NextYearRate*100, "%", "Discount=",Discount,"%")

# Step1: 计算到期净值
#YearEndNetValue= CurNetValue + 1*(CurYearRate)*MonthToFicalYearEnd/12
#YearEndNetValue = round(YearEndNetValue, 4)
#NetGap = round(YearEndNetValue-CurNetValue, 4)

# Step2: 计算定折到期收益净值
#FiscalTimeEarn = round(YearEndNetValue - 1, 4)
#print("YearEndNetValue =", YearEndNetValue, "NetGap =", NetGap,"FiscalTimeEarn = ",FiscalTimeEarn)

# Step3: 计算定折到期收益率
#InvestReturnRate = FiscalTimeEarn/CurPrice*100
#InvestReturnRate = round(InvestReturnRate, 2)
#print("InvestReturnRate =", InvestReturnRate, "%");

#InvestReturnRate*=0.91
#InvestReturnRate = round(InvestReturnRate,2)
#print("Realistic ReturnRate=", InvestReturnRate,"%" );

#2016年全年收益率
NextYearEarRate = (NextYearRate)*(12-MonthToFicalYearEnd)/12+(CurYearRate)*MonthToFicalYearEnd/12
NextYearEarRate = round(NextYearEarRate*100, 2)
print("NextYearEarRate = ",NextYearEarRate, "%")

# 计算隐含收益率
UniteRate = (NextYearRate)/(CurPrice-(CurNetValue-1)+(MonthToFicalYearEnd/12)*(NextYearRate-CurYearRate))
UniteRate = UniteRate*100
UniteRate = round(UniteRate, 3)
print("HideReturnRate = ", UniteRate, "%")

#计算合理价格

EstimateValue = CurYearRate/CurMaxReturnRate+CurNetValue-1

print("CurMaxReturnRate =", round(CurMaxReturnRate*100,2),"%")
print("EstimateValue =", round(EstimateValue,3))
print("CurPrice =",round(CurPrice,3), "Cur/Est =", round(CurPrice/EstimateValue*100,3),"%")


