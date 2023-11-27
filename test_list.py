import pytest
from list import List, Vector, Stack, Queue

def test_list():
    my_list = List([1, 2, 3])
    assert str([1, 2, 3]) == my_list.display()

def test_list_empty():
    my_list = List([])
    assert str([]) == my_list.display()

def test_list_add():
    my_list = List([1, 2, 3])
    my_list.add(4)
    assert str([1, 2, 3, 4]) == my_list.display()

def test_list_remove():
    my_list = List([1, 2, 3])
    my_list.remove(2)
    assert str([1, 3]) == my_list.display()

def test_list_size():
    my_list = List([1, 2, 3])
    assert 3 == my_list.size()

def test_vector():
    my_vector = Vector([1, 2, 3, 4])
    assert str([1, 2, 3, 4]) == my_vector.display()

def test_vector_add():
    my_vector = Vector([1, 2, 3, 4])
    another = Vector([1, 2, 3, 4])
    assert str([2, 4, 6, 8]) == my_vector.add(another).display()


def test_scalar_multiply():
    my_vector = Vector([1, 2, 3, 4])
    assert str([2, 4, 6, 8]) == my_vector.scalar_multiply(2).display()

@pytest.fixture
def empty_stack():
    return Stack()

@pytest.fixture
def stack_with_elements():
    return Stack([1, 2, 3])

def test_push(empty_stack):
    empty_stack.push(42)
    assert not empty_stack.is_empty()
    assert empty_stack.items == [42]

def test_pop(stack_with_elements):
    popped_item = stack_with_elements.pop()
    assert popped_item == 3
    assert stack_with_elements.items == [1, 2]

def test_pop_empty_stack(empty_stack):
    popped_item = empty_stack.pop()
    assert popped_item is None
    assert empty_stack.is_empty()

def test_is_empty(empty_stack, stack_with_elements):
    assert empty_stack.is_empty()
    assert not stack_with_elements.is_empty()


@pytest.fixture
def empty_queue():
    return Queue()

@pytest.fixture
def queue_with_elements():
    return Queue([1, 2, 3])

# Tests for Queue
def test_enqueue(empty_queue):
    empty_queue.enqueue(42)
    assert not empty_queue.is_empty()
    assert empty_queue.items == [42]

def test_dequeue(queue_with_elements):
    dequeued_item = queue_with_elements.dequeue()
    assert dequeued_item == 1
    assert queue_with_elements.items == [2, 3]

def test_dequeue_empty_queue(empty_queue):
    dequeued_item = empty_queue.dequeue()
    assert dequeued_item is None
    assert empty_queue.is_empty()