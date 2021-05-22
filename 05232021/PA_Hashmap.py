# I got to use a map dictionary (identical values) in one place as it is 
# but in another I should convert keys as values and values as keys!

# Note
'''
+ This is only for dictionary which has identical values and when considered as hashmap.
- If dictionary which has duplicate values may not work well.
- If dictionary which has collection as values may also not work.
'''

# Identical values
Hashmap = {
    'BlankValidationError': 'BVE01',
    'InvalidFormatError': 'IFE01',
    'InvalidTypeError': 'ITE01',
    'InvalidLengthError': 'IVL01',
}

# Logic to conver the keys as values and values as keys.
ReverseHashmap = {Hashmap[_]: _ for _ in Hashmap}

# Usage
print('Original Hashmap:')
print(Hashmap)
print()
print('Reversed Hashmap:')
print(ReverseHashmap)

# Output
'''
Original Hashmap:
{'BlankValidationError': 'BVE01', 'InvalidFormatError': 'IFE01', 'InvalidTypeError': 'ITE01', 'InvalidLengthError': 'IVL01'}

Reversed Hashmap:
{'BVE01': 'BlankValidationError', 'IFE01': 'InvalidFormatError', 'ITE01': 'InvalidTypeError', 'IVL01': 'InvalidLengthError'}
'''
