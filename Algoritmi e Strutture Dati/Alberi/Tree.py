from errno import ESTALE
from tkinter.messagebox import NO
from Nodo import nodo

class Tree(object):
    """ Albero https://github.com/joowani/binarytree"""
    def __init__(self):
        self.tree = {}

    def view_tree(self):
        """ Info about the tree """
        print("Node info for tree are:")
        for _ in self.tree.keys():
            tmp = nodo(self.tree[_]['key'],self.tree[_]['child_left'],self.tree[_]['child_right'],self.tree[_]['parent'],self.tree[_]['label'])
            print('\n',tmp.get_info(),'\n')
        return self.tree

    def view_tree_info(self):
        """ Info on individual tree nodes """
        print("All node in tree are:")
        for _ in self.tree.keys():
            print('\n','node:',self.tree[_]['label'],'-- key:',self.tree[_]['key'],'\n')
        return self.tree

    def add_node_root(self,key):
        """ Adding the root node in the tree object """
        label = 'root'
        node = nodo(key,None,None,None,label)
        self.tree[label] = { 'label': label,'key': node.key, 'child_right': node.child_right, 'child_left': node.child_left,'parent': node.parent_node }
        return self.tree

    def add_node(self,new_node_key,new_node_label):
        """ Adding a node in the tree, if empty the tree inserts the node as the root"""
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
            # self.tree [z.label] to print all separate nodes; See view_tree () method
            self.tree[z.label] = { 'label': z.label, 'key': z.key, 'child_right': z.child_right, 'child_left': z.child_left,'parent': z.parent_node }
            y['child_left'] = { 'label': z.label, 'key': z.key, 'child_right': z.child_right, 'child_left': z.child_left,'parent': y['label'] }
        else:
            # self.tree [z.label] to print all separate nodes; See view_tree () method 
            self.tree[z.label] = { 'label': z.label, 'key': z.key, 'child_right': z.child_right, 'child_left': z.child_left,'parent': z.parent_node }
            y['child_right'] = { 'label': z.label, 'key': z.key, 'child_right': z.child_right, 'child_left': z.child_left,'parent': y['label'] }
        return self.tree

    def search_node(self,search_key):
        """ Search for a node by key; If not present, it returns to the root node """
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

    def tree_min(self,node_key):
        """ Search for the minimum value starting from a specific node """
        node = self.search_node(node_key)
        if not node:
            return Exception('nodo non trovato!')
        while node['child_left']:
            node = node['child_left']
        return node

    def tree_max(self,node_key):
        """ Search for the maximum value starting from a specific node """
        node = self.search_node(node_key)
        if not node:
            return Exception('nodo non trovato!')
        while node['child_right']:
            node = node['child_right']
        return node

    def tree_successor(self,node):
        """ Successore di un nodo 'node' è il nodo con la chiave più piccola ma maggiore di node['key']; -> None se la chiave del nodo è la maggiore nell'albero """
        pass

    def tree_predecessor(self,node):
        """ Predecessore di un nodo 'node' ... """
        pass








