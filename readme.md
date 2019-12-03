# Advanced Problem 5
By Stephen Knapper, Cameron Palmer, and Colson

## Introduction
The goal of this problem was to find the highest EigenValue
in a M, where
<pre>
    | 6 -4 1 |
M = |-4 6 -1 | 
    |1 -1 11 |
</pre>
We chose to use Python with Numpy and the power 
method to derive our solution.\
Attached is our code with comments explaining each function, 
parameters, and what that function returns.

## Our Process
1. We declare our matrix
2. We run our matrix through our power method function
    * In the power method we create a random vector that is 
    the size of the matrix
    * We then create a normalized vector initialized to 0
    * After that, we iterate `num_iterations` times
    * Each time we iterate, we do the dot product of our vector
     `v_0` and our matrix to produce `v_1`
    * Then we normalize `v_1` and get `v_1_norm` and with each
      iteration, this brings us closer to our Eigenvalue each time
    * Last in the iteration process, we recalculate `v_0` by dividing
      `v_1` by `v_1_norm`, this will eventually give a basis
      for the Eigenspace
