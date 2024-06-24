from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('register_login.html')

@app.route('/register', methods=['POST'])
def register():
    # Spracovanie registrácie
    return 'Registrácia úspešná!'

@app.route('/login', methods=['POST'])
def login():
    # Spracovanie prihlásenia
    return 'Prihlásenie úspešné!'

@app.route('/')
def index():
    return render_template('create_journey.html')

@app.route('/create_journey', methods=['POST'])
def create_journey():
    route = request.form['route']
    time = request.form['time']
    conditions = request.form['conditions']
    # Uložte tieto údaje do databázy alebo iného úložiska
    return 'Inzerát bol vytvorený!'

journeys = [
    {'route': 'Bratislava - Trnava', 'date': '2024-06-01', 'seats_available': 3},
    {'route': 'Bratislava - Nitra', 'date': '2024-06-15', 'seats_available': 2}
    # Pridajte ďalšie cesty sem
]

@app.route('/')
def index():
    return render_template('journeys.html', journeys=journeys)

@app.route('/search_journeys')
def search_journeys():
    search_query = request.args.get('search_query')
    filtered_journeys = [journey for journey in journeys if search_query.lower() in journey['route'].lower()]
    return render_template('journeys.html', journeys=filtered_journeys)

@app.route('/')
def index():
    return render_template('journeys.html', journeys=journeys)

@app.route('/register_for_journey', methods=['POST'])
def register_for_journey():
    username = request.form['username']
    password = request.form['password']
    journey_id = int(request.form['journey_id'])
    # Skontrolujte prihlásenie používateľa a pridajte ho na cestu s ID journey_id
    return f'Prihlásenie na cestu s ID {journey_id} úspešné!'



if __name__ == '__main__':
    app.run(debug=True)
