# apollo11/file_manager.py

import os
import shutil
import logging
from typing import Dict, List

class FileManager:
    def __init__(self):
        # Asegura que la carpeta 'backups' exista
        os.makedirs('backups', exist_ok=True)

    def manage_files(self, data: Dict[str, List[Dict[str, str]]]):
        """
        Gestiona los archivos generados a partir de los datos simulados.

        Parameters:
        - data (Dict[str, List[Dict[str, str]]]): Un diccionario que contiene información de dispositivos por misión.
        """
        # Asegura que la carpeta 'devices' exista
        os.makedirs('devices', exist_ok=True)

        for project, files in data.items():
            # Tomar solo el primer archivo para simplificar la lógica
            file_content = files[0]
            file_name = f"APL{project}-{len(files)}"
            file_path = os.path.join('devices', file_name + '.log')

            # Escribir el contenido del archivo
            with open(file_path, 'w') as file:
                file.write(f"Date: {file_content['date']}\nMission: {file_content['mission']}\n"
                            f"Device Type: {file_content['device_type']}\nDevice Status: {file_content['device_status']}\n"
                            f"Hash: {file_content['hash']}\n")
                
                # Registrar la generación del archivo en el registro
                logging.info(f"File {file_name} generated for project {project}")

    def move_processed_files(self):
        """
        Mueve el último archivo procesado a la carpeta de backups.
        """
        backup_folder = 'backups'
        os.makedirs(backup_folder, exist_ok=True)

        # Obtener el último archivo en 'devices' según la última modificación
        latest_file = max(os.listdir('devices'), key=lambda x: os.path.getmtime(os.path.join('devices', x)))
        source_path = os.path.join('devices', latest_file)
        destination_path = os.path.join(backup_folder, latest_file)

        # Mover el archivo procesado a la carpeta de backups
        shutil.move(source_path, destination_path)

        # Registrar el movimiento del archivo procesado en el registro
        logging.info("Processed file moved to the backups folder.")
