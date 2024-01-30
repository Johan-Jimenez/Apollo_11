# apollo11/file_manager.py

import json
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
            file_name = f"APL{project}-{len(files)}"
            file_path = os.path.join('devices', file_name + '.log')
            data_mision = {project: files}

            # Escribir el contenido del archivo
            with open(file_path, 'w') as file:
                file.write(json.dumps(data_mision, indent=4))

                # Registrar la generación del archivo en el registro
                logging.info(
                    f"File {file_name} generated for project {project}")

    def move_processed_files(self):
        """
        Mueve el último archivo procesado a la carpeta de backups.
        """
        backup_folder = 'backups'
        os.makedirs(backup_folder, exist_ok=True)

        # Obtener el último archivo en 'devices' según la última modificación
        content = os.listdir('./devices')
        for files in content:
            source_path = os.path.join('devices', files)
            destination_path = os.path.join(backup_folder, files)
            # Mover el archivo procesado a la carpeta de backups
            shutil.move(source_path, destination_path)

        # Registrar el movimiento del archivo procesado en el registro
        logging.debug(f'Archivo {files} moviendose a backup')
        logging.info("Processed file moved to the backups folder.")
