# -*- coding: UTF-8 -*-  
# 运行接受中文字符


# Step1. 数据分类，不同的号分到不同的sheet里面去。 
#        1. 要发现多少个代码
#        2. 然后保存
# 1. 打开，读取一行 判断是否以及是获取过的代码。
# 2. 若不存在，创建新的sheet,添加新代码到已知sheet名字列表里.
# 3. 保存到sheet里面
# 4. 记录以及获取的代码，
# 5. 重复 #1知道数据源的row已经读完

from openpyxl import load_workbook
from openpyxl import Workbook
import os

src_wb_name = '1.xlsx'

src_wb = load_workbook(src_wb_name)

active_src_ws = src_wb.active

src_row_num = len(tuple(active_src_ws.rows))

src_columns_num = len(tuple(active_src_ws.columns))

print("src_row_num=:", src_row_num, "src_columns_num:", src_columns_num)



# 定义一个如何从数据源中获取需要信息的位置
src_stock_date = 'A'
src_stock_id_row = 'B'
src_stock_name_row = 'C'
src_stock_op_row = 'D'
src_stock_deal_num_row = 'E'
src_stock_deal_price_row = 'F'
src_stock_hold_num = 'H'
src_stock_deal_broker_fee_row = 'J'
src_stock_deal_tax_row = 'K'



dst_wb_name= 'test.xlsx'
dst_wb = Workbook()

active_dst_ws = dst_wb.active

active_dst_ws.title = "week analysis"
active_dst_ws.sheet_properties.tabColor = "1072BA"

# 定义一个空的list,用来存放股票代码
dst_stock_id_list = [] 

# 先生成 dst的第一行的标题栏
dst_stock_id_row = 'A'
dst_stock_name_row = 'B'
dst_stock_op_row = 'C'
dst_stock_deal_num_row = 'D'
dst_stock_deal_price_row = 'E'
dst_stock_deal_broker_fee_row = 'F'
dst_stock_deal_tax_row = 'G'
dst_stock_hold_num = 'H'
dst_stock_deal_date = 'I'



#active_dst_ws[dst_stock_id_row+'1'] = '股票代码'
#active_dst_ws[dst_stock_name_row+'1'] = '股票名称'
#active_dst_ws[dst_stock_op_row+'1'] = '买卖'
#active_dst_ws[dst_stock_deal_num_row+'1'] = '成交数量'
#active_dst_ws[dst_stock_deal_price_row+'1'] = '成交价格'
#active_dst_ws[dst_stock_deal_broker_fee_row+'1'] = '券商佣金'
#active_dst_ws[dst_stock_deal_tax_row+'1'] = '印花税'

# 外面应该是个循环
for src_rowidx in range (2, src_row_num):
	sheet = active_dst_ws
	# 1. 打开，读取一行 判断是否以及是获取过的代码。
	temp_stock_id = active_src_ws[src_stock_name_row+str(src_rowidx)].value
	#print("temp_stock_id:", temp_stock_id)
	#2. 若不存在，创建新的sheet,添加新代码到已知sheet名字列表里.
	if temp_stock_id in dst_stock_id_list:
		sheet = dst_wb.get_sheet_by_name(temp_stock_id);
	else:
		#print(str(temp_stock_id))
		sheet = dst_wb.create_sheet(temp_stock_id);
		sheet.sheet_properties.tabColor = "1072BA"
		
		sheet[dst_stock_id_row+'1'] = '股票代码'
		sheet[dst_stock_name_row+'1'] = '股票名称'
		sheet[dst_stock_op_row+'1'] = '买卖'
		sheet[dst_stock_deal_num_row+'1'] = '成交数量'
		sheet[dst_stock_deal_price_row+'1'] = '成交价格'
		sheet[dst_stock_deal_broker_fee_row+'1'] = '券商佣金'
		sheet[dst_stock_deal_tax_row+'1'] = '印花税'
		sheet[dst_stock_hold_num+'1'] = '可用余额'
		sheet[dst_stock_deal_date+'1'] = '成交日期'
		# 4. 记录以及获取的代码，
		dst_stock_id_list.append(temp_stock_id)
		
	
	#插入到dst的后面
	sheet_row_num = len(tuple(sheet.rows))
	sheet_row_num = sheet_row_num + 1
	# 3. 保存到sheet里面
	sheet[dst_stock_id_row+str(sheet_row_num)].value = active_src_ws[src_stock_id_row+str(src_rowidx)].value
	sheet[dst_stock_name_row+str(sheet_row_num)].value = active_src_ws[src_stock_name_row+str(src_rowidx)].value
	sheet[dst_stock_op_row+str(sheet_row_num)].value = active_src_ws[src_stock_op_row+str(src_rowidx)].value
	sheet[dst_stock_deal_num_row+str(sheet_row_num)].value = active_src_ws[src_stock_deal_num_row+str(src_rowidx)].value
	sheet[dst_stock_deal_price_row+str(sheet_row_num)].value = active_src_ws[src_stock_deal_price_row+str(src_rowidx)].value
	sheet[dst_stock_deal_broker_fee_row+str(sheet_row_num)].value = active_src_ws[src_stock_deal_broker_fee_row+str(src_rowidx)].value
	sheet[dst_stock_deal_tax_row+str(sheet_row_num)].value = active_src_ws[src_stock_deal_tax_row+str(src_rowidx)].value
	sheet[dst_stock_hold_num+str(sheet_row_num)].value = active_src_ws[src_stock_hold_num + str(src_rowidx)].value
	sheet[dst_stock_deal_date+str(sheet_row_num)].value = active_src_ws[src_stock_date+str(src_rowidx)].value
	
os.remove(dst_wb_name)	
dst_wb.save(dst_wb_name)