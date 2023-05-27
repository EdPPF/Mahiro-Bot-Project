import discord

def handle_response(message):
    about = "Mahiro Bot V 1.0\n- Código disponível em:\nhttps://github.com/EdPPF/Mahiro-Bot-Project.git"
    coms = ["`!que`", "`!com`", "`!help`", "`!image`"]
    help = "Para uma lista de comandos, digíte `!com`. Para receber uma resposta minha no privado, inicie sua mensagem com `?`."

    usr_msg = message.lower()

    if (usr_msg == "mahiro!"):
        return "Aqui!"
    
    if (usr_msg == "!que"):
        return about
    
    if (usr_msg == "!com"):
        return coms
    
    if (usr_msg == "!help"):
        return help
    
    if (usr_msg == "!image"):
        image_url = "https://github.com/EdPPF/Mahiro-Bot-Project/tree/master/imgs/idkwtf.jpg"
        return f"UwUpsie\n {image_url}"

    return "https://github.com/EdPPF/Mahiro-Bot-Project/tree/master/imgs/oopsie.png"
