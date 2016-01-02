import os
import time
import sys

ROOT = "%s/show" % (os.path.expanduser("~"))

def setproject(project):
	subfolder = ["seq", "product/sound", "product/in", "product/out", "product/scan", "temp"]
	for i in subfolder:
		os.system("mkdir -p %s/%s/%s" % (ROOT, project, i))

def setshot(project, shotname):
	projd = ROOT +"/"+ project
	if not os.path.exists("%s/seq/%s" % (projd, shotname)):
		subfolder = ["2d/wip", "2d/src", "3d", "plate"]
		for i in subfolder:
			os.system("mkdir -p %s/seq/%s/%s" % (projd, shotname, i))
		os.system("touch %s/seq/%s/2d/%s" % (projd, shotname, shotname + "_comp_v01.nk"))
		os.system("cp %s/initfile/init.blend %s/seq/%s/3d/%s" % (os.path.abspath(os.path.dirname(__file__)),projd, shotname, shotname + "_blender_v01.blend"))

def projectlist():
	rlist = []
	for i in os.listdir(ROOT):
		if os.path.isdir(ROOT +"/"+ i):
			rlist.append(i)
	return rlist

def seqlist(project):
	rlist = []
	for i in os.listdir("%s/%s/seq/" % (ROOT, project)):
		if os.path.isdir("%s/%s/seq/%s" % (ROOT, project, i)):
			rlist.append(i)
	return rlist

def filelist(project, seq, task):
	flist = []
	if os.path.isdir("%s/%s/seq/%s/%s" % (ROOT, project, seq, task)):
		for i in os.listdir("%s/%s/seq/%s/%s" % (ROOT, project, seq, task)):
			if os.path.isfile("%s/%s/seq/%s/%s/%s" % (ROOT, project, seq, task, i)):
				if i[0] == ".":
					pass
				elif "~" in i:
					pass
				elif i.rsplit(".",1)[1] == "autosave":
					pass
				else:
					flist.append(i)
		return flist
	else:
		return flist	


def rmdot(list):
	nlist = []
	for i in list:
		if i[0] != ".":
			nlist.append(i)
		else:
			pass
	return nlist


def selectproject():
	projectlist = rmdot(os.listdir(ROOT))
	menunum = 1
	for i in projectlist:
		if i[0] != ".":
			print("%s. %s" % (menunum, i))
			menunum = menunum + 1
		else:
			rmlist.append(i)
	
	projectnum = raw_input("Select Project(q:quit) : ")
	project = projectlist[int(projectnum) - 1]
	print("Select %s." % (project))
	return project

if __name__ == "__main__":
	print seqlist("diamond")
