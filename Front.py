%matplotlib qt
from tkinter import *
import Back, tkinter.ttk as ttk, matplotlib.pyplot as plt, pandas as pd, tkinter.messagebox
from PIL import Image, ImageTk

#Creacion Tk
root = Tk()
root.geometry('1000x680')
root.title('My BCRA stats App')
root.configure(bg='darkcyan')
root.resizable(0,0)

#globales
keys_api = Back.dic_keys_auxiliares()

#Funciones
def crear_grafico(rango):
    try:
        lista_valores = Back.lista_por_rango(Back.request(keys_api[filtro.get()]), rango)
        x_labels = [val[0] for val in lista_valores]
        y_labels = [val[1] for val in lista_valores]
        plt.figure(figsize=(12, 6))
        ax = pd.Series(y_labels).plot(kind='bar')
        ax.set_xticklabels(x_labels)

        rects = ax.patches

        for rect, label in zip(rects, y_labels):
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2, height + 5, label, ha='center', va='bottom')
    except KeyError:
        tkinter.messagebox.showinfo('Error','Seleccione un campo')

def set_valores():
    try:
        valores = Back.busqueda_ultimo(Back.request(keys_api[filtro.get()]))
        lbl_ultimo_valor.configure(text=round(valores['ultimo']['v']))
        lbl_ultimo_par.configure(text="{0}:{1}".format(valores['ultimo']["d"], round(valores['ultimo']["v"])))
        lbl_var_diaria_valor.configure(text=str(valores['var_diario'][2]))
        lbl_var_diaria_par.configure(text="{0}:{1}".format(valores['var_diario'][1],round(valores['var_diario'][0])))
        lbl_var_mensual_valor.configure(text=str(valores['var_mensual'][2]))
        lbl_var_mensual_par.configure(text="{0}:{1}".format(valores['var_mensual'][1],round(valores['var_mensual'][0])))
        lbl_var_anual_valor.configure(text=str(valores['var_anual'][2]))
        lbl_var_anual_par.configure(text="{0}:{1}".format(valores['var_anual'][1],round(valores['var_anual'][0])))
    except KeyError:
        tkinter.messagebox.showinfo('Error','Seleccione un campo')
    
def set_valores_hist(x):
    try:
        valor = Back.historicos(Back.request(keys_api[filtro.get()]))
        lbl_hist_fecha_max.configure(text=valor[1]["d"])
        lbl_hist_valor_max.configure(text=round(valor[1]["v"]))
        lbl_hist_fecha_min.configure(text=valor[0]["d"])
        lbl_hist_valor_min.configure(text=round(valor[0]["v"]))
    except KeyError:
        tkinter.messagebox.showinfo('Error','Seleccione un campo')

#GUI
    #Top
    #Frame main:
frame_main = Frame(root, width=970, height=640, bg='salmon', bd=10, relief=SUNKEN)
frame_main.place(x=15, y=20)

raw_image = Image.open(r'C:\Users\Agus\Downloads\finantial.jpg')
resized = raw_image.resize((425, 285), Image.ANTIALIAS)
finantial = ImageTk.PhotoImage(resized, master=frame_main)
label_img = Label(frame_main, image=finantial, bd=0)
label_img.place(x=510, y=90)
label_img.image = finantial

raw_image = Image.open(r'C:\Users\Agus\Downloads\Bcra_logo.png')
resized = raw_image.resize((75, 70), Image.ANTIALIAS)
logo_bcr = ImageTk.PhotoImage(resized, master=frame_main)
label_img = Label(frame_main, image=logo_bcr, bd=0)
label_img.place(x=230, y=10)
label_img.image = logo_bcr


    #Combobox Principal
lbl_combo = Label(frame_main, text='Seleccione un campo', bg="lightgray",fg="indigo", bd=2, font=("Montserrat",10,"bold"))
lbl_combo.place(x=460, y=25)
filtro=StringVar(frame_main)
cmb = ttk.Combobox(frame_main, values=list(keys_api.keys()), textvariable=filtro, width=60, state='readonly')
cmb.place(x=330, y=45)
btn_mensual = Button(frame_main, text="Buscar", bg="black",fg="pink", command=set_valores).place(x=730, y= 45)
    #Frame_variaciones
