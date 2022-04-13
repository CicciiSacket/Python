class nodo(object):
    """ Nodo dell'albero binario """
    def __init__(self,key,child_left,child_right,parent_node,label):
        self.key = key
        self.child_left = child_left
        self.child_right = child_right 
        self.parent_node = parent_node
        self.label = label

    def get_info(self):
        return {'key': self.key, 'child_right': self.child_right, 'child_left': self.child_left, 'parent': self.parent_node}
        
