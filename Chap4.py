import math

'''Vectors:
'''

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
def squared_distance(v,w):
    return sum_of_square(vector_subtract(v,w))

def distance(v,w):
    return math.sqrt(squared_distance(v,w))   # Or: return magnitude(vector_subtract(v,w))



'''Matrix:
'''

# Shape (rows & columns)
def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows,num_cols

def get_rows(A,i):
    return A[i]

def get_cols(A,j):
    return [A_i[j] for A_i in A]

# Make(Generate) a matrix based on its shape
def make_matrix(num_rows,num_cols,entry_fn):
    return [[entry_fn(i,j)
            for j in range(num_cols)]
            for i in range(num_rows)]
# this return a matrix whose (i,j)th entry is entry_fn(i,j)

def is_diagonal(i,j):
    return 1 if i==j else 0

identity_matrix = make_matrix(5,5,is_diagonal)








