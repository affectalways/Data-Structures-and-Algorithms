# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 10:38
# @Author  : affectalways
# @Site    : 
# @Contact : affectalways@gmail.com
# @File    : huffman_tree.py
# @Software: PyCharm

class Node(object):
    def __init__(self, value, left_child_node=None, right_child_node=None):
        self.value = value
        self.left_child_node = left_child_node
        self.right_child_node = right_child_node


class Huffman_Tree(object):
    def __init__(self):
        pass

    def generate_subtree(self, nodes):
        # subtree_root = nod
        left_child_node, right_child_node = nodes[0], nodes[1]
        subtree_root_value = left_child_node.value + right_child_node.value
        subtree_root = Node(subtree_root_value, left_child_node=left_child_node, right_child_node=right_child_node)
        # 返回子树的根节点
        return subtree_root

    # 广度优先遍历
    def void_translevel(self, node):
        if node is None:
            print '树为空'
            return

        queue = [node]
        while len(queue):
            current_node = queue.pop(0)
            print current_node.value,
            if current_node.left_child_node is not None:
                queue.append(current_node.left_child_node)
            if current_node.right_child_node is not None:
                queue.append(current_node.right_child_node)


def select_two_smallest_nodes(node_space):
    if node_space is None or len(node_space) == 1:
        print '哈夫曼树构造完成！'
        return None, node_space
    result = node_space[:2]
    # node_space.pop(0)
    # node_space.pop(0)
    node_space = node_space[2:]
    return result, node_space


if __name__ == "__main__":
    node_space = [2, 3, 7, 10, 4, 2, 5]
    print '用以下节点构造哈夫曼树'
    print node_space
    print '\n'
    for index, value in enumerate(node_space):
        node = Node(value)
        node_space[index] = node
    huffman_tree = Huffman_Tree()

    while True:
        # 按value排序
        node_space.sort(key=lambda x: x.value)
        two_smallest_nodes, node_space = select_two_smallest_nodes(node_space)
        if two_smallest_nodes is None:
            tree_root = node_space[0]
            break
        # print two_smallest_nodes
        subtree_root = huffman_tree.generate_subtree(two_smallest_nodes)
        node_space.append(subtree_root)
    print '\n构造的哈夫曼树为：'
    huffman_tree.void_translevel(tree_root)
    # for node in node_space:
    #     print node.value,
    # print two_smallest_nodes
