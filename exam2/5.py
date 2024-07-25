def abbrev(s):
    pre_marker = []
    markers = []
    for index, i in enumerate(s):
        if i == "{" and len(pre_marker) == 0:
            pre_marker.append(index)
        if i == "}" and len(pre_marker) == 1:
            pre_marker.append(index)
            markers.append(pre_marker)
            pre_marker = []
            
    
    remove_index = []

    for marker in markers:
        for i in range(marker[0], marker[1] + 1):
            remove_index.append(i)

    result = ""
    for index, i in enumerate(s):
        if index in remove_index:
            continue
        result += i
    return result
        
        

s1 = "abc{defgh}ijk"
s2 = "abcde{123!abc?de}"
s3 = "{}a{}bc{def}g{hij}"

print(abbrev(s3))

