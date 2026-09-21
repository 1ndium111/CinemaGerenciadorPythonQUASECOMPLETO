import customtkinter as ctk  # Importação da biblioteca customtkinter para criar a interface gráfica moderna

# Definição de constantes globais para o layout do cinema (boa prática recomendada pelo Prof. Roger)
FILEIRAS = 10  # Número total de fileiras de assentos
COLUNAS = 20   # Número total de colunas de assentos por fileira

# Listas globais para armazenar os botões de assento de cada sala (permite rastrear o estado de cada cadeira)
assentos_sala1_lista = []
assentos_sala2_lista = []
assentos_sala3_lista = []

# Função para exibir a tela inicial e esconder todas as outras
def mostrar_tela_inicial():
    esconder_todas_as_telas()  # Oculta qualquer frame ativo no momento
    frame_inicial.pack(fill="both", expand=True)  # Exibe o frame da tela inicial ocupando toda a janela

# Função para exibir a Sala 1 e esconder as demais
def mostrar_sala1():
    esconder_todas_as_telas()
    frame_sala1.pack(fill="both", expand=True)

# Função para exibir a Sala 2 e esconder as demais
def mostrar_sala2():
    esconder_todas_as_telas()
    frame_sala2.pack(fill="both", expand=True)

# Função para exibir a Sala 3 e esconder as demais
def mostrar_sala3():
    esconder_todas_as_telas()
    frame_sala3.pack(fill="both", expand=True)

# Função utilitária para ocultar todos os frames de tela da aplicação antes de transições
def esconder_todas_as_telas():
    frame_inicial.pack_forget()
    frame_sala1.pack_forget()
    frame_sala2.pack_forget()
    frame_sala3.pack_forget()

# Função que alterna a cor do botão do assento entre verde (livre) e vermelho (selecionado)
def alternar_assento(btn):
    # Se o botão estiver desativado (já reservado), bloqueia novas alterações
    if btn.cget("state") == "disabled":
        return
    # Verifica a cor atual: se for verde, muda para vermelho; senão, volta para verde
    if btn.cget("fg_color") == '#2FA572':
        btn.configure(fg_color='#A52F2F', hover_color='#6B1E1E')  # Vermelho (assento selecionado)
    else:
        btn.configure(fg_color='#2FA572', hover_color='#1E6B4A')  # Verde (assento livre)

# Função que processa a reserva dos assentos de uma sala específica (torna vermelhos/selecionados em inutilizados)
def realizar_reserva(lista_assentos):
    # Percorre cada botão de assento da lista informada daquela sala
    for btn in lista_assentos:
        # Se o assento estiver marcado como selecionado (vermelho)
        if btn.cget("fg_color") == '#A52F2F':
            btn.configure(state="disabled")  # Torna o assento inutilizado/bloqueado
    # Após efetivar as reservas da sala, retorna para a tela inicial
    mostrar_tela_inicial()

# ==========================
# CONFIGURAÇÃO DA JANELA PRINCIPAL
# ==========================
app = ctk.CTk()  # Instancia a janela principal da aplicação com CustomTkinter
app.title("Gerenciador de Cinema")  # Define o título exibido na barra da janela
app.geometry("1060x750")  # Define as dimensões da janela (largura x altura em pixels)

# ==========================
# 1 - TELA INICIAL
# ==========================
frame_inicial = ctk.CTkFrame(app, fg_color="#ECDBCA")  # Frame container da tela inicial com cor de fundo personalizada

lbl_inicial = ctk.CTkLabel(
    frame_inicial,
    text="Cinema Sesi Referência",
    fg_color="#ECDBCA",
    text_color="#000000"
)  # Rótulo de título/boas-vindas na tela inicial
lbl_inicial.pack(pady=30)  # Posiciona o rótulo com espaçamento vertical de 30px

btn_ir_sala1 = ctk.CTkButton(frame_inicial, text="Ir para a Sala 1", command=mostrar_sala1)
btn_ir_sala1.pack(pady=10)  # Botão de navegação para a Sala 1

btn_ir_sala2 = ctk.CTkButton(frame_inicial, text="Ir pra sala 2", command=mostrar_sala2)
btn_ir_sala2.pack(pady=10)  # Botão de navegação para a Sala 2

btn_ir_sala3 = ctk.CTkButton(frame_inicial, text="Ir pra sala 3", command=mostrar_sala3)
btn_ir_sala3.pack(pady=10)  # Botão de navegação para a Sala 3

# ==========================
# 2 - TELA DA SALA 1
# ==========================
frame_sala1 = ctk.CTkFrame(app, fg_color="#ECDBCA")  # Frame container da Sala 1

lbl_sala1 = ctk.CTkLabel(
    frame_sala1,
    text="Sala 1 - Clube da Luta",
    font=("Comic Sans MS", 14),
    fg_color="#ECDBCA",
    text_color="#000000"
)
lbl_sala1.pack(pady=10)  # Título da Sala 1

btn_voltar_sala1 = ctk.CTkButton(frame_sala1, text="Voltar para o início", command=mostrar_tela_inicial)
btn_voltar_sala1.pack(pady=10)  # Botão de retorno ao início

tela1 = ctk.CTkLabel(
    frame_sala1,
    text="T E L O N A",
    fg_color="#333333",
)
tela1.pack(fill="x", padx=60, pady=10)  # Representação visual da tela de projeção

frame_assentos1 = ctk.CTkFrame(frame_sala1, fg_color="transparent")  # Container transparente para a grade de assentos
frame_assentos1.pack()

