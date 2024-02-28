import unittest
from unittest.mock import patch
from io import StringIO
import os
from Pycrypt import EncryptionTool


class TestEncryptionTool(unittest.TestCase):

    def setUp(self):
        self.file_path = 'test_file.txt'
        with open(self.file_path, 'w') as f:
            f.write('Test data for encryption')

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_encrypt_decrypt(self):
        key = 'test_key'
        salt = 'test_salt'

        encrypted_file = self.file_path + ".kryp"

        # Encrypt the file
        with patch('sys.stdout', new=StringIO()) as fake_out:
            encrypt_tool = EncryptionTool(self.file_path, key, salt)
            for _ in encrypt_tool.encrypt():
                pass
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "")

        # Decrypt the file
        with patch('sys.stdout', new=StringIO()) as fake_out:
            decrypt_tool = EncryptionTool(encrypted_file, key, salt)
            for _ in decrypt_tool.decrypt():
                pass
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "")

            # Check content integrity
            with open(self.file_path, 'r') as f:
                decrypted_content = f.read()
                self.assertEqual(decrypted_content, 'Test data for encryption')

    def test_abort(self):
        key = 'test_key'
        salt = 'test_salt'

        encrypted_file = self.file_path + ".kryp"

        # Encrypt the file
        with patch('sys.stdout', new=StringIO()) as fake_out:
            encrypt_tool = EncryptionTool(self.file_path, key, salt)
            for _ in encrypt_tool.encrypt():
                pass
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "")

        # Abort encryption
        with patch('sys.stdout', new=StringIO()) as fake_out:
            encrypt_tool.abort()
            self.assertFalse(os.path.exists(encrypted_file))
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "")

    def test_hash_key_salt(self):
        key = 'test_key'
        salt = 'test_salt'

        encrypt_tool = EncryptionTool(self.file_path, key, salt)

        self.assertIn('key', encrypt_tool.hashed_key_salt)
        self.assertIn('salt', encrypt_tool.hashed_key_salt)
        self.assertEqual(len(encrypt_tool.hashed_key_salt['key']), 32)
        self.assertEqual(len(encrypt_tool.hashed_key_salt['salt']), 16)


if __name__ == '__main__':
    unittest.main()
