

import random

import flet as ft
from flet import ElevatedButton, Container


def main(pagina: ft.Page):
    pagina.fonts = {'gv': '/fonts/Jacquard12-Regular.ttf'}
    pagina.title = 'Romeuzaap'
    

    chat = ft.Column()
    # 10 as mensagens que já foram enviadas (chat)

    def api(mensagem):
        if mensagem == f'{nome_usuario.value} entrou no chat':
            texto_chat = ft.Text(mensagem, color=cor_entrada.value)
        else:
            texto_chat = ft.Text(mensagem)

        chat.controls.append(texto_chat)
        pagina.update()

    pagina.pubsub.subscribe(api)

    def enviar_msn(evento):
        tx_msn = texto_msn.value
        nome_msn = nome_usuario.value
        mensagem = f'{nome_msn}: {tx_msn}'
        pagina.pubsub.send_all(mensagem)
        texto_msn.value = ''
        pagina.update()

    # 12 botão de enviar
    enviar = ft.ElevatedButton('enviar', on_click=enviar_msn)
    # 11 campo digite sua mensagem
    texto_msn = ft.TextField(label='Digite uma mensagem', on_submit=enviar_msn)

    # 7 sumir com o titulo romeuzaap
    # 8 fechar a janela(popup)
    # 9 carregar chat
    linha = ft.Row([texto_msn, enviar])

    def bt_janela(evento):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar_chat)
        janela.open = False
        pagina.add(chat)
        mensagem = f'{nome_usuario.value} entrou no chat'
        pagina.pubsub.send_all(mensagem)
        pagina.add(linha)
        pagina.update()

    cor_entrada = ft.Dropdown(
        width=100,
        label='cor texto',
        options=[

            ft.dropdown.Option("Blue"),
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),

        ]
    )
    # 4 titulo: bem vindo ao romeuzaap
    titulo_janela = ft.Text('Bem vindo ao Romeuzaap')
   # 6 botão: entrar no chat
    botao_chat = ElevatedButton('Entrar no chat', on_click=bt_janela)
    # 5 campo de texto -> escreva seu nome no chat
    nome_usuario = ft.TextField(label='escreva seu nome', on_submit=bt_janela)
    # 3 popup (janela na frente da tela)
    janela = ft.AlertDialog(
        title=titulo_janela,
        content=nome_usuario,
        actions=[ 
            botao_chat,
            cor_entrada
        ]
    )

    def entrar_chat(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()

    titulo = ft.Container(
        ft.Text(
            'Romeuzaap',
            size=80,
            weight=ft.FontWeight.BOLD,
            style=ft.TextStyle(
                foreground=ft.Paint(
                    gradient=ft.PaintLinearGradient(
                        begin=ft.Offset(x=0, y=0),
                        end=ft.Offset(x=500, y=0),
                        colors=[
                            ft.colors.CYAN,
                            ft.colors.PINK
                        ]
                    )
                )
            )
        ),
        padding=30,
        shadow=ft.BoxShadow(blur_radius=300, color=ft.colors.GREY),
        margin=ft.margin.all(30)
    )
    
    botao_iniciar_chat = ElevatedButton('iniciar chat', on_click=entrar_chat)
    # 1 titulo: romeuzaap
    pagina.add(titulo)
    # 2 botão de iniciar chat
    pagina.add(botao_iniciar_chat)


ft.app(target=main, assets_dir="Desktop")
