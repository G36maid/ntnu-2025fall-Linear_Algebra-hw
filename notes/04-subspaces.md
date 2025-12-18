# Chapter 4: Subspaces and their Properties

## 4.1 Subspaces

### Definition
A set $W$ of vectors in $\mathbb{R}^n$ is called a **subspace** of $\mathbb{R}^n$ if it satisfies three properties:
1. **Zero Vector**: $\mathbf{0} \in W$.
2. **Closed under Addition**: If $\mathbf{u}, \mathbf{v} \in W$, then $\mathbf{u} + \mathbf{v} \in W$.
3. **Closed under Scalar Multiplication**: If $\mathbf{u} \in W$ and $c$ is a scalar, then $c\mathbf{u} \in W$.

**Examples**:
- $\mathbb{R}^n$ itself is a subspace.
- The set $\{\mathbf{0}\}$ is the **zero subspace**.
- Any subspace other than $\{\mathbf{0}\}$ is a **nonzero subspace**.

### Theorem 4.1
The **span** of a finite nonempty subset of $\mathbb{R}^n$ is a subspace of $\mathbb{R}^n$.

### Subspaces Associated with a Matrix
For an $m \times n$ matrix $A$:

1. **Null Space ($\text{Null } A$)**:
   - The solution set of $Ax = \mathbf{0}$.
   - $\text{Null } A = \{ \mathbf{v} \in \mathbb{R}^n \mid A\mathbf{v} = \mathbf{0} \}$.
   - Subspace of $\mathbb{R}^n$ (Theorem 4.2).

2. **Column Space ($\text{Col } A$)**:
   - The span of the columns of $A$.
   - $\text{Col } A = \{ A\mathbf{v} \mid \mathbf{v} \in \mathbb{R}^n \}$.
   - Subspace of $\mathbb{R}^m$.

3. **Row Space ($\text{Row } A$)**:
   - The span of the rows of $A$.
   - Equivalent to $\text{Col } A^T$.
   - Subspace of $\mathbb{R}^n$.

### Subspaces Associated with a Linear Transformation
For $T: \mathbb{R}^n \to \mathbb{R}^m$:
- **Range of $T$**: Same as $\text{Col } A$ (Subspace of $\mathbb{R}^m$).
- **Null Space of $T$**: Same as $\text{Null } A$ (Subspace of $\mathbb{R}^n$).

---

## 4.2 Basis and Dimension

### Basis
Let $V$ be a nonzero subspace of $\mathbb{R}^n$. A **basis** for $V$ is a linearly independent generating set for $V$.
- **Standard Basis** for $\mathbb{R}^n$: $\mathcal{E} = \{ \mathbf{e}_1, \dots, \mathbf{e}_n \}$.
- The **pivot columns** of a matrix form a basis for its column space.

### Theorems on Bases
- **Reduction Theorem (4.3)**: A generating set can be reduced to a basis by removing vectors.
- **Extension Theorem (4.4)**: A linearly independent set can be extended to a basis. Every nonzero subspace has a basis.
- **Theorem 4.5**: Any two bases for a subspace $V$ contain the **same number** of vectors.

### Dimension
The **dimension** of a nonzero subspace $V$ ($\dim V$) is the number of vectors in a basis for $V$.
- $\dim \{\mathbf{0}\} = 0$.

### Theorems on Dimension
- **Theorem 4.6**: If $\dim V = k$, any subset of $V$ with more than $k$ vectors is linearly dependent.
- **Theorem 4.7**: Let $\dim V = k$ and $S$ be a subset of $V$ with exactly $k$ vectors. $S$ is a basis if:
  - $S$ is linearly independent, OR
  - $S$ generates $V$.

To show a set $\mathcal{B}$ is a basis for $V$:
1. Show $\mathcal{B} \subseteq V$.
2. Show $\mathcal{B}$ is linearly independent (or generates $V$).
3. Confirm $|\mathcal{B}| = \dim V$.

---

## 4.3 The Dimension of Subspaces Associated with a Matrix

