import customtkinter as ctk    # Importação da biblioteca customtkinter para criar a interface gráfica

FILEIRAS = 10    # Criação das constantes das fileiras, de acordo com as sábias palavras do Prof. Roger: É uma boa prática.
COLUNAS = 20     

def mostrar_tela_inicial():
    esconder_todas_as_telas()    # Esconde todas as telas ativas
    frame_inicial.pack(fill="both", expand=True)    # Mostra o frame da tela inicial preenchendo a janela

def mostrar_sala1():
    esconder_todas_as_telas()    
    frame_sala1.pack(fill="both", expand=True)    # Mostra o frame da Sala 1 preenchendo a janela

def mostrar_sala2():
    esconder_todas_as_telas()    
    frame_sala2.pack(fill="both", expand=True)    # Mostra o frame da Sala 2 preenchendo a janela

def mostrar_sala3():
    esconder_todas_as_telas()    
    frame_sala3.pack(fill="both", expand=True)    # Mostra o frame da Sala 3 preenchendo a janela

def esconder_todas_as_telas():
    frame_inicial.pack_forget()    # Remove os frames da tela
    frame_sala1.pack_forget() 
    frame_sala2.pack_forget()
    frame_sala3.pack_forget()

def botao_pra_adicionar_algo():
    if (algo_novo.winfo_ismapped() == False):    # Verifica se o texto não está visível na tela
        algo_novo.pack(pady=10)    # Se não estiver, exibe ele na tela
    if (algo_novo.winfo_ismapped() == True):    # Verifica se o texto já está visível
            algo_novo.pack_forget()    # Se estiver, esconde ele da tela

# Função que alterna a cor do botão do assento entre verde e vermelho ao ser clicado
def alternar_assento(btn):
    # Verifica a cor atual do botão para decidir se muda para vermelho ou verde
    if btn.cget("fg_color") == '#2FA572':
        btn.configure(fg_color='#A52F2F', hover_color='#6B1E1E')  # Vermelho (assento ocupado/selecionado)
    else:
        btn.configure(fg_color='#2FA572', hover_color='#1E6B4A')  # Verde (assento livre)

app = ctk.CTk()    # Criação da janela principal com o CTk
app.title("Gerenciador de Cinema")    # Definição do título da janela
app.geometry("1060x750")    # Definição das dimensões da janela (aumentada levemente para caber o novo botão)

# 1 - Tela Inicial
frame_inicial = ctk.CTkFrame(app, fg_color="#ECDBCA")    # Cria o frame da tela inicial com cor de fundo personalizada

lbl_inicial = ctk.CTkLabel(frame_inicial, text="Cinema H. Romeu Pinto Pintóvsky", font=("Comic Sans MS", 14), fg_color="#ECDBCA", text_color="#000000")    # Cria o texto de boas-vindas da tela inicial
lbl_inicial.pack(pady=30)    # Insere o rótulo de texto na tela com espaçamento vertical

btn_ir_sala1 = ctk.CTkButton(frame_inicial, text="Ir para a Sala 1", command=mostrar_sala1)    # Botão para navegar até a Sala 1
btn_ir_sala1.pack(pady=10)    # Insere o botão na tela com espaçamento

btn_ir_sala2 = ctk.CTkButton(frame_inicial, text="Ir pra sala 2", command=mostrar_sala2)    # Botão para navegar até a Sala 2
btn_ir_sala2.pack(pady=10)    # Insere o botão na tela com espaçamento

btn_ir_sala3 = ctk.CTkButton(frame_inicial, text="Ir pra sala 3", command=mostrar_sala3)    # Botão para navegar até a Sala 3
btn_ir_sala3.pack(pady=10)    # Insere o botão na tela com espaçamento

btn_adicionar = ctk.CTkButton(frame_inicial, text="Mostrar algo novo", command=botao_pra_adicionar_algo)    # Botão que alterna a exibição do texto secreto
btn_adicionar.pack(pady=10)    # Insere o botão na tela com espaçamento

