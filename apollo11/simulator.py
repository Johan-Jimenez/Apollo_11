# apollo11/simulator.py

from typing import Dict, List
from datetime import datetime
import logging
import time
import signal
import sys
from apollo11.data_generator import DataGenerator
from apollo11.file_manager import FileManager
from apollo11.report_generator import ReportGenerator
from apollo11.dashboard_generator import DashboardGenerator


class Apolo11Simulator:
    def __init__(self, simulation_interval: int, max_files: int, min_files: int, project: str):
        """
        Inicializa el simulador Apolo-11 con parámetros específicos.

        Parameters:
        - simulation_interval (int): Intervalo de simulación en segundos.
        - max_files (int): Número máximo de archivos a generar en cada ciclo de simulación.
        - project (str): Proyecto/misión para la simulación.
        """
        self.simulation_interval = simulation_interval
        self.max_files = max_files
        self.min_files = min_files
        self.project = project
        self.data_generator = DataGenerator()
        self.file_manager = FileManager()
        self.report_generator = ReportGenerator()
        self.dashboard_generator = DashboardGenerator()

        signal.signal(signal.SIGINT, self.handle_interrupt)

    def run_simulation(self, num_cycles: int):
        """
        Ejecuta la simulación de Apolo-11 durante un número específico de ciclos.

        Parameters:
        - num_cycles (int): Número de ciclos de simulación a ejecutar.
        """
        try:
            for _ in range(num_cycles):
                data = self.data_generator.generate_data(
                    self.max_files, self.min_files)
                self.file_manager.manage_files(data)
                self.report_generator.generate_reports(data)
                self.file_manager.move_processed_files()
                self.dashboard_generator.generate_dashboard(
                    210124120000, 210124129999)

                logging.info(
                    "Ciclo completado. Esperando el próximo ciclo...")
                time.sleep(self.simulation_interval)

        except KeyboardInterrupt:
            self.handle_interrupt(None, None)
            # Interrupción del ciclo con CTRL+C

    def handle_interrupt(self, signum, frame):
        """
        Maneja la interrupción del simulador por parte del usuario (CTRL+C).
        Finaliza la simulación.

        Parameters:
        - signum: Señal de interrupción.
        - frame: Marco de ejecución actual.
        """
        logging.info("Simulación interrumpida por el usuario. Finalizando...")
        sys.exit(0)
