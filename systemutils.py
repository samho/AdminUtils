#!/usr/bin/env python
#encoding=utf-8

class systemutils():
    """
    AdminUtils Systemutils class，用于处理系统相关操作，包括系统进程处理，系统类型，文件查找等。.	
    """
    def __init__(self, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
	    self.stdin = stdin
	    self.stdout = stdout
	    self.stderr = stderr