def strip_comments(strng, markers):
    s = strng.split('\n')
    l = []
    for line in s:
        for m in markers:
            if m in line:
                line = line.split(m)[0]
        l.append(line.rstrip())
            
    return '\n'.join(l)