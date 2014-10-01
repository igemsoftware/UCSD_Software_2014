"""
Subtitle

Descriptive paragraph

******************************************************************************
@author: Huwate(Kwat) Yeerna, University of California, San Diego
******************************************************************************
"""

import itertools as it
import math


def remove_duplicates_within_list(lst):
    seen = set()
    seen_add = seen.add
    return [x for x in lst if not (x in seen or seen_add(x))]


def list_is_type(lst, typ):
    if type(lst) != list:
        raise TypeError("list_is_type(lst, typ): lst is not a list")
    elif len(lst) <= 0:
        raise ValueError("list_is_type(lst, typ): lst is empty")
    return all(isinstance(x, typ) for x in lst)


def remove_duplicated_lists_within_a_list_of_lists(list_of_lists):
    if type(list_of_lists) == list and len(list_of_lists) > 0 and list_is_type(list_of_lists, list):
        list_of_lists.sort()
        trimmed = list(list_of_lists for list_of_lists, _ in it.groupby(list_of_lists))
        return trimmed
    else:
        raise TypeError("remove_duplicated_lists_within_a_list_of_lists(list_of_lists): list_of_lists should be in the form: [[],[],... ]")


def uniquely_merge_list_of_lists(list_of_lists):
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


def uniquely_merge_multi_dimensional_list_of_lists(multi_dimentional_list_of_lists):
    final_merged_list = uniquely_merge_list_of_lists(multi_dimentional_list_of_lists)
    if type(final_merged_list) == list and len(final_merged_list) > 0 and list_is_type(final_merged_list, list):
        return uniquely_merge_multi_dimensional_list_of_lists(final_merged_list)
    else:
        return final_merged_list


def elements_match(list_of_lists, lst):
    return set(lst).issubset(uniquely_merge_multi_dimensional_list_of_lists(list_of_lists))


def get_matching_list(list_of_lists, lst):
    if type(lst) != list:
        raise TypeError("get_matching_list(list_of_lists, lst): lst is not a list object")
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
    matched_inp_spe, matched_inp_idx = get_matching_list(list_of_lists, lst)
    if len(matched_inp_spe) > 0:
        return True, matched_inp_idx
    else:
        return False, []


def activated(inp_dic, rep_dic, ope, spe_list):
    inp_trans = inp_dic[ope]
    is_activated, activated_inp_idx_list = match_any_list(inp_trans, spe_list)
    rep_inp_trans = rep_dic[ope]
    rep = []
    for activated_inp_idx in activated_inp_idx_list:
        rep.extend(rep_inp_trans[activated_inp_idx])
    if is_activated:
        return True, rep
    else:
        return False, rep


def reverse_index(sequence, element):
    for i, e in enumerate(reversed(sequence)):
        if element == e:
            return len(sequence) - 1 - i
    else:
        raise ValueError("r_index(sequence, element): element not in the sequence")


def remove_parentheses(sequence):
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
    element_index = sequence.index(element)
    sequence_before_element = sequence[:element_index:1]
    sequence_after_element = sequence[element_index + 1::1]
    return {0: sequence_before_element, 1: sequence_after_element}


def format_values(value_list):
    formatted_value_list = []
    for value in value_list:
        if isinstance(value, unicode):
            formatted_value_list.append(str(value))
        elif math.isnan(value):
            formatted_value_list.append("na")
        else:
            formatted_value_list.append(value)
    return formatted_value_list



# End of helper.py