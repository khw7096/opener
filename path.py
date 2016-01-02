import os
import time
import sys

PROJECTROOT = "%s/project" % (os.path.expanduser("~"))

def setproject(project):
	subfolder = ["seq", "product/sound", "product/in", "product/out", "product/scan", "temp"]
	for i in subfolder:
		os.system("mkdir -p %s/%s/%s" % (PROJECTROOT, project, i))

def setshot(project, shotname):
	projd = PROJECTROOT +"/"+ project
	if not os.path.exists("%s/seq/%s" % (projd, shotname)):
		subfolder = ["2d/wip", "2d/src", "3d", "plate"]
		for i in subfolder:
			os.system("mkdir -p %s/seq/%s/%s" % (projd, shotname, i))
		os.system("touch %s/seq/%s/2d/%s" % (projd, shotname, shotname + "_comp_v01.nk"))
		#os.system("cp ~/lazypic/tool/config/initfile/init.blend %s/seq/%s/3d/%s" % (projd, shotname, shotname + "_blender_v01.blend"))

def checkos():
	if sys.platform == 'linux2':
		return "lin"
	elif sys.platform == 'darwin':
		return "osx"
	else:
		return "win"

def projectlist():
	rlist = []
	for i in os.listdir(PROJECTROOT):
		if os.path.isdir(PROJECTROOT +"/"+ i):
			rlist.append(i)
	try:
		rlist.remove("backup")
	except:
		pass
	return rlist

def seqlist(project):
	rlist = []
	for i in os.listdir("%s/%s/seq/" % (PROJECTROOT, project)):
		if os.path.isdir("%s/%s/seq/%s" % (PROJECTROOT, project, i)):
			rlist.append(i)
	return rlist

def filelist(project, seq, task):
	flist = []
	for i in os.listdir("%s/%s/seq/%s/%s" % (PROJECTROOT, project, seq, task)):
		if os.path.isfile("%s/%s/seq/%s/%s/%s" % (PROJECTROOT, project, seq, task, i)):
			if i[0] == ".":
				pass
			elif "~" in i:
				pass
			elif i.rsplit(".",1)[1] == "autosave":
				pass
			else:
				flist.append(i)
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
	projectlist = rmdot(os.listdir(PROJECTROOT))
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
