

def read_txt_file(input_file):
    #add your code here
    return docs

def build_inverted_index(docs):
    # add your code here
    return inverted_index

def binary_query_case(input_text, inverted_index, docs):
    # add your code here
    return answer


def multi_query_case(input_text, inverted_index, docs):
    # add your code here
    return answer

docs = read_txt_file('Docs.txt')
inverted_index = build_inverted_index(docs)

print('input query:', "schizophrenia AND drug")
answer1 = binary_query_case("schizophrenia AND drug", inverted_index,docs)
print('query output:', answer1)

print('input query:', "breakthrough OR new")
answer2 = binary_query_case("breakthrough OR new", inverted_index,docs)
print('query output:', answer2)

print('input query:', "(drug OR treatment) AND schizophrenia")
answer3 = multi_query_case("(drug OR treatment) AND schizophrenia", inverted_index, docs)
print('query output:', answer3)
