# Homework 3 Official Solutions

## Question 1 (16%)
**Problem:** Find generating sets for the range and null space of linear transformation $T$.

**Solution:**
The standard matrix of linear transformation $T$ is $A = [T(\mathbf{e}_1) \quad T(\mathbf{e}_2) \quad T(\mathbf{e}_3)]$:
$$
A = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & -1 \\ 1 & 2 & 1 \end{bmatrix}
$$

The reduced row echelon form (RREF) of $A$ is:
$$
R = \begin{bmatrix} 1 & 0 & -1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}
$$

**(i) Range of T**
The range of $T$ equals the column space of $A$. The pivots are in columns 1 and 2.
A generating set for the range of $T$ is:
$$
\left\{ \begin{bmatrix} 1 \\ 0 \\ 1 \\ 1 \end{bmatrix}, \begin{bmatrix} 1 \\ 1 \\ 0 \\ 2 \end{bmatrix}, \begin{bmatrix} 0 \\ 1 \\ -1 \\ 1 \end{bmatrix} \right\} \quad \text{or simply} \quad \left\{ \begin{bmatrix} 1 \\ 0 \\ 1 \\ 1 \end{bmatrix}, \begin{bmatrix} 1 \\ 1 \\ 0 \\ 2 \end{bmatrix} \right\}
$$

**(ii) Null Space of T**
The null space is the solution to $A\mathbf{x} = \mathbf{0}$. From RREF, $x_1 - x_3 = 0$ and $x_2 + x_3 = 0$.
Let $x_3 = 1$, then $x_1 = 1, x_2 = -1$.
A generating set for the null space of $T$ is:
$$
\left\{ \begin{bmatrix} 1 \\ -1 \\ 1 \end{bmatrix} \right\}
$$

---

## Question 2 (12%)
**Problem:** Given a linear transformation $T$, find a basis for the range and null space.

**Solution:**
**(a) Basis for the range of T**
The standard matrix of $T$ is:
$$
A = \begin{bmatrix} -2 & -1 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 1 & 2 & 3 & 4 \\ 2 & 3 & 4 & 5 \end{bmatrix}
$$
The reduced row echelon form of $A$ is:
$$
R = \begin{bmatrix} 1 & 0 & -1 & -2 \\ 0 & 1 & 2 & 3 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}
$$
The pivots correspond to the first two columns. Thus, a basis for the range of $T$ is:
$$
\left\{ \begin{bmatrix} -2 \\ 0 \\ 1 \\ 2 \end{bmatrix}, \begin{bmatrix} -1 \\ 0 \\ 2 \\ 3 \end{bmatrix} \right\}
$$

**(b) Basis for the null space of T**
The null space is $\{ \mathbf{x} \in \mathbb{R}^4 ; A\mathbf{x} = \mathbf{0} \}$. From RREF:
$x_1 - x_3 - 2x_4 = 0 \implies x_1 = x_3 + 2x_4$
$x_2 + 2x_3 + 3x_4 = 0 \implies x_2 = -2x_3 - 3x_4$
The general solution is:
$$
\mathbf{x} = x_3 \begin{bmatrix} 1 \\ -2 \\ 1 \\ 0 \end{bmatrix} + x_4 \begin{bmatrix} 2 \\ -3 \\ 0 \\ 1 \end{bmatrix}
$$
Basis for the null space:
$$
\left\{ \begin{bmatrix} 1 \\ -2 \\ 1 \\ 0 \end{bmatrix}, \begin{bmatrix} 2 \\ -3 \\ 0 \\ 1 \end{bmatrix} \right\}
$$

---

## Question 3 (12%)
**Problem:** Find a basis for the subspace $V$ that contains $L$.

**Solution:**
We form a matrix with the vector from $L$ followed by the generators of $V$.
Augmented matrix leads to a row echelon form identifying the pivot columns.
Based on the provided solution, the basis for the subspace $V$ that contains $L$ is:
$$
\left\{ \begin{bmatrix} 0 \\ 0 \\ 1 \\ 0 \end{bmatrix}, \begin{bmatrix} 1 \\ -1 \\ -3 \\ 2 \end{bmatrix}, \begin{bmatrix} -3 \\ 1 \\ 3 \\ 2 \end{bmatrix} \right\}
$$

---

## Question 4 (12%)
**Problem:** Given a linearly independent subset $L$ of subspace $V$, find a basis for $V$ containing $L$.

**Solution:**
From the pivot columns of the augmented matrix (columns of $L$ followed by generators of $V$), which has the row echelon form:
$$
R = \begin{bmatrix} 1 & 0 & 1/7 & 2/7 & \dots \\ 0 & 1 & 8/7 & 9/7 & \dots \\ 0 & 0 & 0 & 0 & \dots \\ 0 & 0 & 0 & 0 & \dots \end{bmatrix}
$$
We select the columns corresponding to the pivots. The resulting basis for $V$ containing $L$ is:
$$
\left\{ \begin{bmatrix} -1 \\ -1 \\ 6 \\ -7 \end{bmatrix}, \begin{bmatrix} 5 \\ -9 \\ -2 \\ -1 \end{bmatrix}, \begin{bmatrix} 1 \\ -2 \\ 0 \\ 1 \end{bmatrix} \right\}
$$

