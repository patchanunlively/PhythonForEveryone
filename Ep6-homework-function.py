def print_models(unprinted, printed):
    """3d print a set of models."""
    while unprinted:
        print('--------------------------------')
        print(f'unprinted (before pop): {unprinted}')
        current_model = unprinted.pop()
        print(f'unprinted (after pop): {unprinted}')

        print('\n')
        print(">> Pop = " + current_model)

        print('\n')
        print(f'printed (before append): {printed}')
        printed.append(current_model)
        print(f'printed (after append): {printed}')
        



# Store some unprinted designs,
# and print each of them.
original = ['phone case', 'pendant', 'ring']
printed = []

print('--------------------------------')
print(f'original : {original}')

print_models(original[:], printed)

print('----Result---------------')
print("printed:", printed)