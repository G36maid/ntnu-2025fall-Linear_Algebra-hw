# Chapter 7: Orthogonality

## 7.1 The Geometry of Vectors

### Norm and Dot Product
- **Norm (Length)**: For a vector $v \in \mathbb{R}^n$, the norm is $\|v\| = \sqrt{v_1^2 + \dots + v_n^2}$.
- **Unit Vector**: A vector with norm 1. Any nonzero vector can be **normalized** by $u = \frac{v}{\|v\|}$.
- **Distance**: The distance between $u$ and $v$ is $\|u - v\|$.
- **Dot Product**: $u \cdot v = u^T v = \sum_{i=1}^n u_i v_i$.

**Properties (Theorem 7.1)**:
1. $u \cdot u = \|u\|^2 \ge 0$, and $u \cdot u = 0 \iff u = \mathbf{0}$.
2. $u \cdot v = v \cdot u$.
3. $u \cdot (v+w) = u \cdot v + u \cdot w$.
4. $(cu) \cdot v = c(u \cdot v)$.

### Orthogonality
Vectors $u$ and $v$ are **orthogonal** (perpendicular) if $u \cdot v = 0$.
- **Pythagorean Theorem (Theorem 7.2)**: $u$ and $v$ are orthogonal iff $\|u+v\|^2 = \|u\|^2 + \|v\|^2$.

### Inequalities
- **Cauchy-Schwarz Inequality**: $|u \cdot v| \le \|u\| \|v\|$.
- **Triangle Inequality**: $\|u + v\| \le \|u\| + \|v\|$.

---

## 7.2 Orthogonal Vectors

### Definitions
- **Orthogonal Set**: A set of vectors where every distinct pair is orthogonal.
- **Orthonormal Set**: An orthogonal set consisting of unit vectors.

**Theorem 7.5**: Any orthogonal set of nonzero vectors is linearly independent.

### Orthogonal Basis
If $\mathcal{B} = \{v_1, \dots, v_k\}$ is an orthogonal basis for subspace $W$, any $u \in W$ is:
$$ u = \sum_{i=1}^k \frac{u \cdot v_i}{\|v_i\|^2} v_i $$
If $\mathcal{B}$ is **orthonormal**:
$$ u = \sum_{i=1}^k (u \cdot v_i) v_i $$

### The Gram-Schmidt Process (Theorem 7.6)
Converts a basis $\{u_1, \dots, u_k\}$ into an orthogonal basis $\{v_1, \dots, v_k\}$:
1. $v_1 = u_1$
2. $v_2 = u_2 - \frac{u_2 \cdot v_1}{\|v_1\|^2}v_1$
3. $v_3 = u_3 - \frac{u_3 \cdot v_1}{\|v_1\|^2}v_1 - \frac{u_3 \cdot v_2}{\|v_2\|^2}v_2$
4. $\dots$

### QR Factorization
If $A$ is an $m \times n$ matrix with linearly independent columns, then $A = QR$:
- $Q$: An $m \times n$ matrix with orthonormal columns (columns form an orthonormal basis for Col $A$).
- $R$: An $n \times n$ upper triangular matrix with positive diagonal entries.

---

## 7.3 Orthogonal Projections

### Orthogonal Complement ($W^\perp$)
The set of all vectors orthogonal to every vector in subspace $W$.
- $W^\perp$ is a subspace.
- $(\text{Row } A)^\perp = \text{Null } A$.
- $(\text{Col } A)^\perp = \text{Null } A^T$.
- $\dim W + \dim W^\perp = n$.

### Orthogonal Decomposition (Theorem 7.7)
Any $u \in \mathbb{R}^n$ can be uniquely written as $u = w + z$, where $w \in W$ and $z \in W^\perp$.
- $w$ is called the **orthogonal projection** of $u$ on $W$ ($U_W(u)$).
- If $\{v_1, \dots, v_k\}$ is an orthonormal basis for $W$:
  $$ w = (u \cdot v_1)v_1 + \dots + (u \cdot v_k)v_k $$

### Projection Matrix ($P_W$)
The standard matrix such that $P_W u = w$.
- **Theorem 7.8**: If columns of matrix $C$ form a basis for $W$:
  $$ P_W = C(C^T C)^{-1} C^T $$
- If columns of $U$ form an **orthonormal** basis for $W$:
  $$ P_W = UU^T $$

**Closest Vector Property**: The projection $w = P_W u$ is the vector in $W$ closest to $u$ (minimizes $\|u - w\|$).

---

## 7.4 Least-Squares Approximation

### The Method of Least Squares
Given $Ax = b$ (typically inconsistent), find $x$ to minimize the error $\|Ax - b\|$.
This is equivalent to solving $Ax = \hat{b}$, where $\hat{b} = P_{\text{Col } A} b$.

### Normal Equations
To find the least-squares solution, solve:
$$ A^T A x = A^T b $$
- If columns of $A$ are linearly independent, $A^T A$ is invertible, and $x = (A^T A)^{-1} A^T b$.

---

## 7.5 Orthogonal Matrices and Operators

### Orthogonal Matrix
A square matrix $Q$ is orthogonal if its columns form an orthonormal basis.

**Theorem 7.9 (Equivalent Conditions)**:
1. $Q$ is orthogonal.
2. $Q^T Q = I$ ($Q$ is invertible and $Q^{-1} = Q^T$).
3. Preserves dot products: $(Qu) \cdot (Qv) = u \cdot v$.
4. Preserves norms: $\|Qu\| = \|u\|$.

### Rigid Motions
A transformation $F$ is a rigid motion if it preserves distances: $\|F(u) - F(v)\| = \|u - v\|$.
- Every rigid motion on $\mathbb{R}^n$ is a composition of an orthogonal operator and a translation.

---

## 7.6 Symmetric Matrices

### Properties
A matrix $A$ is **symmetric** if $A^T = A$.
- **Theorem 7.14**: Eigenvectors corresponding to distinct eigenvalues are orthogonal.
- **Theorem 7.15**: $A$ is symmetric iff there is an **orthonormal basis** of eigenvectors.
  $$ A = PDP^T $$
  where $P$ is an orthogonal matrix and $D$ is diagonal.

### Spectral Decomposition (Theorem 7.16)
$$ A = \lambda_1 P_1 + \lambda_2 P_2 + \dots + \lambda_n P_n $$
where $P_i = u_i u_i^T$ is the projection matrix onto the eigenspace of $\lambda_i$.

---

## 7.7 Singular Value Decomposition (SVD)

### Theorem 7.18
Any $m \times n$ matrix $A$ of rank $k$ can be factored as:
$$ A = U \Sigma V^T $$
- $U$: $m \times m$ orthogonal matrix (Left singular vectors).
- $V$: $n \times n$ orthogonal matrix (Right singular vectors).
- $\Sigma$: $m \times n$ "diagonal" matrix with singular values $\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_k > 0$.
  - $\sigma_i = \sqrt{\lambda_i(A^T A)}$.

### Pseudoinverse ($A^\dagger$)
Also called the Moore-Penrose generalized inverse.
$$ A^\dagger = V \Sigma^\dagger U^T $$
where $\Sigma^\dagger$ is obtained by transposing $\Sigma$ and inverting the nonzero singular values.

**Applications**:
- **Least Norm Solution**: For $Ax=b$, the vector $z = A^\dagger b$ minimizes $\|Az - b\|$. If multiple solutions exist, it is the one with minimum norm.
- **Projection**: $P_{\text{Col } A} = A A^\dagger$.