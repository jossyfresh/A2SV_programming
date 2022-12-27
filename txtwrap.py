def wrap(string, max_width):
    l = 0
    s = textwrap.wrap(string,max_width)
    x = '\n'.join(s)
    return x
