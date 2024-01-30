# apollo11/data_generator.py

import os
import random
import hashlib
from datetime import datetime
from typing import Dict, List


class DataGenerator:
    MISSIONS = ["ORBONE", "CLNM", "TMRS", "GALXONE", "UNKN"]
    DEVICE_STATES = ["excellent", "good",
                     "warning", "faulty", "killed", "unknown"]

    def generate_data(self, max_files: int, min_files: int) -> Dict[str, List[Dict[str, str]]]:
        """
        Genera datos simulados para dispositivos en una misión.

        Parameters:
        - max_files (int): La cantidad máxima de archivos a generar.
        - project (str): La misión para la cual se generarán los datos.

        Returns:
        Dict[str, List[Dict[str, str]]]: Un diccionario que contiene información de dispositivos por misión.
        """
        data = {}

        for _ in range(random.randint(min_files, max_files)):
            project = random.choice(
                ['ORBONE', 'CLNM', 'TMRS', 'GALXONE', 'UNKN'])
            mission = project if project in self.MISSIONS else "UNKN"
            device_type = f'device_{random.randint(1, 10)}'
            device_status = random.choice(self.DEVICE_STATES)

            # Generar hash para la misión y el estado conocidos
            hash_value = self.generate_hash(
                mission, device_type, device_status)

            # Contenido del archivo simulado
            file_content = {
                "date": datetime.now().strftime("%d%m%y%H%M%S"),
                "mission": mission,
                "device_type": device_type,
                "device_status": device_status,
                # Tomar solo los primeros 32 caracteres del hash
                "hash": hash_value[:32]
            }

            # Almacenar datos en el diccionario por misión
            if project not in data:
                data[project] = []

            data[project].append(file_content)

        return data

    def generate_hash(self, mission: str, device_type: str, device_status: str) -> str:
        """
        Genera un hash para la información dada.

        Parameters:
        - mission (str): La misión del dispositivo.
        - device_type (str): El tipo de dispositivo.
        - device_status (str): El estado del dispositivo.

        Returns:
        str: El hash generado.
        """
        # Generar hash solo si la misión no es "unknown"
        if mission == "UNKN":
            return "unknown"

        # Calcular el hash utilizando la información proporcionada
        data_to_hash = f"{datetime.now().strftime('%d%m%y%H%M%S')}{mission}{device_type}{device_status}"
        hash_value = hashlib.sha256(data_to_hash.encode()).hexdigest()
        return hash_value
