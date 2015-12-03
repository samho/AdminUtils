#!/usr/bin/env python
#encoding=utf-8

class datautils():
    """
    AdminUtils Data Utils class. 用于处理文件/目录的拷贝，移动，删除，重命名，压缩等操作。	
    """
    def __init__(self, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
	    self.stdin = stdin
	    self.stdout = stdout
	    self.stderr = stderr