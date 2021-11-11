# Apliquei o teste automatizado nos casos de testes em que eu tinha base de conhecimento para automatizar.

# Escrevi o meu teste automatizado utilizando a linguagem Python e biblioteca Selenium para Python.
    Utilizei o Selenium por ser um framework compátivel com a grande maioria dos browser disponíveis atualmente no mercado. Além disso permite uma perfeita integração com a linguagem Python, permitindo assim que sejam criados casos de testes mais complexos, resolvendo-se através da programação orientada a objeto.


## Configurações necessárias

    1) É necessário possuir os seguintes programos instalados na máquina:
        - Visual Studio Code
        - Python na versão 3.9.5  ou superior

    2) Após precisaremos instalar as seguintes ferramentas para o Python:

        - Selenium
        - Virtual Env
        - Behave

# Selenium: 
    Para instalar o Selenium, deve-se rodar o comando 'python pip install selenium' através do CMD ou PowerShell. Caso haja dúvidas pode consultar o seguinte site: https://    selenium-python.readthedocs.io/installation.html

# Virtual Env: 
    Para instalar a Virtual Env, deve-se rodar o comando 'python pip install virtualenv' através do CMD ou PowerShell. Após criar um ambiente virtual com o comando 'venv   nomedavirtualenv'. Por fim ativar o ambiente virtual com o comando 'nomedavirtualenv\Scripts\activate.bat'. Caso haja dúvidas pode consultar o seguinte site: https://docs.python.org/    pt-br/3/tutorial/venv.html
    
# Behave: 
    Para instalar o behave usar o comando 'python pip install behave' através do CMD ou PowerShell.

# Observação
    Todas as três tarefas acimas devem ser executadas utilizando o interpretador Python. 
    
    Caso o Python não esteja ná váriavel path do Windows, pode-se navegar até o caminho onde esta alocado o arquivo pip.exec e executar os comandos. Exemplo pelo CMD:  'D:\Programas\Python\Scripts pip install selenium'.
    Caso haja dúvidas pode consultar o seguinte site: https://www.mundodoshackers.com.br/como-executar-um-codigo-python-pelo-prompt-de-comando#:~:text=Para%20chamar%20o%20Python%20ou, caminho%20para%20o%20c%C3%B3digo.py.

    Para rodar o cenário de testes, acessar o seguinte arquivo no Visual Studio: features/ steps/ testeAutomatizado.py. Nele digitar o comando 'behave' pelo terminal. Sera executado os cenários de teste descritos no arquivo [teste.feature](\features).