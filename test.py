import sys


'''finds the last index of an element in a sequence'''
def rindex(sequence, element):
    for i, e in enumerate(reversed(sequence)):
        if element == e:
            return len(sequence) - 1 - i
    else:
            raise ValueError("rindex(sequence, element): element not in the sequence")



'''removes the outer most parentheses "()" and returns the token afte the ")"'''
def parentheses(sequence):
    print "parentheses(sequence): sequence: ", sequence
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
                raise ValueError("parentheses(sequence): ')' without '('")
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
    print "parentheses(sequence): no parentehses in the sequence"
    return None



'''splits a sequence by a given element and stores the elements
before and after the element into a dictionary'''
def split_by(sequence, element):
    element_index = sequence.index(element)
    sequence_before_element = sequence[:element_index:1]
    sequence_after_element = sequence[element_index + 1::1]
    return {0: sequence_before_element, 1: sequence_after_element}


'''parseInputLogic'''
def parseInputLogic(userInput):
    #print "parseInputLogic(tokens): tokens: ", tokens
    user_input_token = userInput.split()
    return g0(user_input_token)



'''g0:= g1 > g1'''
def g0(tokens):
    #print "g0(tokens): tokens: ", tokens
    if '>' not in tokens:
        raise ValueError("g(tokens): no output")
    else:
        input_output_dictionary = split_by(tokens, '>')
    return gOutput(g1(input_output_dictionary[0]), g1(input_output_dictionary[1]))



'''g1:= g2 or g1 | g2 and g1 | g2'''
def g1(tokens):        
    #print "g1(tokens): tokens: ", tokens
    if len(tokens) > 1 and tokens[1] == 'or':
        "g2 or g1"
        #print "UISA.g0(tokens): detected 'or'"
        "splits tokens by the first occuring 'or' and stores the tokens before and after the 'or' in a dictionary"
        or_dictionary = split_by(tokens, 'or')
        return gOr(g2(or_dictionary.get(0)), g1(or_dictionary.get(1)))
    elif len(tokens) > 1 and tokens[1] == 'and':
        "g2 and g1"
        #print "UISA.g1(tokens): detected 'and'"
        "splits tokens by the first occuring 'and' and stores the tokens before and after the 'and' in a dictionary"
        and_dictionary = split_by(tokens, 'and')
        return gAnd(g2(and_dictionary.get(0)), g1(and_dictionary.get(1)))            
    else:
        "g2"
        "delegates to g2"
        return g2(tokens)



'''g2:= (g1) or g1 | (g1) and g1 | (g1) | interactor''' 
def g2(tokens):
    #print "g2(tokens): tokens: ", tokens
    if tokens[0] == "(":
        "(g1) or g1 | (g1) and g1| (g1)"
        #print "UISA.g2(tokens): detected '('"
        "token after the last occuring ')'"
        token_after_last_closer = parentheses(tokens)
        if token_after_last_closer == 'or':    
            "splits tokens by the first occuring 'or' and stores the tokens before and after the 'or' in a dictionary"
            or_dictionary = split_by(tokens, 'or')
            return gOr(g1(or_dictionary.get(0)), g1(or_dictionary.get(1)))
        elif token_after_last_closer == 'and':
            "splits tokens by the first occuring 'and' and stores the tokens before and after the 'and' in a dictionary"
            and_dictionary = split_by(tokens, 'and')
            return gAnd(g1(and_dictionary.get(0)), g1(and_dictionary.get(1)))
        else:
            "delegates to interactor"
            return g1(tokens)
    else:
        "interactor"
        "delegates to interactor"
        return interactor(tokens)



'''interactor:= lacI | cI | ... | etc.'''
def interactor(tokens):
    #print "interactor(tokens): tokens: ", tokens
    "returns an interactor"
    return tokens



'''>'''
def gOutput(tokens1, tokens2):
    toBeReturned = []
    for token1 in tokens1:
        for token2 in tokens2: 
            toBeReturned.append( (token1, token2) )
            "toBeReturned.append(('[' + token1 + '] ---> [' + token2 + ']'))"
    return toBeReturned



'''Or'''
def gOr(tokens1, tokens2):
    return tokens1 + tokens2



'''And'''
def gAnd(tokens1, tokens2):
    toBeReturned = []
    for token1 in tokens1:
        for token2 in tokens2:
            toBeReturned.append(token1 + " and " + token2)
    return toBeReturned


print sys.argv


def main():
    print "SUCCESS"
    userInput = sys.argv[1]
    toBeReturned = parseInputLogic(userInput)
    print toBeReturned
    return toBeReturned

if __name__ == "__main__":
    main()
