import torch
from dns import tokenizer
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from transformers import pipeline

# bot.send_message(message.chat.id, model('Матвей: ' + message.text, gpt))

chatbot = pipeline("text-generation", model="EleutherAI/gpt-neo-2.7B")


async def ML_request(text):
    response = chatbot(text, max_length=100)
    return response[0]["generated_text"].strip()
