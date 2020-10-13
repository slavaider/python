from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'YouWillNeverGuess'


@app.route('/setuser/<user>')
def set_user(user: str):
    session['user'] = user
    return f'User value set to {session["user"]}'


@app.route('/getuser')
def get_user():
    if session.get('user'):
        return f'User value already set to {session["user"]}'


if __name__ == '__main__':
    app.run(debug=True)
