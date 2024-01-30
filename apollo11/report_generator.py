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
            # Almacenar datos en el diccionario por misión
            if project not in self.report:
                self.report[project] = {}
            project_states = {'excellent': 0, 'good': 0,
                              'warning': 0, 'faulty': 0, 'killed': 0, 'unknown': 0}
            for file_content in files:
                project_states[file_content['device_status']] += 1
            self.project_device_states[project] = project_states
            for keys in project_states.keys():
                file_value = project_states[keys]
                if keys not in self.report[project].keys():
                    report_value = 0
                else:
                    report_value = self.report[project][keys]
                self.report[project][keys] = file_value + report_value
            logging.debug(
                f'Se ha agregado la mision {project} con {len(files)} misiones al reporte')
        # Generar un único informe consolidado
        report_filename = f'APLSTATS-REPORT-{datetime.now().strftime("%d%m%y%H%M%S")}.log'
        report_path = os.path.join('reports', report_filename)
        # Se hace un recuento de los dispositivos que se encuentran en cada estado
        for project, device_states in self.report.items():
            disconnections = self.report[project]['unknown']
            inoperable_devices = self.report[project]['faulty'] + \
                self.report[project]['killed']
            self.report[project]['disconnections'] = disconnections
            self.report[project]['inoperable_devices'] = inoperable_devices
        # Se hace un calculo del porcentaje de dispositivos que hay en cada estado.
        for project in self.project_device_states.keys():
            total_devices = sum(
                self.report[project][state] for state in self.project_device_states[project])
            for state in self.project_device_states[project]:
                state_count = self.project_device_states[project][state]
                percentage = (state_count / total_devices) * \
                    100 if total_devices > 0 else 0
                percentages[state] = percentage
            self.report[project]['total_devices'] = total_devices
            self.report[project]['percentages'] = percentages

        logging.debug(f"Reporte generado: {report_filename}")
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
