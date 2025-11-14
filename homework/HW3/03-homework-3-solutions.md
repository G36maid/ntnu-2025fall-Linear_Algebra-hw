# Homework 3 Solutions: Linear Algebra (2025)

## Question 1 (16%)
**Problem:** Find generating sets for the range and null space of linear transformation T defined as 
$T\left(\begin{bmatrix} x_1 \ x_2 \ x_3 \end{bmatrix}\right) = \begin{bmatrix} x_1 + x_2 \ x_2 + x_3 \ x_1 - x_3 \ x_1 + 2x_2 + x_3 \end{bmatrix}$

**Solution:**
The transformation T can be represented by a matrix A such that $T(x) = Ax$.
$A = \begin{bmatrix} 1 & 1 & 0 \ 0 & 1 & 1 \ 1 & 0 & -1 \ 1 & 2 & 1 \end{bmatrix}$

**Range(T):**
The range of T is the column space of A. We find the basis for the column space by row reducing A.
$\begin{bmatrix} 1 & 1 & 0 \ 0 & 1 & 1 \ 1 & 0 & -1 \ 1 & 2 & 1 \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 0 & -1 \ 0 & 1 & 1 \ 0 & 0 & 0 \ 0 & 0 & 0 \end{bmatrix}$
The pivot columns are the first two columns. So a basis for the range of T is:
$\left\{\begin{bmatrix} 1 \ 0 \ 1 \ 1 \end{bmatrix}, \begin{bmatrix} 1 \ 1 \ 0 \ 2 \end{bmatrix}\right\}$
A generating set for the range is the set of all linear combinations of these basis vectors.

**Null Space(T):**
The null space of T is the set of all x such that $T(x) = 0$. From the RREF of A, we have:
$x_1 - x_3 = 0 \Rightarrow x_1 = x_3$
$x_2 + x_3 = 0 \Rightarrow x_2 = -x_3$
$x_3$ is a free variable.
The general solution is $x = x_3\begin{bmatrix} 1 \ -1 \ 1 \end{bmatrix}$.
A basis for the null space is $\left\{\begin{bmatrix} 1 \ -1 \ 1 \end{bmatrix}\right\}$.
A generating set for the null space is the set of all scalar multiples of this basis vector.

## Question 2 (12%)
**Problem:** Given a linear transformation T defined as 
$T\left(\begin{bmatrix} x_1 \ x_2 \ x_3 \ x_4 \end{bmatrix}\right) = \begin{bmatrix} -2x_1 - x_2 + x_4 \ 0 \ x_1 + 2x_2 + 3x_3 + 4x_4 \ 2x_1 + 3x_2 + 4x_3 + 5x_4 \end{bmatrix}$

(a) Find a basis for the range of T;
(b) If the null space of T is nonzero, find a basis for the null space of T.

**Solution:**
The matrix representation of T is:
$A = \begin{bmatrix} -2 & -1 & 0 & 1 \ 0 & 0 & 0 & 0 \ 1 & 2 & 3 & 4 \ 2 & 3 & 4 & 5 \end{bmatrix}$

**(a) Basis for the range of T:**
The range of T is the column space of A. We find the RREF of A.
$\begin{bmatrix} 1 & 0 & -1 & -2 \ 0 & 1 & 2 & 3 \ 0 & 0 & 0 & 0 \ 0 & 0 & 0 & 0 \end{bmatrix}$
The pivot columns are the first two columns. A basis for the range of T is:
$\left\{\begin{bmatrix} -2 \ 0 \ 1 \ 2 \end{bmatrix}, \begin{bmatrix} -1 \ 0 \ 2 \ 3 \end{bmatrix}\right\}$

**(b) Basis for the null space of T:**
From the RREF of A:
$x_1 - x_3 - 2x_4 = 0 \Rightarrow x_1 = x_3 + 2x_4$
$x_2 + 2x_3 + 3x_4 = 0 \Rightarrow x_2 = -2x_3 - 3x_4$
$x_3, x_4$ are free variables.
The general solution is $x = x_3\begin{bmatrix} 1 \ -2 \ 1 \ 0 \end{bmatrix} + x_4\begin{bmatrix} 2 \ -3 \ 0 \ 1 \end{bmatrix}$.
A basis for the null space is $\left\{\begin{bmatrix} 1 \ -2 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} 2 \ -3 \ 0 \ 1 \end{bmatrix}\right\}$.

## Question 3 (12%)
**Problem:** Let $L = \left\{\begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}\right\}$ and $V = \text{Col}\begin{bmatrix} 1 & -1 & -3 \ 1 & 1 & 3 \ 2 & -2 & -6 \end{bmatrix}$. Find a basis for the subspace V that contains the given linearly independent subset L of V.

