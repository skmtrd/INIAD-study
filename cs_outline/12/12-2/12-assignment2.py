def count_uid(xs):
    uid = [x for x in xs if x.startswith('s1f') and len(x) == 12]
    return len([x + '@iniad.org' for x in uid])




def get_email(xs):
    uid = [x for x in xs if x.startswith('s1f') and len(x) == 12]
    return [x + '@iniad.org' for x in uid]


def exist21(xs):
    uid = [x for x in xs if x.startswith('s1f') and len(x) == 12 and x[5:7] == '21']
    return len(uid) > 0