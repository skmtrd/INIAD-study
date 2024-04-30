def quad_eq(a, b, c):
    up = -b + (b**2 - (4 * a * c)) ** 0.5
    answer = up / 2 * a
    return answer

print(quad_eq(1,5,6))