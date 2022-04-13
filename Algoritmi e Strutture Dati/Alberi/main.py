from traceback import print_list
from Tree import Tree

def main():
    tree = Tree()
    tree.add_node_root(96)
    tree.add_node(6,'Figlio-1','root')
    tree.add_node(1,'Figlio-2','Figlio-1')
    print('#########')
    print(tree.view_tree())
    print('#########')


if __name__ == "__main__":
    main()
