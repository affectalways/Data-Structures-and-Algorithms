# -*- coding: utf-8 -*-
# @Time    : 2018/4/16 13:13
# @Author  : affectalways
# @Site    : 
# @Contact : affectalways@gmail.com
# @File    : tree.py
# @Software: PyCharm

class Node(object):
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

        # def __str__(self):
        #     print '节点值为 ：' + str(self.value)


class Tree(object):
    def add_node(self, node):
        if node is None:
            return
        print '请输入节点值为' + str(node.value) + '子节点'
        left_child_value = raw_input('请输入左子节点值：')
        right_child_value = raw_input('请输入右子节点值：')
        if left_child_value is not None and left_child_value.lower() != 'none':
            left_child_node = Node(left_child_value)
            node.left_child = self.add_node(left_child_node)
        if right_child_value is not None and right_child_value.lower() != 'none':
            right_child_node = Node(right_child_value)
            node.right_child = self.add_node(right_child_node)
        return node

    # 添加节点
    def add(self, value):
        # 创建的节点
        created_node = Node(value)
        # 若根节点为空，则创建根节点
        if self.root is None:
            self.root = created_node
            return
        # 根节点不为空，则添加左右子节点
        tree_list = [self.root]
        while True:
            current_node = tree_list.pop(0)
            # 若左节点为空，则添加该子节点
            if current_node.left_child is None:
                current_node.left_child = created_node
                return
            # 若左节点不为空，则将左节点添加进tree_list
            else:
                tree_list.append(current_node.left_child)

            if current_node.right_child is None:
                current_node.right_child = created_node
                return
            else:
                tree_list.append(current_node.right_child)

    # 深度优先搜索（先序，后序，中序）
    # 先序
    def preorder_traversal(self, node):
        if node is None:
            return
        print node.value,
        self.preorder_traversal(node.left_child)
        self.preorder_traversal(node.right_child)

    # 中序
    def inorder_traversal(self, node):
        if node is None:
            return
        self.inorder_traversal(node.left_child)
        print node.value,
        self.inorder_traversal(node.right_child)

    def postorder_traversal(self, node):
        if node is None:
            return
        self.postorder_traversal(node.left_child)
        self.postorder_traversal(node.right_child)
        print node.value,

    # 广度优先搜索
    # 其实也就是层次遍历
    def void_translevel(self, node):
        if node is None:
            print '树为空'
            return

        queue = []
        queue.append(node)
        while len(queue):
            current_node = queue.pop(0)
            print current_node.value,
            if current_node.left_child is not None:
                queue.append(current_node.left_child)
            if current_node.right_child is not None:
                queue.append(current_node.right_child)


if __name__ == "__main__":
    value = raw_input('请输入根节点的值：')
    root = Node(value)
    tree = Tree()
    root = tree.add_node(root)
    print '先序遍历'
    tree.preorder_traversal(root)
    print '\n中序遍历'
    tree.inorder_traversal(root)
    print '\n后序遍历'
    tree.postorder_traversal(root)
    print '\n广度优先遍历'
    tree.void_translevel(root)
