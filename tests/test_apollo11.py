import unittest
from unittest.mock import patch
from io import StringIO
from apollo11 import main  # Importa directamente la función main desde el módulo apollo11

class TestApolo11(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout):
        # Prueba la función main en apollo11.py
        with self.assertRaises(SystemExit) as context:
            main()
        
        # Verifica que la salida sea correcta
        self.assertEqual(context.exception.code, 0)
        
        # Verifica que el mensaje esperado esté en la salida estándar
        expected_output = "Ciclo completado. Esperando el próximo ciclo..."
        self.assertIn(expected_output, mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
