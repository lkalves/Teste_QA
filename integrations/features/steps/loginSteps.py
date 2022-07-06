from selenium.webdriver.common.keys import Keys
from behave import *

from integrations.elements.loginElements import LoginElements, ForgotPassword, SignupUser

loginElements = LoginElements()
forgotPassword = ForgotPassword()
signupUser = SignupUser()


# Login Facebook
@given('que estou na tela de login')
def telaLogin(context):
    context.browser.get(loginElements.url)


@when('quando insiro as credenciais e clico em login')
def inserirCredencial(context):
    loginElements.loadFormElements(context)
    loginElements.formLogin.send_keys(loginElements.email)
    loginElements.formSenha.send_keys(loginElements.senha)
    loginElements.formSenha.send_keys(Keys.RETURN)


@then('devo visualizar a tela de segundo fator de autenticação')
def visualizaTelaInicial(context):
    assert loginElements.viewHomePage(context)


@when('clico em esqueceu a senha')
def clicarEsqueceuSenha(context):
    loginElements.forgotPass(context)
    loginElements.esqueciSenha.click()


@then('devo visualizar a tela de esqueci a senha')
def visualizaTelaEsqueciSenha(context):
    assert forgotPassword.findTitle(context)


# Botão cadastrar novo usuario
@When('clico em fazer novo cadastro')
def clicarCadastroUsuario(context):
    loginElements.signupUser(context)
    loginElements.cadastrarUser.click()

@Then('devo visualizar a tela de cadastro de usuario')
def visualizarCadastroUsuario(context):
    assert signupUser.visualizarTelaCadastro(context)