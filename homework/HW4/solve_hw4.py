import sympy as sp


def solve_q1():
    print("\n--- Question 1 ---")
    # Plane W: x + 2y - 3z = 0
    # Normal vector n
    n = sp.Matrix([1, 2, -3])

    # Basis B
    b1 = sp.Matrix([-2, 1, 0])
    b2 = sp.Matrix([3, 0, 1])
    b3 = sp.Matrix([1, 2, -3])  # This is n

    # (a) Find Tw(v) for v in B
    # Since b1 and b2 are in W (check dot product with n), Tw(b1) = b1, Tw(b2) = b2
    # Since b3 is normal to W, Tw(b3) = -b3

    print(f"Check if b1 in W: {n.dot(b1) == 0}")
    print(f"Check if b2 in W: {n.dot(b2) == 0}")
    print(f"Check if b3 is normal: {b3 == n}")

    # So Tw_B (Matrix representation relative to B) is diagonal
    # (c) [Tw]_B
    Tw_B = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -1]])
    print(f"[Tw]_B = \n{Tw_B}")

    # (d) Standard matrix A
    # A = P * [Tw]_B * P^-1 where P is the change of basis matrix from B to standard basis
    P = sp.Matrix.hstack(b1, b2, b3)
    A = P * Tw_B * P.inv()
    print(f"Standard Matrix A = \n{A}")

    # (e) Explicit formula
    x1, x2, x3 = sp.symbols("x1 x2 x3")
    v = sp.Matrix([x1, x2, x3])
    Tv = A * v
    print(f"T(v) = \n{Tv}")


def solve_q3():
    print("\n--- Question 3 ---")
    A = sp.Matrix([[-4, 6, 0], [0, 2, 0], [-5, 5, 1]])
    eigenvals = A.eigenvals()
    eigenvects = A.eigenvects()
    print(f"Eigenvalues: {eigenvals}")
    print("Eigenvectors:")
    for val, mult, basis in eigenvects:
        print(f"Lambda = {val}, Multiplicity = {mult}, Basis = {basis}")


def solve_q4():
    print("\n--- Question 4 ---")
    A = sp.Matrix([[-2, 3, 6], [-2, -8, -2], [6, -1, 4]])
    char_poly = A.charpoly()
    print(f"Characteristic Polynomial: {char_poly.as_expr()}")

    eigenvects = A.eigenvects()
    print("Eigenvectors:")

    P_cols = []
    D_diag = []

    is_diagonalizable = True
    for val, mult, basis in eigenvects:
        print(f"Lambda = {val}, Multiplicity = {mult}, Basis = {basis}")
        if len(basis) != mult:
            is_diagonalizable = False
        for vec in basis:
            P_cols.append(vec)
            D_diag.append(val)

    if is_diagonalizable and len(P_cols) == 3:
        P = sp.Matrix.hstack(*P_cols)
        D = sp.diag(*D_diag)
        print(f"P = \n{P}")
        print(f"D = \n{D}")
        print(f"Check A == PDP^-1: {A == P * D * P.inv()}")
    else:
        print("Not diagonalizable")


def solve_q6():
    print("\n--- Question 6 ---")
    A = sp.Matrix([[4, -5, 0], [0, -1, 0], [0, 0, -1]])
    eigenvects = A.eigenvects()
    print(f"Eigenvalues: {A.eigenvals()}")

    is_diagonalizable = True
    total_dim = 0
    for val, mult, basis in eigenvects:
        print(f"Lambda = {val}, Multiplicity = {mult}, Basis = {basis}")
        total_dim += len(basis)

    if total_dim == 3:
        print("Diagonalizable. Basis B is the union of bases for eigenspaces.")
    else:
        print("Not diagonalizable.")


def solve_q7():
    print("\n--- Question 7 ---")
    c = sp.symbols("c")
    # T(x)
    # [ 1  2 -1 ]
    # [ 0  c  0 ]
    # [ 6 -1  6 ]
    A = sp.Matrix([[1, 2, -1], [0, c, 0], [6, -1, 6]])
    # Characteristic polynomial given as -(t-c)(t-3)(t-4)
    # Roots are c, 3, 4

    # We need to check cases where eigenvalues are repeated.
    # Case 1: c = 3
    # Case 2: c = 4

    # If c != 3 and c != 4, then we have 3 distinct eigenvalues => diagonalizable.

    # Check c = 3
    print("Checking c = 3:")
    A3 = A.subs(c, 3)
    print(f"Eigenvalues for c=3: {A3.eigenvals()}")
    print(f"Eigenvectors for c=3: {A3.eigenvects()}")

    # Check c = 4
    print("Checking c = 4:")
    A4 = A.subs(c, 4)
    print(f"Eigenvalues for c=4: {A4.eigenvals()}")
    print(f"Eigenvectors for c=4: {A4.eigenvects()}")


def solve_q8():
    print("\n--- Question 8 ---")
    # T(au + bv + cw) = au + bv - cw
    # Basis B = {u, v, w}
    # T(u) = u
    # T(v) = v
    # T(w) = -w

    # Matrix representation [T]_B relative to basis B itself (which are eigenvectors)
    T_B = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -1]])
    print(f"[T]_B = \n{T_B}")
    print(f"Eigenvalues: {T_B.eigenvals()}")
    print(f"Is diagonalizable: {T_B.is_diagonalizable()}")


if __name__ == "__main__":
    solve_q1()
    solve_q3()
    solve_q4()
    solve_q6()
    solve_q7()
    solve_q8()
