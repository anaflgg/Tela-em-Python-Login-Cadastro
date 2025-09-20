import FreeSimpleGUI as sg
import json
import os
import hashlib

def hash_senha(senha: str) -> str:
    return hashlib.sha256(senha.encode()).hexdigest()

def carregar_usuarios():
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as f:
            return json.load(f)
    return {}

def salvar_usuarios(usuarios):
    with open("usuarios.json", "w") as f:
        json.dump(usuarios, f, indent=4)

def tela_cadastro():
    layout = [
        [sg.Text("Novo Usuário"), sg.Input(key="novo_usuario")],
        [sg.Text("Nova Senha"), sg.Input(key="nova_senha", password_char="*")],
        [sg.Button("Cadastrar"), sg.Button("Cancelar")]
    ]
    janela = sg.Window("Cadastro", layout)

    while True:
        evento, valores = janela.read()
        if evento in (sg.WINDOW_CLOSED, "Cancelar"):
            break
        if evento == "Cadastrar":
            usuarios = carregar_usuarios()
            usuario = valores["novo_usuario"]
            senha = valores["nova_senha"]

            if usuario in usuarios:
                sg.popup_error("Usuário já existe!")
            elif usuario == "" or senha == "":
                sg.popup_error("Preencha todos os campos!")
            else:
                usuarios[usuario] = hash_senha(senha)
                salvar_usuarios(usuarios)
                sg.popup("Usuário cadastrado com sucesso!")
                janela.close()
                tela_login()
                return
            
    janela.close()

def tela_login():

        layout = [
            [sg.Text("Usuário"), sg.Input(key="usuario")],
            [sg.Text("Senha"), sg.Input(key="senha", password_char="*")],
            [sg.Button("Entrar"), sg.Button("Cancelar")]
        ]
        janela = sg.Window("Login", layout)

        while True:
            evento, valores = janela.read()
            if evento in (sg.WINDOW_CLOSED, "Cancelar"):
                break
            if evento == "Entrar":
                usuarios = carregar_usuarios()
                usuario = valores["usuario"]
                senha = valores["senha"]

                if usuario in usuarios and usuarios[usuario] == hash_senha(senha):
                    sg.popup(f"Bem-vindo(a), {usuario}!")
                    break
                else:
                    sg.popup_error("Usuário ou senha inválidos!")

        janela.close()

def main ():
    sg.theme("Reddit")

    escolha = sg.popup_yes_no("Você já tem conta?")

    if escolha == "Yes":
        tela_login()
    elif escolha == "No":
        tela_cadastro()

if __name__ == "__main__":
    main()

