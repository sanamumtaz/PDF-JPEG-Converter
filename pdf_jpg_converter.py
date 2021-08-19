#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Aug 19, 2021 03:17:27 AM PKT  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import pdf_jpg_converter_support

global conversion_mode
conversion_mode = "pdf"


def vp_start_gui(mode):
    '''Starting point when module is the main routine.'''
    global val, w, root, conversion_mode
    conversion_mode = mode
    root = tk.Tk()
    top = Toplevel1 (root)
    pdf_jpg_converter_support.init(root, top, conversion_mode)
    root.mainloop()

w = None
def create_Toplevel1(rt, mode, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root, conversion_mode
    #rt = root
    conversion_mode = mode
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    pdf_jpg_converter_support.init(w, top, conversion_mode, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("421x370+340+106")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("PDF ⇔ JPG")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        global conversion_mode

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.285, rely=0.035, height=39, width=158)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 16 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''PDF ⇔ JPG''')

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.713, rely=0.051, height=24, width=87)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#bbddff")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(
            command=pdf_jpg_converter_support.convert_pdf if conversion_mode == "jpg" else pdf_jpg_converter_support.convert_jpg)
        self.Button1.configure(text='''PDF → JPG''' if conversion_mode == "jpg" else '''JPG → PDF''')

        self.TFrame1 = ttk.Frame(top)
        self.TFrame1.place(relx=0.048, rely=0.181, relheight=0.716
                , relwidth=0.876)
        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief="groove")

        self.Label2 = tk.Label(self.TFrame1)
        self.Label2.place(relx=0.244, rely=0.102, height=42, width=184)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 12")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Convert JPG to PDF''' if conversion_mode == "jpg" else '''Convert PDF to JPG''')

        self.Button2 = tk.Button(self.TFrame1)
        self.Button2.place(relx=0.108, rely=0.355, height=24, width=127)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(command=pdf_jpg_converter_support.select_files)
        self.Button2.configure(text='''Select JPG(s)''' if conversion_mode == "jpg" else '''Upload PDF''')

        self.Button3 = tk.Button(self.TFrame1)
        self.Button3.place(relx=0.271, rely=0.792, height=24, width=167)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#008000")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#ffffff")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(state='disabled')
        self.Button3.configure(
            command=pdf_jpg_converter_support.convert_images if conversion_mode == "jpg" else pdf_jpg_converter_support.convert2jpg)
        self.Button3.configure(text='''Convert to %s''' % ("PDF" if conversion_mode == "jpg" else "JPG"))

        self.Message1 = tk.Message(self.TFrame1)
        self.Message1.place(
            relx=0.108 if conversion_mode == "jpg" else 0.461,
            rely=0.453 if conversion_mode == "jpg" else 0.36,
            relheight=0.132,
            relwidth=0.84 if conversion_mode == "jpg" else 0.54)
        self.Message1.configure(anchor='nw')
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(justify='center')
        self.Message1.configure(text='''No %s Selected''' % ("File(s)" if conversion_mode == "jpg" else "File"))
        self.Message1.configure(width=310)

        self.Label3 = tk.Label(self.TFrame1)
        self.Label3.place(relx=0.461, rely=0.34, height=28, width=194)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#f97e71")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''*Files will be joined alphabetically''')
        self.Label3.destroy() if conversion_mode == "pdf" else None

        self.TEntry1 = ttk.Entry(self.TFrame1)
        self.TEntry1.place(relx=0.298, rely=0.604, relheight=0.079
                , relwidth=0.477)
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="ibeam")
        self.TEntry1.bind("<KeyRelease>", pdf_jpg_converter_support.is_name_empty)
        self.TEntry1.destroy() if conversion_mode == "pdf" else None

        self.Label4 = tk.Label(self.TFrame1)
        self.Label4.place(relx=0.108, rely=0.604, height=21, width=64)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''PDF Name:''')
        self.Label4.destroy() if conversion_mode == "pdf" else None

        self.Label5 = tk.Label(self.TFrame1)
        self.Label5.place(relx=0.786, rely=0.604, height=21, width=24)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''.pdf''')
        self.Label5.destroy() if conversion_mode == "pdf" else None


if __name__ == '__main__':
    vp_start_gui("pdf")





