# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import tkinter as tk         
from tkinter import messagebox      # python 3
from tkinter import font  as tkfont # python 3
import crudFunctions as cf
from tkinter.filedialog import askopenfilename

import _thread       
from PIL import ImageTk, Image
global result 
class BSGP(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        result = tk.StringVar()
        self.title("BSGP GUI")
        
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()
        print(self.geometry())
        size = tuple(int(pos) for pos in "800x400".split('x'))
        x = int(w/2 - size[0]/2)
        y = int(h/2 - size[1]/2)
        print(size)
        print("%dx%d+%d+%d" % (size + (x, y)))
        self.geometry("%dx%d+%d+%d" % (size + (x, y)))
        
        self.title_font1 = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others "1600x800+0+0"
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        for F in (Start, PageOne):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            frame.grid(row=0, column=0, sticky="nsew")
            frame.configure(background="steelblue")

        self.show_frame("Start")
        menubar = tk.Menu(self)
        
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open csv..",command= lambda: PageOne.insertCsv())
        filemenu.add_command(label="Save")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.destroy)
        menubar.add_cascade(label="File", menu=filemenu)
        # create a pulldown menu, and add it to the menu bar
        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Generate Excel",
                            command=lambda: result.set(cf.generateExcel()))
        editmenu.add_command(label="Generate Certificate..",command=lambda: result.set(cf.generateSchoolCertificate()))
        
        menubar.add_cascade(label="Generate", menu=editmenu)
        
        self.config(menu=menubar)

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class Start(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="BSGP Gui", font=controller.title_font1)
        
        button3 = tk.Button(self, text="Start",
                            command=lambda: controller.show_frame("PageOne"))
        label.pack(side="top", fill="x", pady=10)
        
        button3.pack()
#        menubar.pack()
from io import BytesIO

class PageOne(tk.Frame):
    global nameVar,img
    def info(d):
        tk.messagebox.showinfo("Message",d)
    
    def insertCsv():
        filename = askopenfilename()
        print("inserting file ",filename)
        val = cf.insertAll(filename)
        tk.messagebox.showinfo("Message",val)
        
    def setImg(data,k):
            output =BytesIO(data)
            output.seek(0)
            file =Image.open(output)
            basewidth =1500
            wpercent = (basewidth / float(file.size[0]))
                                    
            hsize = int((float(file.size[1]) * float(wpercent)))
            
            file = file.resize((basewidth, hsize), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(file)
            k.create_image(-100,-200, anchor='nw',image = img)
            
            k.image=img

                
    def __init__(self, parent, controller):
        global cnt,temp
        tk.Frame.__init__(self, parent)
        self.controller = controller
#        nameVar = tk.StringVar()
        canvas = tk.Canvas(self,width=1300, height=350)
        
        namesVar = tk.StringVar()
        fatherVar = tk.StringVar()
        classVar = tk.StringVar()
        sectionVar = tk.StringVar()
        schoolCodeVar = tk.StringVar()
        
        cnt = tk.IntVar()
        temp = tk.IntVar()
        cnt.set(23)
        
#        nameVar.set("/home/ratnesh/Downloads/passport_cv.png")
#        loadEntry(23)
        name = tk.Label(self,text="Name", fg="white",bg="blue",height=3, width=40)
        father = tk.Label(self,text="Father",fg="white",bg="blue",height=3, width=40)
        classs = tk.Label(self,text="Class", fg="white",bg="blue",height=3, width=40)
        section = tk.Label(self,text="Section",fg="white",bg="blue",height=3, width=40)
        school = tk.Label(self,text="School",fg="white",bg="blue",height=3, width=40)
        
        nEntry = tk.Entry(self, textvariable = namesVar, width=40)
        fEntry = tk.Entry(self, textvariable = fatherVar, width=40)
        cEntry = tk.Entry(self, textvariable = classVar, width=40)
        temp.set(cnt.get())
        def callback():
            print("temp:",temp.get())
            try:
                if(namesVar.get() != ''):
                    _thread.start_new_thread( cf.update(namesVar.get(), fatherVar.get(), schoolCodeVar.get(), classVar.get(), sectionVar.get(),temp.get()), )
            except Exception as e:
                print("Error: unable to start thread",e)
            print("callback",cnt.get())
            dataObj = cf.gotoId(cnt.get())
            namesVar.set(dataObj[3])
            fatherVar.set(dataObj[4])
            schoolCodeVar.set(dataObj[5])
            classVar.set(dataObj[6])
            sectionVar.set(dataObj[7])
            PageOne.setImg(dataObj[1],canvas) 
            temp.set(cnt.get())
                    
            return True
        sEntry = tk.Entry(self, textvariable = sectionVar, width=40, validate="focusout", validatecommand= callback)
        
        nexts = tk.Button(self, text="Next", 
                           command= lambda: cnt.set(cnt.get()+1), height=10, width=20)
        
        scEntry = tk.Entry(self, textvariable = schoolCodeVar, width=40)
        
        idEntry = tk.Entry(self, textvariable=cnt, validate="focusout", validatecommand= callback)
                
        result = tk.StringVar()
        result_lbl = tk.Label(self, font=controller.title_font1,textvariable = result)
        
        previous = tk.Button(self, text="Previous",
                           command=lambda: cnt.set(cnt.get()-1), height=10, width=20)
        goto = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("Start"))
        
        save = tk.Button(self, text="Save",
                           command= lambda: result.set(cf.update(namesVar.get(), fatherVar.get(), schoolCodeVar.get(), classVar.get(), sectionVar.get(),cnt.get())))
        

        canvas.grid(sticky="n",columnspan=4)
        result_lbl.grid(row=1,columnspan=4)
        previous.grid(row=2,column=0,rowspan=4)
        nexts.grid(row=2,column=3,rowspan=4)
        
        
        name.grid(row=2,column=1)
        nEntry.grid(row=2,column=2)
        
        father.grid(row=3,column=1)
        fEntry.grid(row=3,column=2)

        classs.grid(row=4,column=1)
        cEntry.grid(row=4,column=2)
        
        section.grid(row=5,column=1)
        sEntry.grid(row=5,column=2)
        
        school.grid(row=6,column=0,columnspan=2)
        scEntry.grid(row=6,column=2,columnspan=2)
        goto.grid(row=7,column=0,columnspan=2)
        idEntry.grid(row=7,column=2,columnspan=2)
        save.grid(row=8,sticky="s",columnspan=4)
        


if __name__ == "__main__":
    app = BSGP()
    app.mainloop()

