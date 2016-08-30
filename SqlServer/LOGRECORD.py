#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zhukai.jiang'
import logging

class LOGRECORD:
	'''
	自定义log记录
	'''

	def __init__ (self, LogName, FileName):
		self.LogName = LogName
		self.FileName = FileName

	def GetLogger(self):
		logger = logging.getLogger(self.LogName)
		logger.setLevel(logging.DEBUG)

		# 创建一个handler，用于写入日志文件
		fh = logging.FileHandler(self.FileName)
		fh.setLevel(logging.DEBUG)

		# 再创建一个handler，用于输出到控制台
		ch = logging.StreamHandler()
		ch.setLevel(logging.DEBUG)

		# 定义handler的输出格式
		formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		fh.setFormatter(formatter)
		ch.setFormatter(formatter)

		# 给logger添加handler
		logger.addHandler(fh)
		logger.addHandler(ch)

		return logger




