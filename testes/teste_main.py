import unittest
import hashlib
import main

class TestApp(unittest.TestCase):
    def test_hash_senha(self):
        senha = "1234"
        hashed = main.hash_senha(senha)
        self.assertNotEqual(senha, hashed)
        self.assertEqual(main.hash_senha("1234"), hashed)

    def test_cadastro_e_login(self):
        usuarios = {}
        usuario = "teste"
        senha = "senha123"
        usuarios[usuario] = main.hash_senha(senha)

        self.assertTrue(
            usuarios[usuario] == main.hash_senha("senha123")
        )

        self.assertFalse(
            usuarios[usuario] == main.hash_senha("errada")
        )

if __name__ == "__main__":
    unittest.main()