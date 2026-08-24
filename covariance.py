height = [1.70, 1.62, 1.52, 1.85, 1.91, 1.42]
weight = [72, 64, 84, 80, 72, 70]

n = len(height)

# To Calculate sum of Height & Weight
sum_height = 0
sum_weight = 0

for i in range(n):
    sum_height = sum_height + height[i]
    sum_weight = sum_weight + weight[i]

# To Calculate mean
mean_height = sum_height / n
mean_weight = round(sum_weight / n, 3)

# TO Calculate deviations and their products
sum_x2 = 0
sum_y2 = 0
sum_xy = 0

for i in range(n):

    x = height[i] - mean_height
    y = weight[i] - mean_weight

    x2 = x * x
    y2 = y * y
    xy = x * y
    sum_x2 = sum_x2 + x2
    sum_y2 = sum_y2 + y2
    sum_xy = sum_xy + xy

# TO Calculate covariance values
cov_h = sum_x2 / (n - 1)
cov_w = sum_y2 / (n - 1)
cov_hw = sum_xy / (n - 1)

print("\nCovariance Matrix:")
print("[", round(cov_h, 5), ",", round(cov_hw, 5), "]")
print("[", round(cov_hw, 5), ",", round(cov_w, 5), "]")