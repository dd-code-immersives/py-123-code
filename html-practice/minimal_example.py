from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def minimal():
    return render_template('simple-content.html')

@app.route("/variable/<message>")
def minimal():
    return render_template('passing-a-variable.html', message=message)

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

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
	app.run(debug = True)