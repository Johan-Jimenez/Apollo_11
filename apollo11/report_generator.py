# apollo11/report_generator.py

import os
import logging
import json
from datetime import datetime
from typing import Dict, List


class ReportGenerator:
    def __init__(self):
        # Inicializa el atributo project_device_states como un diccionario vacío
        self.project_device_states: Dict[str, Dict[str, int]] = {}
        self.report: Dict[str, List[Dict]] = {}

    def generate_reports(self, data: Dict[str, List[Dict[str, str]]]):
        """
        Genera informes consolidados a partir de los datos simulados.

        Parameters:
        - data (Dict[str, List[Dict[str, str]]]): Un diccionario que contiene información de dispositivos por misión.
        """
        # Inicializar el diccionario si aún no ha sido inicializado
        if not isinstance(self.project_device_states, dict):
            self.project_device_states = {}
        # Se inicializan los diccionarios donde se almacenaran datos
        percentages = {}
        mision_status = {}
        device_dict = {}
        # Actualizar el diccionario con nuevos datos
        for project, files in data.items():
            project_states = {'excellent': 0, 'good': 0,
                              'warning': 0, 'faulty': 0, 'killed': 0, 'unknown': 0}
            for file_content in files:
                project_states[file_content['device_status']] += 1
            self.project_device_states[project] = project_states
        # Generar un único informe consolidado
        report_filename = f'APLSTATS-REPORT-{datetime.now().strftime("%d%m%y%H%M%S")}.log'
        report_path = os.path.join('reports', report_filename)
        # Se hace un recuento de los dispositivos que se encuentran en cada estado
        for project, device_states in self.project_device_states.items():
            for state, count in device_states.items():
                device_dict[state] = count
            mision_status.update(device_dict)
            mision_status['disconnections'] = device_dict['unknown']
            mision_status['inoperable_devices'] = device_dict['faulty'] + \
                device_dict['killed']
        # Se hace un calculo del porcentaje de dispositivos que hay en cada estado.
        for project in self.project_device_states.keys():
            total_devices = sum(
                device_states[state] for state in self.project_device_states[project])
            for state in self.project_device_states[project]:
                state_count = self.project_device_states[project][state]
                percentage = (state_count / total_devices) * \
                    100 if total_devices > 0 else 0
                percentages[state] = percentage
        mision_status['total_devices'] = total_devices
        mision_status['percentages'] = percentages
        self.report[project] = mision_status

        logging.debug(f"Informe consolidado generado: {report_filename}")
        # Se guarda el reporte en un archivo .log en la carpeta ./devices
        with open(report_path, 'w', encoding='utf-8') as report_file:
            report_file.write(json.dumps(self.report, indent=4))

    def get_current_timestamp(self):
        """
        Obtiene la marca de tiempo actual en el formato '%Y%m%d%H%M%S'.

        Returns:
        - str: Marca de tiempo actual.
        """
        return datetime.now().strftime('%Y%m%d%H%M%S')
