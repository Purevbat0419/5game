from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'kids_games_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess_number', methods=['GET', 'POST'])
def guess_number():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
    message = None
    if request.method == 'POST':
        guess = int(request.form['guess'])
        if guess == session['number']:
            message = "Зөв! Та яллаа! Шинэ тоо сонгогдлоо."
            session['number'] = random.randint(1, 100)
        elif guess < session['number']:
            message = "Их тоо оруулна уу"
        else:
            message = "Бага тоо оруулна уу"
    return render_template('guess_number.html', message=message)

@app.route('/rock_paper_scissors', methods=['GET', 'POST'])
def rock_paper_scissors():
    message = None
    user_choice = None
    computer_choice = None
    if request.method == 'POST':
        user_choice = request.form['choice']
        computer_choice = random.choice(['Хайч', 'Чулуу', 'Даавуу'])
        if user_choice == computer_choice:
            message = "Тэнцлээ!"
        elif (user_choice == 'Хайч' and computer_choice == 'Даавуу') or \
             (user_choice == 'Чулуу' and computer_choice == 'Хайч') or \
             (user_choice == 'Даавуу' and computer_choice == 'Чулуу'):
            message = "Та яллаа!"
        else:
            message = "Компьютер яллаа!"
    return render_template('rock_paper_scissors.html', message=message, user_choice=user_choice, computer_choice=computer_choice)

@app.route('/picture_guess', methods=['GET', 'POST'])
def picture_guess():
    animals = {
        'Заан': 'Том чихтэй, сүүлтэй, том биетэй амьтан',
        'Арслан': 'Шаргал үстэй, сүүлтэй, хүчирхэг амьтан',
        'Зөгий': 'Далавчтай, зүүтэй, бал өгдөг амьтан',
        'Нохой': 'Үстэй, сүүлтэй, гэрийн амьтан',
        'Муур': 'Үстэй, сүүлтэй, гэрийн амьтан'
    }
    if 'animal' not in session:
        session['animal'] = random.choice(list(animals.keys()))
    message = None
    if request.method == 'POST':
        guess = request.form['guess'].strip().lower()
        if guess == session['animal'].lower():
            message = f"Зөв! Энэ бол {session['animal']} байсан."
            session['animal'] = random.choice(list(animals.keys()))
        else:
            message = "Буруу, дахин оролдоно уу"
    description = animals[session['animal']]
    return render_template('picture_guess.html', message=message, description=description)

@app.route('/fibonacci_guess', methods=['GET', 'POST'])
def fibonacci_guess():
    seq = [1, 1, 2, 3, 5, 8, 13, 21]
    message = None
    if request.method == 'POST':
        guess = int(request.form['guess'])
        if guess == 34:
            message = "Зөв! Дараагийн тоо 34"
        else:
            message = "Буруу, дахин оролдоно уу"
    return render_template('fibonacci_guess.html', message=message, seq=seq)

@app.route('/jenga', methods=['GET', 'POST'])
def jenga():
    if 'tower' not in session:
        session['tower'] = ['Block 1', 'Block 2', 'Block 3', 'Block 4', 'Block 5']
    message = None
    if request.method == 'POST':
        remove = request.form['remove']
        if remove in session['tower']:
            session['tower'].remove(remove)
            if len(session['tower']) == 0:
                message = "Та яллаа! Байшин нурав!"
                session['tower'] = ['Block 1', 'Block 2', 'Block 3', 'Block 4', 'Block 5']
            else:
                message = f"{remove} блокыг авлаа"
        else:
            message = "Блок байхгүй"
    return render_template('jenga.html', message=message, tower=session['tower'])

if __name__ == '__main__':
    app.run(debug=True)