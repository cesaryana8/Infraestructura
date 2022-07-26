from flask import Flask
app=Flask(__name__)

#Primera ruta
@app.route('/')
def index():
    return "PC5 - Yana Alanoca Cesar Florencio"