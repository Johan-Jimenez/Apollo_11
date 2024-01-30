import unittest
from apollo11.simulator import Apolo11Simulator

class TestSimulator(unittest.TestCase):
    def test_run_simulation(self):
        # Prueba la función run_simulation en simulator.py
        simulator = Apolo11Simulator(
            simulation_interval=10, max_files=5, min_files=2, project="ORBONE"
        )
        with self.assertLogs(level='INFO') as cm:
            simulator.run_simulation(num_cycles=2)
        self.assertIn('Ciclo completado. Esperando el próximo ciclo...', cm.output[0])

    def test_handle_interrupt(self):
        # Prueba la función handle_interrupt en simulator.py
        simulator = Apolo11Simulator(
            simulation_interval=10, max_files=5, min_files=2, project="ORBONE"
        )
        with self.assertLogs(level='INFO') as cm:
            simulator.handle_interrupt(signum=None, frame=None)
        self.assertIn('Simulación interrumpida por el usuario. Finalizando...', cm.output[0])
        self.assertEqual(cm.output[1], 'Simulación interrumpida por el usuario. Finalizando...')

if __name__ == '__main__':
    unittest.main()
