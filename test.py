import numpy as np
import matplotlib.pyplot as plt

# Define the yd(k) function
def yd(k):
    if 0 < k < 200:
        return 2
    elif 200 <= k < 400:
        return 0.5
    else:
        return np.nan  # Use NaN for out-of-range values for better plotting

# Generate k values from 0 to 400
k_values = np.arange(0, 401)
yd_values = [yd(k) for k in k_values]

# Plot yd(k)
plt.plot(k_values, yd_values, label='$y_d(k)$')

# Add labels and title
plt.xlabel('Step (k)')
plt.ylabel('Tracking Performance')
plt.title('Desired Trajectory $y_d(k)$')
plt.legend()
plt.grid(True)

# Show plot
plt.show()
