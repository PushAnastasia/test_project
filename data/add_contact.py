from model.group import Group
import random
import string

constant = [
    Group(name="name1"),
    Group(name="name2")
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group(name="TestClient")] + [
    Group(name= random_string("contact", 10)) for i in range(3)
  ]
