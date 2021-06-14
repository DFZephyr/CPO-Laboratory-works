
import copy
## mutable version for HashMap

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

    def append(self, node):
        # insert new node before the tail node
        prev = self.tail.prev
        node.prev = prev
        node.next = prev.next
        prev.next = node
        node.next.prev = node
        self.size += 1

    def delete(self, node):
        # remove the node
        prev = node.prev
        next = node.next
        next.prev, prev.next = prev, next
        self.size -= 1

    def get_list(self):
        # return a list include all node
        ret = []
        cur = self.head.next
        while cur != self.tail:
            ret.append(cur)
            cur = cur.next
        return ret

    def get_by_key(self, key):
        # get node by key
        cur = self.head.next
        while cur != self.tail:
            if cur.key == key:
                return cur
            cur = cur.next
        return None

    def get_by_value(self, value):
        cur = self.head.next
        while cur != self.tail:
            if cur.key == value:
                return cur
            cur = cur.next
        return None


class HashMap(object):
    """
        hashmap design using separate chaining to deal with collision resolution
    """

    def __init__(self,headers=None,capacity=16, load_factor=0.75,):
        self.capacity = capacity
        self.load_factor = load_factor
        self.cap = 0
        self.size = 0
        self.cur= 0
        if headers is None:
            self.headers = [LinkedList() for _ in range(capacity)]
        else:
            self.headers=headers
    def __eq__(self, other):
        self_copy=copy.deepcopy(self)
        other_copy = copy.deepcopy(other)
        if self.to_list().__contains__(None) and other.to_list().__contains__(None):
            self_copy.remove(None)
            other_copy.remove(None)
            return   self_copy.to_list().sort()== other_copy.to_list().sort()
        if not self.to_list().__contains__(None) and not other.to_list().__contains__(None):
            return self.to_list().sort() == other.to_list().sort()
        else:
            return False

    def __get_hash_key(self, key):
        return hash(key) & (self.capacity - 1)

    def put(self, key, val=None):
        hash_key = self.__get_hash_key(key)
        linked_list = self.headers[hash_key]
        if self.cap >= self.load_factor * self.capacity:
            self.__reset()
            hash_key = self.__get_hash_key(key)
            linked_list = self.headers[hash_key]
        node = linked_list.get_by_key(key)
        if linked_list.head.next == linked_list.tail:
            self.cap = self.cap + 1
        if node is not None:
            node.value = val
        else:
            node = Node(key, val)
            linked_list.append(node)
        self.size += 1

    def getValue(self, key):
        hash_key = self.__get_hash_key(key)
        linked_list = self.headers[hash_key]
        node = linked_list.get_by_key(key)
        return node.value if node is not None else None

    def getNode(self, key):
        hash_key = self.__get_hash_key(key)
        linked_list = self.headers[hash_key]
        node = linked_list.get_by_key(key)
        return node if node is not None else None

    def delete_by_key(self, key):
        node = self.getNode(key)
        if node is None:
            return False
        hash_key = self.__get_hash_key(key)
        linked_list = self.headers[hash_key]
        linked_list.delete(node)
        self.size -= 1
        return True

    def to_list(self):
        res = []
        iter=self.__iter__()
        cur = iter.cur
        curNode = iter.headers[0].head
        while cur <= iter.size:
            if (curNode == iter.headers[iter.cur].head):
                curNode = curNode.next
            if (curNode == iter.headers[cur].tail):
                cur = cur + 1
                curNode = iter.headers[cur].head
            else:
                res.append(curNode.key)
            curNode = curNode.next
        return res
    def to_list_key(self):
        res = []
        iter=self.__iter__()
        cur = iter.cur
        curNode = iter.headers[0].head
        while cur <= iter.size:
            if (curNode == iter.headers[iter.cur].head):
                curNode = curNode.next
            if (curNode == iter.headers[cur].tail):
                cur = cur + 1
                curNode = iter.headers[cur].head
            else:
                res.append(curNode.key)
            curNode = curNode.next
        return res


    def map(self, f):
        iter=self.__iter__()
        cur = iter.cur
        curNode = iter.headers[0].head
        while cur <= iter.size:
            if (curNode == iter.headers[iter.cur].head):
                curNode = curNode.next
            if (curNode == iter.headers[cur].tail):
                cur = cur + 1
                curNode = iter.headers[cur].head
            else:
                curNode.value = f(curNode.value)
            curNode = curNode.next

    def reduce(self, f, initial_state):
        state = initial_state
        iter = self.__iter__()
        cur = iter.cur
        curNode = iter.headers[0].head
        while cur <= iter.size:
            if (curNode == iter.headers[cur].head):
                curNode = curNode.next
            if (curNode == iter.headers[cur].tail):
                cur = cur + 1
                curNode = iter.headers[cur].head
            else:
                state = f(state,curNode.value)
            curNode = curNode.next
        return state
    def filter(self,fun):
        iter = self.__iter__()
        cur = iter.cur
        curNode = iter.headers[0].head
        while cur <= iter.size:
            if (curNode == iter.headers[cur].head):
                curNode = curNode.next
            if (curNode == iter.headers[cur].tail):
                cur = cur + 1
                curNode = iter.headers[cur].head
            else:
                if(not fun(curNode.value)):
                    curNode=curNode.next
                    self.delete_by_key(curNode.prev.key)
                if(curNode==iter.headers[cur].tail):
                    cur = cur + 1
                    curNode = iter.headers[cur].head
                else:
                    curNode = curNode.next
        return  self


    def __iter__(self):
        return self

    def __next__(self):
        if self.cur == self.size-1 and self.headers[self.cur].head!=self.headers[self.cur].tail:
            raise StopIteration
        tmp = self.headers[self.cur].head
        self.headers[self.cur].head = self.headers[self.cur].head.next
        return tmp

    def __reset(self):
        headers = [LinkedList() for _ in range(self.capacity * 2)]
        cap = self.capacity
        self.capacity = self.capacity * 2
        self.cap = 0
        for i in range(cap):
            linked_list = self.headers[i]
            nodes = linked_list.get_list()
            for u in nodes:
                hash_key = self.__get_hash_key(u.key)
                headlist = headers[hash_key]
                if headlist.head.next == headlist.tail:
                    self.cap = self.cap + 1
                headlist.append(u)
        self.headers = headers
    def get_size(self):
        return self.size

class Set(object):
    def __init__(self):
        self.hashmap=HashMap()
    def add(self,key=None, val=1):
        if(self.hashmap.getNode(key) ==None):
            self.hashmap.put(key,val)
    def remove(self,key):
        self.hashmap.delete_by_key(key)
    def get_size(self):
        return self.hashmap.get_size()
    def from_list(self,list):
        for i in list:
            self.add(i)
        return self;
    def to_list(self):
        return self.hashmap.to_list()
    def to_list_key(self):
        return self.hashmap.to_list_key()
    def find(self,value):
        return self.hashmap.getValue(value)
    def filter(self,fun):
        return self.hashmap.filter(fun)
    def map(self,f):
        self.hashmap.map(f)
        return self.hashmap
    def reduce(self,f,initial_state):
        return self.hashmap.reduce(f,initial_state)
    def mconcat(self, a, b):
        if a != None and b != None:
           a_key=a.to_list_key()
           a_value=a.to_list()
           b_key = b.to_list_key()
           b_value = b.to_list()
           for i in range(len(a_key)):
               self.add(a_key[i], a_value[i])
           for i in range(len(b_key)):
               self.add(b_key[i], b_value[i])
        return self
    def mempty(self):
        return None


    def __iter__(self):
        return self
    def __next__(self):
        self.hashmap.__next__()










