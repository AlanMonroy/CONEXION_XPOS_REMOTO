#Creador: Roberto Alan Rodriguez Monroy
#import pyautogui
#import keyboard
import json
import os
from tkinter import filedialog
import os.path as path

class Controlador:
    def __init__(self):
        while True:
            self.contador = 0
            def conectar_controlador_json():
                self.contador += 1
                try:
                    with open('controlador.json','r',encoding="UTF-8") as archivo:
                        self.data = json.load(archivo)
                except Exception as e:
                    if self.contador == 20:
                        self.crear_json()
                    print(e)
                    conectar_controlador_json()

            conectar_controlador_json()

            if self.data["CONTROLADOR"] == "XPOS":  # COMPROBAR QUE CONTROLADOR XPOS TIENE ACCESO #
                print(self.data["CONTROLADOR"])
                self.data["CONTROLADOR"] = "REMOTO"    # CAMBIAR A REMOTO #

                # TOMAR SCREENSHOT #
                if self.data['SCREENSHOT']['ESTATUS'] == True:
                    nombre = self.data['SCREENSHOT']['NOMBRE_SCREEN']
                    self.tomar_screen(nombre)
                    #self.cambiar_estatus(nueva_info)

                # Verificiar el apartado por ejecutar direccionamiento y su estatus
                if self.data['INICAR_DIRECCIONAMIENTO']['ESTATUS'] == True:
                    self.activar_exe(self.data['INICAR_DIRECCIONAMIENTO']['RUTA'])
                    # RESETEAR VALORES #
                    self.data['INICAR_DIRECCIONAMIENTO']['ESTATUS'] = False
                    self.data['INICAR_DIRECCIONAMIENTO']['RUTA'] = ''

                with open("controlador.json","w", encoding="UTF-8") as file:
                    print("cambio")
                    json.dump(self.data,file, indent=7)
            else:
                print("Json ocupado por controlador REMOTO")
        """
        if path.exists('controlador.json'):
            while True:
                self.contador = 0
                def abrir_controlador_json():
                    self.contador += 1 
                    try:
                        with open('controlador.json','r',encoding="UTF-8") as archivo:
                            self.data = json.load(archivo)
                    except Exception as e:
                        if self.contador == 991:
                            print("###################################################")
                            print(f"Instancia",e)
                            self.crear_json()
                        print("Archivo 'Controlador' no encontrado.")
                        print("---------------------------------------")
                        abrir_controlador_json()

                abrir_controlador_json()

                if self.data["CONTROLADOR"] == "XPOS":
                    if self.data['SCREENSHOT']['ESTATUS'] == True:
                        nombre = i['SCREENSHOT']['NOMBRE_SCREEN']
                        self.tomar_screen(nombre)
                        self.cambiar_estatus(nueva_info)
                    # Verificiar el apartado por ejecutar direccionamiento y su estatus
                    if self.data['INICAR_DIRECCIONAMIENTO']['ESTATUS'] == True:
                        self.activar_exe(self.data['INICAR_DIRECCIONAMIENTO']['RUTA'])
                        # RESETEAR VALORES #
                        self.data['INICAR_DIRECCIONAMIENTO']['ESTATUS'] = False
                        self.data['INICAR_DIRECCIONAMIENTO']['RUTA'] = ''

                    with open("controlador.json","w", encoding="UTF-8") as file:
                        json.dump(self.data,file, indent=7)
                else:
                    print("Json ocupado por controlador REMOTO")
        else:
            crear_json()"""

        #keyboard.add_hotkey("alt+a", self.tomar_screen)
    """
    def tomar_screen(self,nombre):
        # Capturar pantalla.
        screenshot = pyautogui.screenshot()
        # Guardar imagen.
        screenshot.save(f"C:/Controlador_QA/Screen/{nombre}.png")
        #messagebox.showinfo("Notificación","Screen tomada")
        print("Foto tomada")

    def cambiar_estatus(self):
        nueva_info = list()
        nueva_info.append({"SCREENSHOT": {'ESTATUS':False, 'NOMBRE_SCREEN': nombre}
            })

        with open("controlador.json","w", encoding="UTF-8") as file:
            json.dump(nueva_info,file, indent=7)

    def crear_json(self):
        nueva_info = dict()
        nombre = 'screen_1'
        nueva_info = {  
                        "CONTROLADOR": 'XPOS',
                        "SCREENSHOT": {'ESTATUS':False, 'NOMBRE_SCREEN': nombre},
                        "INICAR_DIRECCIONAMIENTO": {'ESTATUS':False, 'RUTA': ''},
                    }

        with open("controlador.json","w", encoding="UTF-8") as file:
            json.dump(nueva_info,file, indent=7)"""

    def crear_json(self):
        nueva_info = dict()
        nombre = 'screen_1'
        nueva_info = {
                        "CONTROLADOR": "REMOTO",
                        "SCREENSHOT": {'ESTATUS':False, 'NOMBRE_SCREEN': nombre},
                        "INICAR_DIRECCIONAMIENTO": {'ESTATUS':False, 'RUTA': ''},
                    }

        with open("controlador.json","w", encoding="UTF-8") as file:
            json.dump(nueva_info,file, indent=7)

    def activar_exe(self,ruta):
        os.system(ruta)

if __name__ =="__main__":   
    llamar_controlador= Controlador()
    #llamar_controlador.crear_json()

