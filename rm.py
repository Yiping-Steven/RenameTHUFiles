# coding=utf8
#-----------------------------------------
# author: Yiping Zheng
# contact: zhengyp13@qq.com
# Version: 1.0
# Created on: 2017, Apr 27th 18:55
#-----------------------------------------

import os
import sys
import re

# 获取目标路径下的文件名列表，存放在listdir中
# --------- 指定路径方法1：敲键盘 （已废弃）--------------
# cwd=os.getcwd()
# u=u'/课程/随机3/'
# cwd+=u
# listdir=os.listdir(cwd)

# --------- 指定路径方法2：命令行拖拽 --------------
# 启动时：$python remove_redundant_number.py [dir1] [dir2] [dir3]...
print "start processing..."
for dir in sys.argv[1:]:
	listdir = os.listdir(dir)
	cwd = dir+'/'

	def chk(match):
		if match is None:
			return False
		else:
			return True

	for filename in listdir:
		#去除烦人的“_xxxx.”
		old_name= filename
		print 'oldname:'+cwd+old_name
		proc1=old_name.split('.')#去除后缀
		if len(proc1)>2:
			print "Can't process due to multiple '.'"
			continue
		if proc1[0]=="":
			continue #跳过隐藏文件
		else:
			proc2=proc1[0].split('_')
			# 如果文件名中有“_”,且最后一个“_“后跟的是数字，则视为疑似冗余信息：
			if len(proc2)>1:
				if proc2[-1].isdigit():
					#检验是否是学号或日期：
					pattern1=re.compile(r'2000')
					pattern2=re.compile(r'201')
					pattern3=re.compile(r'19')
					match1=pattern1.match(proc2[-1])			
					match2=pattern2.match(proc2[-1])
					match3=pattern3.match(proc2[-1])
					#学号检验方法：长十位且以’2000‘或’201‘开头
					if (len(proc2[-1])==10) and (chk(match1) or chk(match2)):
						continue
					if (chk(match1) or chk(match2) or chk(match3)):
					#日期检验方法：以‘2000’或‘201’或‘19’开头
						continue
					else:
						# 如果学号也不是...就去他丫的
							del proc2[-1]
							new_name=''
							for element in proc2:
								new_name+=element
							old_name=cwd+filename
							new_name=cwd+new_name+'.'+proc1[1]
							print "newname:"+new_name
							os.rename(old_name,new_name)
print "finished processing..."