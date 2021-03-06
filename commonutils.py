#!/usr/bin/env python
#encoding=utf-8

import os
import const


class commonutils():
    """
    AdminUtils Common class，主要用于项目中的通用方法。.	
    """
   
    def __init__(self, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
	    self.stdin = stdin
	    self.stdout = stdout
	    self.stderr = stderr
    
    def get_os_type(self):
	if os.name == "nt":
	    return const.SYSTEM_PLATFORM_WINDOWS
	elif os.name == "posix":
	    return const.SYSTEM_PLATFORM_LINUX
	else:
	    return const.SYSTEM_PLATFORM_OTHERS

	
if __name__ == '__main__':
    common = commonutils()
    print common.get_os_type()
