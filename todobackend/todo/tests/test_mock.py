import unittest
from unittest import mock
from manage import main


# Test to check the response of app when a module not found
class TestDjangoImport(unittest.TestCase):
    @mock.patch('builtins.__import__',
                side_effect=ImportError("Django not installed"))
    def test_django_import_error(self, mock_import):
        with self.assertRaises(ImportError) as cm:
            main()

        self.assertEqual(
            str(cm.exception),
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )
