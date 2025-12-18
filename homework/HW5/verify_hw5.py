import numpy as np


def verify_q1():
    print("\n--- Question 1 Verification (Random Matrix) ---")
    m, n = 4, 3
    A = np.random.randn(m, n)
    # (a) Null spaces
    # Null(A) = {x | Ax=0}. Null(ATA) = {x | ATAx=0}.
    # Check if a vector in Null(A) is in Null(ATA) (trivial)
    # Check if a vector in Null(ATA) is in Null(A)
    # Hard to pick random vector in null space numerically exactly, but can check rank.

    rank_A = np.linalg.matrix_rank(A)
    ATA = A.T @ A
    rank_ATA = np.linalg.matrix_rank(ATA)

    print(f"Rank(A): {rank_A}")
    print(f"Rank(ATA): {rank_ATA}")
    assert rank_A == rank_ATA
    print("Rank(A) == Rank(ATA) verified.")

def verify_q2():
    print("\n--- Question 2 Verification ---")
    v1 = np.array([1, -1, 0, 2], dtype=float)
    v2 = np.array([1, 1, 1, 3], dtype=float)
    v3 = np.array([3, 1, 1, 5], dtype=float)

    Sigma = [v1, v2, v3]
    A = np.column_stack(Sigma)
    b = np.array([8, 0, 1, 11], dtype=float)

    print("Matrix A:")
    print(A)

    # (a) Gram-Schmidt
    u1 = v1
    e1 = u1 / np.linalg.norm(u1)

    u2 = v2 - np.dot(v2, e1) * e1 # This is projection onto e1 (which is direction of u1)
    # Wait, Gram-Schmidt usually formulated as subtracting projections onto previous u's.
    # proj_u1 v2 = (v2 . u1 / u1 . u1) * u1 = (v2 . e1) * e1. Correct.
    e2 = u2 / np.linalg.norm(u2)

    u3 = v3 - np.dot(v3, e1) * e1 - np.dot(v3, e2) * e2
    e3 = u3 / np.linalg.norm(u3)

    Q_calc = np.column_stack([e1, e2, e3])
    print("\nCalculated Q (Orthonormal Basis):")
    print(Q_calc)

    # Check orthogonality
    print("Q^T Q (should be Identity):")
    print(np.round(Q_calc.T @ Q_calc, 5))

    # (b) QR Factorization
    # A = QR => R = Q^T A
    R_calc = Q_calc.T @ A
    print("\nCalculated R:")
    print(np.round(R_calc, 5))

    print("Q @ R (should be A):")
    print(np.round(Q_calc @ R_calc, 5))

    # (c) Solve Ax = b => QRx = b => Rx = Q^T b
    # Solve Rx = y where y = Q^T b
    y = Q_calc.T @ b
    # R is upper triangular, can use back substitution, or just linalg.solve (since R is square 3x3 if we consider full QR? No, reduced QR m x n).
    # A is 4x3. Q is 4x3. R is 3x3.
    # Ax = b is overdetermined (4 eqs, 3 vars). Wait, b might be in Col(A).
    # Let's check if b is in Col(A).
    # If b is in Col(A), then Ax=b has exact solution.
    # If not, we are finding least squares? The problem says "solve the system", implying it's consistent.

    # Using np.linalg.solve on Rx = y
    x_sol = np.linalg.solve(R_calc, y)
    print("\nSolution x:")
    print(x_sol)

    print("Check Ax - b (should be 0 if consistent):")
    print(np.round(A @ x_sol - b, 5))

