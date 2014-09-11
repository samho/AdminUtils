#!/usr/bin/env python
#encoding=utf-8

class dbutils():
    """
    AdminUtils Database class，主要用于针对数据库的操作，包括数据导入，导出，插入，修改，删除，数据库状态等.	
    """
    def __init__(self, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
	    self.stdin = stdin
	    self.stdout = stdout
	    self.stderr = stderr