algo_novo = ctk.CTkLabel(frame_inicial, text="pinto kkkkk", font=("Comic Sans MS", 14), fg_color="#ECDBCA", text_color="#000000")    # Label que aparece ao clicar no botão anterior

# 2 - Tela da Sala 1
frame_sala1 = ctk.CTkFrame(app, fg_color="#ECDBCA")    # Cria o frame principal da Sala 1

lbl_sala1 = ctk.CTkLabel(frame_sala1, text="Sala 1 - Clube da Luta", font=("Comic Sans MS", 14), fg_color="#ECDBCA", text_color="#000000")    # Rótulo indicando o nome da sala
lbl_sala1.pack(pady=10)    # Insere o rótulo na tela

btn_voltar_sala1 = ctk.CTkButton(frame_sala1, text="Voltar para o início", command=mostrar_tela_inicial)    # Botão para retornar à tela inicial
btn_voltar_sala1.pack(pady=10)    # Insere o botão de voltar na tela

tela1 = ctk.CTkLabel(    # Quadrado que irá mostrar onde é a telona do cinema na Sala 1
    frame_sala1,
    text="T E L O N A",
    fg_color="#333333",
)
tela1.pack(fill="x", padx=60, pady=10)    # O FILL manda alargar o espaço todo pelo eixo X

frame_assentos1 = ctk.CTkFrame(frame_sala1, fg_color="transparent")    # Cria um FRAME com fundo transparente para conter os assentos da Sala 1
frame_assentos1.pack()    # Insere o frame de assentos na tela

for x in range(FILEIRAS):    # Loop para percorrer cada fileira da Sala 1
    letra = chr(65 + x)    # Converte o número em letra usando a tabela ASCII (65 = 'A', 66 = 'B', etc.)
    for y in range(1, COLUNAS + 1):    # Loop para percorrer cada coluna (assento) da fileira
        codigo = f"{letra}{y}"    # Monta o código alfanumérico do assento (ex: A1, B12)
        btn = ctk.CTkButton(    # Cria um botão para cada assento
            frame_assentos1,
            text=codigo,
            width=45,
            height=40,
            fg_color='#2FA572',    # Cor verde padrão do botão
            hover_color='#1E6B4A',    # Cor de quando passa o mouse por cima
        )
        btn.configure(command=lambda b=btn: alternar_assento(b))
        btn.grid(row=x, column=y - 1, padx=4, pady=4)

btn_reservar1 = ctk.CTkButton(frame_sala1, text="Reservar Lugares", command=mostrar_tela_inicial, fg_color='#A52F2F', hover_color='#6B1E1E')    # Botão para confirmar a reserva e voltar ao início
btn_reservar1.pack(pady=10)    # Insere o botão de reserva no final do frame da Sala 1

# 3 - Tela da Sala 2
frame_sala2 = ctk.CTkFrame(app, fg_color="#ECDBCA")    # Cria o frame principal da Sala 2

lbl_sala2 = ctk.CTkLabel(frame_sala2, text="Sala 2 - Bee Movie", font=("Comic Sans MS", 14), fg_color="#ECDBCA", text_color="#000000")    # Rótulo indicando o nome da sala
lbl_sala2.pack(pady=10)    # Insere o rótulo na tela

btn_voltar_sala2 = ctk.CTkButton(frame_sala2, text="Voltar para o início", command=mostrar_tela_inicial)    # Botão para retornar à tela inicial
btn_voltar_sala2.pack(pady=10)    # Insere o botão de voltar na tela

tela2 = ctk.CTkLabel(    # Quadrado que irá mostrar onde é a telona do cinema na Sala 2
    frame_sala2,
    text="T E L O N A",
    fg_color="#333333",
)
tela2.pack(fill="x", padx=60, pady=10)    # O FILL manda alargar o espaço todo pelo eixo X

