from Tree import Tree

def main():
    tree = Tree()
    tree.add_node_root(96)

    tree.add_node(88,'Figlio-3')
    tree.add_node(6,'Figlio-1')
    tree.add_node(100,'Figlio-2')
    print('\n########\n')
    # print(tree.add_node(None,'Figlio-2'))
    # print(tree.add_node(111,None))
    # print('\n########\n')
    # print(tree.search_node(6))
    # print('\n########\n')
    # print(tree.tree_min())
    # print('\n########\n')
    # print(tree.tree_max())
    # print('\n########\n')
    print(tree.tree_successor(tree.search_node(88)))
    print(tree.tree_predecessor(tree.search_node(6)))

    print('\n#### END ####\n')

    # tree.view_tree_info()
    # tree.view_tree()


if __name__ == "__main__":
    main()
