from flask import Flask, render_template, request, redirect, url_for
from todo_app.data.db_items import add_todo_item, get_todo_items, get_todo_item, update_status, delete_todo_item
from todo_app.data.Item import Item
from todo_app.data.ViewModel import ViewModel
from todo_app.flask_config import Config
from todo_app.data.Status import Status
from oauth import blueprint

from todo_app.utils.require_github_auth import login_required
from werkzeug.middleware.proxy_fix import ProxyFix

def create_app():
      app = Flask(__name__)
      app.config.from_object(Config())
      app.register_blueprint(blueprint, url_prefix="/login")
      app.wsgi_app = ProxyFix(app.wsgi_app)

      @app.route('/')
      @login_required
      def index():
            items = get_todo_items()

            item_list = [Item.from_db(item) for item in items]
            item_view_model = ViewModel(item_list)

            return render_template('index.html', view_model=item_view_model)

      @app.route('/add', methods=['POST'])
      @login_required
      def add_item():
            if 'added_item' in request.form.keys():
                  item_title = request.form['added_item']
                  add_todo_item(item_title)

            return redirect(url_for('index'))

      @app.route('/update', methods=['POST'])
      @login_required
      def update_item_status():
            if 'updated_item' in request.form.keys():
                  updated_item_id = request.form['updated_item']
                  updated_item = get_todo_item(updated_item_id)

                  if updated_item["status"] == Status.TODO.value:
                        update_status(updated_item_id, Status.COMPLETE.value)
                  elif updated_item["status"] == Status.COMPLETE.value:
                        update_status(updated_item_id, Status.TODO.value)

            return redirect(url_for('index'))

      @app.route('/delete', methods=['POST'])
      @login_required
      def delete_item():
            if 'deleted_item' in request.form.keys():
                  deleted_item_id = request.form['deleted_item']
                  delete_todo_item(deleted_item_id)

            return redirect(url_for('index'))

      return app