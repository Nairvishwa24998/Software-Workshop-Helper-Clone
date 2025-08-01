# %%

# %%
import sys

print(sys.version)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# %%

# %%
# ──── 1. Read TSV data ───────────────────────────────────────────────────────
print("=== Reading TSV data ===")
file1 = '/Users/melissazulle/Typing_project/safety_check/vertical_index/Index_angles_project.tsv'

try:
    # Read the TSV file
    df1 = pd.read_csv(file1, sep='\t', skiprows=11)  # skip 11 rows because the data starts at row 12
    print(f"Successfully loaded {len(df1)} rows and {len(df1.columns)} columns")
    print(f"First few columns: {list(df1.columns[:10])}")
except FileNotFoundError:
    print(f"File not found: {file1}")
    print("Please update the file path to point to your actual TSV file")

# %%

# ──── 2. Inspect columns and clean names ─────────────────────────────────────
# print("=== Column inspection ===")
print(f"Total columns: {len(df1.columns)}")

# Clean column names of any hidden characters
df1.columns = df1.columns.str.strip()

# Look for required marker columns
required_markers = ['R_Cout', 'R_Cin', 'R_I1', 'R_I2']
marker_coords = ['X', 'Y', 'Z']

print("\nChecking for required marker columns:")
for marker in required_markers:
    for coord in marker_coords:
        col_name = f"{marker} {coord}"
        if col_name in df1.columns:
            print(f" Found: {col_name} ")
        else:
            print(f" Missing: {col_name} ")

# %%

# %%
# ──── 3. Define calculation functions ────────────────────────────────────────
print("=== Defining calculation functions ===")


def midpoint(x1, y1, z1, x2, y2, z2):
    """Calculate midpoint between two 3D points"""
    xmid = (x1 + x2) / 2
    ymid = (y1 + y2) / 2
    zmid = (z1 + z2) / 2
    return xmid, ymid, zmid


def line_vector(x1, y1, z1, x2, y2, z2):
    """Calculate vector from point1 to point2"""
    vx = x2 - x1
    vy = y2 - y1
    vz = z2 - z1
    return vx, vy, vz


def angle_between_vectors(vx1, vy1, vz1, vx2, vy2, vz2):
    """Calculate angle between two 3D vectors in degrees"""
    # Calculate magnitudes
    mag1 = np.sqrt(vx1 ** 2 + vy1 ** 2 + vz1 ** 2)
    mag2 = np.sqrt(vx2 ** 2 + vy2 ** 2 + vz2 ** 2)

    dot = vx1 * vx2 + vy1 * vy2 + vz1 * vz2

    # Calculate angle (with clipping to avoid numerical errors)
    cos_theta = np.clip(dot / (mag1 * mag2), -1.0, 1.0)
    angle_rad = np.arccos(cos_theta)
    return np.degrees(angle_rad)


