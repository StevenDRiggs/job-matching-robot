from flask import (
    Flask,
    redirect,
    request,
    session,
    url_for,
)
from markupsafe import escape


app = Flask(__name__)
app.secret_key = b'draw the secret key from dotenv'


# access the static files via, e.g. url_for('static', filename='style.css')


@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return 'Login form'

'''alternatively
@app.get('/login')
def login_get():
    ...

@app.post('/login')
def login_post():
    ...
'''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

@app.route('/projects/')  # can be loaded with the slash or without (without redirects to with)
def projects():
    return 'The project page'

@app.route('/about')  # cannot be loaded with a trailing slash, i.e. /about/
def about():
    return 'The about page'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('hello'))
    print(url_for('hello', next='/'))
    print(url_for('show_user_profile', username='John Doe'))
