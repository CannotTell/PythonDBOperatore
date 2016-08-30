#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zhukai.jiang'

from MSSQL import *

sqlDBName = "USE K2; SELECT * FROM Workspace.Action"

HOST = "192.168.107.20"
USER = "sa"
PW = "shdl2800"
DB_NAME = "aZaaS.Framework"



db = MSSQL(HOST, USER, PW, DB_NAME)


ll = db.ExecQuery(sqlDBName)
lis = []
for i in ll:
	for val in i:
		if val == None:
			lis.append("")
			continue
		lis.append(str(val))

for x in lis:
	print x + " "
