import unittest
import os
import json
from apollo11.file_manager import FileManager

class TestFileManager(unittest.TestCase):
    def test_manage_files(self):
        # Prueba la función manage_files en file_manager.py
        file_manager = FileManager()
        data = {'ORBONE': [{'date': '210124120000', 'mission': 'ORBONE', 'device_type': 'device_1', 'device_status': 'excellent', 'hash': 'hash_value'}]}
        file_manager.manage_files(data)
        self.assertTrue(os.path.exists('devices'))
        self.assertFalse(os.path.exists('backups'))

    def test_move_processed_files(self):
        # Prueba la función move_processed_files en file_manager.py
        file_manager = FileManager()
        data = {'ORBONE': [{'date': '210124120000', 'mission': 'ORBONE', 'device_type': 'device_1', 'device_status': 'excellent', 'hash': 'hash_value'}]}
        file_manager.manage_files(data)
        file_manager.move_processed_files()
        self.assertTrue(os.path.exists('backups'))
        self.assertFalse(os.path.exists('devices'))

if __name__ == '__main__':
    unittest.main()
