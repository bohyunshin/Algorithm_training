from math import ceil, log2

class SegmentationTree():
    def __init__(self, input_list):
        self._input_list = input_list[:]
        self._init_tree()
        self._is_propagated = True

    def _init_tree(self):
        ### CREATE SEGMENTATION TREE INFRASTRUCTURE

        # lenght of list
        self._n = len(self._input_list)
        # calc. height
        height = ceil(log2(self._n))
        # calc. number of nodes
        n_nodes = 2 * (2**height) - 1
        # create empty seg_tree_list
        self._seg_tree = [None] * n_nodes

        ### FILL IN SEGMENTATION TREE
        # propagate seg_tree_list
        arr_left = 0
        arr_right = self._n-1
        seg_node_index = 0
        self._propagate(arr_left, arr_right, seg_node_index)

    def _propagate(self, arr_left, arr_right, seg_node_index):
        # recursive implementation
        # Base cases
        if arr_left > arr_right: # went too far
            return
        if arr_left == arr_right: # when honed into target index
            # grab value from input list
            value = self._input_list[arr_left]
            # assign value into seg_tree at correct index
            self._seg_tree[seg_node_index] = value
            return

        # Recursive call = we're at a parent node
        mid = (arr_left + arr_right) // 2

        # left side
        left_seg_node_index = seg_node_index * 2 + 1
        left_node_arr_left = arr_left
        left_node_arr_right = mid
        self._propagate(left_node_arr_left,left_node_arr_right,left_seg_node_index)

        # right side
        right_seg_node_index = seg_node_index * 2 + 2
        right_node_arr_left = mid+1 # might go over
        right_node_arr_right = arr_right
        self._propagate(right_node_arr_left, right_node_arr_right, right_seg_node_index)

        # handle parent
        left_val = self._seg_tree[left_seg_node_index]
        right_val = self._seg_tree[right_seg_node_index]
        self._seg_tree[seg_node_index] = left_val + right_val # aggregation = sum

    def query(self, query_left, query_right):
        arr_left = 0
        arr_right = self._n - 1
        seg_node_index = 0

        # if not yet propagate, propagate before query
        # propagate if internal list changed
        if not self._is_propagated:
            self._propagate(arr_left, arr_right, seg_node_index)

        # start searching from root node
        return self._query_helper(query_left, query_right, arr_left, arr_right, seg_node_index)


    def _query_helper(self, query_left, query_right, arr_left, arr_right, seg_node_index):
        # recursive implementation
        # Base cases
        if arr_left > arr_right: # went too far
            return 0

        if query_right < arr_left or query_left > arr_right: # node is outside of query range
            return 0

        if query_left <= arr_left and arr_right <= query_right: # current node completely within query range
            return self._seg_tree[seg_node_index]

        # Recursive call = means we're at a parent that is partially covering query
        mid = (arr_left + arr_right) // 2

        # left side
        left_seg_node_index = seg_node_index * 2 + 1
        left_node_arr_left = arr_left
        left_node_arr_right = mid
        left_val = self._query_helper(query_left, query_right, left_node_arr_left,left_node_arr_right,left_seg_node_index)

        # right side
        right_seg_node_index = seg_node_index * 2 + 2
        right_node_arr_left = mid+1 # might go over
        right_node_arr_right = arr_right
        right_val = self._query_helper(query_left, query_right, right_node_arr_left, right_node_arr_right, right_seg_node_index)

        # handle parent
        return left_val + right_val # aggregation = sum

    def update(self, arr_index, new_value):
        # lazy update -> because we're not propagating until
        # we're truely ready to do so
        old_value = self._input_list[arr_index]
        if old_value != new_value:
            self._input_list[arr_index] = new_value
            self._is_propagated = False

nums = [1,3,5]
st = SegmentationTree(nums)
assert st.query(0,2) == 9
st.update(1,2)
assert st.query(0,2) == 8


nums_2 = [3,4,10,2,7]
st_2 = SegmentationTree(nums_2)
print(st_2._seg_tree)