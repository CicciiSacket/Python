from errno import ESTALE
from tkinter.messagebox import NO
from Nodo import nodo

class Tree(object):
    """ Albero https://github.com/joowani/binarytree"""
    def __init__(self):
        self.tree = {}

    def view_tree(self):
        """ Info dell'albero """
        print("Node info for tree are:")
        for _ in self.tree.keys():
            tmp = nodo(self.tree[_]['key'],self.tree[_]['child_left'],self.tree[_]['child_right'],self.tree[_]['parent'],self.tree[_]['label'])
            print('\n',tmp.get_info(),'\n')
        return self.tree

    def view_tree_info(self):
        """ Info sui singoli nodi dell'albero """
        print("All node in tree are:")
        for _ in self.tree.keys():
            print('\n','node:',self.tree[_]['label'],'-- key:',self.tree[_]['key'],'\n')
        return self.tree

    def add_node_root(self,key):
        """ Aggiunta del nodo radice nell'oggetto albero """
        label = 'root'
        node = nodo(key,None,None,None,label)
        self.tree[label] = { 'label': label,'key': node.key, 'child_right': node.child_right, 'child_left': node.child_left,'parent': node.parent_node }
        return self.tree

    def add_node(self,new_node_key,new_node_label):
        """ Aggiunta di un nodo nell'albero, se vuoto l'albero inserisce il nodo come radice """
        z = nodo(new_node_key,None,None,None,new_node_label)
        if z.key is None or z.label is None:
            return Exception('Chiave o label errati!')
        y =  None
        x = self.tree['root']
        while x != None:
            y = x
            if z.key < x['key']:
                x = x['child_left']
            else:
                x = x['child_right']
        z.parent_node = y
        if y == None:
            self.tree['root'] = { 'label': z.label, 'key': z.key, 'child_right': z.child_right, 'child_left': z.child_left,'parent': z.parent_node }
        elif z.key < y['key']:
            """  self.tree[z.label] per avere la stampa di tutti i nodi separati; Vedi metodo view_tree() """
            self.tree[z.label] = { 'label': z.label, 'key': z.key, 'child_right': z.child_right, 'child_left': z.child_left,'parent': z.parent_node }
            y['child_left'] = { 'label': z.label, 'key': z.key, 'child_right': z.child_right, 'child_left': z.child_left,'parent': y['label'] }
        else:
            """  self.tree[z.label] per avere la stampa di tutti i nodi separati; Vedi metodo view_tree() """
            self.tree[z.label] = { 'label': z.label, 'key': z.key, 'child_right': z.child_right, 'child_left': z.child_left,'parent': z.parent_node }
            y['child_right'] = { 'label': z.label, 'key': z.key, 'child_right': z.child_right, 'child_left': z.child_left,'parent': y['label'] }
        return self.tree

    def search_node(self,search_key):
        """ Ricerca di un nodo mediante key; Se non presente torna nodo radice"""
        x = self.tree['root']
        if not x:
            return Exception('nodo root vuoto!')
        if search_key is None:
            return Exception('Chiave di ricerca vuota non ammissibile!')
        while x != None and search_key != x['key']:
            if search_key < x['key']:
                x = x['child_left']
            else:
                x = x['child_right']
        return x

    def tree_min(self):
        """ Ricerca del valore minimo dell'albero """
        x = self.tree['root']
        if not x:
            return Exception('nodo root vuoto!')
        while x['child_left'] != None:
            x = x['child_left']
        return x

    def tree_max(self):
        """ Ricerca del valore minimo dell'albero """
        x = self.tree['root']
        if not x:
            return Exception('nodo root vuoto!')
        while x['child_right'] != None:
            x = x['child_right']
        return x

    def tree_successor(self,node):
        """ Successore di un nodo 'node' è il nodo con la chiave più piccola ma maggiore di node['key']; -> None se la chiave del nodo è la maggiore nell'albero """
        if not node:
            return Exception('Il nodo parametro non esiste!')
        if node['child_right'] is None:
            return self.tree_min()
        y = node['parent']
        while y != None and node == y['child_right']:
            node = y
            y = y['parent']
        return y

    def tree_predecessor(self,node):
        """ Predecessore di un nodo 'node' ... """
        if not node:
            return Exception('Il nodo parametro non esiste!')
        if node['child_left'] is None:
            return self.tree_max()
        y = node['parent']
        while y != None and node == y['child_left']:
            node = y
            y = y['parent']
        return y








