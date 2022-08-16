import sub_excel


#function 1: by search
#input = searchKey
searchKey = '圖書館'

dbNoList = sub_excel.getDbNoList(searchKey)
webList = sub_excel.getWebList(dbNoList)

for i in range (0, len(webList)):
    for j in range (0, 4):
        print (webList[i][j])
        j+=1
    i+=1


#function 2: by filters
#input = select filters
filterKeys = [['金融業','傳統產業'], [], ['100'], ['台50']]

dbNoListFsA = sub_excel.dbNoListFs (filterKeys)
if len(dbNoListFsA) == 0:
    print ('SORRY, NO DATA')
webList = sub_excel.getWebList(dbNoListFsA)

for i in range (0, len(webList)):
    for j in range (0, 4):
        print (webList[i][j])
        j+=1
    i+=1

