# coding=gbk
import sys
import pymssql

# �������ݿ�����
try:
	conn = pymssql.connect(host = "192.168.107.20", user = "sa", password = "shdl2800", database = "aZaaS.Framework")
except pymssql.OperationalError, msg:
	print "error: Could not Connection SQL Server!please check your dblink configure!"
	sys.exit()
else:
	cur = conn.cursor()

# ��ѯ���ݿ�
query = "select name, database_id, recovery_model_desc  from sys.databases"
cur.execute(query)
conn.commit
rows = cur.fetchall()

print ('                      ')
print ('-----���������------- ')
print ('                     ')
for (name, database_id, recovery_model_desc) in rows:
	database_id = bytes(database_id)  # ��intת��ת��Ϊ�ַ�������
	print ('���ݿ���:' + str(name) + ';')
	print ('���ݿ�id:' + database_id)
	print ('���ݿ�ָ�ģʽ:' + str(recovery_model_desc))
	print ('                      ')
print ('-----���������н��!------- ')

# �ر����ӣ��ͷ���Դ


cur.close()
conn.close()
