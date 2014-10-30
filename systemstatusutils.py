#!/usr/bin/env python
#encoding=utf-8

import commonutils
import const
import os
import psutil
import types

class systemstatusutils():
    """
    AdminUtils System Status class，主要用于获取显示系统状况，包括CPU负载，HardDisk，网络I/O，内存等.	
    """
    SYSTEM_PLATFORM = ""
    common_utils = None
    const_attributes = None
    
    def __init__(self, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
	    self.stdin = stdin
	    self.stdout = stdout
	    self.stderr = stderr
	    self.common_utils = commonutils.commonutils()
	    self.const_attributes = const.Const()
	    self.SYSTEM_PLATFORM = self.common_utils.get_os_type()
    
    def system_memory_status(self):
	memoryStatus = psutil.virtual_memory()
	'''For Windwos platform'''
	if self.SYSTEM_PLATFORM == self.const_attributes.SYSTEM_PLATFORM_WINDOWS:
	    result = {"total":memoryStatus.total/1024**2,
	              "available":memoryStatus.available/1024**2,
	              "used":memoryStatus.used/1024**2,
	              "free":memoryStatus.free/1024**2
	              }
	'''For Linux platform'''
	if self.SYSTEM_PLATFORM == self.const_attributes.SYSTEM_PLATFORM_LINUX:
	    result = {"total":memoryStatus.total/1024**2,
	              "available":memoryStatus.available/1024**2,
	              "used":memoryStatus.used/1024**2,
	              "free":memoryStatus.free/1024**2,	
	              "buffers":memoryStatus.buffers/1024**2,
	              "cached":memoryStatus.cached/1024**2}
	    
	return result
    
    def process_memory_status(self, pid=None):
	memoryStatus = psutil.virtual_memory()
	if pid == None:
	    p = psutil.Process()
	else:
	    p = psutil.Process(pid)
	p_dict = p.as_dict()
	return  p_dict["memory_info"].rss/1024**2
	
	

if __name__ == '__main__':
    sys_status = systemstatusutils()
    #print sys_status.SYSTEM_PLATFORM
    #print "System total memory is: %s M" % (sys_status.system_memory_status()["total"])
    print "The special Process cost memory %s M." % (sys_status.process_memory_status(26152))
