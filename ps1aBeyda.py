# here are the input commands that you can use
lowerVal, upperVal, step  = map(float, input().strip().split())
inps = input().strip().split()
a, b, c, d, indicator = float(inps[0]), float(inps[1]), float(inps[2]), float(inps[3]), (inps[4] == "True")
x = float(input())

final_value = 0
max_result = 0

L = lowerVal
U = upperVal
S = step
H = L or U


while H <= U:
    
    if indicator:
        y = ((H**3)*x**3+a*H*x**2+b*x+c)**d
    
    else:
        y = ((H**3)*x**3+a*H*x**2+b*x+c)/d
    
    if y > max_result:
        max_result = y
        final_value = H
    
    H = H + S

print('Value: %.6f, Result: %.6f' % (final_value, max_result))
