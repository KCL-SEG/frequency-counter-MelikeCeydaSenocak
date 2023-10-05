"""Frequencies function."""

def frequencies(items):
    frequencies = {}
    
    for item in items:
        key = str(item)

        if key not in frequencies:
            frequencies[key] = 1

        else:
            frequencies[key] += 1

    return frequencies
