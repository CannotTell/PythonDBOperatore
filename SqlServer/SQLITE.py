#!/usr/bin/env python
# -*- coding: utf8 -*-
__author__ = 'zhukai.jiang'

import sqlite3, os


class SQLITE:
	"""
	对pymssql的简单封装
	pymssql库，该库到这里下载：http://www.lfd.uci.edu/~gohlke/pythonlibs/#pymssql
	使用该库时，需要在Sql Server Configuration Manager里面将TCP/IP协议开启

	用法：

	"""

	def __init__ (self, path):
		self.path = path

	def CLOSEDB (self):
		self.conn.close()

	def __GetConnect (self):
		"""
		得到连接信息
		返回: conn.cursor()
		"""
		try:
			self.conn = sqlite3.connect(database = self.path)
			cur = self.conn.cursor()
			return cur
		except Exception, e:
			print Exception, ":", e

	def ExecQuery (self, sql):
		"""
		执行查询语句
		返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段

		调用示例：
				ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
				resList = ms.ExecQuery("SELECT id,NickName FROM WeiBoUser")
				for (id,NickName) in resList:
					print str(id),NickName
		"""
		cur = self.__GetConnect()
		cur.execute(sql)

		resList = cur.fetchall()

		# 查询完毕后必须关闭连接
		# self.conn.close()
		return resList

	def ExecNonQuery (self, sql):
		"""
		执行非查询语句

		调用示例：
			cur = self.__GetConnect()
			cur.execute(sql)
			self.conn.commit()
			self.conn.close()
		"""
		cur = self.__GetConnect()
		cur.execute(sql)
		self.conn.commit()

	def INSERT (self, sql, curs):
		cur = self.__GetConnect()
		cur.execute(sql, curs)
		self.conn.commit()

	# self.conn.close()


if __name__ == '__main__':
	path = os.getcwd() + "\SQLSERVER\\test.db"
	sql = "SELECT type, name FROM sqlite_master WHERE type='table' "
	create_table_sql = '''CREATE TABLE `student` (
	                           `id` int(11) NOT NULL,
	                          `name` varchar(20) NOT NULL,
	                           `gender` varchar(4) DEFAULT NULL,
	                           `age` int(11) DEFAULT NULL,
                          `address` varchar(200) DEFAULT NULL,
	                          `phone` varchar(20) DEFAULT NULL,
	                          PRIMARY KEY (`id`)
	                        )'''
	db = SQLITE(path)
	# db = sqlite3.connect("test.db")
	db.ExecNonQuery(create_table_sql)
	list = db.ExecQuery(sql)
	for (type, name) in list:
		print name

	db.CLOSEDB()
