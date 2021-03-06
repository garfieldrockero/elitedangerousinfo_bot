#encoding=utf8
from config import *

@bot.message_handler(func=lambda m: m.content_type == 'text' and m.text in ['Ayuda'])
@bot.message_handler(commands=['help'])
def help(m):
    cid = m.chat.id
    uid = m.from_user.id
    with open("extras/version.txt", 'r') as f:
        version = f.read()
    if cid in admin:
        txt = responses['help']['admin']
        for a, b in responses['commands']['admin'].items():
            txt += '\n/' + a + ': ' + b
    else:
        txt = responses['help']['user']
        for a, b in responses['commands']['user'].items():
            txt += '\n/' + a + ': ' + b
    txt += "\n\n*VERSION* " + version
    bot.send_chat_action(cid,'typing')
    bot.send_message(cid,txt, parse_mode="Markdown")
    bot.send_message(administrador, "[AVISO - INFO] Ayuda usado por " + str(m.from_user.first_name))
