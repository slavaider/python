from flask import Flask, render_template, request, redirect, escape

from repeat_from_book.web_development.dbhelp import DataBaseUse


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Ищет буквы из letters в phrase"""
    return set(letters).intersection(set(phrase))


def log_request(req, results: str) -> None:
    with DataBaseUse(app.config['db_config']) as cursor:
        _SQL = """INSERT INTO log(phrase, letters, ip, browser_string, results) VALUES (%s,%s,%s,%s,%s)"""
        agent = str(req.user_agent.browser).title()
        cursor.execute(_SQL, (req.form['phrase'], req.form['letters'], req.remote_addr, agent, results))


app = Flask(__name__)
app.config['db_config'] = {'dbname': 'test_database',
                           'user': 'postgres',
                           'password': 'admin'}


@app.route('/search4', methods=['POST'])
def do_search():
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    title = 'Results:'
    log_request(request, results)
    return render_template('results.html', the_phrase=phrase, the_title=title, the_results=results,
                           the_letters=letters)


@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title='Welcome!!!')


@app.route('/view_log')
def view_log():
    with DataBaseUse(app.config['db_config'])  as cursor:
        _SQL = """SELECT id,ts,phrase,letters,ip,browser_string,results FROM log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
    titles = ['ID', 'Time', 'Phrase', 'Letters', 'IP', 'User_agent', 'Results']
    return render_template('view_log.html', the_title='View Log', row_titles=titles, the_data=contents)


if __name__ == '__main__':
    app.run(debug=True)
