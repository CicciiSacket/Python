from errno import ESTALE
from tkinter import N, Y
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

    def tree_successor(self,node_key):
        """ Successor of a node 'node' is the node with the key smaller but greater than node ['key'] """
        node = self.search_node(node_key)
        if node['child_right']:
            return self.tree_min(node['child_right']['key'])
        y = node['parent_node']
        while y and node is node['child_right']:
            node = y 
            y = y['parent_node']
        return y

    def tree_predecessor(self,node_key):
        """ Predecessor of a 'node' node """
        node = self.search_node(node_key)
        if node['child_left']:
            return self.tree_max(node['child_left']['key'])
        y = node['parent_node']
        while y and node is node['child_left']:
            node = y 
            y = y['parent_node']
        return y

    def transplant(self,node_key_1,node_key_2):
        node_old = self.search_node(node_key_1)
        node_new = self.search_node(node_key_2)
        tmp_obj_node = nodo(node_new['key'],node_new['child_left'],node_new['child_right'],node_new['parent'],node_new['label'])
        if not node_old or not node_new:
            return Exception('Node not found')
        if not node_old['parent']:
            self.tree['root'] = { 'label': node_new['label'],'key': node_new['key'], 'child_right': node_new['child_right'], 'child_left': node_new['child_left'],'parent': node_new['parent'] }
        elif node_new == tmp_obj_node.child_left:
            tmp_obj_node.child_left = { 'label': node_new['label'],'key': node_new['key'], 'child_right': node_new['child_right'], 'child_left': node_new['child_left'],'parent': node_new['parent'] }
        else:
            tmp_obj_node.child_right = { 'label': node_new['label'],'key': node_new['key'], 'child_right': node_new['child_right'], 'child_left': node_new['child_left'],'parent': node_new['parent'] }
        if node_new:
            tmp_obj_node.parent_node = node_old['parent']

    def delete_node(self,node_key):
        node = self.search_node(node_key)
        if not node:
            return Exception('Node not found')
        if not node['child_left']:
            self.transplant(node['key'],node['child_right']['key'])
        elif not node['child_right']:
            self.transplant(node['key'],node['child_left']['key'])
        else:
            y = self.tree_min(node['child_right']['key'])
            if y['parent'] != node['label']:
                self.transplant(y['key'],y['child_right'])
                y['child_right'] = node['child_right']
                y['child_right']['parent'] = y
            self.transplant(node['key'],y['key'])
            y['child_left'] = node['child_left']
            y['child_left']['parent'] = y
        return self.view_tree_info()

