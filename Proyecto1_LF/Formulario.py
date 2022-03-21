import re
from Elementos import Elementos
from os import startfile

class Formulario():

    def __init__(self):
        self.variable = ""
        self.valor = ""
        self.elementos = []
        self.compnentes = []
        self.id = 0
        self.id2 = 0
        self.id3 = 0
        

    
    def Crear(self, contenido):
        global id
        id = 0
        self.elementos = []
        self.variable = ""
        self.valor = ""
        buffer = ""
        var = ""
        estado = 0

        i = 0
        while i < len(contenido):
            c = contenido[i]


            if c == "<":
                i+=1
                c = contenido[i]
                while c != ">":
                    c = contenido[i]

                    if re.search(r'[a-zA-Z]', c):
                        buffer+=c
                        var = str(buffer)
                        var = var.lower()
                        i+=1
                        aux = contenido[i]

                        if var == "tipo":
                            i-=1
                            self.variable = var
                            i+=1
                            c = contenido[i]
                            while c != '"':
                                i+=1
                                c = contenido[i]
                                
                                if c == '"':
                                    i+=1
                                    c = contenido[i]
                                    while c != '"':
                                        self.valor+=c
                                        i+=1
                                        c = contenido[i]
                                    self.elementos.append(Elementos(self.variable, self.valor))
                                    buffer = ""
                                    self.valor = ""
                                    continue
                        
                        elif var == "valor" and not re.search(r'[a-zA-Z]', aux):
                            #acepta valor entre comillas
                            self.variable = var
                            i-=1
                            i+=1
                            c = contenido[i]
                            while c != '"':
                                i+=1
                                c = contenido[i]

                                if c == '"':
                                    i+=1
                                    c = contenido[i]
                                    while c != '"':
                                        self.valor+=c
                                        i+=1
                                        c = contenido[i]
                                    self.elementos.append(Elementos(self.variable, self.valor))
                                    buffer = ""
                                    self.valor = ""
                                    continue
                        
                        elif var == "fondo":
                            #acepta valor entre comillas
                            self.variable = var
                            i-=1
                            i+=1
                            c = contenido[i]
                            while c != '"':
                                i+=1
                                c = contenido[i]
                                
                                if c == '"':
                                    i+=1
                                    c = contenido[i]
                                    while c != '"':
                                        self.valor+=c
                                        i+=1
                                        c = contenido[i]
                                    self.elementos.append(Elementos(self.variable, self.valor))
                                    buffer = ""
                                    self.valor = ""
                                    continue

                        elif var == "valores":
                            #acepta valor entre parentesis
                            self.variable = var
                            i-=1
                            i+=1
                            c = contenido[i]
                            while c != '[':
                                i+=1
                                c = contenido[i]
                                
                                if c == '[':
                                    i+=1
                                    c = contenido[i]
                                    while c != ']':
                                        self.valor+=c
                                        i+=1
                                        c = contenido[i]
                                    self.elementos.append(Elementos(self.variable, self.valor))
                                    buffer = ""
                                    self.valor = ""
                                    break

                        elif var == "evento":
                            #acepta info o entrada
                            self.variable = var
                            i-=1
                            i+=1
                            c = contenido[i]
                            buffer = ""
                            while not re.search(r'[a-zA-Z]', c):
                                i+=1 
                                c = contenido[i]

                                if re.search(r'[a-zA-Z]', c):
                                   
                                    while re.search(r'[a-zA-Z]', c):
                                        c = contenido[i]
                                        buffer+=c
                                        var = str(buffer)
                                        var = var.lower()

                                        if var == "info":
                                            self.valor = var
                                            self.elementos.append(Elementos(self.variable, self.valor))
                                            buffer = ""
                                            self.valor = ""
                                            break
                                    
                                        elif var == "entrada":
                                            self.valor = var
                                            self.elementos.append(Elementos(self.variable, self.valor))
                                            buffer = ""
                                            self.valor = ""
                                            break
                                        else:
                                            i+=1 

                                     

                        else:
                            i-=1


                    
                    i+=1
                self.crear_componentes()
                self.elementos.clear()
            else:
                i+=1

        self.crear_formulario()          

    def crear_componentes(self):
        
        for c in self.elementos:  #buscara en el unico compomente existente en la lista
            #print(c.variable, c.valor)
            if c.variable == "tipo":  #encuentra la variable tipo
                if c.valor == "etiqueta":  #verifica si su valor es etiqueta
                    for c in self.elementos:
                        if c.variable == "valor":
                            etiqueta = "<center>"+"\n"+"<label>" + str(c.valor) + "</label>"+"\n"+"</center>"+"\n"+"<br>"+"\n"
                            self.compnentes.append(etiqueta)
                            break
                    

                elif c.valor == "texto": #verifica si el valor de la variable tipo es texto
                    x = 0
                    
                    for c in self.elementos:
                        
                        y = 0
                        if c.variable == "valor":
                            texto = '<center><label>' + str(c.valor) + "</label>"+"\n"
                            
                            for c in self.elementos:
                                
                                if c.variable == "fondo":

                                    texto+='<input type="text"'+ 'name="Input"'+"placeholder="+'"'+str(c.valor)+'"'+"/>"+"</center><br>"+"\n"
                                    self.compnentes.append(texto)
                                    break
                                else:
                                    y+=1

                            if y == len(self.elementos):
                                for c in self.elementos:
                                    if c.variable == "valor":
                                        texto+='<input type="text"'+ 'name="Input"'+"/>"+"</center><br>"+"\n"
                                        self.compnentes.append(texto)
                                        break
                        else:
                            x+=1
 
                    if x == len(self.elementos):
                        for c in self.elementos:
                            if c.variable == "fondo":
                                texto ='<center><input type="text"'+ 'name="Input"'+"placeholder="+'"'+str(c.valor)+'"'+"/>"+"</center><br>"+"\n"
                                self.compnentes.append(texto)
                                break
                                
                        

                            
                            
                        

                elif c.valor == "grupo-radio":
                    opcion = ""
                    self.id+=1
                    y = 0
                    for c in self.elementos:
                        if c.variable == "valor":
                            radio = "<center><label for="+'"'+str(c.valor)+'"><b>'+str(c.valor)+"</b></label><br>"+"\n"+'<radio class="opciones">'
                            
                            for c in self.elementos:
                                if c.variable == "valores":
                                    cadena = str(c.valor)
                                    i = 0
                                    while i < len(cadena):
                                        x = cadena[i]
                                        if x == "'":
                                            i+=1
                                            x = cadena[i]
                                            while x != "'":
                                                opcion+=x
                                                i+=1
                                                x = cadena[i]  
                                            
                                            radio+= '<input type="radio"'+ 'name="'+str(self.id)+'"' + "value="+'"'+str(opcion)+'">'+ str(opcion)+"\n"
                                            opcion = ""
                                            i+=1
                                        else:
                                            i+=1

                            radio+="</radio></center><br>"+"\n"
                            self.compnentes.append(radio)

                        else:
                            y+=1
                    
                    if y == len(self.elementos): #significa que no encontro valor
                        radio = '<center><radio class="opciones">'
                        for c in self.elementos:
                            if c.variable == "valores":
                                cadena = str(c.valor)
                                z = 0
                                while z < len(cadena):
                                    x = cadena[z]
                                    if x == "'":
                                        z+=1
                                        x = cadena[z]
                                        while x != "'":
                                            opcion+=x
                                            z+=1
                                            x = cadena[z]
                                        radio+= '<input type="radio"'+ 'name="'+str(self.id)+'"' + "value="+'"'+str(opcion)+'">'+ str(opcion)+"\n"
                                        opcion = ""
                                        z+=1
                                    else:
                                        z+=1
                                        
                                    
                                
                        radio+="</radio></center><br>"+"\n"
                        self.compnentes.append(radio)
                            
                            
                        




                elif c.valor == "grupo-option":
                    opcion = ""
                    self.id3+=1
                    y = 0

                    for c in self.elementos:
                        if c.variable == "valor":
                            option = "<center><label for="+'"'+str(c.valor)+'"'+"><b>"+str(c.valor)+'</b></label>'+"\n"+'<select class="lista" id="'+str(self.id3)+'">'+"\n"
                            
                            for c in self.elementos:
                                if c.variable == "valores":
                                    cadena = str(c.valor)
                                    i = 0
                                    while i < len(cadena):
                                        x = cadena[i]
                                        
                                        if x == "'":
                                            i+=1
                                            x = cadena[i]
                                            while x != "'":
                                                opcion+=x
                                                i+=1
                                                x = cadena[i]
                                            
                                            option+='<option value="'+str(opcion)+'">'+str(opcion)+"</option>"+"\n"
                                            opcion = ""
                                            
                                            i+=1
                                        else:
                                            i+=1

                                    
                            option+="</select></center><br>"+"\n"
                            self.compnentes.append(option)

                        else:
                            y+=1
                    
                    if y == len(self.elementos):
                        option = '<center><select class="lista" id="'+str(self.id3)+'">'+"\n"
                        for c in self.elementos:
                            if c.variable == "valores":
                                cadena = str(c.valor)
                                i = 0
                                while i < len(cadena):
                                    x = cadena[i]

                                    if x == "'":
                                        i+=1
                                        x = cadena[i]
                                        while x != "'":
                                            opcion+=x
                                            i+=1
                                            x = cadena[i]
                                        
                                        option+='<option value="'+str(opcion)+'">'+str(opcion)+"</option>"+"\n"
                                        opcion = ""
                                        
                                        i+=1
                                    else:
                                        i+=1

                                
                        
                        option+="</select></center><br>"+"\n"
                        self.compnentes.append(option)

                elif c.valor == "boton":
                    for c in self.elementos:
                        if c.variable == "evento":
                            y = 0
                            
                            boton = '<center><input data-bs-toggle="modal" data-bs-target="#modalexample"type="button"'+'id="'+str(c.valor)+'"'
                            for c in self.elementos:
                                if c.variable == "valor":
                                    boton+="value="+'"'+c.valor+'"'+"></center>"+"\n"
                                    self.compnentes.append(boton)
                                    break
                                else:
                                    y+=1

                    
                    if y == len(self.elementos):
                       boton+='value="Boton"></center>'+"\n"
                       self.compnentes.append(boton)
                    
    

    def crear_formulario(self):

        componentes = ""
        for c in self.compnentes:
            componentes+=c

        inicio = '<html>'+"\n"+'<head>'+"\n"+'<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">'+"\n"+'<title>Formulario</title>'+"\n"+'</head>'+"\n"
        inicio+='<body style="background-color:#69FFF7;">'+"\n"+'<h1  align="center">Formulario</h1>'+"\n"
        final = '<div id="datos"></div><script src="app.js"></script></body></html>'

        contenido = inicio + componentes + final

        archivo = open("formulario.html", "w")
        archivo.write(contenido)
        archivo.close

        startfile("formulario.html")
        