# Homework 1: Linear Algebra (2025)

### Question 1 (11%)
Determine whether the following system is consistent, and if so, find the vector form of its general solution.

$$
\begin{cases}
x_1 - x_2 + x_4 = -4 \\
x_1 - x_2 + 2x_4 + 2x_5 = -5 \\
3x_1 - 3x_2 + 2x_4 - 2x_5 = -11
\end{cases}
$$

### Question 2 (11%)
Find the rank and nullity of the matrix:

$$
\begin{bmatrix}
1 & 1 & -1 & 6 \\
0 & 5 & -1 & 7 \\
2 & -4 & 1 & -3 \\
-1 & -3 & 1 & 1
\end{bmatrix}
$$

### Question 3 (14%)
The input-output matrix for an economy with sectors of metals, nonmetals, and services follows:

$$
\begin{array}{c|ccc}
& \text{Met.} & \text{Nonm.} & \text{Svcs.} \\
\hline
\text{Metal} & 0.2 & 0.2 & 0.1 \\
\text{Nonmetals} & 0.4 & 0.4 & 0.2 \\
\text{Services} & 0.2 & 0.2 & 0.1
\end{array}
$$

(a) What is the net production corresponding to a gross production of $50 million of metals, $60 million of nonmetals, and $40 million of services?

(b) What gross production is required to satisfy exactly a demand for $120 million of metals, $180 million of nonmetals, and $150 million of services?

### Question 4 (11%)
Let $A$ and $B$ be $m \times n$ matrices such that $B$ can be obtained by performing a single elementary row operation on $A$. Prove that if the rows of $A$ are linearly independent, then the rows of $B$ are also linearly independent.

### Question 5 (20%)
Let $A$ be an $m \times n$ matrix with reduced row echelon form $R$. Determine the reduced row echelon form of each of the following matrices:

(a) $[A \quad 0]$
(b) $[a_1 \quad a_2 \quad \dots \quad a_k]$ for $k < n$, where $a_i = Ae_i$.
(c) $cA$, where $c$ is a nonzero scalar.
(d) $[I_m \quad A]$
(e) $[A \quad cA]$, where $c$ is any scalar.

### Question 6 (11%)
Given the matrix $A$:
$$
A = \begin{bmatrix}
0 & -1 & 1 & 1 \\
2 & -1 & 0 & 3 \\
-2 & 1 & 1 & -3
\end{bmatrix}
$$
Determine whether the equation $Ax=b$ is consistent for every $b$ in $\mathbb{R}^4$.

### Question 7 (11%)
Determine, if possible, a value of $r$ for which the following set of vectors is linearly dependent:

$$
\left\{
\begin{bmatrix} 1 \\ 0 \\ -1 \\ 1 \end{bmatrix},
\begin{bmatrix} 0 \\ -1 \\ 2 \\ 1 \end{bmatrix},
\begin{bmatrix} -1 \\ 1 \\ 1 \\ 0 \end{bmatrix},
\begin{bmatrix} -1 \\ 9 \\ r \\ -2 \end{bmatrix}
\right\}
$$

### Question 8 (11%)
Let $u_1, u_2, \dots, u_k$ be vectors in $\mathbb{R}^n$ and $c_1, c_2, \dots, c_k$ be nonzero scalars. Prove that:

$$
\text{Span}\{u_1, u_2, \dots, u_k\} = \text{Span}\{c_1u_1, c_2u_2, \dots, c_ku_k\}
$$