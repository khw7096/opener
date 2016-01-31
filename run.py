import os
import subprocess

def excute(cmd):
	fd = subprocess.Popen(cmd, shell=True,
					stdin=subprocess.PIPE,
					stdout=subprocess.PIPE,
					stderr=subprocess.PIPE)
	return fd.stdout, fd.stderr

def run(filepath):
	head, ext = os.path.splitext(filepath)
	if ext == ".nk":
		nukepath = "/Applications/Nuke9.0v8/Nuke9.0v8.app/Contents/MacOS/Nuke9.0v8 --nukex"
		excute("%s %s" % (nukepath, filepath))
	elif ext == ".ntp":
		natronpath = "/Applications/Natron.app/Contents/MacOS/Natron"
		excute("%s %s" % (natronpath, filepath))
	elif ext == ".mov":
		excute("open %s" % (filepath))
	elif ext == ".blend":
		blenderpath = "/Application/Blender/blender.app/Contents/MacOS/blender"
		excute("%s %s" % (blenderpath, filepath))
	else:
		pass

if __name__ == "__main__":
	testfile = ""
	run(testfile)