---

## Question 5 (12%)
**Problem:** For linear transformation $T$, determine dimensions and injectivity/surjectivity.

**Solution:**
The standard matrix of $T$ is:
$$
A = \begin{bmatrix} -1 & -1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 0 \end{bmatrix}
$$
Row echelon form:
$$
\begin{bmatrix} -1 & -1 & 1 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{bmatrix}
$$
**(a)** $\text{rank } A = 3$. Dimension of Range(T) is 3.
**(b)** Nullity is $3 - 3 = 0$. Dimension of Null(T) is 0.
**(c)** Since Nullity is 0, $T$ is **one-to-one**. Since Rank equals dimension of codomain (3), $T$ is **onto**. Thus, $T$ is bijective.

---

## Question 6 (12%)
**Problem:** Find the unique representation of $\mathbf{u} = [a, b, c]^T$ as a linear combination of basis vectors.

**Solution:**
By Theorem 4.11, $[\mathbf{u}]_\mathcal{B} = B^{-1}\mathbf{u}$, where $B = [\mathbf{b}_1 \mathbf{b}_2 \mathbf{b}_3]$.
$$
[\mathbf{u}]_\mathcal{B} = \begin{bmatrix} 1 & 1 & 0 \\ -1 & 0 & 1 \\ 2 & 1 & 1 \end{bmatrix}^{-1} \begin{bmatrix} a \\ b \\ c \end{bmatrix} = \begin{bmatrix} -2 & -1 & 1 \\ 3 & 1 & -1 \\ -2 & 0 & 1 \end{bmatrix} \begin{bmatrix} a \\ b \\ c \end{bmatrix}
$$
$$
= \begin{bmatrix} -2a - b + c \\ 3a + b - c \\ -2a + c \end{bmatrix}
$$
That is, $\mathbf{u} = (-2a - b + c)\mathbf{b}_1 + (3a + b - c)\mathbf{b}_2 + (-2a + c)\mathbf{b}_3$.

---

## Question 7 (12%)
**Problem:** Let $\mathcal{B} = \{b_1, b_2, b_3\}$. (a) Show basis. (b) Matrix A. (c) Relationship.

**Solution:**
**(a)** Let $B = [b_1 \quad b_2 \quad b_3]$. The reduced row echelon form of $B$ is $I_3$. Since $\text{rank } B = 3$, $\mathcal{B}$ is a linearly independent subset of $\mathbb{R}^3$ containing 3 vectors, hence a basis.

**(b)** $A = [[e_1]_\mathcal{B} \quad [e_2]_\mathcal{B} \quad [e_3]_\mathcal{B}] = B^{-1}I_3 = B^{-1}$.
$$
A = \begin{bmatrix} 2 & -3 & -1 \\ -4 & -1 & 2 \\ 3 & 1 & -1 \end{bmatrix}
$$

**(c)** $A = B^{-1}$ as shown in (b).

---

## Question 8 (12%)
**Problem:** Compute $[\mathbf{v}]_\mathcal{B}$ given $[\mathbf{v}]_\mathcal{A}$.

**Solution:**
Let $A = [u_1 \dots u_n]$ and $B = [u_1 \quad u_1+u_2 \quad \dots \quad u_1+u_n]$.
Then
$$
B = A \begin{bmatrix} 1 & 1 & \dots & 1 \\ 0 & 1 & \dots & 0 \\ \vdots & & \ddots & \vdots \\ 0 & 0 & \dots & 1 \end{bmatrix}
$$
Since $[\mathbf{v}]_\mathcal{B} = B^{-1}\mathbf{v}$:
$$
B^{-1}\mathbf{v} = \left( A \begin{bmatrix} 1 & 1 & \dots & 1 \\ 0 & 1 & \dots & 0 \\ \vdots & & \ddots & \vdots \\ 0 & 0 & \dots & 1 \end{bmatrix} \right)^{-1} \mathbf{v}
$$
$$
= \begin{bmatrix} 1 & -1 & \dots & -1 \\ 0 & 1 & \dots & 0 \\ \vdots & & \ddots & \vdots \\ 0 & 0 & \dots & 1 \end{bmatrix} A^{-1}\mathbf{v}
$$
Given $[\mathbf{v}]_\mathcal{A} = A^{-1}\mathbf{v} = [a_1, a_2, \dots, a_n]^T$:
$$
[\mathbf{v}]_\mathcal{B} = \begin{bmatrix} 1 & -1 & \dots & -1 \\ 0 & 1 & \dots & 0 \\ \vdots & & \ddots & \vdots \\ 0 & 0 & \dots & 1 \end{bmatrix} \begin{bmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{bmatrix} = \begin{bmatrix} a_1 - a_2 - \dots - a_n \\ a_2 \\ \vdots \\ a_n \end{bmatrix}
$$