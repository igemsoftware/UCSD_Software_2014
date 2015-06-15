"""
SBiDer helper functions

******************************************************************************
@author: Huwate(Kwat) Yeerna(Ernar), University of California, San Diego
******************************************************************************
"""


import itertools as it
import math


def remove_duplicates_within_list(lst):
    """
    Create a list with only unique elements form another list.
    
    :param lst: list whose unique elements will be stored in a new list.
    :return: a list that contains non-duplicated elements from the parameter list.
    """
    
    seen = set()
    seen_add = seen.add
    return [x for x in lst if not (x in seen or seen_add(x))]


def list_is_type(lst, typ):
    """
    Check if all elements of a list are the specified type.
    
    :param lst: list whose elements are checked.
    :param typ: type specified.
    :return: True only if all elements of the list is the specified type, False otherwise.
    """
    
    if type(lst) != list:
        raise TypeError("list_is_type(lst, typ): lst is not a list")
    elif len(lst) <= 0:
        raise ValueError("list_is_type(lst, typ): lst is empty")
    return all(isinstance(x, typ) for x in lst)


def remove_duplicated_lists_within_a_list_of_lists(list_of_lists):
    """
    Create a list that contains unique lists within another list.
    
    :param list_of_lists: list that contains duplicated lists.
    :return: list that contains unique lists from the list.
    """
    
    if type(list_of_lists) == list and len(list_of_lists) > 0 and list_is_type(list_of_lists, list):
        list_of_lists.sort()
        trimmed = list(list_of_lists for list_of_lists, _ in it.groupby(list_of_lists))
        return trimmed
    else:
        raise TypeError(
            "remove_duplicated_lists_within_a_list_of_lists(list_of_lists): list_of_lists should be in the form: [[],[],... ]")


def uniquely_merge_list_of_lists(list_of_lists):
    """
    Create a list that contain unique elements from lists within itself.
    
    :param list_of_lists: list that contains lists
    :return: list that contains unique elements from lists within the list.
    """
    
    if type(list_of_lists) == list and len(list_of_lists) > 0:
        if list_is_type(list_of_lists, list):
            remove_duplicated_lists_within_a_list_of_lists(list_of_lists)
            merged_list = list(list_of_lists[0])
            for a_list in list_of_lists[1::]:
                for e in a_list:
                    if e not in merged_list:
                        merged_list.append(e)
            return merged_list
        else:
            return list(list_of_lists)
    else:
        return list_of_lists


def uniquely_merge_multi_dimensional_list_of_lists(multi_dimensional_list_of_lists):
    """
    Create a list that contain unique elements from lists within itself.
    
    :param multi_dimensional_list_of_lists: list that contains lists
    :return: list that contains unique elements from lists within the list.
    """
    
    final_merged_list = uniquely_merge_list_of_lists(multi_dimensional_list_of_lists)
    if type(final_merged_list) == list and len(final_merged_list) > 0 and list_is_type(final_merged_list, list):
        return uniquely_merge_multi_dimensional_list_of_lists(final_merged_list)
    else:
        return final_merged_list


def contain_all_elements(list_of_lists, lst):
    """
    Check if a list that matches the specified list.
    
    :param list_of_lists: list whose inner lists are checked.
    :param lst: list matched
    :return: True only if the list_of_lists contain a list that matches lst.
    """
    
    if type(lst) != list:
        raise TypeError("contain_all_elements(list_of_lists, lst): lst must be a list")
    return set(lst).issubset(uniquely_merge_multi_dimensional_list_of_lists(list_of_lists))


def contain_an_element(lst1, lst2):
    """
    Check if at least on of the elements is a list is in another list.
    
    :param lst1: list that may contain at least one element from anther list.
    :param lst2: list whose elements are searched for in another list.
    :return: True only if at least an element from lst2 in found in lst1.
    """
    
    if type(lst1) != list or type(lst2) != list:
        raise TypeError("contain_an_element(lst1, lst2): lst1 and lst2 must be lists")
    for e in lst2:
        if e in lst1:
            return True
    return False


def get_matching_list_and_index(list_of_lists, lst):
    """
    Get a matching list within a list of lists that matches a specified list.
    
    :param list_of_lists: list whose inner lists are checked to see if any of them match the specified list.
    :param lst: list checked.
    :return: list within list_of_lists that matches the specified list.
    """
    
    if type(lst) != list:
        raise TypeError("get_matching_list(list_of_lists, lst): lst is not a list")
    elif type(list_of_lists) == list and len(list_of_lists) > 0 and list_is_type(list_of_lists, list):
        matching_list = []
        matching_list_idx = []
        for idx, a_list in enumerate(list_of_lists):
            if all([x in lst for x in a_list]):
                matching_list.append(a_list)
                matching_list_idx.append(idx)
        return matching_list, matching_list_idx
    else:
        raise TypeError("get_matching_list(list_of_lists, lst): list_of_lists should be in the form: [[],[],... ]")


