from Nodo import nodo

class Tree(object):
    """ Albero https://github.com/joowani/binarytree"""
    def __init__(self):
        self.tree = {}

    def view_tree(self):
        print("Node info for tree are:")
        print(self.tree)
        return self.tree

    def view_tree_info(self):
        print("All node in tree are:")
        for _ in self.tree.keys():
            print('\n',self.tree[_],'\n')
        return self.tree

    def add_node_root(self,key):
        label = 'root'
        node = nodo(key,None,None,None,label)
        self.tree[label] = { 'label': label,'key': node.key, 'child_right': node.child_right, 'child_left': node.child_left,'parent': node.parent_node }
        return self.tree

    def add_node(self,new_node_key,new_node_label,parent):
        if not parent in self.tree.keys():
            return Exception('Parent does not exist!')
        z = nodo(new_node_key,None,None,parent,new_node_label)
        self.tree[new_node_label] = { 'label': z.label,'key': z.key, 'child_right': z.child_right, 'child_left': z.child_left,'parent': z.parent_node }
        if self.tree[parent]['key'] > z.key and self.tree[parent]['child_left'] is None:
            self.tree[parent]['child_left'] = { 'label': z.label, 'key': z.key, 'child_right': z.child_right, 'child_left': z.child_left,'parent': z.parent_node }
            if self.tree[parent]['child_left'] is not None:
                #Si sceglie come padre quello precedente
                pass 
        if self.tree[parent]['key'] < z.key and self.tree[parent]['child_right'] is None:
            self.tree[parent]['child_right'] = { 'label': z.label, 'key': z.key, 'child_right': z.child_right, 'child_left': z.child_left,'parent': z.parent_node }
            if self.tree[parent]['child_left'] is not None:
                #Si sceglie come padre quello precedente
                pass
        else:
            return Exception('A child already exists for this node!')
