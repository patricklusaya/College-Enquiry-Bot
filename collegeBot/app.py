from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

english_bot = ChatBot(
    "Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter",
        logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, I did not catch that. Would you mind clarifying?',
            
        }
    ],
    
    
    )
    
trainer = ChatterBotCorpusTrainer(english_bot)
  
english_bot.storage.drop()
# trainer.train("chatterbot.corpus.english.greetings")
trainer.train("chatterbot.corpus.custom")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


if __name__ == "__main__":
    app.run()
