# Chapter 5: Eigenvalues, Eigenvectors, and Diagonalization

## 5.1 Eigenvalues and Eigenvectors

### Definitions
- **For a Linear Operator $T$ on $\mathbb{R}^n$**:
  A nonzero vector $v$ in $\mathbb{R}^n$ is an **eigenvector** of $T$ if $T(v) = \lambda v$ for some scalar $\lambda$. The scalar $\lambda$ is the **eigenvalue** corresponding to $v$.

- **For an $n \times n$ Matrix $A$**:
  A nonzero vector $v$ in $\mathbb{R}^n$ is an **eigenvector** of $A$ if $Av = \lambda v$ for some scalar $\lambda$.
  
  The eigenvectors and eigenvalues of a linear operator are the same as those of its standard matrix.

### Properties
- An eigenvector corresponds to exactly one eigenvalue.
- If $v$ is an eigenvector for $\lambda$, then any nonzero multiple $cv$ is also an eigenvector for $\lambda$.
- **Finding Eigenvectors**: The eigenvectors corresponding to $\lambda$ are the nonzero solutions of the homogeneous system:
  $$ (A - \lambda I_n)x = \mathbf{0} $$

### Eigenspace
The set of all solutions to $(A - \lambda I_n)x = \mathbf{0}$ (including the zero vector) is called the **eigenspace** of $A$ corresponding to $\lambda$.
- It is the null space of $(A - \lambda I_n)$.
- It is a subspace of $\mathbb{R}^n$.

---

## 5.2 The Characteristic Polynomial

### Finding Eigenvalues
For $\lambda$ to be an eigenvalue, there must exist a nonzero $v$ such that $(A - \lambda I_n)v = \mathbf{0}$. By the Invertible Matrix Theorem, this implies $A - \lambda I_n$ is **not invertible**, so its determinant must be zero.

**Characteristic Equation**:
$$ \det(A - \lambda I_n) = 0 $$

- **Characteristic Polynomial**: $p(t) = \det(A - tI_n)$. This is a polynomial of degree $n$.
- The eigenvalues are the roots of the characteristic polynomial.
- For triangular matrices, eigenvalues are the diagonal entries.

### Multiplicity
The **(algebraic) multiplicity** of an eigenvalue $\lambda$ is the largest integer $k$ such that $(t - \lambda)^k$ is a factor of the characteristic polynomial.

**Theorem 5.1**:
The dimension of the eigenspace corresponding to $\lambda$ (geometric multiplicity) is less than or equal to the algebraic multiplicity of $\lambda$.

### Similar Matrices
Matrices $A$ and $B$ are **similar** if $B = P^{-1}AP$ for some invertible $P$.
- Similar matrices have the same characteristic polynomial.
- They have the same eigenvalues with the same multiplicities.
- Their corresponding eigenspaces have the same dimension.

---

## 5.3 Diagonalization of Matrices

### Definition
An $n \times n$ matrix $A$ is **diagonalizable** if it is similar to a diagonal matrix $D$. That is, there exists an invertible matrix $P$ and a diagonal matrix $D$ such that:
$$ A = PDP^{-1} \quad (\text{or } D = P^{-1}AP) $$

### Theorem 5.2
An $n \times n$ matrix $A$ is diagonalizable if and only if there is a **basis for $\mathbb{R}^n$ consisting of eigenvectors** of $A$.
- The columns of $P$ are the eigenvectors.
- The diagonal entries of $D$ are the corresponding eigenvalues.

### Theorem 5.3
Eigenvectors corresponding to **distinct eigenvalues** are linearly independent.
- Corollary: If an $n \times n$ matrix has $n$ distinct eigenvalues, it is diagonalizable.

### Algorithm for Diagonalization
1. Find eigenvalues of $A$.
2. Find linearly independent eigenvectors for each eigenvalue (bases for eigenspaces).
3. If the total number of independent eigenvectors is $n$, form $P$ with these vectors as columns.
4. Form $D$ with corresponding eigenvalues on the diagonal.

### Test for Diagonalization
An $n \times n$ matrix $A$ is diagonalizable if and only if:
1. The sum of algebraic multiplicities of its eigenvalues is $n$ (all roots are real, if working in $\mathbb{R}$).
2. For each eigenvalue $\lambda$, **Geometric Multiplicity = Algebraic Multiplicity**.
   $$ \dim(\text{Null }(A - \lambda I_n)) = \text{multiplicity of } \lambda $$

---

## 5.4 Diagonalization of Linear Operators

A linear operator $T$ is diagonalizable if there is a basis $\mathcal{B}$ for $\mathbb{R}^n$ consisting of eigenvectors of $T$.
- The matrix representation of $T$ relative to this basis, $[T]_\mathcal{B}$, is a diagonal matrix.
- $[T]_\mathcal{B} = B^{-1}AB$, where $A$ is the standard matrix and $B$ is the matrix of basis vectors.

---

## 5.5 Applications

### Markov Chains
- **Transition Matrix**: A square matrix with non-negative entries where columns sum to 1.
- **Regular Matrix**: A transition matrix $A$ where $A^m$ has all positive entries for some $m$.

**Theorem 5.4**:
If $A$ is a regular transition matrix:
1. 1 is an eigenvalue of $A$.
2. There is a unique probability vector $v$ (steady-state vector) corresponding to eigenvalue 1.
3. The sequence $A^m p$ converges to $v$ as $m \to \infty$ for any probability vector $p$.