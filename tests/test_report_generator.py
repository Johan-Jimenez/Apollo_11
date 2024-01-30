import unittest
import os
from apollo11.report_generator import ReportGenerator

class TestReportGenerator(unittest.TestCase):
    def test_generate_reports(self):
        # Prueba la función generate_reports en report_generator.py
        report_generator = ReportGenerator()
        data = {'ORBONE': [{'date': '210124120000', 'mission': 'ORBONE', 'device_type': 'device_1', 'device_status': 'excellent', 'hash': 'hash_value'}]}
        report_generator.generate_reports(data)
        self.assertTrue(os.path.exists('reports'))

    def test_get_current_timestamp(self):
        # Prueba la función get_current_timestamp en report_generator.py
        report_generator = ReportGenerator()
        timestamp = report_generator.get_current_timestamp()
        self.assertTrue(timestamp)

if __name__ == '__main__':
    unittest.main()
