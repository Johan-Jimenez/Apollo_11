import unittest
from apollo11.dashboard_generator import DashboardGenerator

class TestDashboardGenerator(unittest.TestCase):
    def test_dashboard_data_update(self):
        # Prueba la función dashboard_data_update en dashboard_generator.py
        dashboard_generator = DashboardGenerator()
        dashboard_generator.mission_device_states = {'ORBONE': {'excellent': 5, 'good': 3, 'warning': 1, 'faulty': 0, 'killed': 0, 'unknown': 2}}
        data_add = {'ORBONE': {'excellent': 3, 'good': 2, 'warning': 0, 'faulty': 1, 'killed': 0, 'unknown': 1}}
        dashboard_generator.dashboard_data_update(
            data_dash=dashboard_generator.mission_device_states, data_add=data_add
        )
        self.assertEqual(dashboard_generator.mission_device_states['ORBONE']['excellent'], 8)

    def test_dashboard_data_clean(self):
        # Prueba la función dashboard_data_clean en dashboard_generator.py
        dashboard_generator = DashboardGenerator()
        dashboard_generator.mission_device_states = {'ORBONE': {'excellent': 5, 'good': 3, 'warning': 1, 'faulty': 0, 'killed': 0, 'unknown': 2}}
        dashboard_generator.dashboard_data_clean()
        self.assertEqual(dashboard_generator.mission_device_states['ORBONE']['excellent'], 0)

    def test_print_dashboard(self):
        # Prueba la función print_dashboard en dashboard_generator.py
        dashboard_generator = DashboardGenerator()
        with self.assertLogs(level='DEBUG') as cm:
            dashboard_generator.print_dashboard()
        self.assertIn('Tablero de control actualizado', cm.output[0])

if __name__ == '__main__':
    unittest.main()
