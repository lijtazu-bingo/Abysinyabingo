from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

TOKEN = '8019235278:AAHrfTzLDJxLIgKddEbLYNC-zDqBb66mDZY'
TELEGRAM_API = f'https://api.telegram.org/bot{TOKEN}'

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="am">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Abysinyabingo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #121212;
            color: #ffffff;
            text-align: center;
            padding: 20px;
        }
        h1 { color: #00ffcc; }
        .timer-box {
            font-size: 22px;
            color: #ffaa00;
            background: #1e1e1e;
            padding: 15px;
            border-radius: 10px;
            margin: 20px auto;
            max-width: 300px;
            border: 1.5px solid #00ffcc;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(10, 1fr);
            gap: 5px;
            max-width: 500px;
            margin: 20px auto;
        }
        .num-cell {
            background: #2a2a2a;
            padding: 8px 4px;
            border-radius: 5px;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <h1>Abysinyabingo Mini-App</h1>
    <div class="timer-box" id="timer">ቀጣይ ዙር የሚጀምረው በ: 30 ሰከንድ</div>
    <h3>የቢንጎ ቁጥሮች (1 - 400)</h3>
    <div class="grid">
        {% for i in range(1, 401) %}
            <div class="num-cell">{{ i }}</div>
        {% endfor %}
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if data and 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')

        web_app_url = 'https://abysinyabingo.onrender.com'  # የ Render ሊንክዎ ሲመጣ እዚህ ይስተካከላል

        if text == '/start':
            payload = {
                'chat_id': chat_id,
                'text': 'እንኳን ደህና መጡ ወደ Abysinyabingo! ጨዋታውን ለመጀመር ከታች ያለውን ቁልፍ ይጫኑ:',
                'reply_markup': {
                    'inline_keyboard': [[
                        {
                            'text': '🚀 ቢንጎ ተጫወት',
                            'web_app': {'url': web_app_url}
                        }
                    ]]
                }
            }
            requests.post(f'{TELEGRAM_API}/sendMessage', json=payload)
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
