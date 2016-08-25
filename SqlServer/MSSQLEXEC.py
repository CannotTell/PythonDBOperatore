# coding=utf-8
from MSSQL import *

__author__ = 'zhukai.jiang'


def test ():
	sqlDBName = "SELECT name, database_id, recovery_model_desc FROM sys.databases"
	sqlTable = "SELECT name FROM sysobjects WHERE xtype='U'"
	HOST = "192.168.107.20"
	USER = "sa"
	PW = "shdl2800"
	DB_NAME = "aZaaS.Framework"

	db = MSSQL(HOST, USER, PW, DB_NAME)
	rows = db.ExecQuery(sqlDBName)
	listDataName = dict()
	listTable = dict()
	ListCloumns = dict()
	for (name, database_id, recovery_model_desc) in rows:
		if name == "master" or name == "tempdb" or name == "model" or name == "msdb":
			continue
		print name
		dbname = name
		sql = "USE [" + name + "];" + sqlTable
		# print sql
		tables = db.ExecQuery(sql)
		# sqlUse = "USE [" + name + "]"
		for (name) in tables:
			print "  " + ', '.join(map(str, name))
			tname = ', '.join(map(str, name))
			sqlCou = "USE [" + dbname + "];" + "SELECT COLUMN_NAME, DATA_TYPE FROM information_schema.columns WHERE table_name='" + tname + "'"

			# db.ExecNonQuery(sqlUse)
			clous = db.ExecQuery(sqlCou)
			for (COLUMN_NAME, TYPE_NAME) in clous:
				print "    " + COLUMN_NAME + ":" + TYPE_NAME

	db.CLOSEDB()


if __name__ == '__main__':
	test()
