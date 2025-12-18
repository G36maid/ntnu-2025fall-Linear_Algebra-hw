# Chapter 2: Matrices and Linear Transformations

## 2.1 Matrix Multiplication

### Definitions
Let $A$ be an $m \times n$ matrix and $B$ be an $n \times p$ matrix. The product $AB$ is the $m \times p$ matrix whose columns are $Ab_1, Ab_2, \dots, Ab_p$, where $b_j$ is the $j$-th column of $B$.
$$ C = AB = [Ab_1 \quad Ab_2 \quad \dots \quad Ab_p] $$

### Properties
- **Associativity**:
  - $A(Bv) = (AB)v$ for any vector $v$.
  - $(AB)C = A(BC)$ (Associative law of matrix multiplication).
- **Non-Commutativity**: Generally, $AB \neq BA$.
- **Row-Column Rule**: The $(i,j)$-entry of $AB$ is the dot product of the $i$-th row of $A$ and the $j$-th column of $B$:
  $$ (AB)_{ij} = \sum_{k=1}^n a_{ik}b_{kj} $$

### Theorem 2.1: Algebraic Properties
Let $A, B$ be $k \times m$, $C$ be $m \times n$, and $P, Q$ be $n \times p$.
1. $s(AC) = (sA)C = A(sC)$
2. $A(CP) = (AC)P$
3. $(A+B)C = AC + BC$ (Right distributive)
4. $C(P+Q) = CP + CQ$ (Left distributive)
5. $I_k A = A = A I_m$
6. Multiplication by zero matrix results in zero matrix.
7. $(AC)^T = C^T A^T$

### Special Matrices
- **Diagonal Matrix**: A square matrix where all non-diagonal entries are zero.
- **Symmetric Matrix**: A square matrix $A$ where $A^T = A$.
  - Example: Diagonal matrices are symmetric.
  - $(AB)^T = B^T A^T$.

---

## 2.3 Invertibility and Elementary Matrices

### Invertibility
An $n \times n$ matrix $A$ is **invertible** if there exists an $n \times n$ matrix $B$ such that:
$$ AB = BA = I_n $$
$B$ is called the inverse of $A$, denoted $A^{-1}$.
- If $A$ is invertible, $Ax=b$ has the unique solution $x = A^{-1}b$.

### Theorem 2.2: Properties of Inverses
1. $(A^{-1})^{-1} = A$
2. $(AB)^{-1} = B^{-1}A^{-1}$
3. $(A^T)^{-1} = (A^{-1})^T$

### Elementary Matrices
An **elementary matrix** is obtained by performing a single elementary row operation on the identity matrix $I$.
- **Theorem**: If $E$ is an elementary matrix, $EA$ is the result of performing the same row operation on $A$.
- Elementary matrices are invertible, and their inverses are also elementary matrices.

### Theorem 2.3
If $A$ has reduced row echelon form (RREF) $R$, there exists an invertible matrix $P$ such that $PA = R$.
- $P$ is a product of elementary matrices.

### The Column Correspondence Property
If a column $j$ of the RREF $R$ is a linear combination of other columns of $R$, then column $j$ of the original matrix $A$ is the *same* linear combination of the corresponding columns of $A$.

**Theorem 2.4**:
1. The pivot columns of $A$ are linearly independent.
2. Each non-pivot column of $A$ is a linear combination of the previous pivot columns (coefficients come from the RREF).

---

## 2.4 The Inverse of a Matrix

### Determining Invertibility
**Theorem 2.5**: An $n \times n$ matrix $A$ is invertible if and only if its RREF is $I_n$.

### Algorithm for Matrix Inversion
1. Form the augmented matrix $[A \mid I_n]$.
2. Row reduce to RREF $[R \mid B]$.
3. If $R = I_n$, then $B = A^{-1}$.
4. If $R \neq I_n$, $A$ is not invertible.

### Theorem 2.6: The Invertible Matrix Theorem
For an $n \times n$ matrix $A$, the following are equivalent:
1. $A$ is invertible.
2. RREF of $A$ is $I_n$.
3. Rank $A = n$.
4. Span of columns of $A$ is $\mathbb{R}^n$.
5. $Ax = b$ is consistent for every $b \in \mathbb{R}^n$.
6. Nullity $A = 0$.
7. Columns of $A$ are linearly independent.
8. The only solution to $Ax = 0$ is $0$.
9. There exists $B$ such that $BA = I_n$ or $AC = I_n$.
10. $A$ is a product of elementary matrices.

