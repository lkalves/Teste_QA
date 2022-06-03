# Teste_QA
 Repositorio de automatização

### Para os teste será necessário ter o chromedriver já instalado nas variaveis de ambiente. 
### Caso contrario será necessário apontar no arquivo `environment.py` dentro da função 
### `browser_chrome`
### [```context.browser = Chrome("D:/chromedriver/chromedriver.exe")```](https://github.com/lkalves/Teste_QA/blob/main/integrations/features/environment.py#L7)
### O download deve ser baixado no site abaixo:
### https://chromedriver.chromium.org/downloads

## Para instalar os pacotes necessários deverão ser feito a instalação do arquivo `pip install -r requirements.txt`

## Para rodar o teste automatizado do Facebook, é preciso que coloque e-mail, usuário ou numero de telefone no campo
## [`self.email`](https://github.com/lkalves/Teste_QA/blob/main/integrations/elements/loginElements.py#L7) do arquivo [*loginElements.py*](https://github.com/lkalves/Teste_QA/blob/main/integrations/elements/loginElements.py) e o campo senha deve ser alterado em [`self.senha`](https://github.com/lkalves/Teste_QA/blob/main/integrations/elements/loginElements.py#L8) do mesmo arquivo.

# Rodando os testes:
## Testes de login *Facebook*
### comandos:
- `cd integrations`
- `python -m behave`

## Testes de *API*
### comandos:
- `cd unittest_API`
- `python -m unittest`