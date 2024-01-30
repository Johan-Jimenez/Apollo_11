import unittest
from apollo11.data_generator import DataGenerator

class TestDataGenerator(unittest.TestCase):
    def test_generate_data(self):
        # Prueba la función generate_data en data_generator.py
        data_generator = DataGenerator()
        max_files = 5
        min_files = 2
        data = data_generator.generate_data(max_files, min_files)
        self.assertIsInstance(data, dict)
        self.assertTrue(data)

    def test_generate_hash(self):
        # Prueba la función generate_hash en data_generator.py
        data_generator = DataGenerator()
        mission = 'ORBONE'
        device_type = 'device_1'
        device_status = 'excellent'
        hash_value = data_generator.generate_hash(mission, device_type, device_status)
        self.assertTrue(hash_value)

if __name__ == '__main__':
    unittest.main()
