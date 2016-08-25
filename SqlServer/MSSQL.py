#!/usr/bin/env python
# -*- coding: GBK -*-
__author__ = 'zhukai.jiang'

import pymssql


class MSSQL:
	"""
	��pymssql�ļ򵥷�װ
	pymssql�⣬�ÿ⵽�������أ�http://www.lfd.uci.edu/~gohlke/pythonlibs/#pymssql
	ʹ�øÿ�ʱ����Ҫ��Sql Server Configuration Manager���潫TCP/IPЭ�鿪��

	�÷���

	"""

	def __init__ (self, host, user, pwd, db):
		self.host = host
		self.user = user
		self.pwd = pwd
		self.db = db

	def CLOSEDB(self):
		self.conn.close()

	def __GetConnect (self):
		"""
		�õ�������Ϣ
		����: conn.cursor()
		"""
		if not self.db:
			raise (NameError, "û���������ݿ���Ϣ")
		self.conn = pymssql.connect(host = self.host, user = self.user, password = self.pwd, database = self.db)
		cur = self.conn.cursor()
		if not cur:
			raise (NameError, "�������ݿ�ʧ��")
		else:
			return cur

	def ExecQuery (self, sql):
		"""
		ִ�в�ѯ���
		���ص���һ������tuple��list��list��Ԫ���Ǽ�¼�У�tuple��Ԫ����ÿ�м�¼���ֶ�

		����ʾ����
				ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
				resList = ms.ExecQuery("SELECT id,NickName FROM WeiBoUser")
				for (id,NickName) in resList:
					print str(id),NickName
		"""
		cur = self.__GetConnect()
		cur.execute(sql)

		resList = cur.fetchall()

		# ��ѯ��Ϻ����ر�����
		#self.conn.close()
		return resList

	def ExecNonQuery (self, sql):
		"""
		ִ�зǲ�ѯ���

		����ʾ����
			cur = self.__GetConnect()
			cur.execute(sql)
			self.conn.commit()
			self.conn.close()
		"""
		cur = self.__GetConnect()
		cur.execute(sql)
		self.conn.commit()
		#self.conn.close()