frame_assentos2 = ctk.CTkFrame(frame_sala2, fg_color="transparent")    # Cria um FRAME com fundo transparente para conter os assentos da Sala 2
frame_assentos2.pack()    # Insere o frame de assentos na tela

for x in range(FILEIRAS):    # Loop para percorrer cada fileira da Sala 2
    letra = chr(65 + x)    # Converte o número em letra (A, B, C...)
    for y in range(1, COLUNAS + 1):    # Loop para percorrer cada coluna da fileira
        codigo = f"{letra}{y}"    # Monta o código do assento
        btn = ctk.CTkButton(    # Cria um botão para cada assento da Sala 2
            frame_assentos2,
            text=codigo,
            width=45,
            height=40,
            fg_color='#2FA572',
            hover_color='#1E6B4A',
        )
        btn.configure(command=lambda b=btn: alternar_assento(b))
        btn.grid(row=x, column=y - 1, padx=4, pady=4)

btn_reservar2 = ctk.CTkButton(frame_sala2, text="Reservar Lugares", command=mostrar_tela_inicial, fg_color='#A52F2F', hover_color='#6B1E1E')    # Botão para confirmar a reserva e voltar ao início
btn_reservar2.pack(pady=10)    # Insere o botão de reserva no final do frame da Sala 2

# 4 - Tela da Sala 3
frame_sala3 = ctk.CTkFrame(app, fg_color="#ECDBCA")    # Cria o frame principal da Sala 3

lbl_sala3 = ctk.CTkLabel(frame_sala3, text="Sala 3 - Roger, O Filme", font=("Comic Sans MS", 14), fg_color="#ECDBCA", text_color="#000000")    # Rótulo indicando o nome da sala
lbl_sala3.pack(pady=10)    # Insere o rótulo na tela

btn_voltar_sala3 = ctk.CTkButton(frame_sala3, text="Voltar para o início", command=mostrar_tela_inicial)    # Botão para retornar à tela inicial
btn_voltar_sala3.pack(pady=10)    # Insere o botão de voltar na tela

tela3 = ctk.CTkLabel(    # Quadrado que irá mostrar onde é a telona do cinema na Sala 3
    frame_sala3,
    text="T E L O N A",
    fg_color="#333333",
)
tela3.pack(fill="x", padx=60, pady=10)    # O FILL manda alargar o espaço todo pelo eixo X

frame_assentos3 = ctk.CTkFrame(frame_sala3, fg_color="transparent")    # Cria um FRAME com fundo transparente para conter os assentos da Sala 3
frame_assentos3.pack()    # Insere o frame de assentos na tela

for x in range(FILEIRAS):    # Loop para percorrer cada fileira da Sala 3
    letra = chr(65 + x)    # Converte o número em letra (A, B, C...)
    for y in range(1, COLUNAS + 1):    # Loop para percorrer cada coluna da fileira
        codigo = f"{letra}{y}"    # Monta o código do assento
        btn = ctk.CTkButton(    # Cria um botão para cada assento da Sala 3
            frame_assentos3,
            text=codigo,
            width=45,
            height=40,
            fg_color='#2FA572',
            hover_color='#1E6B4A',
        )
        btn.configure(command=lambda b=btn: alternar_assento(b))
        btn.grid(row=x, column=y - 1, padx=4, pady=4)

btn_reservar3 = ctk.CTkButton(frame_sala3, text="Reservar Lugares", command=mostrar_tela_inicial, fg_color='#A52F2F', hover_color='#6B1E1E')    # Botão para confirmar a reserva e voltar ao início
btn_reservar3.pack(pady=10)    # Insere o botão de reserva no final do frame da Sala 3

mostrar_tela_inicial()    # Define qual tela abre primeiro ao iniciar o programa
app.mainloop()    # Inicia o loop principal da interface gráfica para manter a janela aberta