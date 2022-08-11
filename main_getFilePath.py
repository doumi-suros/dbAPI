import sub_excel

searchKey = '圖書館'

dbNoList = sub_excel.getDbNoList(searchKey)

webList = sub_excel.getWebList(dbNoList)

for i in range (0, len(webList)):
    for j in range (0, 4):
        print (webList[i][j])
        j+=1
    i+=1



