import pandas


reptPath = 'C:\\SUROS_BI\\Panorays_Reports_220809A\\'
excelFile = 'DBsourceData_220809.xlsx'
baseData = pandas.read_excel(excelFile, sheet_name=0, usecols=[0,1,2,3,4,6,7,8,10])
reptList = pandas.read_excel(excelFile, sheet_name=2, usecols=[0,1,2,3,22])
baseHead = ['DB編號', '中文全名', '中文簡稱', '英文全名', '英文簡稱', '別名1', '別名2', '別名3', '股票簡稱']
reptHead = ['DB編號', '報告檔案夾', 'Date', 'pdfName', 'csvName']


dbNoList = []

#input search key word to get dbNoList
def getDbNoList (searchKey):
    for j in range (1, 9):    #BaseData search columns length
        for i in range (1, 1903):    #BaseData search rows length
            cellValue = baseData[baseHead[j]].values[i]    #get cell value on columns by rows
            if searchKey.lower() in str(cellValue).lower():    #if cell contains search key
                dbNo = str(baseData[baseHead[0]].values[i]).strip()    #get dbNo
                if dbNo not in dbNoList:    #exclude same dbNo
                    dbNoList.append(dbNo)    #add new dbNo to list
            i+=1
        j+=1
    return dbNoList



#input dbNo List to get webList
def getWebList (dbNoList):
    countDbNo = len (dbNoList)
    webList = []
    for i in range (0, countDbNo):    #get web List by dbNoList orders
        for m in range (1, 1673):    #ReportList search rows length
            aList = []
            reptCell = reptList[reptHead[0]].values[m]    #get cell value on dbNo col by rows
            if str(dbNoList[i]).strip() in str(reptCell):    #if find match dbNo
                reptDate = reptList[reptHead[2]].values[m].strip()    #get report date
                aList.append(reptDate)
                
                reptFolder = reptList[reptHead[1]].values[m].strip()    #get report dir
                reptPdf = reptList[reptHead[3]].values[m].strip()    #get pdf file name
                if reptPdf == 'no.pdf':
                    pdfPath = False
                else:
                    pdfPath = reptPath + reptFolder + '\\' + reptPdf    #get pdf path
                aList.append(pdfPath)
                
                reptCsv = reptList[reptHead[4]].values[m].strip()    #get csv file name
                if reptCsv == 'no.csv':
                    csvPath = False
                else:
                    csvPath = reptPath + reptFolder + '\\' + reptCsv    #get csv path
                aList.append(csvPath)
                
                for n in range (1, 1903):    #basedata search rows length
                    baseCell = baseData[baseHead[0]].values[n].strip()    #get cell value on dbNo col by rows
                    if str(dbNoList[i]).strip() in str(baseCell):    #if find match dbNo
                        comFull = baseData[baseHead[1]].values[n].strip()    #get comFull cell value
                        if comFull == None:    #if no chinese full name
                            comFull = baseData[baseHead[4]].values[n].strip()    #company = eng short name
                        aList.insert(0, comFull)
                        break
                    n+=1
    
                webList.append(aList)
            m+=1    
        i+=1    
    return webList






