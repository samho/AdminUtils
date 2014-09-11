#!/usr/bin/env python
#encoding=utf-8

class commonutils():
    """
    AdminUtils Common class，主要用于项目中的通用方法。.	
    """
    def __init__(self, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
	    self.stdin = stdin
	    self.stdout = stdout
	    self.stderr = stderr