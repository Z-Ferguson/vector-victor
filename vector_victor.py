import math
class ShapeError(Exception):
    pass

# Variables for matrices generally are in uppercase.
# The shape of a matrix is its number of rows and columns, always in that order.
# The number of rows is usually called n and the number of columns called k.
def shape(vector):
    row = len(vector)
    tuple = (row, )
    return tuple

    # vector addition in vector_add()
def vector_add(vector1, vector2):
    if shape(vector1) == shape(vector2):
        return [v1 + v2 for v1, v2 in zip(vector1, vector2)]
    else:
        raise ShapeError

    # vector subtraction in vector_sub()
def vector_sub(vector1, vector2):
    if shape(vector1) == shape(vector2):
        return [v1 - v2 for v1, v2 in zip(vector1, vector2)]
    else:
        raise ShapeError

    # vector sum in vector_sum()
def vector_sum(*args):
    vector_shape = [shape(vector) for vector in args]
    if min(vector_shape) == max(vector_shape):
        return [sum(v1) for v1 in zip(*args)]
    else:
        raise ShapeError

def dot(vector_one, vector_two):
    if shape(vector_one) == shape(vector_two):
        return sum([v1 * v2 for v1, v2 in zip(vector_one, vector_two)])
    else:
        raise ShapeError

    # vector multiplication by a scalar in vector_multiply()
def vector_multiply(vector, scalar):
    return [(number * scalar) for number in vector]

# mean of multiple vectors in vector_mean()
def vector_mean(*args):
    return [(sum(x)/len(args)) for x in zip(*args)]

# magnitude in magnitude()
def magnitude(vector):
    return ((sum([x**2 for x in vector])))**(1/2)
