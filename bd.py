#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3


class ConnectBD(object):


    # inicializando o Banco de dados
    def __init__(self, bd_name):
        try:
            # definindo atributo conexao
            self.conexao = sqlite3.connect(bd_name)

            # definindo atributo direcionador
            self.direcionador = self.conexao.cursor()

        except sqlite3.Error:
            # mensagem de erro caso não abra o BD
            print("Erro na conexao do banco de dados!")
            return False

    # Fechando a conexão com Banco de dados

    def fechar_banco(self):
        self.conexao.close()

    # criando schema

    def cria_schema(self):
        try:

            #tabela sensor luminosidadeINTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
            sql = '''CREATE TABLE IF NOT EXISTS luminosity(idluminosity INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                luminosidade REAL, coleta_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP );'''
            self.gravar_dados(sql)

	           # tabela sensor movimentos e distancia
            sql = '''CREATE TABLE IF NOT EXISTS motion(idmotion INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    pir BOOLEAN, ultrasonic REAL, coleta_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL);'''
            self.gravar_dados(sql)

            # tabela sensor luminosidade
            sql = '''CREATE TABLE IF NOT EXISTS noise(idnoise INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    ruido REAL, coleta_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL);'''
            self.gravar_dados(sql)


        except sqlite3.Error:
            print "Erro na conexao com BD"


    def gravar_dados(self, sql):
        #if (self.conexao):
        self.direcionador.execute(sql)
        self.conexao.commit()