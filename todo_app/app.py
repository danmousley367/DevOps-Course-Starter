from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.db_items import add_db_item, get_db_items, get_db_item, update_status, delete_db_item
from todo_app.data.Item import Item
from todo_app.data.ViewModel import ViewModel
from todo_app.flask_config import Config
from todo_app.data.Status import Status

def create_app():
      app = Flask(__name__)
      app.config.from_object(Config())

      @app.route('/')
      def index():
            items = get_db_items()

            item_list = [Item.from_db(item) for item in items]
            item_view_model = ViewModel(item_list)

            return render_template('index.html', view_model=item_view_model)

      @app.route('/add', methods=['POST'])
      def add_item():
            if 'added_item' in request.form.keys():
                  item_title = request.form['added_item']
                  add_db_item(item_title)

            return redirect(url_for('index'))

      @app.route('/update', methods=['POST'])
      def update_item_status():
            if 'updated_item' in request.form.keys():
                  updated_item_id = request.form['updated_item']
                  updated_item = get_db_item(updated_item_id)

                  if updated_item["status"] == Status.TODO.value:
                        update_status(updated_item_id, Status.COMPLETE.value)
                  elif updated_item["status"] == Status.COMPLETE.value:
                        update_status(updated_item_id, Status.TODO.value)

            return redirect(url_for('index'))

      @app.route('/delete', methods=['POST'])
      def delete_item():
            if 'deleted_item' in request.form.keys():
                  deleted_item_id = request.form['deleted_item']
                  delete_db_item(deleted_item_id)

            return redirect(url_for('index'))

      return app