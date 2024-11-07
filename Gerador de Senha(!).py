import random
import string
import PySimpleGUI as sg
import os


class PassGen:
    def __init__(self):
        # LAYOUT
        sg.theme('Black')
        layout = [
            [sg.Text('Site/App', size=(10, 1)),
             sg.Input(key='site', size=(20, 1))],
            [sg.Text('Login/Usuário:', size=(10, 1)),
            sg.Input(key='usuario', size=(20, 1))],
            [sg.Output(size=(35, 7))],
            [sg.Button('Gerar Senha')]

        ]
        # TITULO JANELA
        self.janela = sg.Window('Gerador de Senhas', layout)
        pass

        #CÓDIGO FUNCIONANDO
    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break #O código para de rodar assim que a janela for fechada
            if evento == 'Gerar Senha': #O que vai acontecer quando clicar no botão para gerar senha
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
                self.salvar_senha(nova_senha, valores)

    def gerar_senha(self, valores): #Caracteres que serão utilizados para criar a senha:
        char_list = string.ascii_letters + string.digits + '!@#$%&'
        chars = random.choices(char_list, k=15)
        new_pass = ''.join(chars)
        return new_pass



    def salvar_senha(self, nova_senha, valores): #Salvando arquivo txt com infos de qual site/usuario/senha
        with open('senhas.txt', 'a', newline='') as arquivo:
            arquivo.writelines(
                f"Site: {valores['site']} \nUsuario: {valores['usuario']} \nNova Senha: {nova_senha}\n\n")


        print ('Arquivo salvo!')

gen = PassGen()
gen.Iniciar()
