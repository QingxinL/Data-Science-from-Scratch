import math

# Vector_add:
def vector_add(v,w):
    return [v_i + w_i for v_i, w_i in zip(v,w)]

# Vector subtract:
def vector_subtract(v,w):
    return [v_i-w_i for v_i, w_i in zip(v,w)]

# Sum of a list of vectors:
def vector_sum(vectors):
    result = vectors[0]      # Or: return reduce(vector_add,vectors)
    for vector in vectors:
        result = vector_add(result,vector)
    return result

# Multiply a vector by a scalar
def scalar_multiply(c,v):   # c is the constant
    return [c*v_i for v_i in v]

# Compute the mean vector of a list of vectors:
def vector_mean(vectors):
    return scalar_multiply(1/len(vectors),vector_sum(vectors))

# Dot product
def dot(v,w):
    return sum(v_i*w_i for v_i,w_i in zip(v,w))

# Sum of Squares: (Vector's square)
def sum_of_square(v):
    return dot(v,v)

# Vector's Magnitude:
def magnitude(v):
    return math.sqrt(sum_of_square(v))

# Compute distance between two vectors:


