#Creador: Roberto Alan Rodriguez Monroy
#import pyautogui
#import keyboard
import json
import os
from tkinter import filedialog
import time
import logging
from concurrent.futures import ThreadPoolExecutor


class Controlador:
    def __init__(self):
        self.contador = 0
        def conectar_controlador_json():
            self.contador += 1
            try:
                with open('controlador.json', 'r', encoding="UTF-8") as archivo:
                    self.data = json.load(archivo)
            except Exception as e:
                if self.contador == 20:
                    self.crear_json()
                print(e)
                conectar_controlador_json()

        conectar_controlador_json()

    def activar_programa(self):
        if self.data['CONTROLADOR'] == "REMOTO":
            self.data['CONTROLADOR'] = "XPOS"
            self.data['INICAR_DIRECCIONAMIENTO']['ESTATUS'] = True
            self.data['INICAR_DIRECCIONAMIENTO']['RUTA'] = 'C:/Monroy_Direccionamiento'
            with open("controlador.json","w", encoding="UTF-8") as file:
                json.dump(self.data,file, indent=7)
        else:
            print("Json ocupado por controlador XPOS")

    def crear_json(self):
        nueva_info = dict()
        nombre = 'screen_1'
        nueva_info = {
                        "CONTROLADOR": "XPOS",
                        "SCREENSHOT": {'ESTATUS':False, 'NOMBRE_SCREEN': nombre},
                        "INICAR_DIRECCIONAMIENTO": {'ESTATUS':False, 'RUTA': ''},
                    }

        with open("controlador.json","w", encoding="UTF-8") as file:
            json.dump(nueva_info,file, indent=7)

if __name__ =="__main__":
    llamar_controlador = Controlador()

    '''
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: & (mensage)s")
    executor = ThreadPoolExecutor(max_workers=2)
    executor.submit(llamar_controlador.activar_programa())'''
    
    llamar_controlador.activar_programa()  
