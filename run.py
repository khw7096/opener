import os
import subprocess

def excute(cmd):
	fd = subprocess.Popen(cmd, shell=True,
					stdin=subprocess.PIPE,
					stdout=subprocess.PIPE,
					stderr=subprocess.PIPE)
	return fd.stdout, fd.stderr

def getext(path):
	return path.rsplit(".",1)[1]

def run(filepath):
	ext = getext(filepath)
	if ext == "nk":
		nukepath = "/Applications/Nuke6.3v4/Nuke6.3v4.app/Contents/MacOS/Nuke6.3v4 --nukex"
		excute("%s %s" % (nukepath, filepath))
	elif ext == "ntp":
		natronpath = "/Applications/Natron.app/Contents/MacOS/Natron"
		excute("%s %s" % (natronpath, filepath))
	elif ext == "mov":
		excute("open %s" % (filepath))
	elif ext == "blend":
		blenderpath = "/Application/Blender/blender.app/Contents/MacOS/blender"
		excute("%s %s" % (blenderpath, filepath))
	else:
		pass

if __name__ == "__main__":
	testfile = ""
	run(testfile)
