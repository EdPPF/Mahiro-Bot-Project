import json
import random

def handle_response(message):
    about = "Mahiro Bot V 1.0\n- Código disponível em:\nhttps://github.com/EdPPF/Mahiro-Bot-Project.git"
    coms = ["`!abt`", "`!com`", "`!help`", "`!image`"]
    help = "Para uma lista de comandos, digíte `!com`. Para receber uma resposta minha no privado, inicie sua mensagem com `?`."

    # Reading chat.json:
    with open("chat.json", "r") as arquivo:
        json_chat = arquivo.read()

    # Object from chat.json
    chat = json.loads(json_chat)

    usr_msg = message.lower()

    # call
    call = chat[0]
    list_len = len(call["response"])
    random_call_item = random.randrange(list_len)
    random_call_resp = call["response"][random_call_item]
    if (usr_msg in call["user_input"]):
        return random_call_resp
    
    # about
    if (usr_msg == "!abt"):
        return about
    
    # commands
    if (usr_msg == "!com"):
        return coms
    
    # help
    if (usr_msg == "!help"):
        return help
    
    # image
    image = chat[1]
    image_list_len = len(image["response"])
    random_img_item = random.randrange(image_list_len)
    random_image = image["response"][random_img_item]
    if (usr_msg == "!image"):
        return f"{random_image}"

    return "UwUpsie\nhttps://github.com/EdPPF/Mahiro-Bot-Project/tree/Mahiron/imgs/oopsie.png"
