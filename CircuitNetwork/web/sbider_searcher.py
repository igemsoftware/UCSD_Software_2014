"""
Subtitle

Descriptive paragraph

******************************************************************************
@author: Huwate(Kwat) Yeerna, University of California, San Diego
         Joaquin Reina, University of California, San Diego
******************************************************************************
"""

import helper
import node as node


def search_sbider_path_memory(input_dictionary, activated_paths, from_operon):
    activated_ope_dic = {}
    activated_spe_dic = {}
    for path_idx, ope_spe_path in enumerate(activated_paths):
        activated_ope_dic[path_idx] = ope_spe_path[0]
        activated_spe_dic[path_idx] = ope_spe_path[1]
    final_operon_requirement = input_dictionary[from_operon]
    activating_ope_list = []
    for path_idx, spe_produced in activated_spe_dic.items():
        for a_spe_produced in spe_produced:
            for and_spe_required in final_operon_requirement:
                if a_spe_produced in and_spe_required:
                    activating_ope_list.extend(activated_ope_dic.get(path_idx))
    return activating_ope_list


def build_sbider_path_memory_tree(input_dictionary, activated_paths, start_operon):
    root_ope = node.Node(start_operon)
    temp_queue_ope = [root_ope]
    temp_memory = []
    while len(activated_paths) > 0 and len(temp_queue_ope) > 0:
        from_node = temp_queue_ope.pop(0)
        from_operon = from_node.value
        children_operon = search_sbider_path_memory(input_dictionary, activated_paths, from_operon)
        if len(children_operon) > 0:
            for child_operon in children_operon:
                if child_operon not in temp_memory:
                    child_node = node.Node(child_operon)
                    from_node.append_child(child_node)
                    temp_queue_ope.append(child_node)
                    temp_memory.append(child_operon)
    return root_ope.get_path_from_all_leaf()


def build_indirect_sbider_path(input_dictionary,
                               repressor_dictionary,
                               output_dictionary,
                               input_species_list,
                               output_species_list,
                               path_queue,
                               final_operon_path_list,
                               memory_operon,
                               memory_species,
                               activated_paths):
    temp_memory_species = []
    for an_operon in set(input_dictionary.keys()) - set(memory_operon):

        if helper.promoter_activation(input_dictionary, repressor_dictionary, an_operon, [], memory_species, True):

            just_produced_species = output_dictionary[an_operon]
            just_produced_unique_species = helper.uniquely_merge_multi_dimensional_list_of_lists(just_produced_species)

            if helper.match_any_list(just_produced_species, output_species_list):

                if len(activated_paths) > 1:
                    ope_path_backward = build_sbider_path_memory_tree(input_dictionary,
                                                                      activated_paths,
                                                                      an_operon)
                    final_operon_path_list.extend(ope_path_backward)
            else:
                if an_operon not in memory_operon:
                    path_queue.append(([an_operon], just_produced_unique_species))
                    memory_operon.append(an_operon)
                    memory_operon = helper.remove_duplicates_within_list(memory_operon)
                    temp_memory_species.extend(just_produced_unique_species)
                    activated_paths.append([[an_operon], just_produced_unique_species])

    memory_species.extend(temp_memory_species)
    memory_species = helper.remove_duplicates_within_list(memory_species)

    if len(path_queue) > 0:
        build_direct_sbider_path(input_dictionary,
                                 repressor_dictionary,
                                 output_dictionary,
                                 input_species_list,
                                 output_species_list,
                                 path_queue,
                                 final_operon_path_list,
                                 memory_operon,
                                 memory_species,
                                 activated_paths,
                                 True)


def build_direct_sbider_path(input_dictionary,
                             repressor_dictionary,
                             output_dictionary,
                             input_species_list,
                             output_species_list,
                             path_queue,
                             final_operon_path_list,
                             memory_operon,
                             memory_species,
                             activated_paths,
                             indirect_flag):
    while len(path_queue) != 0:

        (previously_visited_operon_list, just_previously_produced_species_list) = path_queue.pop(0)

        for an_operon in set(input_dictionary.keys()) - set(
                helper.uniquely_merge_multi_dimensional_list_of_lists(previously_visited_operon_list)):
            if an_operon not in memory_operon:


                if helper.promoter_activation(input_dictionary, repressor_dictionary, an_operon,
                                              just_previously_produced_species_list, memory_species, False):

                    visited_operon_list = previously_visited_operon_list + [an_operon]
                    just_produced_species = output_dictionary[an_operon]
                    just_produced_unique_species = helper.uniquely_merge_multi_dimensional_list_of_lists(
                        just_produced_species)

                    if helper.match_any_list(just_produced_species, output_species_list):

                        if not indirect_flag:
                            final_operon_path_list.append(visited_operon_list)
                    else:
                        path_queue.append((visited_operon_list, just_produced_unique_species))
                        memory_operon.append(an_operon)
                        memory_operon = helper.remove_duplicates_within_list(memory_operon)
                        memory_species.extend(just_produced_unique_species)
                        memory_species = helper.remove_duplicates_within_list(memory_species)

                    activated_paths.append([[an_operon], just_produced_unique_species])

    if indirect_flag:
        build_indirect_sbider_path(input_dictionary,
                                   repressor_dictionary,
                                   output_dictionary,
                                   input_species_list,
                                   output_species_list,
                                   path_queue,
                                   final_operon_path_list,
                                   memory_operon,
                                   memory_species,
                                   activated_paths)
    return final_operon_path_list


def get_sbider_path(inp_dic,
                    rep_dic,
                    outp_dic,
                    inp_spe,
                    outp_spe,
                    indirect_flag=False):
    final_ope_path = []
    path_queue = [([], inp_spe)]
    memory_ope = []
    memory_spe = []
    memory_spe.extend(inp_spe)
    activated_paths = []
    build_direct_sbider_path(inp_dic,
                             rep_dic,
                             outp_dic,
                             inp_spe,
                             outp_spe,
                             path_queue,
                             final_ope_path,
                             memory_ope,
                             memory_spe,
                             activated_paths,
                             indirect_flag)
    if len(final_ope_path) > 0:
        final_ope_path = helper.remove_duplicated_lists_within_a_list_of_lists(final_ope_path)

    return final_ope_path


# End of sbider_searcher.py
