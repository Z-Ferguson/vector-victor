import math
class ShapeError(Exception):
    pass
#
# class VectorVictor:
    # def __init__(self, vectors, matrices):
    #     self.vectors = vectors
    #     self.matrices = matrices

    # vector shape in shape()
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
        return [x + y for x, y in zip(vector1, vector2)]
    else:
        raise ShapeError
    #
    # # vector subtraction in vector_sub()
def vector_sub(vector1, vector2):
    if shape(vector1) == shape(vector2):
        return [x - y for x, y in zip(vector1, vector2)]
    else:
        raise ShapeError
    #
    # # vector sum in vector_sum()
    # def vector_sum():
    #
    # # dot product in dot()
    # def dot():
    #
    # # vector multiplication by a scalar in vector_multiply()
    # def vector_multiply():
    #
    # # mean of multiple vectors in vector_mean()
    # def vector_mean():
    #
    # # magnitude in magnitude()
    # def magnitude():
