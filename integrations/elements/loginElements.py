from selenium.webdriver.common.by import By


class LoginElements:
    def __init__(self):
        self.formSenha = None
        self.formLogin = None
        self.visualizarPaginaInicio = None
        self.url = 'https://facebook.com'
        self.email = 'EMAIL'
        self.senha = 'SENHA'

    def viewHomePage(self, context):
        try:
            self.visualizarPaginaInicio = context.browser.find_element(By.XPATH,
                                                                       "//*[text()='Autenticação de dois fatores necessária']")
            return True
        except:
            return False

    def loadFormElements(self, context):
        # import ipdb
        # ipdb.sset_trace()
        self.formLogin = context.browser.find_element(By.ID, 'email')
        self.formSenha = context.browser.find_element(By.ID, 'pass')

    def forgotPass(self, context):
        self.esqueciSenha = context.browser.find_element(By.XPATH, "//*[text()='Esqueceu a senha?']")

    def signupUser(self, context):
        self.cadastrarUser = context.browser.find_element(By.XPATH, "//*[text()='Criar nova conta']")


class ForgotPassword:
    def __init__(self):
        pass

    def findTitle(self, context):
        try:
            self.telaEsqueciSenha = context.browser.find_element(By.XPATH,
                                                                 "//*[text()='Insira seu email ou número de celular para procurar a sua conta.']")
            return True
        except:
            return False


class SignupUser:
    def __init__(self):
        pass

    def visualizarTelaCadastro(self, context):
        try:
            self.visualizarTelaNovoUsuario = context.browser.find_element(By.XPATH,
                                                                          "//*[text()='Cadastre-se']")
            return True
        except:
            return False
