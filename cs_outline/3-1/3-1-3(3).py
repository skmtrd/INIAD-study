def mpg_to_kmpl(mpg):
    kmpl = mpg * 0.425143707
    return kmpl

def liters_needed(d, mpg):
    kmpl = mpg_to_kmpl(mpg)
    liters_needed = d / kmpl
    return liters_needed
print(liters_needed(1000, 10))
