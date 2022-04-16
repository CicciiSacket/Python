from Nodo import nodo

class Tree(object):
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

    def search_node_from_label(self,label_node):
        x = self.tree['root']
        if not x:
            return Exception('nodo root vuoto!')
        if label_node is None:
            return Exception('Chiave di ricerca vuota non ammissibile!')
        for _ in self.tree:
            if self.tree[_]['label'] == label_node:
                return self.tree[_]
        return Exception('Node not found!')

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
        old_node = self.search_node(node_key_1)
        new_node = self.search_node(node_key_2) 
        old_parent = self.search_node_from_label(old_node['parent'])
        if not old_parent:
            self.tree['root'] = new_node
        elif old_node == old_parent['child_left']:
            old_parent['child_left'] = new_node
        else:
            old_parent['child_right'] = new_node
        if new_node:
            new_node['parent'] = old_parent

    def delete_node(self,node_key):
        """ delete the root node in the tree object """
        z = self.search_node(node_key)
        if not z['child_left']:
            self.transplant(z['key'],z['child_right']['key'])
        elif not z['child_right']:
            self.transplant(z['key'],z['child_left']['key'])
        else:
            y = self.tree_min(z['child_right']['key'])
            if y['parent'] != z['label']:
                self.transplant(y['key'],y['child_right']['key'])
                y['child_right'] = z['child_right']
                y['child_right']['parent'] = y['parent']
            self.transplant(z['key'],y['key'])
            y['child_left'] = z['child_left']
            y['child_left']['parent'] = y['parent']
        del self.tree[z['label']]
