from Tokens import Token
from Error import Error
import re
from os import startfile
class Reporte_tokens():   

    def __init__(self):
        self.lexema = ''
        self.tokens = []
        self.errores = []
        

    def analisis(self, contenido):
        self.tokens = []
        self.errores = []

        linea = 1
        columna = 1
        self.lexema = ''
        estado = 0
        buffer = ''
        var = ""
        cadena1 = ""
        cadena2 = ""
        
        
        contenido = contenido + '#'
        i = 0
        while i < len(contenido):
            c = contenido[i]
            

            if estado == 0:
                if c == "<":
                    buffer+=c
                    self.tokens.append(Token(buffer, "Simbolo", linea, columna))
                    buffer = ""
                    
                    columna+=1
                    estado = 1  #nos vamos al estado 1
                
                elif c == ">":
                    buffer+=c
                    self.tokens.append(Token(buffer, "Simbolo", linea, columna))
                    buffer = ""
                    
                    columna+=1
                    estado = 1  #Nos vamos al estado 1

                elif c == "~":
                    buffer+=c
                    self.tokens.append(Token(buffer, "Simbolo", linea, columna))
                    buffer = ""
                    
                    columna+=1
                    estado = 1
                
                elif c == ":":
                    buffer+=c
                    self.tokens.append(Token(buffer, "Simbolo", linea, columna))
                    buffer = ""
                    
                    columna+=1
                    estado = 1
                
                elif c == ",":
                    buffer+=c
                    self.tokens.append(Token(buffer, "Simbolo", linea, columna))
                    buffer = ""
                    
                    columna+=1
                    estado = 1

                elif c == "[":
                    buffer+=c
                    self.tokens.append(Token(buffer, "simbolo", linea, columna))
                    buffer = ""
                    
                    columna+=1
                    estado = 1

                elif c == "]":
                    buffer+=c
                    self.tokens.append(Token(buffer, "simbolo", linea, columna))
                    buffer = ""
                    
                    columna+=1
                    estado = 1


                elif re.search(r'[a-zA-Z]', c):
                    buffer+=c
                    columna+=1
                    estado = 1

                elif c == "'":
                    buffer+=c
                    self.tokens.append(Token(buffer, "Simbolo", linea, columna))
                    buffer = ""
                    c = ""
                    columna+=1
                    estado = 3
                
                elif c == '"':
                    buffer+=c
                    self.tokens.append(Token(buffer, "Simbolo", linea, columna))
                    buffer = ""
                    
                    columna+=1
                    estado = 2

                elif c == ' ':
                    columna+=1
                    
                
                elif c == "\n":
                    linea+=1
                    columna = 1
                    

                elif c == "\t":
                    columna+=5
                    
                
                elif c == "\r":
                    pass

                else:
                    buffer+=c
                    print("el buffer es", buffer)
                    self.errores.append(Error("Caracter" + buffer + " no reconocido en el lenguaje", linea, columna))
                    buffer = ""
                    
                    columna+=1

                    
                    
                    

                pass

            elif estado == 1:
                if c == "<":
                    buffer+=c
                    self.tokens.append(Token(buffer, "Simbolo", linea, columna))
                    buffer = ""
                    
                    columna+=1
                    estado = 1  #nos vamos al estado 1
                
                elif c == ">":
                    buffer+=c
                    self.tokens.append(Token(buffer, "Simbolo", linea, columna))
                    buffer = ""
                    
                    columna+=1
                    estado = 1  #Nos vamos al estado 1

                elif c == "~":
                    buffer+=c
                    self.tokens.append(Token(buffer, "Simbolo", linea, columna))
                    buffer = ""
                    
                    columna+=1
                    estado = 1
                
                elif c == ":":
                    buffer+=c
                    self.tokens.append(Token(buffer, "Simbolo", linea, columna))
                    buffer = ""
                    
                    columna+=1
                    estado = 1
                
                elif c == ",":
                    buffer+=c
                    self.tokens.append(Token(buffer, "Simbolo", linea, columna))
                    buffer = ""
                    
                    columna+=1
                    estado = 1

                elif c == "[":
                    buffer+=c
                    self.tokens.append(Token(buffer, "simbolo", linea, columna))
                    buffer = ""
                    
                    columna+=1
                    estado = 1

                elif c == "]":
                    buffer+=c
                    self.tokens.append(Token(buffer, "simbolo", linea, columna))
                    buffer = ""
                    
                    columna+=1
                    estado = 1


                elif re.search(r'[a-zA-Z]', c):
                    buffer+=c
                    var = str(buffer)
                    var = var.lower()
                    columna+=1
                    estado = 1
                    i+=1
                    aux = contenido[i]

                    if var == "tipo":
                        self.tokens.append(Token(buffer, "variable", linea, columna))
                        buffer = ""
                        columna+=4
                        estado = 1
                        var = ""
                        i-=1

                    elif var == "valor" and not re.search(r'[a-zA-Z]', aux):
                        self.tokens.append(Token(buffer, "variable", linea, columna))
                        buffer = ""
                        columna+=5
                        estado = 1
                        var = ""
                        i-=1
                    
                    elif var == "fondo":
                        self.tokens.append(Token(buffer, "variable", linea, columna))
                        buffer = ""
                        columna+=5
                        estado = 1
                        var = ""
                        i-=1

                    elif var == "valores":
                        self.tokens.append(Token(buffer, "variable", linea, columna))
                        buffer = ""
                        columna+=7
                        estado = 1
                        var = ""
                        i-=1
                    
                    elif var == "evento":
                        self.tokens.append(Token(buffer, "variable", linea, columna))
                        buffer = ""
                        columna+=6
                        estado = 1
                        var = ""
                        i-=1
                    
                    elif var == "formulario":
                        self.tokens.append(Token(buffer, "Palabra reservada", linea, columna))
                        buffer = ""
                        columna+=5
                        estado = 1
                        var = ""
                        i-=1
                    
                    elif var == "entrada":
                        self.tokens.append(Token(buffer, "evento", linea, columna))
                        buffer = ""
                        columna+=7
                        estado = 1
                        var = ""
                        i-=1

                    elif var == "info":
                        self.tokens.append(Token(buffer, "evento", linea, columna))
                        buffer = ""
                        columna+=4
                        estado = 1
                        var = ""
                        i-=1


                    elif not re.search(r'[a-zA-Z]', aux):
                        print("el buffer es", buffer)
                        self.errores.append(Error("Caracter" + buffer + " no reconocido en el lenguaje", linea, columna))
                        buffer = ""
                        columna+=len(buffer)
                        i-=1

                    else:
                        i-=1
                        

                elif c == "'":
                    buffer+=c
                    
                    buffer = ""
                    
                    columna+=1
                    estado = 3
                
                elif c == '"':
                    buffer+=c
                    
                    buffer = ""
                    
                    columna+=1
                    estado = 2

                elif c == ' ':
                    columna+=1
                
                elif c == "\n":
                    linea+=1
                    columna = 1

                elif c == "\t":
                    columna+=5
                
                elif c == "\r":
                    pass

                elif c == "#":
                    self.tokens.append(Token('#', "centinela", linea, columna))
                    break
                    
                else:
                    buffer+=c
                    print("el buffer es", buffer)
                    self.errores.append(Error("Caracter" + buffer + " no reconocido en el lenguaje", linea, columna))
                    buffer = ""
                    
                    columna+=1

            elif estado == 2:
                

                if re.search(r'[0-9]', c) or re.search(r'[a-zA-Z]', c):
                    cadena1+=c
                    estado = 2
            
                elif c == '"':
                    cadena1+=c
                    cadena1 = '"' + cadena1
                    self.tokens.append(Token(cadena1, "cadena1", linea, columna))
                    cadena1 = ""
                    estado = 1
            
                else:
                    cadena1+=c
                    estado = 2

            elif estado == 3:
                

                if re.search(r'[0-9]', c) or re.search(r'[a-zA-Z]', c):
                    cadena2+=c
                    estado = 3
            
                elif c == "'":
                    cadena2+=c
                    cadena2 = "'" + cadena2
                    self.tokens.append(Token(cadena2, "cadena2", linea, columna))
                    cadena2 = ""
                    estado = 1
            
                else:
                    cadena2+=c
                    estado = 3
  
            i+=1





    def html_tokens(self):
        
        
        inicio = ' <!DOCTYPE HTML5> <html><head><title>Reporte de tokens</title></head><body style="background-color:#82FF77;"><h1  align="center"> Reporte de tokens </h1>'
        Fin = '</body></html>'
        tabla_inicio= '<center><table border="1"><caption>Lexema con linea y columna donde se encuentra</caption><tr style="background-color:#1DFFE6;"><th>Lexema</th><th>Tipo</th><th>Linea</th><th>Columna</th></tr>'
        tabla_fin = '</table></center>'
        
        for c in self.tokens:
            tabla_inicio += '<tr style="background-color:#A7FFF5;"><td  align="center">' + str(c.lexema) + '</td><td  align="center">' + str(c.tipo) + '</td><td  align="center">' + str(c.linea) + '</td><td  align="center">' + str(c.columna) + '</td></tr>'
            

    
        contenido = inicio + tabla_inicio + tabla_fin + Fin
        archivo = open('Reporte_tokens.html', 'w')
        archivo.write(contenido)
        archivo.close

        startfile('Reporte_tokens.html')
        