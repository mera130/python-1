import math
angle = float(input("Enter angle in degrees: "))
radians = math.radians(angle)

sin_val = math.sin(radians)
cos_val = math.cos(radians)
tan_val = math.tan(radians)

print(f"sin({angle}°) = {sin_val:.4f}")
print(f"cos({angle}°) = {cos_val:.4f}")
print(f"tan({angle}°) = {tan_val:.4f}")