**Solution:**
First, find a basis for V. The columns of the matrix are vectors in V.
Let the matrix be $A = \begin{bmatrix} 1 & -1 & -3 \ 1 & 1 & 3 \ 2 & -2 & -6 \end{bmatrix}$.
Row reduce A to find the pivot columns.
$\begin{bmatrix} 1 & -1 & -3 \ 1 & 1 & 3 \ 2 & -2 & -6 \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 0 & 0 \ 0 & 1 & 3 \ 0 & 0 & 0 \end{bmatrix}$
The pivot columns are the first two. A basis for V is $\left\{\begin{bmatrix} 1 \ 1 \ 2 \end{bmatrix}, \begin{bmatrix} -1 \ 1 \ -2 \end{bmatrix}\right\}$.
The vector in L is $\begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}$. We need to check if this vector is in V.
We can see that $\frac{1}{2}\begin{bmatrix} 1 \ 1 \ 2 \end{bmatrix} + \frac{-1}{2}\begin{bmatrix} -1 \ 1 \ -2 \end{bmatrix} = \begin{bmatrix} 1 \ 0 \ 2 \end{bmatrix} \neq \begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}$.
There must be a typo in the question, as L is not in V. Assuming L is $\begin{bmatrix} 1 \ 1 \ 2 \end{bmatrix}$, then a basis for V that contains L is the basis we found for V.
Assuming the question meant to ask for a basis of V that includes a vector from L, and that L is a typo for a vector that *is* in V, let's assume $L = \left\{\begin{bmatrix} 1 \ 1 \ 2 \end{bmatrix}\right\}$. Then a basis for V containing L is $\left\{\begin{bmatrix} 1 \ 1 \ 2 \end{bmatrix}, \begin{bmatrix} -1 \ 1 \ -2 \end{bmatrix}\right\}$.

## Question 4 (12%)
**Problem:** Given a linearly independent subset $L = \left\{\begin{bmatrix} -1 \ 6 \ -2 \end{bmatrix}, \begin{bmatrix} 5 \ -9 \ -2 \end{bmatrix}\right\}$ of the subspace $V = \text{Span}\left\{\begin{bmatrix} 1 \ -2 \ 0 \end{bmatrix}, \begin{bmatrix} 1 \ -1 \ -2 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 2 \end{bmatrix}, \begin{bmatrix} 1 \ 3 \ 10 \end{bmatrix}\right\}$. Find a basis for the subspace V that contains the given linearly independent subset L of V.

**Solution:**
Let the vectors in L be $l_1, l_2$ and the vectors spanning V be $v_1, v_2, v_3, v_4$.
We form a matrix with the vectors of L and the spanning vectors of V, and find a basis for the column space of this matrix, ensuring that the vectors from L are chosen first.
$A = \begin{bmatrix} -1 & 5 & 1 & 1 & 0 & 1 \ 6 & -9 & -2 & -1 & 1 & 3 \ -2 & -2 & 0 & -2 & 2 & 10 \end{bmatrix}$
Row reduce A:
$\begin{bmatrix} 1 & 0 & 1/7 & 2/7 & -5/21 & -4/7 \ 0 & 1 & 8/7 & 9/7 & 2/21 & 3/7 \ 0 & 0 & 0 & 0 & 0 & 0 \end{bmatrix}$
The pivot columns are the first two. This means that the first two vectors form a basis for the column space.
So, a basis for V that contains L is L itself: $\left\{\begin{bmatrix} -1 \ 6 \ -2 \end{bmatrix}, \begin{bmatrix} 5 \ -9 \ -2 \end{bmatrix}\right\}$.
The dimension of V is 2.

## Question 5 (12%)
**Problem:** For the linear transformation defined by $T\left(\begin{bmatrix} x_1 \ x_2 \ x_3 \end{bmatrix}\right) = \begin{bmatrix} -x_1 - x_2 + x_3 \ x_1 + 2x_2 + x_3 \ x_1 + x_2 \end{bmatrix}$, determine
(a) the dimension of the range of T
(b) the dimension of the null space of T
(c) whether T is one-to-one or on-to.

**Solution:**
The matrix representation of T is:
$A = \begin{bmatrix} -1 & -1 & 1 \ 1 & 2 & 1 \ 1 & 1 & 0 \end{bmatrix}$
Row reduce A:
$\begin{bmatrix} 1 & 0 & -3 \ 0 & 1 & 2 \ 0 & 0 & 1 \end{bmatrix} \rightarrow \begin{bmatrix} 1 & 0 & 0 \ 0 & 1 & 0 \ 0 & 0 & 1 \end{bmatrix}$
The RREF is the identity matrix.
(a) **Dimension of the range of T:** The rank of A is 3. So the dimension of the range of T is 3.
(b) **Dimension of the null space of T:** The nullity of A is the number of columns minus the rank, which is 3 - 3 = 0. The dimension of the null space is 0.
(c) **One-to-one or on-to:**
- A transformation is one-to-one if its null space has dimension 0. Since the nullity is 0, T is **one-to-one**.
- A transformation from $R^3$ to $R^3$ is on-to if the dimension of its range is 3. Since the rank is 3, T is **on-to**.

