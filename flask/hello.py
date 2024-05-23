from flask import Flask, Response
import random as r
from datetime import datetime as dt

voted_count = [0, 0] # きのこ、たけのこ
kinoko_ortakenoko = ["きのこ", "たけのこ"]
vote_history = []


app = Flask(__name__)

@app.route('/')
def main():
    response_text = f"投票サイトへようこそ"
    sugguest_text = f"もちろんあなたは{r.choice(kinoko_ortakenoko)}ですよね？"
    current_status = f"現在の投票数は  きのこ：{voted_count[0]}  たけのこ：{voted_count[1]}  です"
    return f""" 
    <h1>{response_text}</h1>
    <div>{sugguest_text}</div>
    <div>{current_status}</div>
    <a href="/kinoko">きのこ</a>
    <a href="/takenoko">たけのこ</a>
    """
@app.route('/kinoko')
def kinoko():
    global voted_count
    global vote_history
    vote_history.append(f"{dt.now()} きのこに投票されました")
    voted_count[0] += 1
    text = "きのこへの投票ありがとうございます"
    return f"""
    <h1>{text}</h1>
    <a href="/">トップページへ戻る</a>
    """

@app.route('/takenoko')
def takenoko():
    global voted_count
    global vote_history
    vote_history.append(f"{dt.now()} たけのこに投票されました")
    voted_count[1] += 1
    text = "たけのこへの投票ありがとうございます"
    return f"""
    <h1>{text}</h1>
    <a href="/">トップページへ戻る</a>
    """

@app.route('/greeting')
def greeting():
    time = dt.now().hour
    if 5 <= time < 12:
        return "Good morning!"
    elif 12 <= time < 17:
        return "Good afternoon!"
    else:
        return "Good evening!"
    
@app.route('/history')
def history(): 
    history = "\n".join(vote_history)
    return Response(history, mimetype='text/plain')




app.debug = True
app.run()