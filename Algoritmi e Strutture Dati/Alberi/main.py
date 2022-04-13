from traceback import print_list
from Tree import Tree

def main():
    tree = Tree()
    tree.add_node_root(96)
    print(tree.view_tree())
    print('#########')
    tree.add_node(78,'root','Figlio-1')
    print('#########')
    print(tree.view_tree())
    # print('#########')
    # tree = tree.add_node(16,'root','Figlio-2')
    # print('#########')
    # print(tree)



if __name__ == "__main__":
    main()
