from Tree import Tree

def main():
    tree = Tree()
    tree.add_node_root(96)
    tree.add_node(88,'Figlio-3')
    tree.add_node(6,'Figlio-1')
    tree.add_node(100,'Figlio-2')

    # Test methods
    # print('\n########\n')
    # print(tree.add_node(None,'Figlio-2'))
    # print(tree.add_node(111,None))
    # print('\n########\n')
    # print(tree.search_node(6))
    # print('\n########\n')
    # print(tree.tree_min(96))
    # print('\n########\n')
    # print(tree.tree_max(96))
    # print('\n########\n')
    # print(tree.tree_successor(96))
    # print(tree.tree_predecessor(88))
    # tree.view_tree()
    print('\n########\n')
    tree.delete_node(88)
    print('\n########\n')
    tree.view_tree()
    print('\n#### END ####\n')
    tree.view_tree_info()


if __name__ == "__main__":
    main()
