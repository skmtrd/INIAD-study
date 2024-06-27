def tail_ing_to_ed(s):
    if s.endswith('ing'):
        return s[:-3] + 'ed'
    return s

print( tail_ing_to_ed('playing') )

print( tail_ing_to_ed('kingdom') )

print( tail_ing_to_ed('ingress') )
                