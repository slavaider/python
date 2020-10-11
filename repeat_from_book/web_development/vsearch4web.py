from flask import Flask, render_template, request, escape


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Ищет буквы из letters в phrase"""
    return set(letters).intersection(set(phrase))


def log_request(req, res: str) -> None:
    with open('../../files/vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


app = Flask(__name__)


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
    contents = []
    with open('../../files/vsearch.log') as log:
        for i in log:
            contents.append([])
            for j in i.split('|'):
                contents[-1].append(escape(j))
    titles = ['Form Data', 'Remote_addr', 'User_agent', 'Results']
    return render_template('view_log.html', the_title='View Log', row_titles=titles, the_data=contents)


if __name__ == '__main__':
    app.run(debug=True)
