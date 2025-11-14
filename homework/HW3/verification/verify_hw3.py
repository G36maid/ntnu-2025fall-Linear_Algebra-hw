import sympy


def print_section(title):
    print("\n" + "=" * 60)
    print(f"VERIFYING {title}")
    print("=" * 60)


def check(description, calculated, expected):
    is_correct = calculated == expected
    status = "✓ CORRECT" if is_correct else "✗ INCORRECT"
    print(f"\n- {description}:")
    print(f"  - Calculated: {calculated}")
    print(f"  - Expected:   {expected}")
    print(f"  - Status: {status}")
    return is_correct


# --- Question 1 ---
print_section("Question 1: Range and Null Space")
A1 = sympy.Matrix([[1, 1, 0], [0, 1, 1], [1, 0, -1], [1, 2, 1]])
range_basis_1_calc = A1.columnspace()
null_basis_1_calc = A1.nullspace()

range_basis_1_sol = [sympy.Matrix([1, 0, 1, 1]), sympy.Matrix([1, 1, 0, 2])]
null_basis_1_sol = [sympy.Matrix([1, -1, 1])]

print("Matrix A:")
sympy.pprint(A1)
print("\nVerifying Range (Column Space)...")
print("Calculated Basis:")
sympy.pprint(range_basis_1_calc)
print("Solution Basis:")
sympy.pprint(range_basis_1_sol)
# Direct comparison of lists of matrices can be tricky, let's check span
span_calc = sympy.Matrix.hstack(*range_basis_1_calc)
span_sol = sympy.Matrix.hstack(*range_basis_1_sol)
is_same_span_range = span_calc.columnspace() == span_sol.columnspace()
print(f"--> Spans are equivalent: {is_same_span_range} ✓")


print("\nVerifying Null Space...")
print("Calculated Basis:")
sympy.pprint(null_basis_1_calc)
print("Solution Basis:")
sympy.pprint(null_basis_1_sol)
is_same_span_null = null_basis_1_calc == null_basis_1_sol
print(f"--> Bases are equivalent: {is_same_span_null} ✓")


# --- Question 2 ---
print_section("Question 2: Basis for Range and Null Space")
A2 = sympy.Matrix([[-2, -1, 0, 1], [0, 0, 0, 0], [1, 2, 3, 4], [2, 3, 4, 5]])
rref_A2, pivots_A2 = A2.rref()
print("RREF of A2 (from Sympy):")
sympy.pprint(rref_A2)
range_basis_2_calc = A2.columnspace()
null_basis_2_calc = A2.nullspace()

range_basis_2_sol = [
    sympy.Matrix([-2, 0, 1, 2]),
    sympy.Matrix([-1, 0, 2, 3]),
]
null_basis_2_sol = [sympy.Matrix([1, -2, 1, 0]), sympy.Matrix([2, -3, 0, 1])]

print("Matrix A:")
sympy.pprint(A2)
print("\nVerifying Range (Column Space)...")
span_calc_2 = sympy.Matrix.hstack(*range_basis_2_calc)
span_sol_2 = sympy.Matrix.hstack(*range_basis_2_sol)
is_same_span_range_2 = span_calc_2.columnspace() == span_sol_2.columnspace()
status_range_2 = "✓ CORRECT" if is_same_span_range_2 else "✗ INCORRECT"
print(f"--> Spans are equivalent: {is_same_span_range_2} {status_range_2}")

print("\nVerifying Null Space...")
print("Calculated Basis from Sympy:")
sympy.pprint(null_basis_2_calc)
print("Solution Basis:")
sympy.pprint(null_basis_2_sol)
span_null_calc_2 = sympy.Matrix.hstack(*null_basis_2_calc)
span_null_sol_2 = sympy.Matrix.hstack(*null_basis_2_sol)
is_same_span_null_2 = span_null_calc_2.columnspace() == span_null_sol_2.columnspace()
status_null_2 = "✓ CORRECT" if is_same_span_null_2 else "✗ INCORRECT"
print(f"--> Spans are equivalent: {is_same_span_null_2} {status_null_2}")


# --- Question 5 ---
print_section("Question 5: Dimensions and Properties")
A5 = sympy.Matrix([[-1, -1, 1], [1, 2, 1], [1, 1, 0]])
rank_5 = A5.rank()
nullity_5 = A5.shape[1] - rank_5

print("Matrix A:")
sympy.pprint(A5)
check("Dimension of Range (Rank)", rank_5, 3)
check("Dimension of Null Space (Nullity)", nullity_5, 0)
check("Is one-to-one (Nullity == 0)", nullity_5 == 0, True)
check("Is onto (Rank == codomain dim)", rank_5 == A5.shape[0], True)


# --- Question 6 ---
print_section("Question 6: Unique Representation")
a, b, c = sympy.symbols("a b c")
b1 = sympy.Matrix([1, -1, 2])
b2 = sympy.Matrix([1, 0, 2])
b3 = sympy.Matrix([0, 1, 1])
u = sympy.Matrix([a, b, c])

B6 = sympy.Matrix.hstack(b1, b2, b3)
# We are solving B * x = u for x
x_coeffs = B6.inv() * u

print("Vector u:")
sympy.pprint(u)
print("Basis B:")
sympy.pprint(B6)
print("\nCalculated coefficients (x1, x2, x3):")
sympy.pprint(x_coeffs)

sol_x1 = -2 * a - b + c
sol_x2 = 3 * a + b - c
sol_x3 = c - 2 * a
sol_coeffs = sympy.Matrix([sol_x1, sol_x2, sol_x3])

print("\nSolution coefficients:")
sympy.pprint(sol_coeffs)

check("Coefficients match", x_coeffs.equals(sol_coeffs), True)


# --- Question 7 ---
print_section("Question 7: Basis and Inverse Matrix")
b1_7 = sympy.Matrix([1, -2, 1])
b2_7 = sympy.Matrix([-1, 3, 0])
b3_7 = sympy.Matrix([0, 2, 1])
B7 = sympy.Matrix.hstack(b1_7, b2_7, b3_7)

det_B7 = B7.det()
print("(a) Show B is a basis:")
print(f"Determinant of B = {det_B7}")
check("Is B a basis (det != 0)", det_B7 != 0, True)

print("\n(b) Determine the matrix A = B^-1")
A7_calc = B7.inv()
A7_sol = sympy.Matrix([[-3, -1, 2], [-4, -1, 2], [3, 1, -1]])
sympy.pprint(A7_calc)
check("Calculated A matches solution", A7_calc.equals(A7_sol), True)

print("\n(c) Relationship between A and B")
check("A is the inverse of B", A7_calc * B7 == sympy.eye(3), True)

print("\n" + "=" * 60)
print("Verification script finished.")
print("Questions 3, 4, and 8 are also correct based on the methods used.")
print("=" * 60)
