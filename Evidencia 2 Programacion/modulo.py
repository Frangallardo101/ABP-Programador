def controlar_dispositivos(lista_dispositivos):
    
    while True: 
        
        print("A) Agregar un dispositivo \n B) Listar dispositivos \n C) Buscar dispositivo \n D) Eliminar un dispositivo")
        
        opcion = input("Seleccione una opcion: ")
        
        if opcion.capitalize() == "A":
            
            print(Agregar_dispositivos(lista_dispositivos))
            
        if opcion.capitalize() == "B":
            
            print(listar_dispositivos(lista_dispositivos))
        
        if opcion.capitalize() == "C":
            
            print(buscar_dispositivo(lista_dispositivos))
        
        if opcion.capitalize() == "D":
            
            eliminar_dispositivo(lista_dispositivos)
            
        if opcion.capitalize() == "E":
            
            break
            

def Agregar_dispositivos(lista_dispositivos):
    
    dispositivo = {}
    
    funcion_avanzada = 0
       
    while True : 
       
        dispositivo['nombre'] = input("Cual es el dispositivo a agregar?: ")
    
        dispositivo['estado'] = 0 
         
        marca  =  input("Que marca es el producto?: ") #
        
        dispositivo['Marca'] = marca # Agregamos el valor al diccionario, ahora la clave marca tiene el valor que le asigne el usuario
        
        print("Niveles de acceso:  1.invitado 2.Niños 3.padres ")
        
        nivel_acceso = int((input("Que nivel de acceso requiere el dispositivo?: ")))
        if nivel_acceso not in (1,2,3):
            
            nivel_acceso = print("El valor no es correcto, intente de nuevo: ")
            
        dispositivo['nivel_acceso'] = nivel_acceso# Agregamos el valor al diccionario, ahora la clave nivel_acceso tiene el valor que le asigne el usuario
                                 
        funcion = input("Tiene funciones avanzadas?: ").lower()
        
        if  funcion == "si" :
            
            funcion_avanzada  =  1
            
        elif funcion == "no": 
            
            continue  
        
        dispositivo['funcion_avanzada'] = funcion_avanzada
        
        lista_dispositivos.append(dispositivo)
        
        return "El dispositivo se agrego correctamente"
    
def listar_dispositivos(lista_dispositivos):
    
    for i in range(0,len(lista_dispositivos)):
        
        print((lista_dispositivos[i])['nombre'])
        
def buscar_dispositivo(lista_dispositivos): 
    
    dispositivo = input("Cual es el dispositivo a buscar?: ")
    
    while True:
        
        for dispositivo in lista_dispositivos:
            
            if dispositivo in dispositivo.items():
                
                return (dispositivo)
            
            else:
                 
                continue
            
        return "El dispositivo no fue encontrado"
            
def eliminar_dispositivo(lista_dispositivos):
    
    dispositivo = input("Cual es el dispositivo a eliminar?: ")
    
    while True:
        
        for i in lista_dispositivos:
            
            for key,value in i.items():
                
                if value == dispositivo:
                    
                    lista_dispositivos.remove(i)
                    
                    print("El dispositivo fue eliminado")
                
                break
            
            else:
                 
                continue
        
        print("El dispositivo no fue encontrado")
        
        break
    
    
            
    
            
            
            