---

## 2.5 Partitioned Matrices and Block Multiplication

Matrices can be partitioned into **blocks**. Multiplication works on blocks similarly to scalars, provided the dimensions match.
$$ A = \begin{bmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{bmatrix}, \quad B = \begin{bmatrix} B_{11} \\ B_{21} \end{bmatrix} \implies AB = \begin{bmatrix} A_{11}B_{11} + A_{12}B_{21} \\ A_{21}B_{11} + A_{22}B_{21} \end{bmatrix} $$

### Outer Product
For vectors $u \in \mathbb{R}^m, v \in \mathbb{R}^n$, the outer product is $uv^T$ (an $m \times n$ matrix with rank $\le 1$).
$$ AB = \sum_{i=1}^n (\text{col}_i(A))(\text{row}_i(B)) $$

---

## 2.6 The LU Decomposition

A factorization $A = LU$ where:
- $L$: Unit lower triangular matrix (diagonal entries are 1).
- $U$: Upper triangular matrix (often the row echelon form).

### Algorithm
1. Reduce $A$ to row echelon form $U$ using only row replacements (adding a multiple of one row to another below it).
2. Construct $L$:
   - Diagonal entries are 1.
   - If row operation is $R_i \leftarrow R_i - c R_j$, then $L_{ij} = c$.
   - Entries not determined by operations are 0.

### Application
Solve $Ax = b$ efficiently:
1. Solve $Ly = b$ for $y$ (Forward substitution).
2. Solve $Ux = y$ for $x$ (Backward substitution).

---

## 2.7 Linear Transformations and Matrices

### Definitions
- **Function**: $f: S_1 \to S_2$ maps domain $S_1$ to codomain $S_2$.
- **Image**: $f(v)$.
- **Range**: Set of all images.
- **Matrix Transformation**: $T_A(x) = Ax$.

### Linear Transformation
A function $T: \mathbb{R}^n \to \mathbb{R}^m$ is linear if:
1. $T(u+v) = T(u) + T(v)$
2. $T(cu) = cT(u)$

**Properties (Theorem 2.8)**:
- $T(0) = 0$
- $T(-u) = -T(u)$
- $T(au+bv) = aT(u) + bT(v)$

### Theorem 2.9: The Standard Matrix
Every linear transformation $T: \mathbb{R}^n \to \mathbb{R}^m$ corresponds to a unique $m \times n$ matrix $A$:
$$ A = [T(e_1) \quad T(e_2) \quad \dots \quad T(e_n)] $$
such that $T(x) = Ax$.

---

## 2.8 Composition and Invertibility of Linear Transformations

### Properties of $T$ and Matrix $A$
- **Range of $T$**: Span of the columns of $A$.
- **Onto (Surjective)**: Range is $\mathbb{R}^m$.
  - Equivalent to: Columns of $A$ generate $\mathbb{R}^m$.
  - Equivalent to: Rank $A = m$.
- **One-to-One (Injective)**: $T(u)=T(v) \implies u=v$.
  - Equivalent to: Null space contains only $0$.
  - Equivalent to: Columns of $A$ are linearly independent.
  - Equivalent to: Rank $A = n$.

### Composition
If $T: \mathbb{R}^n \to \mathbb{R}^m$ (matrix $A$) and $U: \mathbb{R}^m \to \mathbb{R}^p$ (matrix $B$), then $U \circ T$ is linear with standard matrix $BA$.
$$ (U \circ T)(x) = B(Ax) = (BA)x $$

### Invertibility (Theorem 2.13)
$T$ is invertible iff its standard matrix $A$ is invertible.
- $T$ is invertible $\iff T$ is both one-to-one and onto $\iff n=m$ and Rank $A = n$.
- The standard matrix of $T^{-1}$ is $A^{-1}$.

### Summary Table

| Property of T | Solutions to $Ax=b$ | Columns of A | Rank of A |
| :--- | :--- | :--- | :--- |
| **Onto** | At least one solution for every $b$ | Generating set for $\mathbb{R}^m$ | Rank $A = m$ |
| **One-to-One** | At most one solution for every $b$ | Linearly independent | Rank $A = n$ |
| **Invertible** | Unique solution for every $b$ | Linearly independent generating set | Rank $A = n = m$ |