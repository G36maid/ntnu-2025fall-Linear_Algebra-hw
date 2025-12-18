# Homework 1 Official Solutions

## Question 1 (11%)
**Problem:** Determine whether the following system is consistent.

**Solution:**
Apply Gaussian elimination method to the augmented matrix $[A \mid \mathbf{b}]$.
The reduced row echelon form is $[R \mid \mathbf{c}]$.
The system is **consistent**.
The solution set is given by:
$$
\begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \\ x_5 \end{bmatrix} =
\begin{bmatrix} -3 \\ 0 \\ 0 \\ -1 \\ 0 \end{bmatrix} +
x_2 \begin{bmatrix} 1 \\ 1 \\ 0 \\ 0 \\ 0 \end{bmatrix} +
x_3 \begin{bmatrix} 0 \\ 0 \\ 1 \\ 0 \\ 0 \end{bmatrix} +
x_5 \begin{bmatrix} 2 \\ 0 \\ 0 \\ -2 \\ 1 \end{bmatrix}
$$
where $x_2, x_3, x_5$ are free variables.

---

## Question 2 (11%)
**Problem:** Find the rank and nullity of the matrix.

**Solution:**
The row echelon form of the given matrix has 3 pivot columns (or rows).
Thus:
*   **Rank**: 3
*   **Nullity**: 2

---

## Question 3 (14%)
**Problem:** Input-output matrix for an economy with sectors of metals, nonmetals, and services.

**Solution:**
**(a) Net Production**
Given gross production vector $\mathbf{x} = [50, 60, 40]^T$ and input-output matrix $C$:
$$
C = \begin{bmatrix} 0.2 & 0.2 & 0.1 \\ 0.4 & 0.4 & 0.2 \\ 0.2 & 0.2 & 0.1 \end{bmatrix}
$$
The net production is $\mathbf{x} - C\mathbf{x}$:
$$
\begin{bmatrix} 50 \\ 60 \\ 40 \end{bmatrix} - \begin{bmatrix} 0.2 & 0.2 & 0.1 \\ 0.4 & 0.4 & 0.2 \\ 0.2 & 0.2 & 0.1 \end{bmatrix} \begin{bmatrix} 50 \\ 60 \\ 40 \end{bmatrix} = \begin{bmatrix} 50 \\ 60 \\ 40 \end{bmatrix} - \begin{bmatrix} 26 \\ 52 \\ 26 \end{bmatrix} = \begin{bmatrix} 24 \\ 8 \\ 14 \end{bmatrix}
$$
Result: $24 million metals, $8 million nonmetals, $14 million services.

**(b) Gross Production Required**
Solve for $\mathbf{x}$ in $(I - C)\mathbf{x} = \mathbf{d}$ (or $\mathbf{x}(I-C) = \mathbf{d}^T$ depending on convention, solution implies standard):
Target demand $\mathbf{d} = [120, 180, 150]^T$.
The solution is:
$$
\mathbf{x} = \begin{bmatrix} 370 \\ 680 \\ 400 \end{bmatrix}
$$
Result: $370 million metals, $680 million nonmetals, $400 million services.

---

## Question 4 (11%)
**Problem:** Prove that elementary row operations preserve linear independence of rows.

**Solution:**
*   **Fact 1:** Row interchange permutes the set of rows, preserving independence.
*   **Fact 2:** Scaling a row by non-zero scalar $c$ preserves independence.

**Proof for Row Addition:**
Let rows of $A$ be $\mathbf{u}_1, \dots, \mathbf{u}_m$.
Suppose $B$ is obtained by adding $d$ times row $j$ to row $k$. The rows of $B$ are $\mathbf{u}_1, \dots, d\mathbf{u}_j + \mathbf{u}_k, \dots, \mathbf{u}_m$.
Consider the linear combination:
$$ c_1\mathbf{u}_1 + \dots + c_k(d\mathbf{u}_j + \mathbf{u}_k) + \dots + c_m\mathbf{u}_m = \mathbf{0} $$
Rearranging terms for the original basis $\mathbf{u}_i$:
$$ c_1\mathbf{u}_1 + \dots + (c_j + c_k d)\mathbf{u}_j + \dots + c_k\mathbf{u}_k + \dots + c_m\mathbf{u}_m = \mathbf{0} $$
Since $\mathbf{u}_i$ are linearly independent, all coefficients must be 0:
1.  $c_i = 0$ for all $i \neq j$.
2.  Specifically, $c_k = 0$.
3.  $c_j + c_k d = 0 \implies c_j + 0 = 0 \implies c_j = 0$.
Thus, all $c_i = 0$, proving the rows of $B$ are linearly independent.

---

## Question 5 (20%)
**Problem:** Let $A$ be an $m \times n$ matrix with reduced row echelon form $R$.

**Solution:**
(a) $[R \quad 0]$
(b) $[r_1 \quad r_2 \quad \dots \quad r_k]$ (Pivots of R)
(c) $R$
(d) $[I_m \quad A]$
(e) $[R \quad cR]$

---

## Question 6 (11%)
**Problem:** Determine whether the equation is consistent for all b.

**Solution:**
**No.**
By Theorem 1.6, the reduced row echelon form of $A$ has one zero row.

---

## Question 7 (11%)
**Problem:** Determine value of $r$ for which vectors are linearly dependent.

**Solution:**
Apply elementary row operations to the matrix formed by the vectors:
$$
\begin{bmatrix} 1 & -1 & -1 \\ 0 & 2 & r+17 \\ 0 & 0 & -r-9 \\ 0 & 0 & 0 \end{bmatrix}
$$
The rank of the matrix is less than 3 (vectors are linearly dependent) if and only if the last pivot is zero.
$$ -r - 9 = 0 \implies r = -9 $$
The vectors are linearly dependent iff $r = -9$.

---

## Question 8 (11%)
**Problem:** Show that $\text{Span}\{\mathbf{u}_1, \dots, \mathbf{u}_k\} = \text{Span}\{c_1\mathbf{u}_1, \dots, c_k\mathbf{u}_k\}$ for $c_i \neq 0$.

**Solution:**
Let $S = \text{Span}\{\mathbf{u}_1, \dots, \mathbf{u}_k\}$ and $S' = \text{Span}\{c_1\mathbf{u}_1, \dots, c_k\mathbf{u}_k\}$.

1.  **$S \subseteq S'$**:
    Any vector $\mathbf{v} \in S$ is $\mathbf{v} = \sum a_i \mathbf{u}_i$.
    We can rewrite this as $\mathbf{v} = \sum \frac{a_i}{c_i} (c_i \mathbf{u}_i)$.
    Since this is a linear combination of vectors in $S'$, $\mathbf{v} \in S'$.

2.  **$S' \subseteq S$**:
    Any vector $\mathbf{w} \in S'$ is $\mathbf{w} = \sum d_i (c_i \mathbf{u}_i)$.
    We can rewrite this as $\mathbf{w} = \sum (d_i c_i) \mathbf{u}_i$.
    Since this is a linear combination of vectors in $S$, $\mathbf{w} \in S$.

Therefore, $S = S'$.