### Rank and Nullity
- **Rank**: $\dim(\text{Col } A) = \text{rank } A$.
- **Nullity**: $\dim(\text{Null } A) = \text{nullity } A$.

### Row Space Properties
- A basis for $\text{Row } A$ is given by the **nonzero rows** of the reduced row echelon form (RREF) of $A$.
- $\dim(\text{Row } A) = \text{rank } A^T$.
- **Key Identity**: $\dim(\text{Row } A) = \dim(\text{Col } A) = \text{rank } A$.

### Rank-Nullity Relationship
For a linear transformation $T: \mathbb{R}^n \to \mathbb{R}^m$ (or matrix $A$):
$$ \dim(\text{Null } T) + \dim(\text{Range } T) = \dim(\text{Domain}) $$
$$ \text{nullity } A + \text{rank } A = n $$

### Theorem 4.9
If $V \subseteq W$ are subspaces of $\mathbb{R}^n$, then $\dim V \le \dim W$.
If $\dim V = \dim W$, then $V = W$.

### Summary Table

| Subspace | Basis Construction | Dimension | Containing Space |
| :--- | :--- | :--- | :--- |
| **Col A** | Pivot columns of $A$ | $\text{rank } A$ | $\mathbb{R}^m$ |
| **Null A** | Vectors from general solution of $Ax=\mathbf{0}$ | $n - \text{rank } A$ | $\mathbb{R}^n$ |
| **Row A** | Nonzero rows of RREF of $A$ | $\text{rank } A$ | $\mathbb{R}^n$ |

---

## 4.4 Coordinate Systems

### Theorem 4.10
Let $\mathcal{B} = \{\mathbf{b}_1, \dots, \mathbf{b}_k\}$ be a basis for subspace $V$. Any vector $\mathbf{v} \in V$ has a **unique** representation:
$$ \mathbf{v} = c_1\mathbf{b}_1 + \dots + c_k\mathbf{b}_k $$

### Coordinate Vector
For a basis $\mathcal{B} = \{\mathbf{b}_1, \dots, \mathbf{b}_n\}$ of $\mathbb{R}^n$, the **coordinate vector** of $\mathbf{v}$ relative to $\mathcal{B}$ is:
$$ [\mathbf{v}]_\mathcal{B} = \begin{bmatrix} c_1 \\ \vdots \\ c_n \end{bmatrix} $$

### Theorem 4.11
Let $B = [\mathbf{b}_1 \dots \mathbf{b}_n]$ be the matrix of basis vectors.
- $B[\mathbf{v}]_\mathcal{B} = \mathbf{v}$
- $[\mathbf{v}]_\mathcal{B} = B^{-1}\mathbf{v}$

---

## 4.5 Matrix Representations of Linear Operators

A linear transformation $T: \mathbb{R}^n \to \mathbb{R}^n$ is a **linear operator**.

### $\mathcal{B}$-Matrix
Let $\mathcal{B} = \{\mathbf{b}_1, \dots, \mathbf{b}_n\}$ be a basis for $\mathbb{R}^n$. The matrix representation of $T$ with respect to $\mathcal{B}$ is:
$$ [T]_\mathcal{B} = [[T(\mathbf{b}_1)]_\mathcal{B} \quad \dots \quad [T(\mathbf{b}_n)]_\mathcal{B}] $$

Properties:
- $[T(\mathbf{v})]_\mathcal{B} = [T]_\mathcal{B} [\mathbf{v}]_\mathcal{B}$
- If $\mathcal{B} = \mathcal{E}$ (standard basis), $[T]_\mathcal{E} = A$ (standard matrix).

### Theorem 4.12: Similarity
Let $A$ be the standard matrix of $T$, and $B$ be the matrix with basis vectors $\mathcal{B}$ as columns.
$$ [T]_\mathcal{B} = B^{-1}AB $$
$$ A = B[T]_\mathcal{B}B^{-1} $$

Matrices $A$ and $C$ are **similar** if $C = P^{-1}AP$ for some invertible $P$.
- The $\mathcal{B}$-matrix of an operator is similar to its standard matrix.