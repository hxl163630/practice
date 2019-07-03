
def alienOrder(words):
    """
    :type words: List[str]
    :rtype: str
    """
    if not words or len(words) == 1: return ""

    order = []
    for pair in zip(words, words[1:]):
        for a, b in zip(*pair):
            if a != b:
                order.append(a + b)
                break
    output = []
    char = set(''.join(words))
    while order:
        small_char = set(list(zip(*order))[1])
        free_char = char - small_char
        if not free_char:
            return ""
        output += free_char
        order = list(filter(free_char.isdisjoint, order))
        char -= free_char
    return "".join(output + list(char))


print(alienOrder(["wrt","wrf","er","ett","rftt"]))