
import Hashmap


def size(Set):
    return Set.get_size()

def put(x, y, h):

    return h.add(x, y)

def find(x, h):

    return h.find(x)

def remove(x, h):

    return h.remove(x)

def map(squre, h):

    return h.map(squre)

def reduce(x, y, h):

    return h.reduce(x, y)

def to_list(h):

    return h.to_list()

def from_list(res, h):

    return h.from_list(res)

def mempty(h):
    return h.mempty()

def mconcat(x, y, h):
    return h.mconcat(x, y)

def filter(x, h):

    return h.filter(x)



