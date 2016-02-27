body = '''
def __init__(self, name):
    self.name = name

def be_panda(self):
    print('Bamboo & sleep')
'''

clsname = 'Panda'
bases = (object, )

clsdict = type.__prepare__(clsname, bases)

exec(body, globals(), clsdict)

Panda = type(clsname, bases, clsdict)

p = Panda('Ivo')
print(p.name)
p.be_panda()
