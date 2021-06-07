from tkinter import Tk,Entry,Label,Button,Canvas,NW,ALL, EventType
from PIL import Image,ImageTk
from atractor import Atractor

class Ventana():
    def __init__(self):
        self.main = Tk()
        self.tam = Entry(self.main)
        self.regla = Entry(self.main)
        self.l1 = Label(self.main, text="Tamaño:")
        self.l2 = Label(self.main, text="Regla:")
        self.aceptar = Button(self.main,text="Aceptar",command=self.generar)
        self.canvas = Canvas(self.main,bg="gray",height=950,width=1000)
        self.canvas.bind("<MouseWheel>", self.do_zoom)
        self.canvas.bind('<ButtonPress-1>', lambda event: self.canvas.scan_mark(event.x, event.y))
        self.canvas.bind("<B1-Motion>", lambda event: self.canvas.scan_dragto(event.x, event.y, gain=1))
        self.atractor = Atractor()
        self.mostrar()

    def center(self,win):
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()

    def layaout(self):
        self.l1.place(x=30,y=10)
        self.tam.place(x=95, y=10)
        self.l2.place(x=300,y=10)
        self.regla.place(x=345, y=10)
        self.aceptar.place(x=600,y=6)
        self.canvas.place(x=0,y=50)

    def generar(self):
        self.atractor.generar_imagen(
            int(self.tam.get()),
            int(self.regla.get())
        )
        im = Image.open('atractor.jpg')
        self.canvas.image = ImageTk.PhotoImage(im)
        self.canvas.create_image(0, 0, image=self.canvas.image, anchor='nw')

    def do_zoom(self,event):
        factor = 1.001 ** event.delta
        is_shift = event.state & (1 << 0) != 0
        is_ctrl = event.state & (1 << 2) != 0
        self.canvas.scale(ALL, event.x, event.y, 
                    factor if not is_shift else 1.0, 
                    factor if not is_ctrl else 1.0)

    def mostrar(self):
        self.main.resizable(False, False)
        self.main.title(string="Atractor")
        self.main.geometry('1000x1000')
        self.center(self.main)  
        self.layaout()
        self.main.mainloop()

v = Ventana()