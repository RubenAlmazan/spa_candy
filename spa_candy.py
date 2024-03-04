import pandas as pd
import os

class Masajistas:
    
    def __init__(self, filename):
        self.filename = filename
        self.data = pd.read_csv(filename)

    def menu(self):
        salir = False
        while not salir:
            print("\n**********        MENU DE MASAJISTAS       **********\n")
            print(" (1) Capturar masajista")
            print(" (2) Buscar masajista")
            print(" (3) Mostrar masajistas disponibles")
            print(" (4) Modificar datos del masajista")
            print(" (5) Eliminar masajista")
            print(" (6) Salir\n")
            opcion = input(" -> Ingrese una opcion: ")
            
            if opcion == '1':
                self.capturar()
            elif opcion == '2':
                self.buscar()
            elif opcion == '3':
                self.mostrar_registros()
            elif opcion == '4':
                self.modificar()
            elif opcion == '5':
                self.eliminar()
            elif opcion == '6':
                salir = True
                input("PROGRAMA FINALIZADO...")

                input("Presiona Enter para continuar...")
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("    Ha ingresado una opcion no valida!\n")

    def capturar(self):  
        print("\n **********        CAPTURAR MASAJISTA       **********\n")
        id_masajista = int(input('-> Ingrese un ID valido: '))
        
        if id_masajista in self.data['ID'].values:
            print('ID ya existe en los registros')
        else:
            nombre = input("    Ingrese un nombre: ")
            correo = input("    Ingrese un correo: ")
            telefono = input("    Ingrese un telefono: ")
            
            nuevo_registro = pd.DataFrame([[id_masajista, nombre, correo, telefono, 'Empleado']], columns=self.data.columns)

            self.data = pd.concat([self.data, nuevo_registro], ignore_index=True)
            self.data.to_csv(self.filename, index=False)
            print("Registro agregado exitosamente.")
        
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')

    def eliminar(self):
        print("\n **********        ELIMINAR MASAJISTA       **********\n")
        indice_a_eliminar = int(input(" -> Ingrese un ID a eliminar: "))
        
        if indice_a_eliminar in self.data['ID'].values:
            self.data = self.data[self.data['ID'] != indice_a_eliminar]
            self.data.to_csv(self.filename, index=False)
            print("Registro eliminado exitosamente.")
        else:
            print('ID no encontrado en los registros')
        
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')

    def buscar(self):
        print("\n **********        BUSCAR MASAJISTA       **********\n")
        indice_a_buscar = int(input(" -> Ingrese un ID a buscar: "))

        empleado = self.data[self.data['ID'] == indice_a_buscar]
        
        if empleado.empty:
            print('Registro no encontrado')
        else:
            print(empleado)
        
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')

    def modificar(self):
        print("\n **********        MODIFICAR MASAJISTA       **********\n")
        indice_a_modificar = int(input(" -> Ingrese un ID a modificar: "))
        
        if indice_a_modificar in self.data['ID'].values:
            nombre = input(" -> Ingrese un nombre: ")
            correo = input(" -> Ingrese un correo: ")
            telefono = input(" -> Ingrese un telefono: ")

            self.data.loc[self.data['ID'] == indice_a_modificar, 'Nombre'] = nombre
            self.data.loc[self.data['ID'] == indice_a_modificar, 'Correo'] = correo
            self.data.loc[self.data['ID'] == indice_a_modificar, 'Celular'] = telefono

            self.data.to_csv(self.filename, index=False)
            print("Registro modificado exitosamente.")
        else:
            print('ID no encontrado en los registros')
        
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_registros(self):
        print("\n **********        MOSTRAR REGISTROS DE MASAJISTAS       **********\n")
        empleados = self.data
        print(empleados)
        
        input("Presiona Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
        
        

######################################################################################################
        
masajistas = Masajistas('registros.csv')
masajistas.menu()