def plane_normal(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    """Calculate normal vector to a plane defined by three points for each frame."""
    # Stack coordinates into arrays of shape (n_frames, 3)
    p1 = np.stack([x1, y1, z1], axis=1)
    p2 = np.stack([x2, y2, z2], axis=1)
    p3 = np.stack([x3, y3, z3], axis=1)
    v1 = p2 - p1
    v2 = p3 - p1
    normals = np.cross(v1, v2)
    norms = np.linalg.norm(normals, axis=1, keepdims=True)
    # Avoid division by zero
    normals_normalized = np.divide(normals, norms, out=np.zeros_like(normals), where=norms != 0)
    return normals_normalized


# %%

# Example usage: calculate normal vector for each frame using R_Cout, R_Cin, R_I1
# normals = plane_normal(
#     df1['R_Cout X'], df1['R_Cout Y'], df1['R_Cout Z'],
#     df1['R_Cin X'], df1['R_Cin Y'], df1['R_Cin Z'],
#     df1['R_I1 X'], df1['R_I1 Y'], df1['R_I1 Z'],
#     df1['R_L1 X'], df1['R_L1 Y'], df1['R_L1 Z']
# )

# print("Calculated plane normals for each frame (shape: {})".format(normals.shape))

print("All functions defined successfully")

# %%
# ──── 4. Extract marker coordinates ──────────────────────────────────────────
print("=== Extracting marker coordinates ===")

# R_Cout and R_Cin coordinates
R_Cout_x = df1['R_Cout X']
R_Cout_y = df1['R_Cout Y']
R_Cout_z = df1['R_Cout Z']

R_Cin_x = df1['R_Cin X']
R_Cin_y = df1['R_Cin Y']
R_Cin_z = df1['R_Cin Z']

# R_I1 and R_I2 coordinates
R_I1_x = df1['R_I1 X']
R_I1_y = df1['R_I1 Y']
R_I1_z = df1['R_I1 Z']

R_I2_x = df1['R_I2 X']
R_I2_y = df1['R_I2 Y']
R_I2_z = df1['R_I2 Z']

# R_L1 coordinates
R_L1_x = df1['R_L1 X']
R_L1_y = df1['R_L1 Y']
R_L1_z = df1['R_L1 Z']

print("All marker coordinates extracted successfully")

# %%
# %%
# # ──── 5. Calculate midpoint between R_Cout and R_Cin ────────────────────────
print("=== Calculating midpoint ===")

# Midpoint between R_Cout and R_Cin
xmid, ymid, zmid = midpoint(R_Cout_x, R_Cout_y, R_Cout_z, R_Cin_x, R_Cin_y, R_Cin_z)
print(f"Calculated midpoints for {len(xmid)} frames")

# %%
# ──── 6. Calculate vectors ───────────────────────────────────────────────────
print("=== Calculating vectors ===")

# Vector 1: from plane (normal vector at each frame) to R_I1
# We'll use the plane's centroid (mean of the three points) as the reference point on the plane

# average of R_I1, R_L1, and the midpoint
plane_cx = (R_I1_x + R_L1_x + xmid) / 3
plane_cy = (R_I1_y + R_L1_y + ymid) / 3
plane_cz = (R_I1_z + R_L1_z + zmid) / 3

vx1, vy1, vz1 = line_vector(plane_cx, plane_cy, plane_cz, R_I1_x, R_I1_y, R_I1_z)
print("Vector 1 (plane centroid to R_I1) calculated")

# Vector 2: from R_I1 to R_I2
vx2, vy2, vz2 = line_vector(R_I1_x, R_I1_y, R_I1_z, R_I2_x, R_I2_y, R_I2_z)
print("Vector 2 (R_I1 to R_I2) calculated")

# %%

# ──── 7. Calculate angles ────────────────────────────────────────────────────
print("=== Calculating angles ===")

# Step 1: Calculate unsigned angle
angles = angle_between_vectors(vx1, vy1, vz1, vx2, vy2, vz2)
print(f"Successfully calculated {len(angles)} angles")
print(f"Sample angles: {angles[:5].values}")

# Step 2: Stack vectors to shape (n_frames, 3)
vec1 = np.stack([vx1, vy1, vz1], axis=1)
vec2 = np.stack([vx2, vy2, vz2], axis=1)

# Step 3: Cross product to get rotation axis
cross = np.cross(vec1, vec2)

# Step 4: Define your reference axis (Z-up)
reference_axis = np.array([0, 0, 1])

# Step 5: Dot product of cross product with reference axis to get sign
dot_with_ref = np.dot(cross, reference_axis)
sign = np.sign(dot_with_ref)

# Step 6: Apply sign to the angle
signed_angles = angles * sign

# Step 6b: Scale signed_angles to match ground truth Roll magnitude using Z-score normalization
gt_roll = df2['Roll'].values

# Compute statistics
gt_mean = np.mean(gt_roll)
gt_std = np.std(gt_roll)

calc_mean = np.mean(signed_angles)
calc_std = np.std(signed_angles)

# Scale using z-score formula
scaled_angles = ((signed_angles - calc_mean) / calc_std) * gt_std + gt_mean


# Step 7: Plot the signed angle
plt.plot(signed_angles, 'r-', label='Calculated', linewidth=2)

# %%
# ──── 8. Print angle statistics ──────────────────────────────────────────────
print("\n=== ANGLE STATISTICS ===")
print(f"Mean: {np.mean(angles):.2f}°")
print(f"Std:  {np.std(angles):.2f}°")
print(f"Min:  {np.min(angles):.2f}°")
print(f"Max:  {np.max(angles):.2f}°")
print(angles)
# %%


# %%
# Comparison with idx_prox columns
file2 = '/Users/melissazulle/Typing_project/safety_check/vertical_index/Index_angles_project_6D.tsv'

try:
    # Read the TSV file
    df2 = pd.read_csv(file2, sep='\t', skiprows=13)  # skip 13 rows because the data starts at row 14
except FileNotFoundError:
    print(f"File not found: {file2}")
    print("Please update the file path to point to your actual TSV file")

plt.plot(signed_angles, 'r-', label='Calculated', linewidth=2)
plt.plot(df2['Roll'], '-g')  # 'g' = green line for Roll comparison
plt.legend(['Calculated Angle', 'Ground Truth'])