def verify_q4():
    print("\n--- Question 4 Verification ---")
    u = np.array([1, 3, -2], dtype=float)
    # W: x1 + 2x2 - 3x3 = 0
    #    x1 + x2 - 3x3 = 0
    # Subtracting: x2 = 0.
    # Substitute x2=0 into eq2: x1 - 3x3 = 0 => x1 = 3x3.
    # General solution: x = [3t, 0, t] = t[3, 0, 1].
    # Basis for W: b1 = [3, 0, 1].
    b1 = np.array([3, 0, 1], dtype=float)

    # (a) P_W
    # P_W = A(ATA)^-1 AT where cols of A are basis for W.
    # Here A = column vector b1.
    # P_W = b1 (b1^T b1)^-1 b1^T = (b1 b1^T) / (b1^T b1)
    b1_col = b1.reshape(-1, 1)
    P_W = (b1_col @ b1_col.T) / (b1.T @ b1)
    print("Projection Matrix P_W:")
    print(P_W)

    # (b) w in W, z in W_perp. w = P_W u. z = u - w.
    w = P_W @ u
    z = u - w
    print("\nVector w (in W):")
    print(w)
    print("Vector z (in W_perp):")
    print(z)

    # Check orthogonality
    print(f"w dot z: {np.dot(w, z)}")
    # Check w is in W (proportional to b1)
    print(f"w / b1: {w/b1}") # Should be constant (ignoring div by zero if any)

    # (c) Distance from u to W
    dist = np.linalg.norm(z)
    print(f"\nDistance from u to W: {dist}")

def verify_q6():
    print("\n--- Question 6 Verification ---")
    A = np.array([[1, 2], [1, -1], [2, 1]], dtype=float)
    b = np.array([1, 3, 1], dtype=float)

    # (a) Find z minimizing ||Az - b||. Least squares solution.
    # z = (ATA)^-1 AT b
    ATA = A.T @ A
    ATb = A.T @ b
    z_ls = np.linalg.solve(ATA, ATb)

    print("Least squares solution z:")
    print(z_ls)

    min_norm = np.linalg.norm(A @ z_ls - b)
    print(f"Minimum error ||Az - b||: {min_norm}")

    # (b) Find vector z of least norm for which ||Az-b|| is min.
    # Check if ATA is invertible (full rank).
    print(f"Rank of A: {np.linalg.matrix_rank(A)}")
    print(f"Condition of ATA: {np.linalg.cond(ATA)}")
    # Since rank is 2 (cols are independent), LS solution is unique.
    # So the LS solution IS the solution of least norm.
    # If rank < 2, we would use pseudoinverse.
    z_pinv = np.linalg.pinv(A) @ b
    print("Solution using pseudoinverse (should match):")
    print(z_pinv)

def verify_q7():
    print("\n--- Question 7 Verification ---")
    v = (1/np.sqrt(10)) * np.array([3, 1, 0], dtype=float)
    w = (1/np.sqrt(5)) * np.array([0, -2, 1], dtype=float)

    print(f"Norm v: {np.linalg.norm(v)}")
    print(f"Norm w: {np.linalg.norm(w)}")

    # Construct orthogonal operator T.
    # Reflection across hyperplane orthogonal to v - w.
    # u_ref = v - w
    u_ref = v - w
    # Householder matrix H = I - 2 (u u^T) / (u^T u)
    u_col = u_ref.reshape(-1, 1)
    H = np.eye(3) - 2 * (u_col @ u_col.T) / (u_ref.T @ u_ref)

    print("Matrix T (Householder reflection):")
    print(H)

    print("Check T is orthogonal (T^T T = I):")
    print(np.round(H.T @ H, 5))

    print("Check T(v) = w:")
    Tv = H @ v
    print(f"T(v): {Tv}")
    print(f"w:    {w}")
    print(f"Diff: {np.linalg.norm(Tv - w)}")

def verify_q8():
    print("\n--- Question 8 Verification ---")
    A = np.array([[0, 2, 2], [2, 0, 2], [2, 2, 0]], dtype=float)

    vals, vecs = np.linalg.eigh(A)
    # eigh returns sorted eigenvalues and orthonormal eigenvectors for symmetric matrices.

    print("Eigenvalues:")
    print(vals)
    print("Eigenvectors (columns):")
    print(vecs)

    # Spectral decomposition
    # A = sum(lambda_i * u_i * u_i^T)
    A_reconst = np.zeros_like(A)
    for i in range(len(vals)):
        u = vecs[:, i].reshape(-1, 1)
        A_reconst += vals[i] * (u @ u.T)

    print("\nReconstructed A from spectral decomposition:")
    print(np.round(A_reconst, 5))
    print("Diff from original A:")
    print(np.linalg.norm(A - A_reconst))

if __name__ == "__main__":
    verify_q1()
    verify_q2()
    verify_q4()
    verify_q6()
    verify_q7()
    verify_q8()
