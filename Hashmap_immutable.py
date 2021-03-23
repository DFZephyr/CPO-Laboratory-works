# immutable version for HashMap

class Node(object):
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next
class LinkedList(object):
    def __init__(self):
        self.head = Node(None, 'header')
        self.tail = Node(None, 'tail')
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

# operation
def append(LinkedList, node):
    # insert new node before the tail node
    prev = LinkedList.tail.prev
    node.prev = prev
    node.next = prev.next
    prev.next = node
    node.next.prev = node
    LinkedList.size += 1


def delete(LinkedList, node):
    # remove the node
    prev = node.prev
    next = node.next
    next.prev, prev.next = prev, next
    LinkedList.size -= 1


def get_list(LinkedList):
    # return a list include all node
    ret = []
    cur = LinkedList.head.next
    while cur != LinkedList.tail:
        ret.append(cur)
        cur = cur.next
    return ret


def get_by_key(LinkedList, key):
    # get node by key
    cur = LinkedList.head.next
    while cur != LinkedList.tail:
        if cur.key == key:
            return cur
        cur = cur.next
    return None


def get_by_value(LinkedList, value):
    cur = LinkedList.head.next
    while cur != LinkedList.tail:
        if cur.key == value:
            return cur
        cur = cur.next
    return None
# Hashmap realization
capacity=16
load_factor = 0.75
cap = 0
size = 0
cur= 0
headers = [LinkedList() for _ in range(capacity)]

def __get_hash_key(key):
    return hash(key) & (capacity - 1)
def get_size():
    global size
    return size


def put(key, val=None):
    global cap, size
    hash_key = __get_hash_key(key)
    linked_list = headers[hash_key]
    if cap >= load_factor * capacity:
        __reset()
        hash_key = __get_hash_key(key)
        linked_list = headers[hash_key]
    node = get_by_key(linked_list, key)
    if linked_list.head.next == linked_list.tail:
        cap += 1
    if node is not None:
        node.value = val
    else:
        node = Node(key, val)
        append(linked_list, node)
    size += 1

def getValue(key):
    hash_key = __get_hash_key(key)
    linked_list = headers[hash_key]
    node = get_by_key(linked_list, key)
    return node.value if node is not None else None

def getNode(key):
    hash_key = __get_hash_key(key)
    linked_list = headers[hash_key]
    node = get_by_key(linked_list, key)
    return node if node is not None else None

def delete_by_key(key):
    global size
    node = getNode(key)
    if node is None:
        return False
    hash_key = __get_hash_key(key)
    linked_list = headers[hash_key]
    delete(linked_list, node)
    size -= 1
    return True

def map(f):
    global cur
    curNode = headers[0].head
    while cur <= size:
        if curNode == headers[cur].head:
            curNode = curNode.next
        if curNode == headers[cur].tail:
            cur += 1
            curNode = headers[cur].head
        else:
            curNode.value = f(curNode.value)
        curNode = curNode.next

def __reset():
    global capacity, cap, headers
    headers = [LinkedList() for _ in range(capacity * 2)]
    cap = capacity
    capacity *= 2
    cap = 0
    for i in range(cap):
        linked_list = headers[i]
        nodes = get_list(linked_list)
        for u in nodes:
            hash_key = __get_hash_key(u.key)
            headlist = headers[hash_key]
            if headlist.head.next == headlist.tail:
                cap += 1
            append(headlist, u)
    headers = headers

def reduce(f, initial_state):
    state = initial_state
    global cur
    cur = cur
    curNode = headers[0].head
    while cur <= size:
        if curNode == headers[cur].head:
            curNode = curNode.next
        if curNode == headers[cur].tail:
            cur += 1
            curNode = headers[cur].head
        else:
            state = f(state, curNode.value)
        curNode = curNode.next
    return state