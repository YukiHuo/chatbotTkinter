def recomendar_musica(estado_emocional):
    links = {
        "bom": "https://youtu.be/WevY3mT-o1w?si=d8wNxyVAV3Hgqvh8",
        "neutro": "https://youtu.be/OHx_qmo3YEA?si=f04FzPcaWS2os0W-",
        "ruim": "https://youtu.be/2-MbrxjIoaQ?si=pJsfRXiJD7H8iVfg",



    }

    return links.get(estado_emocional.lower(), "desculpe, ainda não tenho recomendações para esse sentimento.")


def iniciar_chat():
    print("🤖 Chatbot: Oi! como foi seu dia?")
    print("Você pode me contar usando uma dessas emoções: bom, neutro, ruim")


    while True:
        usuario = input("Você: ").lower()

        if usuario == "sair":
            print ("🤖 Chatbot: Até logo! cuide-se!")
            break
        if usuario in ["bom", "neutro", "ruim"]:
            link = recomendar_musica(usuario)
            print(f"🤖 Chatbot: Entendi que você está se sentindo {usuario}.")
            print(f"aqui está uma musica que pode ajudar: {link}")
            print("se quiser conversar mais ou fazer perguntas, estou aqui!")


        else:
            print("🤖 Chatbot: Não entendi muito bem... Você pode me dizer como está se sentindo ou perguntar algo simples sobre o brasil.")
            mostrar_perguntas_disponiveis()
            print("ou digite 'sair' para encerrar.")


iniciar_chat()