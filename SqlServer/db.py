# coding=gbk
import sys
import pymssql

# 尝试数据库连接
try:
	conn = pymssql.connect(host = "192.168.107.20", user = "sa", password = "shdl2800", database = "aZaaS.Framework")
except pymssql.OperationalError, msg:
	print "error: Could not Connection SQL Server!please check your dblink configure!"
	sys.exit()
else:
	cur = conn.cursor()

# 查询数据库
query = "select name, database_id, recovery_model_desc  from sys.databases"
cur.execute(query)
conn.commit
rows = cur.fetchall()

print ('                      ')
print ('-----结果返回中------- ')
print ('                     ')
for (name, database_id, recovery_model_desc) in rows:
	database_id = bytes(database_id)  # 将int转换转换为字符串类型
	print ('数据库名:' + str(name) + ';')
	print ('数据库id:' + database_id)
	print ('数据库恢复模式:' + str(recovery_model_desc))
	print ('                      ')
print ('-----以上是所有结果!------- ')

# 关闭连接，释放资源


cur.close()
conn.close()
