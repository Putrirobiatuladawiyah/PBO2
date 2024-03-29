import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Pinjam import *
class FrmPinjam:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='NOMORBUKTI:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TGLPINJAM:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODEANGGOTA:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODEBUKU1:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODEBUKU2:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TGLHRSKEMBALI:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TGLDIKEMBALIKAN:').grid(row=6, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='STATUSPINJAM:').grid(row=7, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='DENDA:').grid(row=8, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtNomorbukti = Entry(mainFrame) 
        self.txtNomorbukti.grid(row=0, column=1, padx=5, pady=5)
        self.txtNomorbukti.bind("<Return>",self.onCari)
        # Textbox
        self.txtTglpinjam = Entry(mainFrame) 
        self.txtTglpinjam.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtKodeanggota = Entry(mainFrame) 
        self.txtKodeanggota.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtKodebuku1 = Entry(mainFrame) 
        self.txtKodebuku1.grid(row=3, column=1, padx=5, pady=5)
        # Textbox
        self.txtKodebuku2 = Entry(mainFrame) 
        self.txtKodebuku2.grid(row=4, column=1, padx=5, pady=5)
        # Textbox
        self.txtTglhrskembali= Entry(mainFrame) 
        self.txtTglhrskembali.grid(row=5, column=1, padx=5, pady=5)
        # Textbox
        self.txtTgldikembalikan = Entry(mainFrame) 
        self.txtTgldikembalikan.grid(row=6, column=1, padx=5, pady=5)
        # Textbox
        self.txtStatuspinjam = Entry(mainFrame) 
        self.txtStatuspinjam.grid(row=7, column=1, padx=5, pady=5)
        # Textbox
        self.txtDenda = Entry(mainFrame) 
        self.txtDenda.grid(row=8, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('idpinjam','nomorbukti','tglpinjam','kodeanggota','kodebuku1','kodebuku2','tglhrskembali','tgldikembalikan','statuspinjam','denda')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('idpinjam', text='IDPINJAM')
        self.tree.column('idpinjam', width="30")
        self.tree.heading('nomorbukti', text='NOMORBUKTI')
        self.tree.column('nomorbukti', width="40")
        self.tree.heading('tglpinjam', text='TGLPINJAM')
        self.tree.column('tglpinjam', width="50")
        self.tree.heading('kodeanggota', text='KODEANGGOTA')
        self.tree.column('kodeanggota', width="60")
        self.tree.heading('kodebuku1', text='KODEBUKU1')
        self.tree.column('kodebuku1', width="70")
        self.tree.heading('kodebuku2', text='KODEBUKU2')
        self.tree.column('kodebuku2', width="80")
        self.tree.heading('tglhrskembali', text='TGLHRSKEMBALI')
        self.tree.column('tglhrskembali', width="90")
        self.tree.heading('tgldikembalikan', text='TGLDIKEMBALIKAN')
        self.tree.column('tgldikembalikan', width="100")
        self.tree.heading('statuspinjam', text='STATUSPINJAM')
        self.tree.column('statuspinjam', width="110")
        self.tree.heading('denda', text='DENDA')
        self.tree.column('denda', width="120")
        # set tree position
        self.tree.place(x=0, y=300)
        
    def onClear(self, event=None):
        self.txtNomorbukti.delete(0,END)
        self.txtNomorbukti.insert(END,"")
        self.txtTglpinjam.delete(0,END)
        self.txtTglpinjam.insert(END,"")
        self.txtKodeanggota.delete(0,END)
        self.txtKodeanggota.insert(END,"")
        self.txtKodebuku1.delete(0,END)
        self.txtKodebuku1.insert(END,"")
        self.txtKodebuku2.delete(0,END)
        self.txtKodebuku2.insert(END,"")
        self.txtTglhrskembali.delete(0,END)
        self.txtTglhrskembali.insert(END,"")
        self.txtTgldikembalikan.delete(0,END)
        self.txtTgldikembalikan.insert(END,"")
        self.txtStatuspinjam.delete(0,END)
        self.txtStatuspinjam.insert(END,"")
        self.txtDenda.delete(0,END)
        self.txtDenda.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data pinjam
        obj = Pinjam()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["idpinjam"],d["nomorbukti"],d["tglpinjam"],d["kodeanggota"],d["kodebuku1"],d["kodebuku2"],d["tglhrskembali"],d["tgldikembalikan"],d["statuspinjam"],d["denda"]))
    def onCari(self, event=None):
        nomorbukti = self.txtNomorbukti.get()
        obj = Pinjam()
        a = obj.get_by_nomorbukti(nomorbukti)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        nomorbukti = self.txtNomorbukti.get()
        obj = Pinjam()
        res = obj.get_by_nomorbukti(nomorbukti)
        self.txtTglpinjam.delete(0,END)
        self.txtTglpinjam.insert(END,obj.tglpinjam)
        self.txtKodeanggota.delete(0,END)
        self.txtKodeanggota.insert(END,obj.kodeanggota)
        self.txtKodebuku1.delete(0,END)
        self.txtKodebuku1.insert(END,obj.kodebuku1)
        self.txtKodebuku2.delete(0,END)
        self.txtKodebuku2.insert(END,obj.kodebuku2)
        self.txtStatuspinjam.delete(0,END)
        self.txtStatuspinjam.insert(END,obj.statuspinjam)
        self.txtTglhrskembali.delete(0,END)
        self.txtTglhrskembali.insert(END,obj.tglhrskembali)
        self.txtTgldikembalikan.delete(0,END)
        self.txtTgldikembalikan.insert(END,obj.tgldikembalikan)
        self.txtDenda.delete(0,END)
        self.txtDenda.insert(END,obj.denda)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        nomorbukti = self.txtNomorbukti.get()
        tglpinjam = self.txtTglpinjam.get()
        kodeanggota = self.txtKodeanggota.get()
        kodebuku1 = self.txtKodebuku1.get()
        kodebuku2 = self.txtKodebuku2.get()
        tglhrskembali = self.txtTglhrskembali.get()
        tgldikembalikan = self.txtTgldikembalikan.get()
        statuspinjam = self.txtStatuspinjam.get()
        denda = self.txtDenda.get()
        # create new Object
        obj = Pinjam()
        obj.nomorbukti = nomorbukti
        obj.tglpinjam = tglpinjam
        obj.kodeanggota = kodeanggota
        obj.kodebuku1 = kodebuku1
        obj.kodebuku2 = kodebuku2
        obj.tglhrskembali = tglhrskembali
        obj.tgldikembalikan = tgldikembalikan
        obj.statuspinjam = statuspinjam
        obj.denda = denda
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_nomorbukti(nomorbukti)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        nomorbukti = self.txtNomorbukti.get()
        obj = Pinjam()
        obj.nomorbukti = nomorbukti
        if(self.ditemukan==True):
            res = obj.delete_by_nomorbukti(nomorbukti)
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        
        self.onClear()
            
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = FrmPinjam(root2, "Aplikasi Data Pinjam")
    root2.mainloop()
