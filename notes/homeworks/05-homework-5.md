# Homework 5: Linear Algebra (2025)

### Question 1 (10%)
Let $A$ be any $m \times n$ matrix.

(a) Prove that $A^T A$ and $A$ have the same null space.
(b) Use (a) to prove that $\text{rank}(A^T A) = \text{rank}(A)$.

### Question 2 (18%)
Let
$$
\Sigma = \left\{
\begin{bmatrix} 1 \\ -1 \\ 0 \\ 2 \end{bmatrix},
\begin{bmatrix} 1 \\ 1 \\ 1 \\ 3 \end{bmatrix},
\begin{bmatrix} 3 \\ 1 \\ 1 \\ 5 \end{bmatrix}
\right\}.
$$

(a) Apply the Gram-Schmidt process to replace the given linearly independent set $\Sigma$ by an orthogonal set of nonzero vectors with the same span, and obtain an orthonormal set with the same span as $\Sigma$.
(b) Let $A$ be the matrix whose columns are the vectors in $\Sigma$. Determine the matrices $Q$ and $R$ in a QR factorization of $A$.
(c) Use the QR factorization to solve the system $Ax=b$ where
$$
\mathbf{b} = \begin{bmatrix} 8 \\ 0 \\ 1 \\ 11 \end{bmatrix}.
$$

### Question 3 (15%)
Let $\{\mathbf{w}_1, \mathbf{w}_2, \dots, \mathbf{w}_n\}$ be an orthonormal basis for $\mathbb{R}^n$. Prove that, for any vectors $\mathbf{u}$ and $\mathbf{v}$ in $\mathbb{R}^n$,

(a) $\mathbf{u}+\mathbf{v} = (\mathbf{u}\cdot\mathbf{w}_1+\mathbf{v}\cdot\mathbf{w}_1)\mathbf{w}_1 + (\mathbf{u}\cdot\mathbf{w}_2+\mathbf{v}\cdot\mathbf{w}_2)\mathbf{w}_2 + \dots + (\mathbf{u}\cdot\mathbf{w}_n+\mathbf{v}\cdot\mathbf{w}_n)\mathbf{w}_n$.
(b) $\mathbf{u}\cdot\mathbf{v} = (\mathbf{u}\cdot\mathbf{w}_1)(\mathbf{v}\cdot\mathbf{w}_1)+ (\mathbf{u}\cdot\mathbf{w}_2)(\mathbf{v}\cdot\mathbf{w}_2)+ \dots +(\mathbf{u}\cdot\mathbf{w}_n)(\mathbf{v}\cdot\mathbf{w}_n)$. (This is known as Parseval’s identity.)
(c) $\|\mathbf{u}\|^2= (\mathbf{u}\cdot\mathbf{w}_1)^2+ (\mathbf{u}\cdot\mathbf{w}_2)^2+ \dots +(\mathbf{u}\cdot\mathbf{w}_n)^2$.

### Question 4 (15%)
Let
$$
\mathbf{u} = \begin{bmatrix} 1 \\ 3 \\ -2 \end{bmatrix}
$$
and $W$ be the solution set of the system of equations
$$
\begin{cases}
x_1 + 2x_2 - 3x_3 = 0 \\
x_1 + x_2 - 3x_3 = 0
\end{cases}
$$

(a) Find the orthogonal projection matrix $P_W$.
(b) Obtain the unique vectors $\mathbf{w}$ in $W$ and $\mathbf{z}$ in $W^\perp$ such that $\mathbf{u} = \mathbf{w} + \mathbf{z}$.
(c) Find the distance from $\mathbf{u}$ to $W$.

### Question 5 (10%)
Let $W$ be a subspace of $\mathbb{R}^n$. Prove that $P_W P_{W^\perp} = P_{W^\perp} P_W = O$, and hence $P_{W^\perp} = I_n - P_W$ (or $P_W + P_{W^\perp} = I_n$).

### Question 6 (12%)
An inconsistent system of linear equations $Ax=b$ is given where
$$
A = \begin{bmatrix} 1 & 2 \\ 1 & -1 \\ 2 & 1 \end{bmatrix}
\quad \text{and} \quad
\mathbf{b} = \begin{bmatrix} 1 \\ 3 \\ 1 \end{bmatrix}.
$$

(a) Obtain the vector $\mathbf{z}$ for which $\|A\mathbf{z}-\mathbf{b}\|$ is a minimum.
(b) Find the vector $\mathbf{z}$ of least norm for which $\|A\mathbf{z}-\mathbf{b}\|$ is a minimum.

### Question 7 (10%)
Find an orthogonal operator $T$ on $\mathbb{R}^3$ such that $T(\mathbf{v})=\mathbf{w}$ where
$$
\mathbf{v} = \frac{1}{\sqrt{10}} \begin{bmatrix} 3 \\ 1 \\ 0 \end{bmatrix}
\quad \text{and} \quad
\mathbf{w} = \frac{1}{\sqrt{5}} \begin{bmatrix} 0 \\ -2 \\ 1 \end{bmatrix}.
$$

### Question 8 (10%)
Given a symmetric matrix
$$
A = \begin{bmatrix} 0 & 2 & 2 \\ 2 & 0 & 2 \\ 2 & 2 & 0 \end{bmatrix},
$$
find an orthonormal basis of eigenvectors and their corresponding eigenvalues. Use this information to obtain a spectral decomposition of $A$.