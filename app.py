
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/bingo-game')
def bingo_game():
    # 📊 ለዳሽቦርዱ የሚያስፈልጉ መረጃዎች
    game_data = {
        "wallet": "0.00",
        "stake": "10.00"
    }
    # 🎯 ይህ መስመር ነው ቅድም የፈጠርነውን ውብ የላቬንደር bingo.html ፋይል በቀጥታ የሚጠራው
    return render_template('bingo.html', data=game_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
