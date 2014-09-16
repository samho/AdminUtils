#!/usr/bin/env python
#encoding=utf-8

import sys

class Const():
    """
    AdminUtils Const class，定义系统用到的静态变量。.	
    """
    SYSTEM_PLATFORM_WINDOWS = "Windows"
    SYSTEM_PLATFORM_LINUX = "Linux"
    SYSTEM_PLATFORM_OTHERS = "Others"
    
    def __init__(self, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
	    self.stdin = stdin
	    self.stdout = stdout
	    self.stderr = stderr

if __name__ == '__main__':
    const = Const()
    print const.SYSTEM_PLATFORM["Windows"]