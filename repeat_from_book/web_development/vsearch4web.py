from flask import Flask, render_template, request, session, copy_current_request_context, redirect
from repeat_from_book.checker import check_logged_in
from repeat_from_book.web_development.dbhelp import DataBaseUse, MyConnectionError, CredentialError, SQLError, \
    Pagination
from threading import Thread


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Ищет буквы из letters в phrase"""
    return set(letters).intersection(set(phrase))


app = Flask(__name__)
app.config['db_config'] = {'dbname': 'test_database',
                           'user': 'postgres',
                           'password': 'admin'}
app.secret_key = 'AL:cjclcjalcjalckjvlsvjlkcmldcsmlcd'


@app.route('/search4', methods=['POST'])
def do_search():
    @copy_current_request_context
    def log_request(req, results: str) -> None:
        with DataBaseUse(app.config['db_config']) as cursor:
            _SQL = """INSERT INTO log(phrase, letters, ip, browser_string, results) VALUES (%s,%s,%s,%s,%s)"""
            agent = str(req.user_agent.browser).title()
            cursor.execute(_SQL, (req.form['phrase'], req.form['letters'], req.remote_addr, agent, results))

    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    title = 'Results:'
    try:
        t = Thread(target=log_request, args=(request, results))
        t.start()
    except Exception as ex:
        print(repr(ex))
    return render_template('results.html', the_phrase=phrase, the_title=title, the_results=results,
                           the_letters=letters)


@app.route('/login')
def do_login():
    session['logged_in'] = True
    return 'You are now logged in'


@app.route('/logout')
def do_logout():
    session.pop('logged_in')
    return 'You are now logged out'


@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title='Welcome!!!')


@app.route('/view_log', methods=['GET', 'POST'])
@check_logged_in
def view_log(page_number=1):
    try:
        with DataBaseUse(app.config['db_config'])  as cursor:
            _SQL = """SELECT id,ts,phrase,letters,ip,browser_string,results FROM log"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()
        titles = ['ID', 'Time', 'Phrase', 'Letters', 'IP', 'User_agent', 'Results']
        pagination_content = Pagination(contents, 5)
        nums = pagination_content.get_pagination_list_of_nums()
        # S-s- spaghetti code
        if 'page_number' in request.form.keys():
            page_number = int(request.form['page_number'])
            pagination_content.go_to_page(page_number)
        elif 'first_page' in request.form.keys():
            pagination_content.first_page()
            page_number = pagination_content.get_current_page()
        elif 'last_page' in request.form.keys():
            pagination_content.last_page()
            page_number = pagination_content.get_current_page()
        elif (list(request.form.keys()) != []) and ('next' in list(request.form.keys())[-1].split(':')):
            pagination_content.go_to_page(int(list(request.form.keys())[-1].split(':')[-1]) + 1)
            page_number = pagination_content.get_current_page()
        elif (list(request.form.keys()) != []) and ('prev' in list(request.form.keys())[-1].split(':')):
            pagination_content.go_to_page(int(list(request.form.keys())[-1].split(':')[-1]) - 1)
            page_number = pagination_content.get_current_page()
        return render_template('view_log.html', the_title='View Log', row_titles=titles,
                               the_data=pagination_content.get_visible_items(), nums=nums,
                               page_number=page_number)
    except MyConnectionError as ex:
        print('Database switched on?', str(ex))
    except CredentialError as ex:
        print('User-id/password issues', str(ex))
    except SQLError as ex:
        print('Is your query correct?', str(ex))
    except Exception as ex:
        print(repr(ex))
    return 'Error'


if __name__ == '__main__':
    app.run(debug=True)
