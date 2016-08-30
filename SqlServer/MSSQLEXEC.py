# coding=utf-8
from MSSQL import *
from SQLITE import *
from LOGRECORD import *

__author__ = 'zhukai.jiang'


def test ():
	sqlDBName = "SELECT name, database_id, recovery_model_desc FROM sys.databases"
	sqlTable = "SELECT TABLE_SCHEMA, TABLE_NAME FROM INFORMATION_SCHEMA.TABLES"
	HOST = "192.168.107.20"
	USER = "sa"
	PW = "shdl2800"
	DB_NAME = "aZaaS.Framework"
	LOG_NAME = "DB OPERATE ERROR"
	LOG_FILE_NAME = "DB_ERROR_LOG.log"
	log = LOGRECORD(LOG_NAME, LOG_FILE_NAME).GetLogger()

	sqlitePATH = os.getcwd() + "\SQLSERVER\\"

	db = MSSQL(HOST, USER, PW, DB_NAME)

	rows = db.ExecQuery(sqlDBName)

	for (name, database_id, recovery_model_desc) in rows:
		if name == "master" or name == "tempdb" or name == "model" or name == "msdb":
			continue
		print name
		dbname = name
		sql = "USE [" + name + "];" + sqlTable
		# print sql
		try:
			tables = db.ExecQuery(sql)
		except:
			log.info("SELECT TABLES ERROR, DB NAME: " + dbname)
			continue
		# sqlUse = "USE [" + name + "]"
		path = sqlitePATH + dbname + ".db"
		dbLite = SQLITE(path)

		for (TABLE_SCHEMA, TABLE_NAME) in tables:
			# print "  " + ', '.join(map(str, name))
			# tname = ', '.join(map(str, name))
			tname = TABLE_SCHEMA + '.' + TABLE_NAME
			sqliteName = TABLE_SCHEMA + '_' + TABLE_NAME
			print tname
			sqlCou = "USE [" + dbname + "];" + "SELECT name FROM SysColumns WHERE id = OBJECT_ID('" + tname + " ')"

			# db.ExecNonQuery(sqlUse)
			try:
				clous = db.ExecQuery(sqlCou)
			except:
				log.info("SELECT TABLE " + tname + " ERROR")
				continue
			sqliteStr = ''
			for (name) in clous:
				name = ', '.join(map(str, name))
				print "    " + name
				sqliteStr = sqliteStr + strProcess(name) + ','
			sqliteStr = sqliteStr[: -1]
			print "sql:" + str(len(clous)) + sqliteStr
			dbLite.ExecNonQuery("CREATE TABLE " + strProcess(sqliteName) + "(" + sqliteStr + ")")
			tempsql = "USE " + dbname + ";SELECT * FROM " + tname
			try:
				curs = db.ExecQuery(tempsql)
			except:
				log.info("CREATE TABLE " + tname + " ERROR IN SQLITE")
				continue

			insertSQl = "INSERT INTO " + strProcess(sqliteName) + " VALUES (" + "?," * (len(clous) - 1) + "?)"
			for i in curs:
				try:
					dbLite.INSERT(insertSQl, i)
				except:
					a = []
					for val in i:
						if val == None:
							a.append("")
							continue
						a.append(str(val))
					try:
						dbLite.INSERT(insertSQl, a)
					except:
						log.info(tname + " TABLE INSERT ERR")
						continue
		dbLite.CLOSEDB()
	db.CLOSEDB()


def strProcess (str):
	return "[" + str + "]"


if __name__ == '__main__':
	test()