frame_default = Frame(root, width=490, height=280, bg='salmon', bd=15, relief=SUNKEN)
frame_default.place(x=40, y=120)
frame_ultimo = Frame(frame_default, width=150, height=100, bg='darkcyan', bd=8, relief=SUNKEN)
frame_ultimo.place(x=55, y=10)
frame_var_diar = Frame(frame_default, width=150, height=100, bg='darkcyan', bd=8, relief=SUNKEN)
frame_var_diar.place(x=260, y=10)
frame_var_mens = Frame(frame_default, width=150, height=100, bg='darkcyan', bd=8, relief=SUNKEN)
frame_var_mens.place(x=55, y=140)
frame_var_anual = Frame(frame_default, width=150, height=100, bg='darkcyan', bd=8, relief=SUNKEN)
frame_var_anual.place(x=260, y=140)
lbl_ultimo = Label(frame_ultimo,text="Último Registro", bg="salmon",fg="indigo", bd=2, relief=SUNKEN)
lbl_ultimo.place(x=25, y=10)
lbl_ultimo_valor = Label(frame_ultimo,text="--------------", bg='darkcyan',fg="darkblue", bd=2, relief=SUNKEN)
lbl_ultimo_valor.place(x=30, y=35)
lbl_ultimo_par = Label(frame_ultimo,text="------ : -------", bg='salmon',fg="azure", bd=2, relief=SUNKEN)
lbl_ultimo_par.place(x=10, y=60)
lbl_var_diaria = Label(frame_var_diar, text="Variación Diaria", bg="salmon",fg="indigo", bd=2, relief=SUNKEN)
lbl_var_diaria.place(x=25, y=10)
lbl_var_diaria_valor = Label(frame_var_diar, text="--------------", bg='darkcyan',fg="darkblue", bd=2, relief=SUNKEN)
lbl_var_diaria_valor.place(x=30, y=35)
lbl_var_diaria_par = Label(frame_var_diar, text="------ : -------", bg='salmon',fg="springgreen", bd=2, relief=SUNKEN)
lbl_var_diaria_par.place(x=10, y=60)
lbl_var_mensual = Label(frame_var_mens, text="Variación Mensual", bg="salmon",fg="indigo", bd=2, relief=SUNKEN)
lbl_var_mensual.place(x=25, y=10)
lbl_var_mensual_valor = Label(frame_var_mens, text="--------------", bg='darkcyan',fg="darkblue", bd=2, relief=SUNKEN)
lbl_var_mensual_valor.place(x=30, y=35)
lbl_var_mensual_par = Label(frame_var_mens, text="------ : -------", bg='salmon',fg="springgreen", bd=2, relief=SUNKEN)
lbl_var_mensual_par.place(x=10, y=60)
lbl_var_anual = Label(frame_var_anual, text="Variación Anual", bg="salmon",fg="indigo", bd=2, relief=SUNKEN)
lbl_var_anual.place(x=25, y=10)
lbl_var_anual_valor = Label(frame_var_anual, text="--------------", bg='darkcyan',fg="darkblue", bd=2, relief=SUNKEN)
lbl_var_anual_valor.place(x=30, y=35)
lbl_var_anual_par = Label(frame_var_anual, text="------ : -------", bg='salmon',fg="azure", bd=2, relief=SUNKEN)
lbl_var_anual_par.place(x=10, y=60)

    #Frame_Criticos
frame_main_c = Frame(root, width=490, height=200, bg="salmon", bd=15, relief=SUNKEN)
frame_main_c.place(x=40, y=410)
frame_criticos = Frame(frame_main_c, width=430, height=160, bg="darkcyan", bd=10, relief=SUNKEN)
frame_criticos.place(x=20, y=10)

lbl_desc = Label(frame_criticos, text='Valores críticos', bg="darkcyan",fg="indigo", bd=2, font=("Montserrat",10,"bold")).place(x=155, y= 0)

lbl_desc_max = Label(frame_criticos, text="Máximo histórico", bg="salmon",fg="indigo", bd=2, relief=SUNKEN).place(x=70, y=45)
lbl_hist_fecha_max= Label(frame_criticos, text="--------", bg="gray",fg="yellow", bd=2, relief=SUNKEN)
lbl_hist_fecha_max.place(x=85, y=65)
lbl_hist_valor_max= Label(frame_criticos, text="--------", bg="salmon",fg="azure", bd=2, relief=SUNKEN)
lbl_hist_valor_max.place(x=95, y=85)

lbl_desc_min = Label(frame_criticos, text="Minimo histórico", bg="salmon",fg="indigo", bd=2, relief=SUNKEN).place(x=250, y=45)
lbl_hist_fecha_min= Label(frame_criticos, text="--------", bg="gray",fg="yellow", bd=2, relief=SUNKEN)
lbl_hist_fecha_min.place(x=270, y=65)
lbl_hist_valor_min= Label(frame_criticos, text="--------", bg="salmon",fg="azure", bd=2, relief=SUNKEN)
lbl_hist_valor_min.place(x=280, y=85)

btn_min_hist = Button(frame_criticos, text="Obtener valores criticos", command=lambda: set_valores_hist("minimo"), bg="black",fg="pink", bd=2, relief=SUNKEN).place(x=145, y=115)

    #frame_graficos
frame_main_g = Frame(root, width=420, height=200, bg="salmon", bd=15, relief=SUNKEN)
frame_main_g.place(x=540, y=410)
frame_graficos = Frame(frame_main_g, width=350, height=150, bg="darkcyan", bd=10, relief=SUNKEN)
frame_graficos.place(x=25, y=10)

lbl_graficos = Label(frame_graficos, text="Visualización de datos", bg="darkcyan",fg="indigo", bd=2, font=("Montserrat",10,"bold")).place(x=100, y= 0)
btn_anual = Button(frame_graficos, text="Comparación\n Anual", bg="black",fg="pink", command=lambda: crear_grafico("anual")).place(x=10, y= 60)
btn_diario = Button(frame_graficos, text="Comparación\n Diaria", bg="black",fg="pink", command=lambda: crear_grafico("diario")).place(x=120, y= 60)
btn_mensual = Button(frame_graficos, text="Comparación\n Mensual", bg="black",fg="pink", command=lambda: crear_grafico("mensual")).place(x=230, y= 60)

root.mainloop()
