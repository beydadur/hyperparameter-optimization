# here are the input commands that you can use
lowerVal, upperVal, step  = map(float, input().strip().split())

inps = input().strip().split()
a, b, c, d, indicator = float(inps[0]), float(inps[1]), float(inps[2]), float(inps[3]), (inps[4] == "True")
x = float(input())

final_value = 0
max_result = 0

L = lowerVal
U = upperVal

H_upper = U
H_lower = L

while True:
    if indicator:
        y_upper = ((H_upper**3)*x**3+a*H_upper*x**2+b*x+c)**d
    else:
        y_upper = ((H_upper**3)*x**3+a*H_upper*x**2+b*x+c)/d
    
    if indicator:
        y_lower = ((H_lower**3)*x**3+a*H_lower*x**2+b*x+c)**d
    else:
        y_lower = ((H_lower**3)*x**3+a*H_lower*x**2+b*x+c)/d

    if y_upper > y_lower:
        H_lower = (H_upper + H_lower) / 2
        final_value = H_upper
        max_result = y_upper
    elif y_upper < y_lower:
        H_upper = (H_upper + H_lower) / 2
        final_value = H_lower
        max_result = y_lower
    else:
        break


print('Value: %.6f, Result: %.6f' % (final_value, max_result))
