# -*- coding: utf-8 -*-
# @Time    : 2018/4/16 16:12
# @Author  : affectalways
# @Site    : 
# @Contact : affectalways@gmail.com
# @File    : heap.py
# @Software: PyCharm

# 堆，该代码创建最小堆
# 用 是一种特殊的完全二叉树
class Heap(object):
    def __init__(self):
        pass

    # 创建堆, 这个方法要在完全二叉树 广度优先遍历后 才能使用
    def create_heap(self, original_heap):
        original_heap_len = len(original_heap)
        # 叶子节点不需要处理，直接跳过
        for i in range((original_heap_len - 1) / 2, -1, -1):
            self.downward_adjustment(original_heap, i)
        # 返回创建的堆
        return original_heap
        # for item in original_heap:
        #     print item.value,

    # 交换节点的值
    def swap_value(self, original_heap, i, j):
        original_heap[i].value, original_heap[j].value = original_heap[j].value, original_heap[i].value

    # 向下调整
    def downward_adjustment(self, original_heap, i):
        # 利用完全二叉树的节点的下标， 若2*i+1<=n节点的左子节点下标为2*n+1，若2*i+2《=n右子节点下标2*n+2,n为长度
        original_heap_len = len(original_heap)
        while (2 * i + 1) < original_heap_len:
            # 先判断父节点与左子节点的value
            # print '此时 为 ' + str(original_heap[i])
            # print '左子节点为 ' + str(original_heap[2 * i + 1])
            if original_heap[i].value > original_heap[2 * i + 1].value:
                # print original_heap[i], original_heap[2 * i + 1]
                index = 2 * i + 1
            else:
                index = i
            # 查看有无右子节点
            if (2 * i + 2) < original_heap_len:
                # print '右子节点为：' + str(original_heap[2 * i + 2])
                # 若右子节点更小，
                if original_heap[index].value > original_heap[2 * i + 2].value:
                    index = 2 * i + 2
            # 若最小节点不是自己的，说明子节点中有比父节点更小的，交换
            if index != i:
                self.swap_value(original_heap, i, index)
                # 更新i为刚才与他交换的儿子节点的编号，以便继续向下调整
                # print '交换位置为 ' + str(i) + ' ' + str(index)
                # print '交换value 为 ' + str(original_heap[i]) + '  ' + str(original_heap[index])
                # print '\n'
                i = index
            else:
                break

    # 堆排序,这需要在最小堆创建之后执行
    # 由排序过程可见，若想得到升序（由小到大），则建立大顶堆，若想得到降序(由大到小)，则建立小顶堆。
    def heap_sort(self, heap):
        heap_len = len(heap) - 1
        # 将根节点放到最终位置，剩余无序序列继续堆排序
        while heap_len > 0:
            heap[0].value, heap[heap_len].value = heap[heap_len].value, heap[0].value
            self.downward_adjustment(heap[:heap_len], 0)
            heap_len -= 1
        return heap


class Node(object):
    def __init__(self, value, left_child_node=None, right_child_node=None):
        self.value = value
        self.left_child_node = left_child_node
        self.right_child_node = right_child_node

    def __str__(self):
        return str(self.value)


# 完全二叉树
class CompleteBinaryTree(object):
    RESULT = []

    # 用队列记录树的节点，先进先出
    def __init__(self, node=None):
        self.root = node

    def get_root(self):
        return self.root

    def add_node(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return
        tmp_list = [self.root]
        while tmp_list:
            current_node = tmp_list.pop(0)
            if current_node.left_child_node is not None:
                tmp_list.append(current_node.left_child_node)
            else:
                current_node.left_child_node = node
                return
            if current_node.right_child_node is not None:
                tmp_list.append(current_node.right_child_node)
            else:
                current_node.right_child_node = node
                return

    @classmethod
    def initialize_result(cls):
        cls.RESULT = []

    # 深度优先搜索（先序，后序，中序）
    # 先序
    @classmethod
    def preorder_traversal(cls, node):
        if node is None:
            return
        cls.RESULT.append(node)
        # print node.value,
        cls.preorder_traversal(node.left_child_node)
        cls.preorder_traversal(node.right_child_node)

    # 中序
    @classmethod
    def inorder_traversal(cls, node):
        if node is None:
            return
        cls.inorder_traversal(node.left_child_node)
        print node.value,
        cls.inorder_traversal(node.right_child_node)

    @classmethod
    def postorder_traversal(cls, node):
        if node is None:
            return
        cls.postorder_traversal(node.left_child_node)
        cls.postorder_traversal(node.right_child_node)
        print node.value,

    # 广度优先搜索
    # 其实也就是层次遍历
    @classmethod
    def void_translevel(self, node):
        ORIGINAL_HEAP = []
        if node is None:
            print '树为空'
            return
        queue = []
        queue.append(node)
        while len(queue):
            current_node = queue.pop(0)
            # 添加进ORIGINAL_HEAP
            ORIGINAL_HEAP.append(current_node)
            print current_node.value,
            if current_node.left_child_node is not None:
                queue.append(current_node.left_child_node)
            if current_node.right_child_node is not None:
                queue.append(current_node.right_child_node)
        return ORIGINAL_HEAP


if __name__ == "__main__":
    prime_list = [99, 5, 36, 7, 22, 17, 92, 12, 2, 19, 25, 28, 1, 46]
    complete_binary_tree = CompleteBinaryTree()
    flag = 0
    print '初始完全二叉树为：'
    for value in prime_list:
        complete_binary_tree.add_node(value)
    root = complete_binary_tree.get_root()
    # complete_binary_tree.preorder_traversal(root)
    original_heap = complete_binary_tree.void_translevel(root)
    print '\n'
    # for item in original_heap:
    #     print item.value,

    heap = Heap()
    created_heap = heap.create_heap(original_heap=original_heap)
    print '生成的最小堆：'
    for node in created_heap:
        print node.value,
    print '\n'
    print '堆排序：'
    sorted_heap = heap.heap_sort(created_heap)
    for item in sorted_heap:
        print item.value,


# heap.downward_adjustment()
