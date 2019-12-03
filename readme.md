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
3. We then return `v_0` and `v_1_norm` and continue on to check that 
    our Eigenvector is correct
4. We check that our Eigenvector is correct by multiplying the matrix and the
    vector together and checking that the vector produced by that is a multiple 
    of our Eigenvalue.

## Our Results
As you saw above, the matrix M is the input and for output we got
<pre>
Highest eigenvalue is 12.0 and the 
basis eigenvector for the eigenspace is 
V = [ 0.40824829 -0.40824829  0.81649658]
</pre>
The product of this vector and our matrix is 
<pre>
M * V = [4.898979485566356, -4.898979485566356, 9.797958971132713]
</pre>
Also
<pre>
12.0 * V = [4.898979485566356, -4.898979485566356, 9.797958971132713]
</pre>

## Conclusion
Thus we have shown that the highest Eigenvalue of matrix `M`is 12 and 
we have supplied a basis for the corresponding Eigenspace. We have also proven
that the basis we found is in fact an Eigenvector of `M`.


#### Run the Code
To run this code
1. Ensure you have python3.7 installed on your machine.
    * A virtual environment is ideal but not necessarily required.
2. Run `pip install -r requirements.txt`
3. Run `python3.7 find_highest_eigenvalue.py`