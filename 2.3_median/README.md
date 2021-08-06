Question 1

Download the following text file:
Median.txt

The goal of this problem is to implement the "Median Maintenance" algorithm (covered in the Week 3 lecture on heap applications).  The text file contains a list of the integers from 1 to 10000 in unsorted order; you should treat this as a stream of numbers, arriving one by one.  Letting xix_ixi​ denote the iiith number of the file, the kkkth median mkm_kmk​ is defined as the median of the numbers x1,…,xkx_1,\ldots,x_kx1​,…,xk​.  (So, if kkk is odd, then mkm_kmk​ is ((k+1)/2)((k+1)/2)((k+1)/2)th smallest number among x1,…,xkx_1,\ldots,x_kx1​,…,xk​; if kkk is even, then mkm_kmk​ is the (k/2)(k/2)(k/2)th smallest number among x1,…,xkx_1,\ldots,x_kx1​,…,xk​.)

In the box below you should type the sum of these 10000 medians, modulo 10000 (i.e., only the last 4 digits).  That is, you should compute (m1+m2+m3+⋯+m10000) mod 10000(m_1+m_2+m_3 + \cdots + m_{10000}) \bmod 10000(m1​+m2​+m3​+⋯+m10000​)mod10000.

OPTIONAL EXERCISE: Compare the performance achieved by heap-based and search-tree-based implementations of the algorithm.