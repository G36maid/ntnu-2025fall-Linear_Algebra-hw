#!/usr/bin/env python3
"""
Find the correct value of r for Question 7 - Linear Dependence
"""

def determinant_4x4_with_r(r):
    """Calculate determinant of 4x4 matrix with parameter r"""
    # Matrix formed by the vectors:
    # [1,  0, -1, -1]
    # [0, -1,  2,  9]
    # [-1, 2,  1,  r]
    # [1,  1,  0, -2]

    matrix = [
        [1,  0, -1, -1],
        [0, -1,  2,  9],
        [-1, 2,  1,  r],
        [1,  1,  0, -2]
    ]

    def det_3x3(m):
        return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) -
                m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) +
                m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))

    def minor_3x3(matrix, row, col):
        return [[matrix[i][j] for j in range(4) if j != col]
                for i in range(4) if i != row]

    det = 0
    for col in range(4):
        minor = minor_3x3(matrix, 0, col)
        det += ((-1) ** col) * matrix[0][col] * det_3x3(minor)

    return det

def solve_for_r():
    """Find r by expanding determinant symbolically"""
    # Let's expand the determinant manually
    # Using cofactor expansion along first row:
    # det = 1 * minor(0,0) - 0 * minor(0,1) + (-1) * minor(0,2) + (-1) * minor(0,3)

    # minor(0,0) = det of:
    # [-1,  2,  9]
    # [ 2,  1,  r]
    # [ 1,  0, -2]
    minor_00 = [
        [-1,  2,  9],
        [ 2,  1,  r],
        [ 1,  0, -2]
    ]

    def det_3x3_symbolic(m, r_val=None):
        if r_val is not None:
            # Substitute r value
            m = [[m[i][j] if m[i][j] != 'r' else r_val for j in range(3)] for i in range(3)]

        if any('r' in str(cell) for row in m for cell in row):
            # Handle symbolic case
            # For our specific minor_00:
            # det = -1 * (1 * (-2) - r * 0) - 2 * (2 * (-2) - r * 1) + 9 * (2 * 0 - 1 * 1)
            # det = -1 * (-2) - 2 * (-4 - r) + 9 * (-1)
            # det = 2 - 2*(-4 - r) - 9
            # det = 2 + 8 + 2r - 9
            # det = 1 + 2r
            return f"1 + 2*r"
        else:
            return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) -
                    m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) +
                    m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))

    print("Calculating determinant symbolically...")
    print("Matrix:")
    matrix = [
        [1,  0, -1, -1],
        [0, -1,  2,  9],
        [-1, 2,  1, 'r'],
        [1,  1,  0, -2]
    ]

    for row in matrix:
        print("  ", row)

    print("\nExpanding along first row:")
    print("det = 1 * minor(0,0) + 0 * minor(0,1) + (-1) * minor(0,2) + (-1) * minor(0,3)")

    # Calculate each minor
    # minor(0,0):
    print("\nminor(0,0) =")
    minor_00 = [
        [-1,  2,  9],
        [ 2,  1, 'r'],
        [ 1,  0, -2]
    ]
    for row in minor_00:
        print("  ", row)

    # Manually calculate: det = -1*(1*(-2) - r*0) - 2*(2*(-2) - r*1) + 9*(2*0 - 1*1)
    # = -1*(-2) - 2*(-4-r) + 9*(-1)
    # = 2 + 8 + 2r - 9
    # = 1 + 2r
    print("det(minor(0,0)) = 1 + 2r")

    # minor(0,2):
    print("\nminor(0,2) =")
    minor_02 = [
        [ 0, -1,  9],
        [-1,  2, 'r'],
        [ 1,  1, -2]
    ]
    for row in minor_02:
        print("  ", row)

    # det = 0*(2*(-2) - r*1) - (-1)*((-1)*(-2) - r*1) + 9*((-1)*1 - 2*1)
    # = 0 + 1*(2 - r) + 9*(-3)
    # = 2 - r - 27
    # = -25 - r
    print("det(minor(0,2)) = -25 - r")

    # minor(0,3):
    print("\nminor(0,3) =")
    minor_03 = [
        [ 0, -1,  2],
        [-1,  2,  1],
        [ 1,  1,  0]
    ]
    for row in minor_03:
        print("  ", row)

    # det = 0*(2*0 - 1*1) - (-1)*((-1)*0 - 1*1) + 2*((-1)*1 - 2*1)
    # = 0 + 1*(0 - 1) + 2*(-1 - 2)
    # = -1 + 2*(-3)
    # = -1 - 6 = -7
    print("det(minor(0,3)) = -7")

    print("\nCombining:")
    print("det = 1*(1 + 2r) + 0 + (-1)*(-25 - r) + (-1)*(-7)")
    print("det = 1 + 2r + 25 + r + 7")
    print("det = 33 + 3r")

    print("\nFor linear dependence, det = 0:")
    print("33 + 3r = 0")
    print("3r = -33")
    print("r = -11")

    return -11

def verify_result(r_value):
    """Verify that the given r value makes vectors linearly dependent"""
    print(f"\nVerifying r = {r_value}:")

    matrix = [
        [1,  0, -1, -1],
        [0, -1,  2,  9],
        [-1, 2,  1,  r_value],
        [1,  1,  0, -2]
    ]

    print("Matrix with r =", r_value)
    for row in matrix:
        print("  ", row)

    det = determinant_4x4_with_r(r_value)
    print(f"Determinant = {det}")
    print(f"Is determinant zero? {abs(det) < 1e-10}")

    # Also check rank using Gaussian elimination
    rank = get_rank(matrix)
    print(f"Rank = {rank}")
    print(f"Vectors are linearly dependent? {rank < 4}")

def get_rank(matrix):
    """Calculate rank using Gaussian elimination"""
    m = [row[:] for row in matrix]  # Deep copy
    rows, cols = len(m), len(m[0])

    for i in range(min(rows, cols)):
        # Find pivot
        max_row = i
        for k in range(i+1, rows):
            if abs(m[k][i]) > abs(m[max_row][i]):
                max_row = k

        # Swap rows
        m[i], m[max_row] = m[max_row], m[i]

        # Skip if pivot is zero
        if abs(m[i][i]) < 1e-10:
            continue

        # Eliminate column
        for k in range(i+1, rows):
            if abs(m[k][i]) < 1e-10:
                continue
            factor = m[k][i] / m[i][i]
            for j in range(i, cols):
                m[k][j] -= factor * m[i][j]

    rank = 0
    for row in m:
        if any(abs(x) > 1e-10 for x in row):
            rank += 1
    return rank

if __name__ == "__main__":
    print("=" * 60)
    print("FINDING CORRECT VALUE OF r FOR QUESTION 7")
    print("=" * 60)

    print("Vectors:")
    vectors = [
        [1,  0, -1,  1],
        [0, -1,  2,  1],
        [-1, 1,  1,  0],
        [-1, 9, 'r', -2]
    ]

    for i, v in enumerate(vectors):
        print(f"v{i+1} = {v}")

    print("\nNote: The matrix is formed by placing vectors as COLUMNS")
    print("So we need the transpose for our calculation:")

    r_correct = solve_for_r()
    verify_result(r_correct)

    print("\n" + "=" * 60)
    print(f"CORRECT ANSWER: r = {r_correct}")
    print("=" * 60)
