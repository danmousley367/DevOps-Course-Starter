from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.session_items import get_items, add_item, get_item, save_item

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
            if 'item' in request.form.keys():
                  item_title = request.form['item']
                  add_item(item_title)

            if 'checkbox' in request.form.keys():
                  checked_item_id = request.form['checkbox']
                  checked_item = get_item(checked_item_id)

                  if checked_item['status'] == 'Not Started':
                        checked_item['status'] = 'Finished'
                  elif checked_item['status'] == 'Finished':
                        checked_item['status'] = 'Not Started'
                  save_item(checked_item)

            return redirect(url_for('index'))

    items = get_items()
    return render_template('index.html', items=items)