## Question 6 (12%)
**Problem:** Find the unique representation of $u = \begin{bmatrix} a \ b \ c \end{bmatrix}$ as a linear combination of $b_1 = \begin{bmatrix} 1 \ -1 \ 2 \end{bmatrix}$, $b_2 = \begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}$, and $b_3 = \begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix}$.

**Solution:**
We want to find scalars $c_1, c_2, c_3$ such that $u = c_1b_1 + c_2b_2 + c_3b_3$.
This is equivalent to solving the system $Bc = u$, where $B = [b_1 b_2 b_3]$.
$\begin{bmatrix} 1 & 1 & 0 \ -1 & 0 & 1 \ 2 & 1 & 1 \end{bmatrix} \begin{bmatrix} c_1 \ c_2 \ c_3 \end{bmatrix} = \begin{bmatrix} a \ b \ c \end{bmatrix}$
We can find the inverse of B and compute $c = B^{-1}u$.
$B^{-1} = \begin{bmatrix} -2 & -1 & 1 \ 3 & 1 & -1 \ -2 & 0 & 1 \end{bmatrix}$
$\begin{bmatrix} c_1 \ c_2 \ c_3 \end{bmatrix} = \begin{bmatrix} -2 & -1 & 1 \ 3 & 1 & -1 \ -2 & 0 & 1 \end{bmatrix} \begin{bmatrix} a \ b \ c \end{bmatrix} = \begin{bmatrix} -2a - b + c \ 3a + b - c \ -2a + c \end{bmatrix}$
So, $c_1 = -2a - b + c$, $c_2 = 3a + b - c$, $c_3 = -2a + c$.

## Question 7 (12%)
**Problem:** Let $B = \{b_1, b_2, b_3\}$, where $b_1 = \begin{bmatrix} 1 \ -2 \ 1 \end{bmatrix}$, $b_2 = \begin{bmatrix} 3 \ 0 \ 2 \end{bmatrix}$, and $b_3 = \begin{bmatrix} -1 \ 1 \ 1 \end{bmatrix}$.
(a) Show that B is a basis for R^3.
(b) Determine the matrix $A = [[e_1]_B [e_2]_B [e_3]_B]$.
(c) What is the relationship between A and $B = [b_1 b_2 b_3]$?

**Solution:**
**(a) Show that B is a basis for R^3:**
We form a matrix with the vectors of B and check if it's invertible.
$B = \begin{bmatrix} 1 & 3 & -1 \ -2 & 0 & 1 \ 1 & 2 & 1 \end{bmatrix}$
$\det(B) = -1 \neq 0$.
Since the determinant is non-zero, the vectors are linearly independent and span $R^3$. Thus, B is a basis for $R^3$.

**(b) Determine the matrix $A = [[e_1]_B [e_2]_B [e_3]_B]$:**
The columns of A are the coordinates of the standard basis vectors with respect to the basis B.
This means we need to solve $Bc = e_i$ for each $e_i$. This is equivalent to finding $B^{-1}$.
$A = B^{-1}$.
$B^{-1} = \begin{bmatrix} -3 & -1 & 2 \ -4 & -1 & 2 \ 3 & 1 & -1 \end{bmatrix}$
So, $A = \begin{bmatrix} -3 & -1 & 2 \ -4 & -1 & 2 \ 3 & 1 & -1 \end{bmatrix}$.

**(c) What is the relationship between A and $B = [b_1 b_2 b_3]$?**
As shown in part (b), $A = B^{-1}$.

## Question 8 (12%)
**Problem:** Let $A = \{u_1, u_2, ..., u_n\}$ be a basis for R^n. Then, $B = \{u_1, u_1+u_2, ..., u_1+u_n\}$ is also a basis for R^n. If v is a vector in R^n and $[v]_A = \begin{bmatrix} a_1 \ a_2 \ \vdots \ a_n \end{bmatrix}$, compute $[v]_B$.

**Solution:**
Let the basis vectors of B be $b_1, ..., b_n$.
$b_1 = u_1$
$b_2 = u_1 + u_2$
...
$b_n = u_1 + u_n$
We have $v = a_1u_1 + a_2u_2 + ... + a_nu_n$.
We want to find $c_1, ..., c_n$ such that $v = c_1b_1 + c_2b_2 + ... + c_nb_n$.
$v = c_1(u_1) + c_2(u_1+u_2) + ... + c_n(u_1+u_n)$
$v = (c_1+c_2+...+c_n)u_1 + c_2u_2 + ... + c_nu_n$
Comparing the coefficients with the representation of v in basis A:
$a_1 = c_1+c_2+...+c_n$
$a_2 = c_2$
...
$a_n = c_n$
From this, we can find the coefficients $c_i$:
$c_i = a_i$ for $i=2, ..., n$.
$c_1 = a_1 - (c_2+...+c_n) = a_1 - (a_2+...+a_n)$.
So, $[v]_B = \begin{bmatrix} a_1 - \sum_{i=2}^n a_i \ a_2 \ \vdots \ a_n \end{bmatrix}$.
