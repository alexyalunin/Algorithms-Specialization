#!/usr/bin/env python
# coding: utf-8

# test on https://leetcode.com/problems/edit-distance/submissions/

# In[5]:


from dataclasses import dataclass

@dataclass
class TestCase:
    input: str
    output: int


# In[41]:


test_cases = [
    TestCase(input={'X':'AAGACG', 'Y':'CAGAGCTC'}, output=16),
    TestCase(input={'X':'AGTGCTGAAAGTTGCGCCAGTGAC', 'Y':'AGTGCTGAAGTTCGCCAGTTGACG'}, output=12),
    TestCase(input={'X':'CACAATTTTTCCCAGAGAGA', 'Y':'CGAATTTTTCCCAGAGAGA'}, output=7)
]


# In[69]:


import numpy as np


def reconstruct_seq_align(X, Y, A, p_gap, p_mis):
    i, j = len(X), len(Y)
    res_x = []
    res_y = []
    while i > 0 and j > 0:
        x, y = X[i - 1], Y[j - 1]
        result = A[i][j]

        a1 = A[i - 1, j - 1] + (p_mis if x != y else 0)
        a2 = A[i - 1, j] + p_gap
        a3 = A[i, j - 1] + p_gap

        if result == a1:
            res_x.append(x)
            res_y.append(y)
            i -= 1
            j -= 1
        elif result == a2:
            res_x.append(x)
            res_y.append('-')
            i -= 1
        elif result == a3:
            res_x.append('-')
            res_y.append(y)
            j -= 1
        else:
            raise
    return (''.join(res_x)[::-1], ''.join(res_y)[::-1])


def seq_align(X: str, Y: str, p_gap=3, p_mis=4):
    A = np.zeros( (len(X)+1, len(Y)+1) , dtype=int)
    A[0,:] = np.arange(len(Y)+1) * p_gap
    A[:,0] = np.arange(len(X)+1) * p_gap
    for i, x in enumerate(X, 1):
        for j, y in enumerate(Y, 1):
            a1 = A[i-1, j-1] + (p_mis if x!=y else 0)
            a2 = A[i-1, j] + p_gap
            a3 = A[i, j-1] + p_gap
            A[i, j] = min(a1, a2, a3)
    sequences = reconstruct_seq_align(X, Y, A, p_gap, p_mis)
    print(sequences)
    return A


# In[70]:


for test in test_cases:
    output = seq_align(**test.input)
    output = output[-1, -1]
    if output == test.output:
        print( f'OK: pred {output} == real {test.output}' )
    else:
        print( f'ERROR: pred {output} == real {test.output}' )


# In[46]:


score, A = seq_align(**test_cases[0].input)
score, A


# In[ ]:




