weight = 10
learning_rate = 0.1
gradient = 4

new_weght = weight - learning_rate * gradient

print(new_weght)

#Suppose
w = 8
alpha = 0.2
gradient = -5

new_weight = w - alpha * gradient
print(new_weight)

#Suppose

y = 10
x = 2
w = 3
b = 0

y2 = w*x + b

print(y2)

# Now calculate the gradient for this single data point:
#  dMSE/dw = -2(2)(10 - 6) = -16

# Example2
# Suppose
y = 12
x = 2
w = 4
b = 0

Y = w * x + b
print(Y)

# Gradient for a single datapoint is: dMSE/dw = -2(2)(12 - 8) = -16

