import os
import subprocess

def excute(cmd):
	fd = subprocess.Popen(cmd, shell=True,
					stdin=subprocess.PIPE,
					stdout=subprocess.PIPE,
					stderr=subprocess.PIPE)
	return fd.stdout, fd.stderr

def run(filepath):
        app = "open"
	head, ext = os.path.splitext(filepath)
	if ext == ".nk":
		app = "/Applications/Nuke10.0v3/Nuke10.0v3.app/Contents/MacOS/Nuke10.0v3 --nc --startx"
		excute("%s %s" % (app, filepath))
	elif ext == ".ntp":
		app = "/Applications/Natron.app/Contents/MacOS/Natron"
		excute("%s %s" % (app, filepath))
	elif ext == ".blend":
		app = "/Application/Blender/blender.app/Contents/MacOS/blender"
		excute("%s %s" % (app, filepath))
	else:
		excute("%s %s" % (app, filepath))

if __name__ == "__main__":
	testfile = ""
	run(testfile)
