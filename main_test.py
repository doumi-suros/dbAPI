import sub_excel

import pandas


reptPath = 'C:\\SUROS_BI\\Panorays_Reports_220810A\\'
excelFile = 'DBsourceData_220810.xlsx'
baseData = pandas.read_excel(excelFile, sheet_name=0, usecols=[0,1,2,3,4,6,7,8,10])
reptList = pandas.read_excel(excelFile, sheet_name=2, usecols=[0,1,2,3,22])
baseHead = ['DB編號', '中文全名', '中文簡稱', '英文全名', '英文簡稱', '別名1', '別名2', '別名3', '股票簡稱']
reptHead = ['DB編號', '報告檔案夾', 'Date', 'pdfName', 'csvName']

baseDataF = pandas.read_excel(excelFile, sheet_name=0, usecols=[0,16,11,13,14])
baseHeadF = ['DB編號', '產業別', '上市櫃', '百大', '附註1']

cateListHtml = ['教育知識', '金融業', '政府機關', '能源環境', '醫藥業', '電網資訊', '傳統產業', '服務業', '百貨零售', '電子科技', '其它']
cateList = ['edu', 'fin', 'gov', 'life', 'medi', 'net', 'manu', 'serv', 'stor', 'tech', 'com']    #usecols = [16]
stockList = ['上市', '上櫃', '興櫃']    #usecols = [11]
rankList = ['100', '300']    #usecols = [13]
tw50 = ['台50']    #usecols = [14]
filterKeys = [cateListHtml, stockList, rankList, tw50]

"""
searchKey = '圖書館'

dbNoList = sub_excel.getDbNoList(searchKey)
webList = sub_excel.getWebList(dbNoList)
"""

filterKey = '其它'

dbNoListF1 = sub_excel.getDbNoListF1 (filterKey)
print (len(dbNoListF1), dbNoListF1)


