from inspect import isfunction

class Node(object):
    """
        node
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def initNode(value, next):
    """
    :param value:
    :param next:
    :return: LinkList
    """

    return Node(value, next)

def head(list):
    """
    :param list:
    :return: a list first element
    """
    assert list is not None
    assert type(list) is Node
    return list.value


def tail(list):
    """
    :param list:
    :return: tail of the list
    """
    assert list is not None
    assert type(list) is Node
    if list.next is not None:
        list = list.next
        return tail(list)
    return list.value

start_state_take = 1
def take(list, n):
    """
    :param list:
    :param n:
    :return: take N first elements of the list
    """
    assert list is not None
    assert type(list) is Node
    global start_state_take
    if list.next is not None:
        if start_state_take==n:
            return list.value
        else:
            list = list.next
            start_state_take += 1
            return take(list, start_state_take)
    else:
        return list.value

def length(list):
    """
    :param list:
    :return: linkList length
    """
    if list is None:
        return 0
    else:
        return 1 + length(list.next)

def map(list, function):
    """
    :param list:
    :param function:
    :return: lazy list without evaluation
    """
    if list is None:
        return None
    else:
        tmp = function(list.value)
        list = list.next
        return initNode(tmp, map(list, function))

def reduce(list, function, initState):
    """
    :param list:
    :param function:
    :param initState:
    :return: process structure elements to build a return value by specific functions
    """
    state = initState
    if list is not None:
        state = function(state, list.value)
        list = list.next
        return reduce(list, function, state)
    else:
        return state

def empty():
    """
    :return: empty linkList
    """
    return None

def concat(list1, list2):
    """
    :param list1:
    :param list2:
    :return: Connect two link lists
    """
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    tmp = reverse(list1)
    res = list2
    while tmp is not None:
        res = initNode(tmp.value, res)
        tmp = tmp.next
    return res

def reverse(list, e=None):
    def tail_init(list):
        assert type(list) is Node
        return list.next
    if list is None:
        return e
    return reverse(tail_init(list), Node(head(list), e))

def from_list(list):
    res = None
    if len(list) == 0:
        return None
    for e in reversed(list):
        res = initNode(e, res)
    return res




def to_list(list):
    """
    :param list:
    :return: make LinkList be a list
    """
    res = []
    while list is not None:
        res.append(list.value)
        if list.next is not None:
            list = list.next
        else:
            list = None
    return res

def iterator(list):
    cur = list
    while isfunction(cur):
        cur = cur()

    def A():
        nonlocal cur
        if cur is None:
            raise StopIteration
        tmp = cur.value
        if cur.next:
            cur = cur.next
        else:
            cur = cur.next
        return tmp
    return A


