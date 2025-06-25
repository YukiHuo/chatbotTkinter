import tkinter as tk

def recomendar_musica(estado_emocional):
    links = {
        "bom": "https://youtu.be/WevY3mT-o1w?si=d8wNxyVAV3Hgqvh8",
        "neutro": "https://youtu.be/OHx_qmo3YEA?si=f04FzPcaWS2os0W-",
        "ruim": "https://youtu.be/2-MbrxjIoaQ?si=pJsfRXiJD7H8iVfg",



    }

    return links.get(estado_emocional.lower(), "desculpe, ainda não tenho recomendações para esse sentimento.")


def enviar_emocao():
    emocao = entrada_usuario.get().strip()
    if not emocao:
        return
    
    inserir_mensagenm("você", emocao)
    entrada_usuario delete(0, tk.END)

    emocao_lower = emocao.lower()

    if emocao_lower == "sair":
        inserir_mensagem("bot", "até logo! cuide-se!")
        root.after(2000, root.destroy)
        return

    if emocao_lower in ["bom", "neutro", "ruim"]:
        link = recomendar_musica(emocao_lower)
        resposta = f"entendi que você está se sentindo {emocao_lower}. /n Aqui vai uma musica que pode ajudar: {link}"
    else:
        resposta = (
            "não entendi muito bem... /n"
            "tente usar palavras como 'bom', 'neutro' ou 'ruim' /n"
            "ou digite 'sair' para encerrar."
        )

    inserir_mensagem("bot", resposta)

    
def inserir_mensagem(remetente, mensagem):
        chat_text.configure(state="normal")
        chat_text.insert(tk.END, f"{rementente}: {mensagem}/n/n")
        chat_text.configure(state="disabled")
        chat_text.see(tk.END)

root= tk.Tk()
root.title("chatbot emocional")


frame_principal = tk.frame(root, bg="#f0f0f0")
fmae_principal.pack(oadx=10 pady=10)


#Área de chat
chat_text = tk.Text(frame_principal, width=60, height=20, wraps="word", state="disabled", bg="white", fg="black")
chat_text.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

#entrada do usuario
entrada_usuario = 


# def iniciar_chat():
#     print("🤖 Chatbot: Oi! como foi seu dia?")
#     print("Você pode me contar usando uma dessas emoções: bom, neutro, ruim")


#     while True:
#         usuario = input("Você: ").lower()

#         if usuario == "sair":
#             print ("🤖 Chatbot: Até logo! cuide-se!")
#             break
#         if usuario in ["bom", "neutro", "ruim"]:
#             link = recomendar_musica(usuario)
#             print(f"🤖 Chatbot: Entendi que você está se sentindo {usuario}.")
#             print(f"aqui está uma musica que pode ajudar: {link}")
#             print("se quiser conversar mais ou fazer perguntas, estou aqui!")


#         else:
#             print("🤖 Chatbot: Não entendi muito bem... Você pode me dizer como está se sentindo ou perguntar algo simples sobre o brasil.")
#             mostrar_perguntas_disponiveis()
#             print("ou digite 'sair' para encerrar.")


# iniciar_chat()