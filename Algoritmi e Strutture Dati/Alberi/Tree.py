from distutils.command.config import LANG_EXT
from hashlib import new
from Nodo import nodo

class Tree(object):
    """ Albero https://github.com/joowani/binarytree"""
    def __init__(self):
        self.tree = {}

    def view_tree(self):
        return self.tree

    def add_node_root(self,key):
        label = 'root'
        node = nodo(key,None,label)
        self.tree[label] = { 'key':node.key, 'child_right':node.child_right, 'child_left':node.child_left,'parent':node.parent_node }
        return self.tree

    def add_node(self, new_node_key,parent_node,new_node_label):
        new_node = nodo(new_node_key,parent_node,new_node_label)
        y = None
        x = self.tree[parent_node]
        while x != None:
            y = x
            if new_node.key < x['key']:
                x = x['child_left'] 
            else:
                x = x['child_left'] 
        new_node.parent_node = y['key']
        if new_node.key < y['key']:
            y['child_left'] = { 'key': new_node.key, 'child_right':{}, 'child_left':{},'parent':new_node.parent_node }
        else:
            y['child_right'] = { 'key': new_node.key, 'child_right':{}, 'child_left':{},'parent':new_node.parent_node }
        return self.tree








