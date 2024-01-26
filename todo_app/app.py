from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.session_items import get_items, add_item

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
            item_title = request.form['item']
            add_item(item_title)

            return redirect(url_for('index'))

    items = get_items()
    return render_template('index.html', items=items)

