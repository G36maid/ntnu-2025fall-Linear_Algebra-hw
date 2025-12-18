# Chapter 1: Matrices, Vectors, and Systems of Linear Equations

## 1.1 Matrices and Vectors

### Definitions
- **Matrix**: A rectangular array of scalars.
  - If a matrix has $m$ rows and $n$ columns, its size is $m \times n$.
  - A matrix is **square** if $m=n$.
  - The scalar in the $i$-th row and $j$-th column is the $(i,j)$-entry, denoted $a_{ij}$.

$$
A = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix}
$$

- **Equality**: Matrices $A$ and $B$ are equal ($A=B$) if they have the same size and $a_{ij} = b_{ij}$ for all $i, j$.
- **Submatrix**: Obtained by deleting entire rows or columns from a matrix.

### Arithmetic Operations
- **Matrix Addition**: If $A$ and $B$ are $m \times n$, $A+B$ is the matrix where the $(i,j)$-entry is $a_{ij} + b_{ij}$.
- **Scalar Multiplication**: For a scalar $c$, $cA$ has entries $ca_{ij}$.
- **Zero Matrix ($O$)**: An $m \times n$ matrix where every entry is 0.
- **Subtraction**: $A - B$ has entries $a_{ij} - b_{ij}$. Note that $A - A = O$.

### Theorem 1.1: Properties of Matrix Addition and Scalar Multiplication
Let $A, B, C$ be $m \times n$ matrices, and $s, t$ be scalars.
1. $A + B = B + A$ (Commutative law)
2. $(A + B) + C = A + (B + C)$ (Associative law)
3. $A + O = A$
4. $A + (-A) = O$
5. $(st)A = s(tA)$
6. $s(A + B) = sA + sB$
7. $(s + t)A = sA + tA$

### Matrix Transposes
The **transpose** of an $m \times n$ matrix $A$, denoted $A^T$, is the $n \times m$ matrix where the $(i,j)$-entry is the $(j,i)$-entry of $A$.

**Theorem 1.2 (Properties of Transpose)**:
1. $(A + B)^T = A^T + B^T$
2. $(sA)^T = sA^T$
3. $(A^T)^T = A$

### Vectors
- **Row vector**: A matrix with exactly one row.
- **Column vector**: A matrix with exactly one column.
- **$\mathbb{R}^n$**: The set of all column vectors with $n$ components.
- Vectors satisfy the properties in Theorem 1.1.
- Geometry: Vector addition follows the parallelogram law.

---

## 1.2 Linear Combinations, Matrix-Vector Products, and Special Matrices

### Linear Combinations
A linear combination of vectors $u_1, u_2, \dots, u_k$ is a vector of the form:
$$ c_1u_1 + c_2u_2 + \dots + c_ku_k $$
where $c_1, \dots, c_k$ are scalars (coefficients).

### Standard Vectors
The standard vectors of $\mathbb{R}^n$ are:
$$ e_1 = \begin{bmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{bmatrix}, \quad e_2 = \begin{bmatrix} 0 \\ 1 \\ \vdots \\ 0 \end{bmatrix}, \quad \dots, \quad e_n = \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 1 \end{bmatrix} $$
Any vector $v \in \mathbb{R}^n$ is a linear combination of standard vectors: $v = v_1e_1 + \dots + v_ne_n$.

### Matrix-Vector Products
Let $A$ be an $m \times n$ matrix and $v$ be an $n \times 1$ vector. The product $Av$ is:
$$ Av = v_1a_1 + v_2a_2 + \dots + v_na_n = \sum_{j=1}^n v_ja_j $$
where $a_i$ is the $i$-th column of $A$.
The $i$-th component of $Av$ is $\sum_{j=1}^n a_{ij}v_j$.

### Special Matrices
- **Identity Matrix ($I_n$)**: The $n \times n$ matrix with columns $e_1, \dots, e_n$.
  $$ I_2 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}, \quad I_3 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} $$
  Property: $I_n v = v$.
  
- **Rotation Matrix ($A_\theta$)**: Rotates a vector by angle $\theta$.
  $$ A_\theta = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix} $$

### Theorem 1.3: Properties of Matrix-Vector Product
1. $A(u + v) = Au + Av$
2. $A(cu) = c(Au) = (cA)u$
3. $(A + B)u = Au + Bu$
4. $Ae_j = a_j$ (the $j$-th column of $A$)
5. If $Bw = Aw$ for all $w$, then $B = A$.
6. $A\mathbf{0} = \mathbf{0}$
7. $O v = \mathbf{0}$
8. $I_n v = v$

Also, linearity holds: $A(c_1u_1 + \dots + c_ku_k) = c_1Au_1 + \dots + c_kAu_k$.

---

## 1.3 Systems of Linear Equations

### Definitions
- **Linear Equation**: $a_1x_1 + \dots + a_nx_n = b$.
- **System of Linear Equations**: A set of equations in the same variables. Can be written as $Ax = b$.
  - $A$: Coefficient matrix.
  - $x$: Vector of variables.
  - $b$: Constant vector.
