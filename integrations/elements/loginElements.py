from selenium.webdriver.common.by import By


class LoginElements:
    def __init__(self):
        self.url = 'https://facebook.com'
        self.email = 'INSERIR EMAIL, USUARIO OU NUMERO DE TELEFONE'
        self.senha = 'INSERIR SENHA'

    def viewHomePage(self,context):
        try:
            self.visualizarPaginaInicio = context.browser.find_element_by_xpath("//*[text()='Autenticação de dois fatores necessária']")
            return True
        except:
            return False

    def loadFormElements(self,context):
        self.formLogin = context.browser.find_element_by_id('email')
        self.formSenha = context.browser.find_element_by_id('pass')

    def forgotPass(self, context):
        self.esqueciSenha = context.browser.find_element_by_xpath("//*[text()='Esqueceu a senha?']")

    def signupUser(self, context):
        self.cadastrarUser = context.browser.find_element_by_xpath("//*[text()='Criar nova conta']")

class ForgotPassword:
    def __init__(self):
        pass
    def findTitle(self,context):
        try:
            self.telaEsqueciSenha = context.browser.find_element_by_xpath(
            "//*[text()='Insira seu email ou número de celular para procurar a sua conta.']")
            return True
        except:
            return False

class SignupUser:
    def __init__(self):
        pass
    def visualizarTelaCadastro(self,context):
        try:
            self.visualizarTelaNovoUsuario = context.browser.find_element_by_xpath(
                "//*[text()='Cadastre-se']")
            return True
        except:
            return False