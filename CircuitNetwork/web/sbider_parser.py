"""
Subtitle

Descriptive paragraph

******************************************************************************
@author: Huwate(Kwat) Yeerna, University of California, San Diego
******************************************************************************
"""

import helper
import sbider_database as db


def grammar_0(cursor, tokens):
    """
    Grammar for 'grammar_0:= grammar_1 > grammar_1'.

    Argument(s):
        tokens - description

    Return:
        return description
    """

    if '=' not in tokens:
        raise ValueError("grammar_0(tokens): no output")

    else:
        input_output_dictionary = helper.split_by(tokens, '=')

    return grammar_output(grammar_1(cursor, input_output_dictionary[0]), grammar_1(cursor, input_output_dictionary[1]))


def grammar_1(cursor, tokens):
    """
    Grammar for 'grammar_1:= grammar_2 or grammar_1 |
    grammar_2 and grammar_1 |
    grammar_2'.

    Argument(s):
        tokens - description

    Return:
        return description
    """

    if len(tokens) > 1 and tokens[1] == 'or':
        # grammar_2 or grammar_1
        # split tokens by the first occurring 'or' and store the tokens before
        # and after the 'or' in a dictionary
        or_dictionary = helper.split_by(tokens, 'or')
        return grammar_or(grammar_2(cursor, or_dictionary.get(0)), grammar_1(cursor, or_dictionary.get(1)))

    elif len(tokens) > 1 and tokens[1] == 'and':
        # grammar_2 and grammar_1
        # split tokens by the first occurring 'and' and store the tokens
        # before and after the 'and' in a dictionary
        and_dictionary = helper.split_by(tokens, 'and')
        return grammar_and(grammar_2(cursor, and_dictionary.get(0)), grammar_1(cursor, and_dictionary.get(1)))

    else:
        # grammar_2
        return grammar_2(cursor, tokens)


def grammar_2(cursor, tokens):
    """
    Grammar for 'grammar_2:= (grammar_1) or grammar_1 |
    (grammar_1) and grammar_1 |
    (grammar_1) |
    interactor'.

    Argument(s):
        tokens - description

    Return:
        return description
    """

    if len(tokens) <= 0:
        raise ValueError("Invalid Syntax")

    elif tokens[0] == "(":
        # (grammar_1) or grammar_1 | (grammar_1) and grammar_1| (grammar_1)

        # token after the last occurring ')'
        token_after_last_closer = helper.remove_parentheses(tokens)

        if token_after_last_closer == 'or':
            # split tokens by the first occurring 'or' and store the tokens
            # before and after the 'or' in a dictionary

            or_dictionary = helper.split_by(tokens, 'or')
            return grammar_or(grammar_1(cursor, or_dictionary.get(0)), grammar_1(cursor, or_dictionary.get(1)))

        elif token_after_last_closer == 'and':
            # split tokens by the first occurring 'and' and store the tokens
            # before and after the 'and' in a dictionary

            and_dictionary = helper.split_by(tokens, 'and')
            return grammar_and(grammar_1(and_dictionary.get(0)), grammar_1(and_dictionary.get(1)))

        else:
            # grammar_1; delegate to grammar_1
            return grammar_1(cursor, tokens)

    else:
        # interactor; delegate to interactor
        return interactor(cursor, tokens)


def interactor(cursor, token):
    """Grammar for 'interactor'.

    Argument(s):
        tokens - description

    Return:
        return description
    """

    species = token[0]
    return [[db.db_get_species_id_from_name(cursor, species)]]


def grammar_output(tokens1, tokens2):
    """
    Grammar for '>'.

    Argument(s):
        tokens1 - description
        tokens2 - description


    Return:
        return description
    """

    grammar_output_dict = {}

    for token1 in tokens1:
        grammar_output_dict[tuple(token1)] = tuple(tokens2)

    return grammar_output_dict


def grammar_or(tokens1, tokens2):
    """Grammar for 'or'.

    Argument(s):
        tokens1 - description
        tokens2 - description

    Return:
        return description
    """

    return tokens1 + tokens2


def grammar_and(tokens1, tokens2):
    """Grammar for 'and'.

    Argument(s):
        tokens1 - description
        tokens2 - description

    Return:
        return description
    """

    grammar_and_output = []

    for token1 in tokens1:
        for token2 in tokens2:
            grammar_and_output.append(helper.uniquely_merge_list_of_lists([token1, token2]))

    return grammar_and_output


def parse_logic(cursor, logic_input):
    """Parse a logic input into atomized and equivalent logic.

    Argument(s):
        logic - description

    Return:
        return description
    """

    split_logic_input = logic_input.split()

    # begins recursive logic parse
    return grammar_0(cursor, split_logic_input)


# End of sbider_parser.py