- **Solution Set**: The set of all vectors satisfying the system.
- **Consistency**:
  - **Consistent**: Has one or more solutions.
  - **Inconsistent**: Has no solution.

### Elementary Row Operations
Used to solve systems by transforming the **augmented matrix** $[A \mid b]$.
1. **Interchange**: Swap any two rows.
2. **Scaling**: Multiply a row by a nonzero scalar.
3. **Row Addition**: Add a multiple of one row to another.

These operations produce **equivalent** systems (same solution set).

### Reduced Row Echelon Form (RREF)
A matrix is in RREF if:
1. Nonzero rows are above zero rows.
2. The leading entry of a nonzero row is in a column to the right of the leading entry of the preceding row.
3. Leading entries are 1.
4. If a column contains a leading 1, all other entries in that column are 0.

**Theorem 1.4**: Every matrix can be transformed into a unique matrix in RREF.

### Solving Systems
1. Form the augmented matrix $[A \mid b]$.
2. Convert to RREF $[R \mid c]$.
3. If a row $[0 \dots 0 \mid d]$ with $d \neq 0$ exists, the system is **inconsistent**.
4. Otherwise, identify **Basic Variables** (correspond to pivot columns) and **Free Variables**.
5. Express basic variables in terms of free variables to find the general solution.

---

## 1.4 Gaussian Elimination

### Terminology
- **Pivot Position**: Position of a leading entry in the RREF.
- **Pivot Column**: A column containing a pivot position.

### Algorithm
1. **Forward Pass**: Transform matrix to Row Echelon Form.
   - Find leftmost nonzero column (pivot column).
   - Move a nonzero entry to the top (pivot position).
   - Use row replacement to create zeros below the pivot.
   - Repeat for submatrices.
2. **Backward Pass**: Transform to RREF.
   - Make pivots 1 (scaling).
   - Create zeros above pivots (row replacement).

### Rank and Nullity
- **Rank ($rank A$)**: Number of nonzero rows in RREF (number of pivot columns).
- **Nullity ($nullity A$)**: $n - rank A$ (number of free variables).

**Consistency & Solutions**:
- A consistent system has a **unique solution** iff nullity is 0 (no free variables).
- A consistent system has **infinitely many solutions** iff nullity > 0.

---

## 1.6 The Span of a Set of Vectors

### Definition
The **span** of a set $S = \{u_1, \dots, u_k\}$ is the set of all linear combinations of these vectors.
$$ \text{Span } S = \{ c_1u_1 + \dots + c_ku_k \mid c_i \in \mathbb{R} \} $$
A vector $v$ is in Span $S$ iff $Ax = v$ is consistent (where columns of $A$ are $u_i$).

### Theorem 1.6: Equivalence
The following are equivalent for an $m \times n$ matrix $A$:
1. Span of columns of $A$ is $\mathbb{R}^m$.
2. $Ax = b$ is consistent for every $b \in \mathbb{R}^m$.
3. Rank of $A$ is $m$.
4. RREF of $A$ has no zero rows.
5. There is a pivot position in each row of $A$.

### Theorem 1.7
$\text{Span } \{u_1, \dots, u_k, v\} = \text{Span } \{u_1, \dots, u_k\}$ if and only if $v \in \text{Span } \{u_1, \dots, u_k\}$.

---

## 1.7 Linear Dependence and Linear Independence

### Definitions
- **Linearly Dependent**: Vectors $\{u_1, \dots, u_k\}$ are dependent if there exist scalars $c_1, \dots, c_k$ **not all zero** such that:
  $$ c_1u_1 + \dots + c_ku_k = \mathbf{0} $$
- **Linearly Independent**: The only solution to $c_1u_1 + \dots + c_ku_k = \mathbf{0}$ is the trivial solution $c_1 = \dots = c_k = 0$.

### Theorem 1.8: Equivalence for Independence
The following are equivalent for an $m \times n$ matrix $A$:
1. Columns of $A$ are linearly independent.
2. $Ax = b$ has **at most one** solution for each $b$.
3. Nullity of $A$ is 0.
4. Rank of $A$ is $n$.
5. Columns of RREF of $A$ are distinct standard vectors.
6. The only solution to $Ax = \mathbf{0}$ is $\mathbf{0}$.
7. There is a pivot position in each column of $A$.

### Properties
- A set containing the zero vector is linearly dependent.
- Two vectors are dependent iff one is a multiple of the other.
- If a subset contains more than $n$ vectors in $\mathbb{R}^n$, it is dependent.
- **Theorem 1.9**: Vectors are dependent iff one vector is a linear combination of the preceding ones (or the first is zero).

### Summary Table

| Rank of A | No. of Solutions to $Ax=b$ | Columns of A | RREF of A |
| :--- | :--- | :--- | :--- |
| **Rank A = m** | At least one solution for every $b$ | Generating set for $\mathbb{R}^m$ | Every row has a pivot |
| **Rank A = n** | At most one solution for every $b$ | Linearly independent | Every column has a pivot |