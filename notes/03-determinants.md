# Chapter 3: Determinants

## 3.1 Cofactor Expansion

### 2x2 Matrices
For a matrix $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$:
- The **determinant** is $\det A = ad - bc$.
- $A$ is invertible if and only if $\det A \neq 0$.
- If invertible, $A^{-1} = \frac{1}{\det A} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$.

### General Definition (Recursive)
- For a $1 \times 1$ matrix $[a]$, $\det [a] = a$.
- For $n \ge 2$, the determinant is defined using **cofactors**.

**Definitions**:
- **Minor**: The determinant of the $(n-1) \times (n-1)$ submatrix $A_{ij}$ obtained by removing row $i$ and column $j$.
- **Cofactor ($C_{ij}$)**: $C_{ij} = (-1)^{i+j} \det A_{ij}$.

### Theorem 3.1: Cofactor Expansion
The determinant can be computed by expanding along any row $i$:
$$ \det A = \sum_{j=1}^n a_{ij}C_{ij} = a_{i1}C_{i1} + a_{i2}C_{i2} + \dots + a_{in}C_{in} $$

(Note: Expansion works along columns as well, due to Theorem 3.4c).

### Theorem 3.2: Triangular Matrices
The determinant of an upper triangular or lower triangular matrix is the **product of its diagonal entries**.
$$ \det A = a_{11} a_{22} \dots a_{nn} $$

**Block Matrix Property**:
$$ \det \begin{bmatrix} A & B \\ O & I_n \end{bmatrix} = \det A $$

---

## 3.2 Properties of Determinants

### Theorem 3.3: Row Operations
Let $A$ be an $n \times n$ matrix.
1. **Row Interchange**: If $B$ is obtained by swapping two rows of $A$, then $\det B = -\det A$.
2. **Row Scaling**: If $B$ is obtained by multiplying a row of $A$ by scalar $k$, then $\det B = k \det A$.
3. **Row Addition**: If $B$ is obtained by adding a multiple of one row to another, then $\det B = \det A$.
4. **Elementary Matrices**: $\det(EA) = (\det E)(\det A)$.

### Computing Determinants via Reduction
If $A$ is transformed into an upper triangular matrix $U$ using row operations (without scaling), and $r$ is the number of row interchanges performed:
$$ \det A = (-1)^r (u_{11}u_{22}\dots u_{nn}) $$

### Theorem 3.4: Algebraic Properties
Let $A$ and $B$ be square matrices of the same size.
1. $A$ is invertible if and only if $\det A \neq 0$.
2. $\det(AB) = (\det A)(\det B)$.
3. $\det(A^T) = \det A$.
4. If $A$ is invertible, $\det(A^{-1}) = \frac{1}{\det A}$.

### Block Matrices
If $M$ is partitioned as $M = \begin{bmatrix} A & B \\ O & C \end{bmatrix}$ (where $O$ is a zero matrix), then:
$$ \det M = (\det A)(\det C) $$

### Theorem 3.5: Cramer's Rule
Let $A$ be an invertible $n \times n$ matrix and $b \in \mathbb{R}^n$. The unique solution $x$ to $Ax = b$ has components:
$$ x_i = \frac{\det M_i}{\det A} $$
where $M_i$ is the matrix obtained by replacing the $i$-th column of $A$ with vector $b$.