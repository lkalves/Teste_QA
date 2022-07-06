Feature: Tela de login Facebook

   Scenario: Fazer login no Facebook
        Given que estou na tela de login
        When quando insiro as credenciais e clico em login
        Then devo visualizar a tela de segundo fator de autenticação
    
   Scenario: Esqueci a senha
       Given que estou na tela de login
       When clico em esqueceu a senha
       Then devo visualizar a tela de esqueci a senha

   Scenario: Fazer novo cadastro
       Given que estou na tela de login
       When clico em fazer novo cadastro
       Then devo visualizar a tela de cadastro de usuario