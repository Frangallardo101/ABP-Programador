def controlar_dispositivos(lista_dispositivos):
    
    while True: 
        
        print("A) Agregar un dispositivo \n B) Listar dispositivos \n C) Buscar dispositivo \n D) Eliminar un dispositivo")
        
        opcion = input("Seleccione una opcion: ")
        
        if opcion.capitalize() == "A":
            
            Agregar_dispositivos(lista_dispositivos)
            
        if opcion.capitalize() == "B":
            
            listar_dispositivos(lista_dispositivos)
        
        if opcion.capitalize() == "C":
            
            buscar_dispositivo(lista_dispositivos)
        
        if opcion.capitalize() == "D":
            
            eliminar_dispositivo(lista_dispositivos)
            
        if opcion.capitalize() == "E":
            
            break
            

def Agregar_dispositivos(lista_dispositivos):
    
    dispositivo = {}
    
    dispositivo['nombre'] = input("Cual es el dispositivo a agregar?: ")
    
    dispositivo['estado'] = 'apagado'
       
    while True :
        
        accion = input("Que accion realiza el dispositivo?: ")
        
        dispositivo[accion] = 'desactivada'
        
        if (input("El dispositivo realiza otra accion?: ")).lower() == 'si':
            
            continue
        
        else: 
            break
    
    lista_dispositivos.append(dispositivo)
    
def listar_dispositivos(lista_dispositivos):
    
    for i in range(0,len(lista_dispositivos)):
        
        print((lista_dispositivos[i])['nombre'])
        
def buscar_dispositivo(lista_dispositivos): 
    
    dispositivo = input("Cual es el dispositivo a buscar?: ")
    
    while True:
        
        for i in lista_dispositivos:
            
            if dispositivo in i.items():
                
                print(i)
                
                break
            
            else:
                 
                continue
            
def eliminar_dispositivo(lista_dispositivos):
    
    dispositivo = input("Cual es el dispositivo a eliminar?: ")
    
    while True:
        
        for i in lista_dispositivos:
            
            if dispositivo in i.items():
                
                lista_dispositivos.remove(i)
                
                break
            
            else:
                 
                continue
            
            
            