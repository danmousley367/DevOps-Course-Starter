from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.trello_items import add_board_item, get_board_items, get_board_item, update_status, delete_board_item
from todo_app.data.Item import Item
from todo_app.data.ViewModel import ViewModel
import os
from todo_app.flask_config import Config

def create_app():
      app = Flask(__name__)
      app.config.from_object(Config())

      todo_list_id = os.getenv('TRELLO_TODO_LIST_ID')
      done_list_id = os.getenv('TRELLO_DONE_LIST_ID')

      @app.route('/')
      def index():
            todo_items = get_board_items(todo_list_id)
            done_items = get_board_items(done_list_id)
            items = todo_items + done_items

            item_list = [Item.from_trello_card(item) for item in items]
            item_view_model = ViewModel(item_list)

            return render_template('index.html', view_model=item_view_model)

      @app.route('/add', methods=['POST'])
      def add_item():
            if 'added_item' in request.form.keys():
                  item_title = request.form['added_item']
                  add_board_item(item_title)

            return redirect(url_for('index'))

      @app.route('/update', methods=['POST'])
      def update_item_status():
            if 'updated_item' in request.form.keys():
                  updated_item_id = request.form['updated_item']
                  updated_item = get_board_item(updated_item_id)

                  if updated_item["idList"] == todo_list_id:
                        update_status(updated_item_id, done_list_id)
                  elif updated_item['idList'] == done_list_id:
                        update_status(updated_item_id, todo_list_id)

            return redirect(url_for('index'))

      @app.route('/delete', methods=['POST'])
      def delete_item():
            if 'deleted_item' in request.form.keys():
                  deleted_item_id = request.form['deleted_item']
                  delete_board_item(deleted_item_id)

            return redirect(url_for('index'))

      return app