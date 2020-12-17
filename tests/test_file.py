import unittest
from unittest.mock import mock_open, patch, MagicMock
from unittest import mock
from src.file import File


class TestFile(unittest.TestCase):

    def setUp(self):
        self.tmp = File()

    def test_File_read(self):
        open = mock_open(read_data="test data")

        with patch('builtins.open', open):
            self.assertEqual("test data", self.tmp.read('/path/'))

    def test_File_write(self):
        open = mock_open(read_data="test data")

        with patch('builtins.open', open):
            self.tmp.write('/path/', "test data 2")

        open.assert_called_once_with('/path/', 'w+')

    def test_File_delete_success(self):
        mock = MagicMock()
        mock2 = MagicMock()

        with patch('os.path.exists', mock):
            with patch('os.remove', mock2):
                result = self.tmp.delete('/path/')

        self.assertEqual(result, True)

    def test_File_delete_failure(self):
        mock = MagicMock()
        mock.return_value = False
        mock2 = MagicMock()

        with patch('os.path.exists', mock):
            with patch('os.remove', mock2):
                self.assertRaises(Exception, self.tmp.delete, '/path/')


if __name__ == '__main__':
    unittest.main()