# apollo11.py

import sys
import logging
from argparse import ArgumentParser
import yaml
from apollo11.simulator import Apolo11Simulator


def main():
    try:
        # Configuración de LOGGING
        logging.basicConfig(level=logging.DEBUG)

        # Configuración de argumentos de línea de comandos
        parser = ArgumentParser(description="Simulador Apolo-11")
        parser.add_argument(
            "--config", help="Ruta al archivo de configuración YAML", default="config/config.yml")
        parser.add_argument("--project", help="Proyecto a simular",
                            choices=["ORBONE", "CLNM", "TMRS", "GALXONE", "UNKN"], required=False)
        args = parser.parse_args()

        # Cargar configuraciones desde el archivo YAML
        with open(args.config, "r") as config_file:
            config = yaml.safe_load(config_file)

            # Configurar logging, etc. (si es necesario)

            # Crear instancia de Apolo11Simulator y ejecutar la simulación
            apollo_simulator = Apolo11Simulator(
                simulation_interval=config['intervalo_simulacion'],
                max_files=config['max_archivos_generados'],
                min_files=config['min_archivos_generados'],
                project=args.project
            )
            apollo_simulator.run_simulation(num_cycles=10)

    except Exception as e:
        # Manejo de excepciones y registro en LOGGING
        logging.error(f"Error en la ejecución principal: {e}")


if __name__ == "__main__":
    main()
