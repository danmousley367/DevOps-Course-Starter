from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.session_items import get_items, add_item, get_item, save_item, delete_item

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
      items = get_items()
      sorted_items = sorted(items, key=lambda item: item['status'], reverse=True) 

      return render_template('index.html', items=sorted_items)

@app.route('/', methods=['POST'])
def change_item():
      if 'added_item' in request.form.keys():
            item_title = request.form['added_item']
            add_item(item_title)

      if 'updated_item' in request.form.keys():
            updated_item_id = request.form['updated_item']
            updated_item = get_item(updated_item_id)

            if updated_item['status'] == 'Not Started':
                  updated_item['status'] = 'Finished'
            elif updated_item['status'] == 'Finished':
                  updated_item['status'] = 'Not Started'
            save_item(updated_item)

      if 'deleted_item' in request.form.keys():
            deleted_item_id = request.form['deleted_item']
            deleted_item = get_item(deleted_item_id)

            delete_item(deleted_item)

      return redirect(url_for('index'))

