# Importing chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot(
    'Buddy',
    storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
    database_uri = 'sqlite:///database.sqlite3',
    logic_adapters = [
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter']
    )
    
trainer = ListTrainer(bot)
#trainer.train([
#    'Hi',
#    'Hello',
#    'I need your assistance regarding my order',
#    'Please, Provide me with your order id',
#    'I have a complaint.',
#    'Please elaborate, your concern',
#    'How long it will take to receive an order ?',
#    'An order takes 3-5 Business days to get delivered.',
#    'Okay Thanks',
#    'No Problem! Have a Good Day!'
#    ])

trainer.train([
    'Oi',
    'Olá',
    'Bom dia',
    'Bom dia como você está?',
    'Eu estou bem obrigado',
    'Como eu posso ajudar?',
    'Bye',
    'Até mais!'])
    
name = input("Enter Your Name: ")
print("Welcome to the Bot Service! Let me know how can I help you?")
while True:
    request=input(name+':')
    if request=='Bye' or request =='bye':
        print('Bot: Bye')
        break
    else:
        response=bot.get_response(request)
        print('Bot:',response)
