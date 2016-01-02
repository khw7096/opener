from ttk import *
from Tkinter import *
import Pmw
import path
import run
import os

class Opener(Frame):
	
	project = ""
	task = "2d"
	shot = ""
	file = ""
	try:
		projectlist = path.projectlist()
	except:
		path.setproject("temp")
	shotlist = []
	tasklist = ["2d", "3d", "plate"]
	filelist = []
	open_pathvar = ""

	def __init__(self, master):
		#menu bar
		menubar = Menu(master)
		master.config(menu=menubar)
		fileMenu = Menu(menubar)
		fileMenu.add_command(label="Add_Project", command=self.add_project)
		fileMenu.add_command(label="Add_Shot", command=self.add_shot)
		fileMenu.add_command(label="Open browser path", accelerator="F3", command=self.open_path)
		fileMenu.add_command(label="Open terminal path", accelerator="F4", command=self.open_terminal_path)
		fileMenu.add_command(label="Exit", command=self.onExit)
		menubar.add_cascade(labe="File", menu=fileMenu)
		master.bind_all("<F3>", self.open_path_hotkey)
		master.bind_all("<F4>", self.open_terminal_path_hotkey)

		#gui
		self.pathvar = StringVar()
		self.ui_projectlist = Pmw.ScrolledListBox(master, listbox_selectmod=SINGLE, items=self.projectlist, labelpos=NW, label_text='Project', selectioncommand=self.sel_project, listbox_height=6, hull_width=5)
		self.ui_shotlist = Pmw.ScrolledListBox(master, listbox_selectmod=SINGLE, items=self.shotlist, labelpos=NW, label_text='Shot', selectioncommand=self.sel_shot,  listbox_height=6, hull_width=5)
		self.ui_tasklist = Pmw.ScrolledListBox(master, listbox_selectmod=SINGLE, items=self.tasklist, labelpos=NW, label_text='Task', selectioncommand=self.sel_task, listbox_height=6)
		self.ui_filelist = Pmw.ScrolledListBox(master, listbox_selectmod=SINGLE, items=self.filelist, labelpos=NW, label_text='Files', dblclickcommand=self.sel_file, listbox_height=10, hull_width=20)
		self.bt_makeproject = Button(master, text="Make Project", command=self.add_project)
		self.bt_makeshot = Button(master, text="Make Shot", command=self.add_shot)
		self.bt_openfolder = Button(master, text="Open folder", command=self.open_path)
		self.ui_path = Label(master, textvariable=self.pathvar)

		self.ui_projectlist.grid(row=0, column=0, padx=2, pady=0)
		self.ui_shotlist.grid(row=0, column=1, padx=2, pady=0)
		self.ui_tasklist.grid(row=0, column=2, padx=2, pady=0)
		self.bt_makeproject.grid(row=1, column=0, padx=2, pady=0, sticky=NSEW)
		self.bt_makeshot.grid(row=1, column=1, padx=2, pady=0, sticky=NSEW)
		self.bt_openfolder.grid(row=1, column=2, padx=2, pady=0, sticky=NSEW)
		self.ui_filelist.grid(row=2, column=0, columnspan=3, sticky=NSEW, padx=2, pady=2)
		self.ui_path.grid(row=3, column=0, columnspan=3, sticky=W, padx=2, pady=2)

	def onExit(self):
		exit()

	def open_path(self):
		os.system("open %s" % (self.open_pathvar))
	def open_terminal_path(self):
		os.system('open -a Terminal %s' % (self.open_pathvar))

	def open_path_hotkey(self, event):
		os.system("open %s" % (self.open_pathvar))
	def open_terminal_path_hotkey(self, event):
		os.system('open -a Terminal %s' % (self.open_pathvar))

	def add_project(self):
		t = Toplevel()
		t.wm_title("Add Project")
		t.geometry("290x80+300+300")
		field = Pmw.EntryField(t, labelpos=W, label_text="New Project : ")
		ybutton = Button(t, text="Create", command=lambda: self.make_project(field.getvalue(), t))
		nbutton = Button(t, text="Quit", command=lambda: self.onDeleteChild(t))
		field.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='NWSE')
		ybutton.grid(row=1, column=0, padx=5, pady=5, sticky='E')
		nbutton.grid(row=1, column=1, padx=5, pady=5, sticky='W')
	
	def onDeleteChild(self, window):
		window.destroy()

	def make_project(self, projectname, window):
		path.setproject(projectname)
		window.destroy()
		self.update_project()
	
	def add_shot(self):
		t = Toplevel()
		t.wm_title("Add Shot")
		t.geometry("290x80+300+300")
		field = Pmw.EntryField(t, labelpos=W, label_text="New Shot : ")
		ybutton = Button(t, text="Create", command=lambda: self.make_shot(field.getvalue(), t))
		nbutton = Button(t, text="Quit", command=lambda: self.onDeleteChild(t))
		field.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='NWSE')
		ybutton.grid(row=1, column=0, padx=5, pady=5, sticky='E')
		nbutton.grid(row=1, column=1, padx=5, pady=5, sticky='W')
	
	def make_shot(self, shotname, window):
		path.setshot(self.project, shotname)
		window.destroy()
		self.update_shot()


	def sel_project(self):
		sels = self.ui_projectlist.getcurselection()
		if len(sels) == 0:
			self.project = ""
		else:
			self.project = sels[0]
		self.update_shot()
		self.update_path()

	def sel_shot(self):
		sels = self.ui_shotlist.getcurselection()
		if len(sels) == 0:
			self.shot = ""
		else:
			self.shot = sels[0]
		self.update_path()

	def sel_task(self):
		sels = self.ui_tasklist.getcurselection()
		if len(sels) == 0:
			self.task == "2d"
		else:
			self.task = sels[0]
		self.update_file()
		self.update_path()

	def sel_file(self):
		sels = self.ui_filelist.getcurselection()
		if len(sels) == 0:
			self.file = ""
		else:
			self.file = sels[0]
		self.update_path()
		runfile = path.ROOT +"/"+ self.project + "/seq/" + self.shot +"/"+ self.task +"/"+ self.file
		run.run(runfile)

	def update_project(self):
		self.ui_projectlist.clear()
		self.ui_projectlist.setlist(path.projectlist())

	def update_shot(self):
		self.ui_shotlist.clear()
		self.ui_shotlist.setlist(path.seqlist(self.project))

	def update_task(self):
		pass
	
	def update_file(self):
		self.ui_filelist.clear()
		self.ui_filelist.setlist(path.filelist(self.project, self.shot, self.task))
	
	def update_path(self):
		try:
			self.pathvar.set("PATH : %s/%s/seq/%s/%s" % (path.ROOT, self.project, self.shot, self.task))
			self.open_pathvar = "%s/%s/seq/%s/%s" % (path.ROOT, self.project, self.shot, self.task) 
		except:
			self.pathvar.set("Select Shot please~!")

def main():
	root = Tk()
	p = Opener(root)
	root.title("Opener")
	root.geometry("560x390+300+300")
	root.mainloop()

if __name__ == "__main__":
	main()
