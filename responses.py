import json
import random

# Reading chat.json:
with open("chat.json", "r") as arquivo:
    json_chat = arquivo.read()
# Object from chat.json
chat = json.loads(json_chat)

def handle_response(message):
    usr_msg = message.lower()

    call = chat[0]  # call
    list_len = len(call["response"])
    random_call_item = random.randrange(list_len)
    random_call_resp = call["response"][random_call_item]
    # if (usr_msg in call["user_input"]):  # This is already checked (sorta) on bot.on_message
    #     return random_call_resp
    return random_call_resp

def choose_image(): # Only for testing sending an image
    image = chat[1]  # image
    image_list_len = len(image["response"])
    random_img_item = random.randrange(image_list_len)
    random_image = image["response"][random_img_item]
    return f"{random_image}"
