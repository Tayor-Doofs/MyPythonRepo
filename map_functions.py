def quad_expression(a):
    return a**2 + 2*a + 3
numbers = (1,2,3,4,5)

values = map(quad_expression,numbers)

print(sorted(set(values)))