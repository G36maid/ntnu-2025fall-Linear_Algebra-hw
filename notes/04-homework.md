# Homework 4: Linear Algebra (2025)

### Question 1 (20%)
Let $T_w$ be the reflection of $\mathbb{R}^3$ about the plane $W$ in $\mathbb{R}^3$ with equation $x+2y-3z=0$ and let
$$
\mathcal{B} = \left\{
\begin{bmatrix} -2 \\ 1 \\ 0 \end{bmatrix},
\begin{bmatrix} 3 \\ 0 \\ 1 \end{bmatrix},
\begin{bmatrix} 1 \\ 2 \\ -3 \end{bmatrix}
\right\}.
$$
Note that the first two vectors in $\mathcal{B}$ lie in $W$ and the third vector is perpendicular (normal) to $W$ (because the normal vector is $\begin{bmatrix} 1 \\ 2 \\ -3 \end{bmatrix}$).

(a) Find $T_w(\mathbf{v})$ for each vector $\mathbf{v}$ in $\mathcal{B}$.
(b) Show that $\mathcal{B}$ is a basis for $\mathbb{R}^3$.
(c) Find $[T_w]_{\mathcal{B}}$.
(d) Find the standard matrix of $T_w$.
(e) Determine an explicit formula for $T_w \left( \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} \right)$.

### Question 2 (12%)
(Refer to the definition after this problem.) Let $T: \mathbb{R}^n \to \mathbb{R}^m$ be a linear transformation, and $\mathcal{B} = \{\mathbf{b}_1, \mathbf{b}_2, \dots, \mathbf{b}_n\}$ and $\mathcal{C} = \{\mathbf{c}_1, \mathbf{c}_2, \dots, \mathbf{c}_m\}$ be bases for $\mathbb{R}^n$ and $\mathbb{R}^m$, respectively. Let $B$ and $C$ be the matrices whose columns are the vectors in $\mathcal{B}$ and $\mathcal{C}$, respectively. Prove the following:

(a) If $A$ is the standard matrix of $T$, then $[T]_{\mathcal{B}}^{\mathcal{C}} = C^{-1}AB$.
(b) $[T(\mathbf{v})]_{\mathcal{C}} = [T]_{\mathcal{B}}^{\mathcal{C}} [\mathbf{v}]_{\mathcal{B}}$ for any vector $\mathbf{v}$ in $\mathbb{R}^n$.
(c) Let $U: \mathbb{R}^m \to \mathbb{R}^p$ be linear, and let $\mathcal{D}$ be a basis for $\mathbb{R}^p$. Then $[UT]_{\mathcal{B}}^{\mathcal{D}} = [U]_{\mathcal{C}}^{\mathcal{D}} [T]_{\mathcal{B}}^{\mathcal{C}}$.

**Definition**
Let $T: \mathbb{R}^n \to \mathbb{R}^m$ be a linear transformation, and let $\mathcal{B} = \{\mathbf{b}_1, \dots, \mathbf{b}_n\}$ and $\mathcal{C} = \{\mathbf{c}_1, \dots, \mathbf{c}_m\}$ be bases for $\mathbb{R}^n$ and $\mathbb{R}^m$, respectively. The matrix
$$
[[T(\mathbf{b}_1)]_{\mathcal{C}} \quad [T(\mathbf{b}_2)]_{\mathcal{C}} \quad \dots \quad [T(\mathbf{b}_n)]_{\mathcal{C}}]
$$
is called the matrix representation of $T$ with respect to $\mathcal{B}$ and $\mathcal{C}$. It is denoted by $[T]_{\mathcal{B}}^{\mathcal{C}}$.

### Question 3 (12%)
Find the eigenvalues of the linear operator $T$ and determine a basis for each eigenspace, where
$$
T \left( \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} \right) = \begin{bmatrix} -4x_1 + 6x_2 \\ 2x_2 \\ -5x_1 + 5x_2 + x_3 \end{bmatrix}.
$$

### Question 4 (12%)
Given a matrix
$$
A = \begin{bmatrix} -2 & 3 & 6 \\ -2 & -8 & -2 \\ 6 & -1 & 4 \end{bmatrix}
$$
and its characteristic polynomial $-(t + 5)(t + 4)(t + 2)$, find, if possible, an invertible matrix $P$ and a diagonal matrix $D$ such that $A = PDP^{-1}$.

### Question 5 (10%)
Let $A$ be a diagonalizable $n \times n$ matrix. Prove that if the characteristic polynomial of $A$ is $f(t) = a_n t^n + a_{n-1}t^{n-1} + \dots + a_1 t + a_0$, then $f(A) = O$, where $f(A) = a_n A^n + a_{n-1}A^{n-1} + \dots + a_1 A + a_0 I_n$. (This is called the Cayley-Hamilton theorem.)

### Question 6 (10%)
A linear operator $T$ on $\mathbb{R}^n$ is given below. Find, if possible, a basis $\mathcal{B}$ for $\mathbb{R}^n$ such that $[T]_{\mathcal{B}}$ is a diagonal matrix. If no such basis exists, explain why.
$$
T \left( \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} \right) = \begin{bmatrix} 4x_1 - 5x_2 \\ -x_2 \\ -x_3 \end{bmatrix}.
$$

### Question 7 (12%)
Given a linear operator $T$ and its characteristic polynomial $f(t)$, determine all the values of the scalar $c$ for which $T$ on $\mathbb{R}^3$ is not diagonalizable, where
$$
T \left( \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} \right) = \begin{bmatrix} x_1 + 2x_2 - x_3 \\ cx_2 \\ 6x_1 - x_2 + 6x_3 \end{bmatrix}
\quad \text{and} \quad
f(t) = -(t - c)(t - 3)(t - 4).
$$

### Question 8 (12%)
Let $\{\mathbf{u}, \mathbf{v}, \mathbf{w}\}$ be a basis for $\mathbb{R}^3$, and let $T$ be the linear operator on $\mathbb{R}^3$ defined by
$$
T(a\mathbf{u} + b\mathbf{v} + c\mathbf{w}) = a\mathbf{u} + b\mathbf{v} - c\mathbf{w}
$$
for all scalars $a, b,$ and $c$.

(a) Find the eigenvalues of $T$ and determine a basis for each eigenspace.
(b) Is $T$ diagonalizable? Justify your answer.