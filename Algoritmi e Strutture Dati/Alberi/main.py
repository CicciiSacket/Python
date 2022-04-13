from Tree import Tree

def main():
    tree = Tree()
    tree.add_node_root(96)

    tree.add_node(6,'Figlio-1','root')
    tree.add_node(100,'Figlio-2','root')
    
    tree.add_node(88,'Figlio-3','root')


    # tree.add_node(1,'Figlio-2','Figlio-1')
    # tree.add_node(2,'Figlio-3','Figlio-1')

    
    # print(tree.add_node(1,'Figlio-2','Figlio-1'))
    # print(tree.add_node(1,'Figlio-8','Figlio-7'))

    print('\n#########')
    # tree.view_tree()
    print('#########\n')
    # tree.view_tree_info()

if __name__ == "__main__":
    main()
