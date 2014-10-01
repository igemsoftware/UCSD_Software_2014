"""
Subtitle

Descriptive paragraph

******************************************************************************
@author: Huwate(Kwat) Yeerna, University of California, San Diego
******************************************************************************
"""

import helper


class Node(object):
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.value) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

    def append_child(self, obj):
        children_values = []
        for child in self.children:
            children_values.append(child.value)
        obj_value = obj.value
        if obj_value not in children_values:
            self.children.append(obj)
            if type(obj) == Node:
                obj.parent = self

    def get_all_leaf(self):
        leaf_list = []
        if len(self.children) > 0:
            for child_node in self.children:
                leaf_list.extend(child_node.get_all_leaf())
            leaf_list = helper.uniquely_merge_multi_dimensional_list_of_lists(leaf_list)
            return leaf_list
        return [self]

    def get_path_from_all_leaf(self):
        path_list = []
        leaf_list = self.get_all_leaf()

        if len(leaf_list) == 1 and self in leaf_list:
            path_list.append([self.value])
            return path_list

        elif len(leaf_list) > 0:
            for leaf in leaf_list:
                path = [leaf.value]
                pointer_node = leaf
                while pointer_node.parent != self:
                    path.append(pointer_node.parent.value)
                    pointer_node = pointer_node.parent
                path.append(self.value)
                path_list.append(path)
            return path_list
        else:
            return []