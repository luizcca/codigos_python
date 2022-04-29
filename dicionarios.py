import time
d = {}
d['a'] = 'alfa', 'alceu', 'alma'
d['o'] = 'omega', 'omar', 'aracao'
d['g'] = 'gama', 'gasto', 'ganimedes'

'''
>>> d = {}
>>> d['a'] = 'alfa', 'alceu', 'alma'
>>> d['o'] = 'omega', 'omar', 'aracao'
>>> d['g'] = 'gama', 'gasto', 'ganimedes'
>>> d
{'a': ('alfa', 'alceu', 'alma'), 'o': ('omega', 'omar', 'aracao'), 'g': ('gama', 'gasto', 'ganimedes')}
>>> d['a']
('alfa', 'alceu', 'alma')
>>> d['o']
('omega', 'omar', 'aracao')
>>> d['g']
('gama', 'gasto', 'ganimedes')

>>> d.keys()
dict_keys(['a', 'o', 'g'])
>>> d.values()
dict_values([('alfa', 'alceu', 'alma'), ('omega', 'omar', 'aracao'), ('gama', 'gasto', 'ganimedes')])

>>> 'g' in d
True

for chave in d: print(chave)
g
o
a

for chave in d['a']: print(chave)
alfa
alceu
alma
'''
for chave in d:
    print("chave: %s, %s"%(chave,d[chave]))
'''
chave: o, ('omega', 'omar', 'aracao')
chave: a, ('alfa', 'alceu', 'alma')
chave: g, ('gama', 'gasto', 'ganimedes')
'''
