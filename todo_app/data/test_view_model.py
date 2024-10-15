from todo_app.data.ViewModel import ViewModel
from todo_app.data.Item import Item
from todo_app.data.Status import Status

def test_view_model_items_property_returns_all_items():
    item_list = [
        Item("1", "Eat breakfast", Status.COMPLETE.value),
        Item("2", "Have a shower", Status.COMPLETE.value),
        Item("3", "Iron towels", Status.TODO.value)
    ]
    item_view_model = ViewModel(item_list)

    items = item_view_model.items

    assert items == item_list

def test_view_model_done_property_returns_only_items_in_done_list():
    item_list = [
        Item("1", "Eat breakfast", Status.COMPLETE.value),
        Item("2", "Have a shower", Status.COMPLETE.value),
        Item("3", "Iron towels", Status.TODO.value)
    ]
    item_view_model = ViewModel(item_list)

    done_items = item_view_model.done_items

    assert done_items == [
        Item("1", "Eat breakfast", Status.COMPLETE.value),
        Item("2", "Have a shower", Status.COMPLETE.value)
    ]

def test_view_model_todo_property_returns_only_items_in_todo_list():
    item_list = [
        Item("1", "Eat breakfast", Status.COMPLETE.value),
        Item("2", "Have a shower", Status.COMPLETE.value),
        Item("3", "Iron towels", Status.TODO.value)
    ]
    item_view_model = ViewModel(item_list)

    todo_items = item_view_model.todo_items

    assert todo_items == [
        Item("3", "Iron towels", Status.TODO.value)
    ]