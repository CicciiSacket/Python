from Nodo import nodo

class Tree(object):
    """ Albero https://github.com/joowani/binarytree"""
    def __init__(self):
        self.tree = {}

    def view_tree(self):
        print("Node info for tree are:")
        for _ in self.tree.keys():
            tmp = nodo(self.tree[_]['key'],self.tree[_]['child_left'],self.tree[_]['child_right'],self.tree[_]['parent'],self.tree[_]['label'])
            print('\n',tmp.get_info(),'\n')
        return self.tree

    def view_tree_info(self):
        print("All node in tree are:")
        for _ in self.tree.keys():
            print('\n','node:',self.tree[_]['label'],'-- key:',self.tree[_]['key'],'\n')
        return self.tree

    def add_node_root(self,key):
        label = 'root'
        node = nodo(key,None,None,None,label)
        self.tree[label] = { 'label': label,'key': node.key, 'child_right': node.child_right, 'child_left': node.child_left,'parent': node.parent_node }
        return self.tree

    def add_node(self,new_node_key,new_node_label):
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
            self.tree[z.label] = { 'label': z.label, 'key': z.key, 'child_right': z.child_right, 'child_left': z.child_left,'parent': z.parent_node }
            y['child_left'] = { 'label': z.label, 'key': z.key, 'child_right': z.child_right, 'child_left': z.child_left,'parent': y['label'] }
        else:
            self.tree[z.label] = { 'label': z.label, 'key': z.key, 'child_right': z.child_right, 'child_left': z.child_left,'parent': z.parent_node }
            y['child_right'] = { 'label': z.label, 'key': z.key, 'child_right': z.child_right, 'child_left': z.child_left,'parent': y['label'] }
        return self.tree






