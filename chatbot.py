import openai
import os

key = os.environ.get("CHATGPT_KEY")
if key is None:
	print("Coloque a chave API do ChatGPT na variavel \"CHATGPT_KEY\".")
	exit()

openai.api_key = key

def send_message(msg, list_msg=[]):
	list_msg.append({"role":"user", "content": msg})
	rsp = openai.chat.completions.create(
		model = "gpt-3.5-turbo",
		messages = list_msg,
	)
	return rsp.choices[0].message.content

list_msg = []
while True:
	msg = input("Mensagem:")
	if msg == "":
		break
	else:
		rsp = send_message(msg, list_msg)
		list_msg.append({"role":"user","content":rsp})
		print("Chatbot: ",rsp)