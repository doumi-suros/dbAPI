import sub_excel
import sub_msc

searchKey = '中山'

dbNoList = sub_excel.getDbNoList(searchKey)
print (dbNoList)

webList = sub_excel.getWebList(dbNoList)
print (webList)




