from re import X
from Nodo import nodo

class Tree(object):
    """ Albero https://github.com/joowani/binarytree"""
    def __init__(self):
        self.tree = {}

    def view_tree(self):
        i = 0
        for i in self.tree.keys():
            print('\n',self.tree[i],'\n')
        return self.tree

    def add_node_root(self,key):
        label = 'root'
        node = nodo(key,None,None,None,label)
        self.tree[label] = { 'key':node.key, 'child_right':node.child_right, 'child_left':node.child_left,'parent':node.parent_node }
        return self.tree

    def add_node(self,new_node_key,new_node_label,parent):
        z = nodo(new_node_key,None,None,parent,new_node_label)
        self.tree[new_node_label] = { 'key':z.key, 'child_right':z.child_right, 'child_left':z.child_left,'parent':z.parent_node }
        if self.tree[parent]['key'] >= z.key:
            self.tree[parent]['child_left'] = { 'label':new_node_label, 'key':z.key, 'child_right':z.child_right, 'child_left':z.child_left,'parent':z.parent_node }
            return 201
        if self.tree[parent]['key'] <= z.key:
            self.tree[parent]['child_right'] = { 'label':new_node_label, 'key':z.key, 'child_right':z.child_right, 'child_left':z.child_left,'parent':z.parent_node }
            return 201
















