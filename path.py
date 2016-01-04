import os
import time
import sys

ROOT = "%s/show" % (os.path.expanduser("~"))

def setproject(project):
	sub = ["seq", "product/sound", "product/in", "product/out", "product/scan", "temp"]
	for i in sub:
		os.system("mkdir -p %s/%s/%s" % (ROOT, project, i))

def setshot(project, shot):
	initpath = "%s/initfile" % (os.path.abspath(os.path.dirname(__file__)))
	shotpath = "%s/%s/seq/%s" % (ROOT, project, shot)
	if not os.path.exists(shotpath):
		sub = ["2d/wip", "2d/src", "3d", "plate"]
		for i in sub:
			os.system("mkdir -p %s/%s" % (shotpath, i))
		os.system("touch %s/2d/%s" % (shotpath, shot + "_comp_v01.nk"))
		os.system("cp %s/init.blend %s/3d/%s" % (initpath, shotpath, shot + "_blender_v01.blend"))

def projectlist():
	rlist = []
	for i in os.listdir(ROOT):
		if os.path.isdir(ROOT+"/"+i):
			rlist.append(i)
	return rlist

def seqlist(project):
	rlist = []
	seq = "%s/%s/seq" % (ROOT, project)
	for i in os.listdir(seq):
		if os.path.isdir(seq+"/"+i):
			rlist.append(i)
	return rlist

def filelist(project, seq, task):
	flist = []
	taskpath = "%s/%s/seq/%s/%s" % (ROOT, project, seq, task)
	if os.path.isdir(taskpath):
		for i in os.listdir(taskpath):
			if os.path.isfile(taskpath+"/"+i):
				if i[0] == "." or "~" in i:
					pass
				elif i.rsplit(".",1)[1] == "autosave":
					pass
				else:
					flist.append(i)
		return flist
	else:
		return flist	

if __name__ == "__main__":
	print seqlist("temp")