def match_any_list(list_of_lists, lst):
    """
    Check if a list matches any of the lists within a list of lists.
    
    :param list_of_lists: list of lists that contain potential matching lists.
    :param lst: list matched.
    :return: True only is at least a list within the list of lists matches the specified list.
    """
    
    matched_inp_spe = get_matching_list_and_index(list_of_lists, lst)[0]
    if len(matched_inp_spe) > 0:
        return True
    else:
        return False


def activated(inp_dic, ope, spe):
    """
    Check if there is an activation signal for an operon.
    
    :param inp_dic: dictionary of operon and their activation requirement.
    :param ope: operon whose activation signal is checked.
    :param spe: species that may induce activation signal for the operon.
    :return: True only if species match any of the activation requirement of an operon, False otherwise.
    """
    
    inp_trans_req = inp_dic[ope]
    return match_any_list(inp_trans_req, spe)


def repressed(rep_dic, ope, spe):
    """
    Check if there is an repression signal for an operon.
    
    :param rep_dic: dictionary of operon and their repression requirement.
    :param ope: operon whose repression signal is checked.
    :param spe: species that may induce repression signal for the operon.
    :return: True only if species match any of the repression requirement of an operon, False otherwise.
    """
    
    rep = uniquely_merge_multi_dimensional_list_of_lists(rep_dic[ope])
    return contain_an_element(spe, rep)


def promoter_activation(inp_dic, rep_dic, ope, spe, memory_spe, indirect_flag):
    """
    Check if a promoter is activated.
    
    :param inp_dic: dictionary of operon and their activation requirement.
    :param rep_dic: dictionary of operon and their repression requirement.
    :param ope: operon whose activation is checked.
    :param spe: species that can activate or repress an operon.
    :param memory_spe: species that can activate or repress an operon.
    :param indirect_flag: Boolean flag for checking indirect activation of an operon
    :return: True if the operon is activated.
    """

    all_spe = spe + memory_spe

    if indirect_flag:
        activation = activated(inp_dic, ope, all_spe)
    else:
        activation = activated(inp_dic, ope, spe)

    repression = repressed(rep_dic, ope, all_spe)

    promoter_activated = activation and not repression

    return promoter_activated


def reverse_index(sequence, element):
    """
    Find the last occurring index of an element in a sequence.
    
    :param sequence: list checked.
    :param element: element searched.
    :return: index of the last occurring index of an element.
    """
    
    for i, e in enumerate(reversed(sequence)):
        if element == e:
            return len(sequence) - 1 - i
    else:
        raise ValueError("r_index(sequence, element): element not in the sequence")


def remove_parentheses(sequence):
    """
    Remove the outermost parentheses of a string, and return the element right after the closing parentheses.
    
    :param sequence:
    :return:
    """
    
    first_opener_idx_assigned = False
    started = False
    counter = 0
    for idx, e in enumerate(sequence):
        if e == '(':
            if not started:
                started = True
            counter += 1
        elif e == ')':
            if not started:
                raise ValueError("remove_parentheses(sequence): ')' without '('")
            counter -= 1
        if started:
            if not first_opener_idx_assigned:
                first_opener_idx = idx
                first_opener_idx_assigned = True
            if counter == 0:
                sequence.pop(idx)

                if idx < len(sequence):
                    element_after_last_closer = sequence[idx]
                else:
                    element_after_last_closer = None
                sequence.pop(first_opener_idx)
                return element_after_last_closer
    else:
        raise ValueError("remove_parentheses(sequence): sequence is empty")


def split_by(sequence, element):
    """
    Split a sequence by the first occurring index of a specified element,
    and return the the resulting two-halves of the sequence in a dictionary.
    
    :param sequence: sequence that is split.
    :param element: element whose first occurring index splits the sequence.
    :return: dictionary that contains the split two halves of the sequence.
    """
    
    element_index = sequence.index(element)
    sequence_before_element = sequence[:element_index:1]
    sequence_after_element = sequence[element_index + 1::1]
    return {0: sequence_before_element, 1: sequence_after_element}


def format_values(value_list):
    """
    Create a list by adding elements of a list in a standard expression.
    
    :param value_list: list whose elements with non-standard expression are reformatted and added to the new list.
    :return: a new list with elements in standard expression.
    """
    
    formatted_value_list = []
    for value in value_list:
        if isinstance(value, unicode):
            formatted_value_list.append(str(value))
        elif math.isnan(value):
            formatted_value_list.append("na")
        else:
            formatted_value_list.append(value)
    return formatted_value_list


def printplus(obj):
    """
    Pretty-prints the object passed in.
    """
    
    # Dict
    if isinstance(obj, dict):
        for k, v in sorted(obj.items()):
            print(u'{0}: {1}'.format(k, v))

    # List or tuple
    elif isinstance(obj, list) or isinstance(obj, tuple):
        for x in obj:
            print(x)

    # Other
    else:
        print(obj)


# End of SBiDer_helper.py