from Tree import Tree

def main():
    tree = Tree()
    tree.add_node_root(96)

    tree.add_node(88,'Figlio-3')
    tree.add_node(6,'Figlio-1')
    tree.add_node(100,'Figlio-2')


    print(tree.add_node(None,'Figlio-2'))
    print(tree.add_node(111,None))




    # tree.add_node(1,'Figlio-2','Figlio-1')
    # tree.add_node(2,'Figlio-3','Figlio-1')

    
    # print(tree.add_node(1,'Figlio-2','Figlio-1'))
    # print(tree.add_node(1,'Figlio-8','Figlio-7'))

    print('\n#########')
    print('#########\n')
    # tree.view_tree_info()
    tree.view_tree()

    print('#########\n')
if __name__ == "__main__":
    main()
