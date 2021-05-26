# This is common for every programmer/ developer that they might meet this use case at least once.
# Use case: Merging 2 or more dictionaries into single dictionary as quick as possible with no additional tools.


# Dictionary A.
dictionaryA = {
    1622027939: '2090356', 
    1622027940: '2472847', 
    1622027941: '350268', 
    1622027942: '3691962',
    1622027943: '3882093',
}


# Dictionary B.
dictionaryB = {
    '2090356': 1622027944,
    '2472847': 1622027945,
    '350268': 1622027946,
    '3691962': {
        0: 1622027939.2090356,
        1: 1622027940.2472847,
        2: 1622027941.350268,
    },
}


# I want to merge A and B and to get as C in pythonic-way.
# Note: Use dictionary unpacking technic in other word we can say as unpacking **kwargs.
dictionaryC = {**dictionaryA, **dictionaryB}
print(dictionaryC)


# Output
'''
{
    1622027939: '2090356', 
    1622027940: '2472847', 
    1622027941: '350268', 
    1622027942: '3691962', 
    1622027943: '3882093', 
    '2090356': 1622027944, 
    '2472847': 1622027945, 
    '350268': 1622027946, 
    '3691962': {
        0: 1622027939.2090356, 
        1: 1622027940.2472847, 
        2: 1622027941.350268
    }
}
'''