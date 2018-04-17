# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 13:41
# @Author  : affectalways
# @Site    : 
# @Contact : affectalways@gmail.com
# @File    : huffman_encoding.py
# @Software: PyCharm
import sys


class Node(object):
    def __init__(self, value, key=None, label=None, left_child_node=None, right_child_node=None):
        self.key = key
        self.value = value
        # 标注，区分是左右节点，左0右1
        self.label = label
        self.left_child_node = left_child_node
        self.right_child_node = right_child_node


class Huffman_Encoding(object):
    def generate_subtree(self, nodes):
        left_child_node = nodes[0]
        left_child_node.label = 0
        right_child_node = nodes[1]
        right_child_node.label = 1
        subtree_root_value = left_child_node.value + right_child_node.value
        subtree_root = Node(value=subtree_root_value, left_child_node=left_child_node,
                            right_child_node=right_child_node)
        return subtree_root

    def void_translevel(self, root):
        if root is None:
            print '树为空，结束'
            return None
        queue = [root]
        while len(queue):
            current_node = queue.pop(0)
            print current_node.key, current_node.value, current_node.label
            if current_node.left_child_node is not None:
                queue.append(current_node.left_child_node)
            if current_node.right_child_node is not None:
                queue.append(current_node.right_child_node)

    def preorder_traversal(self, node):
        if node is None:
            return

        print str(node.value) + ':' + str(node.label),
        self.preorder_traversal(node.left_child_node)
        self.preorder_traversal(node.right_child_node)

    # 广度优先搜索，但不是最短路径
    def search_node_key(self, key, root):
        if root is None:
            print '树为空！'
            return
        queue = [root]
        search_path = []
        while True:
            current_node = queue.pop(0)
            search_path.append(current_node)
            # 遇到相同的key，跳出
            if current_node.key == key:
                break
            if current_node.left_child_node is not None:
                queue.append(current_node.left_child_node)
            if current_node.right_child_node is not None:
                queue.append(current_node.right_child_node)

        return search_path

    # 最短路径
    def search_nearest_path_func(self, search_path):
        # 此时search_path 并不是最短路径
        if len(search_path) == 1:
            # 就是根节点，那只能返回-1，又不是左节点，也不是右节点
            return [-1]
        # 被要求找的key所在node肯定是在search_path的最后一个
        # 直接提出，剩下其他路径
        be_found_key_node = search_path.pop(-1)
        key_node = be_found_key_node
        # 反转
        # search_path.reverse()
        search_nearest_path = []
        while len(search_path):
            current_node = search_path.pop()
            # print '========================='
            # print current_node.left_child_node
            # print current_node.right_child_node
            if id(current_node.left_child_node) == id(be_found_key_node):
                # print 'hello'
                be_found_key_node = current_node
                search_nearest_path.append(current_node)
            elif id(current_node.right_child_node) == id(be_found_key_node):
                # print 'world'
                be_found_key_node = current_node
                search_nearest_path.append(current_node)

        search_nearest_path.reverse()
        search_nearest_path.append(key_node)
        # search_path.reverse()
        return search_nearest_path

    def get_label(self, search_nearest_path):
        if len(search_nearest_path) == 1:
            # 长度为1，还能如何？第一个肯定是它
            return [-1]
        label = []
        for node in search_nearest_path:
            if node.label is not None:
                label.append(node.label)
        return label


def get_two_smallest_nodes(node_space):
    if node_space is None or len(node_space) == 0:
        print '无节点，为空树'
        return None, None
    if len(node_space) == 1:
        print '哈夫曼树构建成功！'
        return None, node_space

    return node_space[:2], node_space[2:]


if __name__ == "__main__":
    node_space_dict = {'a': 2, 'b': 3, 'c': 7, 'd': 4, 'e': 10, 'f': 2, 'h': 5}
    print '字符：权值 组：'
    print node_space_dict
    node_space = []
    for key, value in node_space_dict.items():
        node_space.append(Node(key=key, value=value))

    if node_space is None:
        print '字符：权值为空'
        sys.exit(0)
    huffman_encoding = Huffman_Encoding()

    while True:
        node_space.sort(key=lambda x: x.value)
        two_smallest_nodes, node_space = get_two_smallest_nodes(node_space)

        if two_smallest_nodes is None and node_space is not None:
            root = node_space[0]
            break

        subtree_node = huffman_encoding.generate_subtree(two_smallest_nodes)
        node_space.append(subtree_node)

    print '\n构造的哈夫曼树为：'
    print '广度优先遍历：'
    huffman_encoding.void_translevel(root)
    print '\n先序遍历'
    huffman_encoding.preorder_traversal(root)
    print '\n'

    for key in node_space_dict.keys():
        print 'key %s 对应编码为 ： ' % str(key)
        search_path = huffman_encoding.search_node_key(key, root)
        for item in search_path:
            print str(item.value) + ':' + str(item.label),
        # for item in search_path:
        #     print item.value,


        print '\n最近路径为：'
        search_nearest_path = huffman_encoding.search_nearest_path_func(search_path)
        label = huffman_encoding.get_label(search_nearest_path)
        for item in search_nearest_path:
            print str(item.value) + ';',
        print '\nlabel 为 ' + str(label)


        print '\n'
