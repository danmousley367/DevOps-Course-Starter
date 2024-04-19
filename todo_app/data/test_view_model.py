from todo_app.data.ViewModel import ViewModel
from todo_app.data.Item import Item

default_done_list_id = "1234abcd"
default_todo_list_id = "5678efgh"

def test_view_model_items_property_returns_all_items():
    item_list = [
        Item("1", "Eat breakfast", default_done_list_id),
        Item("2", "Have a shower", default_done_list_id),
        Item("3", "Iron towels", default_todo_list_id)
    ]
    item_view_model = ViewModel(item_list, default_done_list_id)

    items = item_view_model.items

    assert items == item_list

def test_view_model_done_property_returns_only_items_in_done_list():
    item_list = [
        Item("1", "Eat breakfast", default_done_list_id),
        Item("2", "Have a shower", default_done_list_id),
        Item("3", "Iron towels", default_todo_list_id)
    ]
    item_view_model = ViewModel(item_list, done_list_id=default_done_list_id)

    done_items = item_view_model.done_items

    assert done_items == [
        Item("1", "Eat breakfast", default_done_list_id),
        Item("2", "Have a shower", default_done_list_id)
    ]

def test_view_model_todo_property_returns_only_items_in_todo_list():
    item_list = [
        Item("1", "Eat breakfast", default_done_list_id),
        Item("2", "Have a shower", default_done_list_id),
        Item("3", "Iron towels", default_todo_list_id)
    ]
    item_view_model = ViewModel(item_list, to_do_list_id=default_todo_list_id)

    todo_items = item_view_model.todo_items

    assert todo_items == [
        Item("3", "Iron towels", default_todo_list_id)
    ]