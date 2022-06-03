import unittest
import requests


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.url = "https://7eb984w4j4.execute-api.us-east-1.amazonaws.com/dev/lambdastresstest"
        self.headers = {"Content-Type": "application/json"}
        self.data = {
            "mensagem": "Lorem ipsum dolor sit amet, consectetur adipiscing elite. Seds finibus velito sit amets blandit blandit.",
            "num_destinatario": "12345678908"
        }

    def respostaAPI(self, data):
        resposta = requests.post(self.url, json=data)
        retorno = resposta.json()
        return retorno['statusCode'], retorno['body']

    def test_status_validar_mensagem(self):
        status_code, body = self.respostaAPI(self.data)
        self.assertEqual(status_code, 200)
        self.assertEqual(body, '"Mensagem enviada com sucesso"')

    def test_status_mensagem_vazia(self):
        data = {
            "mensagem": "",
            "num_destinatario": 12345678908
        }
        status_code, body = self.respostaAPI(data)
        self.assertEqual(status_code, 400)
        self.assertEqual(body, 'Mensagem enviada com sucesso')

    def test_status_mensagem_nulo(self):
        data = {
            "mensagem": None,
            "num_destinatario": 12345678908
        }
        status_code, body = self.respostaAPI(data)
        self.assertEqual(status_code, 400)
        self.assertEqual(body, 'O campo mensagem não pode ser nulo')

    def test_status_num_destinatario_nulo(self):
        data = {
            "mensagem": "Lorem ipsum dolor",
            "num_destinatario": None
        }
        status_code, body = self.respostaAPI(data)
        self.assertEqual(status_code, 400)
        self.assertEqual(body, 'O campo mensagem não pode ser nulo')

    def test_status_num_destinatario_vazio(self):
        data = {
            "mensagem": "Lorem ipsum dolor",
            "num_destinatario": ''
        }
        status_code, body = self.respostaAPI(data)
        self.assertEqual(status_code, 400)

    def test_status_num_destinatario_diferente11digitos(self):
        data = {
            "mensagem": "Lorem ipsum dolor",
            "num_destinatario": "12121291"
        }
        status_code, body = self.respostaAPI(data)
        self.assertEqual(status_code, 400)

    def test_mensagem_caracteres(self):
        data = {'mensagem': 'a'*101, "num_destinatario": 12345678908}
        status_code, body = self.respostaAPI(data)
        self.assertEqual(status_code, 400)

    def test_destinatario_ja_recebeu_mensagem(self):
        status_code, body = self.respostaAPI(self.data)
        self.assertEqual(status_code, 200)
        status_code, body = self.respostaAPI(self.data)
        self.assertEqual(status_code, 400)
