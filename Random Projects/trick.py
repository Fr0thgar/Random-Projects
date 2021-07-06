def tuples_to_list_string(lst):
    result = list(map(' '.join, lst))
    return  result

colours = [('red','pink'), ('white','black'), ('orange','green')]
print("Original list of tuples:")
print(colours)
print("\nConvert the said list of tuples to a list of strings:")
print(tuples_to_list_string(colours))
