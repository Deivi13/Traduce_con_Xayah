from tkinter import *
from tkinter import ttk
import translators as ts

# setting up program's geometry.
root = Tk()
root.title("Traduce con Xayah")
root.geometry("1080x400")

def traducir(): 
    # Manejo de errores
    if combo1.get() == "Elegir idioma":
        text1.insert(1.0, "ERROR - Por favor, seleccione idiomas que desea traducir")
        text2.insert(1.0, "ERROR - Por favor, seleccione idiomas que desea traducir") 

    # Obteniendo texto fuente desde opcion del combobox
    if combo1.get() == 'Español':
        _src ='es'        
    elif combo1.get() == 'Ingles':
        _src ='en'
    
    # Obteniendo idioma al que se quiere traducir desde opcion del combobox
    if combo2.get() == 'Español':
        _dest ='es'        
    elif combo2.get() == 'Ingles':
        _dest ='en'
    elif combo2.get() == 'Frances':
        _dest ='fr'
    elif combo2.get() == 'Portuguese':
        _dest ='pt'
    elif combo2.get() == 'Italiano':
        _dest ='it'
    elif combo2.get() == 'Ruso':
        _dest ='ru'
    
    traduccion = ts.google(text1.get(0.1, END), from_language=_src, to_language=_dest)
    text2.insert(1.0, traduccion)

# This function's purpose is to clear both text boxes.
def limpiar():
    text1.delete("1.0","end")
    text2.delete("1.0","end")
    combo1.set("Elegir idioma")
    combo2.set("Elegir idioma")


# This peace of code creates a combobox that enables choosing a languages.
mylabel = Label(root, text="De:",font="Roboto 16")
mylabel.place(x= 65, y=70)
combo1 = ttk.Combobox(root, values=['Español', 'Ingles'], font="Roboto 14",state="r")
combo1.place(x= 100, y=70)
combo1.set("Elegir idioma")


# This peace of code represents a Text area where users can Enter the text the want to translate.
f = Frame(root,bg="Black", bd=3)
f.place(x=10,y=140,width=440,height=210)
text1 = Text(f,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)
text1.insert(1.0, "Texto aqui")

# Here's a combobox to choose which language user wants to translate his/her text.
mylabel2 = Label(root, text="A:",font="Roboto 16")
mylabel2.place(x= 700, y=70)
combo2 = ttk.Combobox(root, values=['Español', 'Ingles', 'Frances', 'Portuguese', 'Italiano', 'Ruso'], font="Roboto 14",state="r")
combo2.place(x= 725, y=70)
combo2.set("Elegir idioma")

# This peace of code represents will show the output's text that user wants to translate.
f2 = Frame(root,bg="Black", bd=3)
f2.place(x=620,y=140,width=440,height=210)
text2 = Text(f2,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)


# Just an image.
logo_image = PhotoImage(file="logo.png")
logo_label = Label(root, image=logo_image, width=238)
logo_label.place(x=400, y=1)

# Added Notes to inform user about character limit.
limite = Label(root, text="El limite de caracteres es 700",font="Roboto 16", bg="white", fg="red")
limite.place(x= 8, y=350)

translate_button = Button(root, text=" Traducir ",font="Roboto 15 bold italic",
                            activebackground="purple", cursor="hand2",bd=5,
                            bg='green',fg="white",command=traducir)
translate_button.place(x=480,y=200)


delete_button = Button(root, text=" Limpiar  ",font="Roboto 15 bold italic",
                            activebackground="purple", cursor="hand2",bd=5,
                            bg='red',fg="white", command=limpiar)
delete_button.place(x=480,y=260)

root.configure(bg="white")
root.mainloop()     