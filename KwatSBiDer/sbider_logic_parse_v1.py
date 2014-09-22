"""Subtitle

Descriptive paragraph

******************************************************************************
@author: Huwate Yeerna, University of California, San Diego
******************************************************************************
"""



import sys



def r_index(sequence, element):
    """Find the last index of an element in a sequence.

    Argument(s):
        sequence - description
        element - descripttion

    Return:
        return description
    """

    for i, e in enumerate(reversed(sequence)):
        if element == e:
            return len(sequence) - 1 - i
        else:
            raise ValueError("r_index(sequence, element):\
                    element not in the sequence")



def remove_parentheses(sequence):
    """Remove the outer most parentheses '()' and return the token after the
    ')'.

    Argument(s):
        sequence - description

    Return:
        return description
    """

    first_opener_idx_assigned = False
    started = False
    counter = 0

    for idx, e in enumerate(sequence):
        if e == '(':
            if started == False:
                started = True
            counter = counter + 1
        elif e == ')':
            if started == False:
                raise ValueError("remove_parentheses(sequence):\
                        missing correcponding parentheses; ')' without '('")
            counter = counter - 1

        if started == True:
            if first_opener_idx_assigned == False:
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
    return None



def split_by(sequence, element):
    """Split a sequence by a given element and store elements before and
    after the element into a dictionary.

    Argument(s):
        sequence - description
        element - desctiption

    Return:
        return description
    """

    element_index = sequence.index(element)

    sequence_before_element = sequence[:element_index:1]
    sequence_after_element = sequence[element_index+1::1]

    return {0: sequence_before_element, 1: sequence_after_element}



def grammar_0(tokens):
    """Grammar for 'grammar_0:= grammar_1 > grammar_1'.

    Argument(s):
        tokens - description

    Return:
        return desctiption
    """

    ###print "grammar_0(tokens): tokens:",tokens

    if '>' not in tokens:
        raise ValueError("grammar_0(tokens):\
                no output found")
    else:
        input_output_dictionary = split_by(tokens, '>')

    return grammar_output(grammar_1(input_output_dictionary[0]),
                          grammar_1(input_output_dictionary[1]))



def grammar_1(tokens):
    """Grammar for 'grammar_1:= grammar_2 or grammar_1 |
    grammar_2 and grammar_1 |
    grammar_2'.

    Argument(s):
        tokens - description

    Return:
        return desctiption
    """

    ###print "grammar_1(tokens): tokens:",tokens

    if len(tokens) > 1 and tokens[1] == 'or':

        # grammar_2 or grammar_1

        ###print "grammar_1(tokens): detected 'or'

        # split tokens by the first occuring 'or' and store the tokens before
        # and after the 'or' in a dictionary
        or_dictionary = split_by(tokens, 'or')
        return grammar_or(grammar_2(or_dictionary.get(0)),
                          grammar_1(or_dictionary.get(1)))

    elif len(tokens) > 1 and tokens[1] == 'and':
        # grammar_2 and grammar_1

        ###print "grammar_1(tokens): detected 'and'"

        # split tokens by the first occuring 'and' and store the tokens
        # before and after the 'and' in a dictionary
         and_dictionary = split_by(tokens, 'and')
         return grammar_and(grammar_2(and_dictionary.get(0)),
                            grammar_1(and_dictionary.get(1)))
    else:
        # grammar_2; delegate to grammar_2
        return grammar_2(tokens)



def grammar_2(tokens):
    """Grammar for 'grammar_2:= (grammar_1) or grammar_1 |
    (grammar_1) and grammar_1 |
    (grammar_1) |
    interactor'.

    Argument(s):
        tokens - desctiption

    Return:
        return desctiption
    """

    ###print "grammar_2(tokens): tokens:",tokens

    if len(tokens) <= 0:
        raise ValueError("grammar_2(tokens):\
                invalid syntax")

    elif tokens[0] == '(':
        # (grammar_1) or grammar_1 | (grammar_1) and grammar_1| (grammar_1)

        ###print "grammar_2(tokens): detected '('"

        #token after the last occuring ')'
        token_after_last_closer = remove_parentheses(tokens)

        if token_after_last_closer == 'or':
            # split tokens by the first occuring 'or' and store the tokens
            # before and after the 'or' in a dictionary

            or_dictionary = split_by(tokens, 'or')
            return grammar_or(grammar_1(or_dictionary.get(0)),
                              grammar_1(or_dictionary.get(1)))

        elif token_after_last_closer == 'and':
            # split tokens by the first occuring 'and' and store the tokens
            # before and after the 'and' in a dictionary

            and_dictionary = split_by(tokens, 'and')
            return grammar_and(grammar_1(and_dictionary.get(0)),
                               grammar_1(and_dictionary.get(1)))

        else:
            # grammar_1; delegate to grammar_1
            return grammar_1(tokens)

    else:
        # interactor; delegate to interactor
        return interactor(tokens)



def interactor(tokens):
    """Grammar for 'interactor'.

    Argument(s):
        tokens - desctiption

    Return:
        return description
    """

    ###print "interactor(tokens): tokens:",tokens

    # return an interactor
    return (tokens)



def grammar_output(tokens1, tokens2):
    """Grammar for '>'.

    Argument(s):
        tokens1 - desctiption
        tokens2 - desctiption


    Return:
        return description
    """

    grammar_output_dict = {}

    for token1 in tokens1:
        value_set = set(tokens2)
        grammar_output_dict[token1] = (value_set)

    return grammar_output_dict



def grammar_or(tokens1, tokens2):
    """Grammar for 'or'.

    Argument(s):
        tokens1 - description
        tokens2 - desctiption

    Return:
        return description
    """

    return tokens1 + tokens2



def grammar_and(tokens1, tokens2):
    """Grammar for 'and'.

    Argument(s):
        tokens1 - desctiption
        tokens2 - description

    Return:
        return description
    """

    grammar_and_output = []

    for token1 in tokens1:
        for token2 in tokens2:
            grammar_and_output.append( (token1,token2) )
    return grammar_and_output



def parse_logic(logic):
    """Parse a logic input into atomized and equivalent logics.

    Argument(s):
        logic - description

    Return:
        return desctiption
    """

    ###print "parse_logic(logic): logic:",logic

    tokens = logic.split()

    # begin recursive logic parse
    return grammar_0(tokens)





if __name__ == '__main__':
    parse_logic(argv[1])
