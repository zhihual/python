# -*- coding: UTF-8 -*-
name = input('请输入你的名字:')
print("欢迎你 %s" % name)
weight=float(input('请输入你的体重（kg）：'))
height=float(input('请输入你的身高（m）：'))
bmi=weight/(height**2)
if 0<bmi<18.5:
    print('你的BMI为'+str(bmi)+',你显得过于苗条了')
elif 18.5<=bmi<25:
    print('你的BMI为'+str(bmi)+',你的身材比较正常')
elif 25<=bmi<28:
    print('你的BMI为'+str(bmi)+',建议你经常锻炼锻炼')
elif 28<=bmi<=32:
    print('你的BMI为'+str(bmi)+',赶紧减点肥')
else:
    print('你的BMI为'+str(bmi)+',你应该马上去减肥')

