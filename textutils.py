#!/usr/bin/env python
#encoding=utf-8

class textutils():
    """
    AdminUtils Text class，主要用于文本内容的处理，包括，查找，替换，删除，可以针对某一段内容或文件。.	
    """
    def __init__(self, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
	    self.stdin = stdin
	    self.stdout = stdout
	    self.stderr = stderr