# Loop para criação da matriz de assentos da Sala 1
for x in range(FILEIRAS):  # Itera pelas fileiras (linhas)
    letra = chr(65 + x)    # Converte índice numérico em letra (65 = 'A', 66 = 'B', etc.)
    for y in range(1, COLUNAS + 1):  # Itera pelas colunas (assentos por fileira)
        codigo = f"{letra}{y}"       # Gera código do assento (ex: A1, B12)
        btn = ctk.CTkButton(
            frame_assentos1,
            text=codigo,
            width=45,
            height=40,
            fg_color='#2FA572',
            hover_color='#1E6B4A',
        )
        btn.configure(command=lambda b=btn: alternar_assento(b))  # Associa clique para alternar cor
        btn.grid(row=x, column=y - 1, padx=4, pady=4)            # Posiciona em grid
        assentos_sala1_lista.append(btn)                          # Armazena referência do botão na lista da Sala 1

btn_reservar1 = ctk.CTkButton(
    frame_sala1,
    text="Reservar Lugares",
    command=lambda: realizar_reserva(assentos_sala1_lista),
    fg_color='#A52F2F',
    hover_color='#6B1E1E'
)
btn_reservar1.pack(pady=10)  # Botão para efetivar a reserva da Sala 1 e bloquear assentos vermelhos

# ==========================
# 3 - TELA DA SALA 2
# ==========================
frame_sala2 = ctk.CTkFrame(app, fg_color="#ECDBCA")  # Frame container da Sala 2

lbl_sala2 = ctk.CTkLabel(
    frame_sala2,
    text="Sala 2 - Bee Movie",
    font=("Comic Sans MS", 14),
    fg_color="#ECDBCA",
    text_color="#000000"
)
lbl_sala2.pack(pady=10)  # Título da Sala 2

btn_voltar_sala2 = ctk.CTkButton(frame_sala2, text="Voltar para o início", command=mostrar_tela_inicial)
btn_voltar_sala2.pack(pady=10)  # Botão de retorno ao início

tela2 = ctk.CTkLabel(
    frame_sala2,
    text="T E L O N A",
    fg_color="#333333",
)
tela2.pack(fill="x", padx=60, pady=10)  # Representação visual da tela de projeção

frame_assentos2 = ctk.CTkFrame(frame_sala2, fg_color="transparent")  # Container transparente para grade de assentos
frame_assentos2.pack()

# Loop para criação da matriz de assentos da Sala 2
for x in range(FILEIRAS):
    letra = chr(65 + x)
    for y in range(1, COLUNAS + 1):
        codigo = f"{letra}{y}"
        btn = ctk.CTkButton(
            frame_assentos2,
            text=codigo,
            width=45,
            height=40,
            fg_color='#2FA572',
            hover_color='#1E6B4A',
        )
        btn.configure(command=lambda b=btn: alternar_assento(b))
        btn.grid(row=x, column=y - 1, padx=4, pady=4)
        assentos_sala2_lista.append(btn)

btn_reservar2 = ctk.CTkButton(
    frame_sala2,
    text="Reservar Lugares",
    command=lambda: realizar_reserva(assentos_sala2_lista),
    fg_color='#A52F2F',
    hover_color='#6B1E1E'
)
btn_reservar2.pack(pady=10)  # Botão para efetivar a reserva da Sala 2 e bloquear assentos vermelhos

# ==========================
# 4 - TELA DA SALA 3
# ==========================
frame_sala3 = ctk.CTkFrame(app, fg_color="#ECDBCA")  # Frame container da Sala 3

lbl_sala3 = ctk.CTkLabel(
    frame_sala3,
    text="Sala 3 - Roger, O Filme",
    font=("Comic Sans MS", 14),
    fg_color="#ECDBCA",
    text_color="#000000"
)
lbl_sala3.pack(pady=10)  # Título da Sala 3

btn_voltar_sala3 = ctk.CTkButton(frame_sala3, text="Voltar para o início", command=mostrar_tela_inicial)
btn_voltar_sala3.pack(pady=10)  # Botão de retorno ao início

tela3 = ctk.CTkLabel(
    frame_sala3,
    text="T E L O N A",
    fg_color="#333333",
)
tela3.pack(fill="x", padx=60, pady=10)  # Representação visual da tela de projeção

frame_assentos3 = ctk.CTkFrame(frame_sala3, fg_color="transparent")  # Container transparente para grade de assentos
frame_assentos3.pack()

# Loop para criação da matriz de assentos da Sala 3
for x in range(FILEIRAS):
    letra = chr(65 + x)
    for y in range(1, COLUNAS + 1):
        codigo = f"{letra}{y}"
        btn = ctk.CTkButton(
            frame_assentos3,
            text=codigo,
            width=45,
            height=40,
            fg_color='#2FA572',
            hover_color='#1E6B4A',
        )
        btn.configure(command=lambda b=btn: alternar_assento(b))
        btn.grid(row=x, column=y - 1, padx=4, pady=4)
        assentos_sala3_lista.append(btn)

btn_reservar3 = ctk.CTkButton(
    frame_sala3,
    text="Reservar Lugares",
    command=lambda: realizar_reserva(assentos_sala3_lista),
    fg_color='#A52F2F',
    hover_color='#6B1E1E'
)
btn_reservar3.pack(pady=10)  # Botão para efetivar a reserva da Sala 3 e bloquear assentos vermelhos

# ==========================
# INICIALIZAÇÃO DA APLICAÇÃO
# ==========================
mostrar_tela_inicial()  # Define e exibe a tela inicial padrão ao abrir o app
app.mainloop()          # Inicia o loop principal de eventos gráficos da interface
