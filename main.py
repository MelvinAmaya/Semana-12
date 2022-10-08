# Melvin Josué Pereira Amaya SMIS010221
# Melvin Adiel Vasquez Mejia SMIS001021

from queue import Empty
import smtplib
from tkinter import  Label,Entry,Button,Tk,Text,messagebox

class interfaz():
    def __init__(self):
        self.usuario = ""
        self.contrasenia = ""
        self.entradaUsu = Empty
        self.entradaPass = Empty
        self.emisor = Empty
        self.reseptor = Empty
        self.mensaje = Empty
        self.ventanaPrin = Empty
        self.ventana2 = Empty
    
    def abri(self):
        ventana2 = Tk()
        ventana2.title("Registro")
        ancho_ventana = 500
        alto_ventana = 300

        x_ventana = ventana2.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = ventana2.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        ventana2.geometry(posicion)

        ventana2.resizable(0,0)
        ventana2.configure(background='dark turquoise')

        lb1 = Label(ventana2,text="Registrarse.",bg='dark turquoise',font='Helvetica 16 bold')
        lb1.pack()
        lb2 = Label(ventana2,text="Correo:",bg='dark turquoise',font='Helvetica 12 bold')
        lb2.place(x=50,y=80)
        self.entradaUsu  = Entry(ventana2)
        self.entradaUsu .place(x=200,y=80,width=200)
        lb2 = Label(ventana2,text="Contraseña de App:",bg='dark turquoise',font='Helvetica 11 bold')
        lb2.place(x=50,y=120)
        self.entradaPass = Entry(ventana2)
        self.entradaPass.place(x=200,y=120,width=200)
        btn = Button(ventana2,text="Registrarse",command=clase.registro,bg='black',font='Helvetica 12 bold',fg="white")
        btn.place(x=150,y=200)
        btn2 = Button(ventana2,text="Regresar",command=clase.ventana_principal,bg='black',font='Helvetica 12 bold',fg="white")
        btn2.place(x=280,y=200)
        self.ventanaPrin.destroy()
        self.ventana2 = ventana2
        ventana2.mainloop()

    def enviar(self):
        if self.emisor.get() == "" and self.receptor.get()=="" and self.usuario == "" and self.contrasenia == "":
            messagebox.showerror("Enviar Correo","Debe Ingresar los datos o registrarse")
        else:
            fromaddr = self.emisor.get() 
            toaddrs = self.receptor.get() 
            msg = self.mensaje.get("1.0","end")
            username = self.usuario 
            password = self.contrasenia
        
            try:
                server = smtplib.SMTP('smtp.gmail.com:587') 
                server.starttls() 
                server.login(username,password) 
                server.sendmail(fromaddr, toaddrs, msg) 
                server.quit()
                self.receptor.delete(0,"end")
                self.mensaje.delete("1.0","end")
                messagebox.showinfo("Enviar Mensaje","Correo enviado exitosamente")
            except:
                messagebox.showerror("Enviar Correo","No se pudo enviar el correo.")

    def registro(self):
        self.usuario = self.entradaUsu.get()
        self.contrasenia = self.entradaPass.get()
        if self.usuario == "" and self.contrasenia == "":
            messagebox.showerror("Registro","Debe Ingresar los datos.")
        else:
            
            messagebox.showinfo("Registro","Datos almacenados")
            clase.ventana_principal()
    

    def ventana_principal(self):
       
        ventana = Tk()
        ventana.title("Enviar Correo")
        ancho_ventana = 500
        alto_ventana = 500

        x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        ventana.geometry(posicion)

        ventana.resizable(0,0)
        ventana.configure(background='dark turquoise')

        lb1 = Label(ventana,text="Enviar correo Electronico.",bg='dark turquoise',font='Helvetica 16 bold')
        lb1.pack()
        lb2 = Label(ventana,text="Enviar a:",bg='dark turquoise',font='Helvetica 12 bold')
        lb2.place(x=50,y=80)
        self.receptor = Entry(ventana)
        self.receptor.place(x=200,y=80,width=200)
        lb2 = Label(ventana,text="Usuario:",bg='dark turquoise',font='Helvetica 12 bold')
        lb2.place(x=50,y=120)
        self.emisor = Entry(ventana)
        self.emisor.insert(0,self.usuario)
        self.emisor.place(x=200,y=120,width=200)
        lb0 = Label(ventana,text="Espacio para el cuerpo del mensaje",bg='dark turquoise',font='Helvetica 12 bold')
        lb0.place(x=50,y=160)
        self.mensaje = Text(ventana)
        self.mensaje.place(x=50,y=190,height=200,width=400)
        btn = Button(ventana,text="Enviar Mensaje",command=clase.enviar,bg='black',font='Helvetica 16 bold',fg="white")
        btn.place(x=50,y=400)
        btn = Button(ventana,text="Registrarce",command=clase.abri,bg='black',font='Helvetica 16 bold',fg="white")
        btn.place(x=250,y=400)
        if self.ventana2 != Empty:
            self.ventana2.destroy()
        
        self.ventanaPrin = ventana
        ventana.mainloop()

clase = interfaz()
clase.ventana_principal()