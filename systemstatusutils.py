#!/usr/bin/env python
#encoding=utf-8

class systemstatusutils():
    """
    AdminUtils System Status class，主要用于获取显示系统状况，包括CPU负载，HardDisk，网络I/O，内存等.	
    """
    def __init__(self, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
	    self.stdin = stdin
	    self.stdout = stdout
	    self.stderr = stderr