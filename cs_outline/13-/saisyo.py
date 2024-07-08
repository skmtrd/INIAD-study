def get_recip(xs):
    try:
        return [1 / a for a in xs]
    except:
        return None
    
ret = get_recip( [ 2.0, 0.0, -1.0 ] )
print(ret)

