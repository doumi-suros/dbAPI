import pandas

excelFile = 'DBsourceData_220809.xlsx'
baseData = pandas.read_excel(excelFile, sheet_name=0, usecols=[0,1,2,3,4,6,7,8,10])
reptList = pandas.read_excel(excelFile, sheet_name=2, usecols=[0,1,2,3,22])
baseHead = ['DB編號', '中文全名', '中文簡稱', '英文全名', '英文簡稱', '別名1', '別名2', '別名3', '股票簡稱']
reptHead = ['DB編號', '報告檔案夾', 'Date', 'pdfName', 'csvName']


dbNoList = []

#input search key word to get dbNoList
def getDbNoList (searchKey):
    for j in range (1, 9):
        for i in range (1, 1903):
            cellValue = baseData[baseHead[j]].values[i]
            if searchKey.lower() in str(cellValue).lower():
                dbNo = str(baseData[baseHead[0]].values[i])
                if dbNo not in dbNoList:
                    dbNoList.append(dbNo)
            i+=1
        j+=1
    return dbNoList

