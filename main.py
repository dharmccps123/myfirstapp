from fastapi import FastAPI
import threading

app = FastAPI()

bot_running = False

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/start")
def start_bot():
    global bot_running
    bot_running = True
    threading.Thread(target=run_bot).start()
    return {"message": "Bot Started"}

@app.post("/stop")
def stop_bot():
    global bot_running
    bot_running = False
    return {"message": "Bot Stopped"}

def run_bot():
    while bot_running:
        print("Running strategy...")
        # Add your Binance logic here