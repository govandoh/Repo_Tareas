# Codigo que implementa AVL 

from graphviz import Digraph

class Node:
    def __init__ (self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        self._update_height(node)
        balance_factor = self._get_balance_factor(node)
        if balance_factor == 2:
            if self._get_balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            node = self._rotate_right(node)
        elif balance_factor == -2:
            if self._get_balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            node = self._rotate_left(node)
        return node

    def _rotate_left(self, rotation_node):
        pivot_node = rotation_node.right
        rotation_node.right = pivot_node.left
        pivot_node.left = rotation_node
        self._update_height(rotation_node)
        self._update_height(pivot_node)
        return pivot_node

    def _rotate_right(self, rotation_node):
        pivot_node = rotation_node.left
        rotation_node.left = pivot_node.right
        pivot_node.right = rotation_node
        self._update_height(rotation_node)
        self._update_height(pivot_node)
        return pivot_node

    def _update_height(self, node):
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

    def _get_balance_factor(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height
    
    def generar_dot(self,node, dot):
        if node is not None:
            dot.node(str(node.key))
        if node.left is not None:
            dot.edge(str(node.key), str(node.left.key))
            self.generar_dot(node.left, dot)
        if node.right is not None:
            dot.edge(str(node.key), str(node.right.key))
            self.generar_dot(node.right, dot)
    
    def view_Tree(self):
        dot = Digraph()
        self.generar_dot(self.root, dot)
        dot.render('avl', format='png',view=True, cleanup=True)
        
    def print_tree(self):
        def print_tree_node(node, indent=0):
            if node is not None:
                print_tree_node(node.right, indent + 4)
                print("  " * indent + str(node.key))
                print_tree_node(node.left, indent + 4)

        return print_tree_node(self.root)
    
    def get_all_nodes(self):
        nodes = []
        self._get_all_nodes(self.root, nodes)
        return nodes


    def _get_all_nodes(self,node,nodes):
        if node:
            self._get_all_nodes(node.left,nodes)
            nodes.append(node.key)
            self._get_all_nodes(node.right,nodes)
            
               
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node

        if key < node.key:
            return self._search(node.left, key)

        return self._search(node.right, key)
