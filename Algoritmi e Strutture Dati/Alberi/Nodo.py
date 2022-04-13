class nodo(object):
    """ Nodo dell'albero binario """
    def __init__(self,key,parent_node,label):
        self.key = key 
        self.child_left = {}
        self.child_right = {}
        self.parent_node = parent_node
        self.label = label

    def get_info(self):
        return (self.key,self.child_left,self.child_right,self.parent_node)
        
