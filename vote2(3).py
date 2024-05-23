from flask import Flask
import requests
import json

def post_slack(message):
  url = 'https://hooks.slack.com/services/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'
  data = {"text": message}
  requests.post(url, data={'payload':json.dumps(data)})

app = Flask(__name__)

kinoko_count = 0    # キノコのアクセス回数
takenoko_count = 0  # タケノコのアクセス回数

@app.route('/')
def index():
  if kinoko_count > takenoko_count:
    msg = '{} vs {}できのこの勝ち！'.format(kinoko_count, takenoko_count)
  elif kinoko_count < takenoko_count:
    msg = '{} vs {}でタケノコの勝ち！'.format(takenoko_count, kinoko_count)
  else:
    msg = '引き分け！どちらも頑張って！'
  return '''
  <h1>現在の状況</h1>
  <p>{}</p>
  <ul>
    <li>きのこ: {}</li>
    <li>たけのこ: {}</li>
  </ul>
  <h2>あなたはどちら派？</h2>
  <ul>
    <li><a href="/kinoko">きのこ</a></li>
    <li><a href="/takenoko">たけのこ</a></li>
  </ul>
  '''.format(msg, '&#x1f344;' * kinoko_count, '&#x1f38d;' * takenoko_count)

@app.route('/takenoko')
def takenoko():
  global takenoko_count
  takenoko_count += 1
  msg = 'タケノコへの投票ありがとうございました'
  post_slack(msg)
  return '''
  <p>{}</p>
  <p><a href="/">戻る</a></p>
  '''.format(msg)

@app.route('/kinoko')
def kinoko():
  global kinoko_count
  kinoko_count += 1
  msg = 'きのこへの投票ありがとうございました'
  post_slack(msg)
  return '''
  <p>{}</p>
  <p><a href="/">戻る</a></p>
  '''.format(msg)

app.debug = True
app.run()
