inputs = int(raw_input())
 
xx, yy = [], []
 
result_x = 0
result_y = 0
 
# its not inline for because it is faster this way
for i in range(inputs):
    xx.append(0)
    yy.append(0)
 
for i in range(inputs):
    numbers = raw_input()
    a = numbers.split(" ")
    xx[int(a[0]) - 1] += 1
    yy[int(a[1]) - 1] += 1
    
for i in range(inputs):
    if xx[i] == 0:
        k = 1
        while k < inputs:
            if i-k >= 0 and xx[i-k] > 1:
                xx[i] += 1
                xx[i-k] -= 1
                result_x += k
                break
            k += 1
    
    if xx[i] == 0:
        k = 1
        while k < inputs:
            if i+k < inputs and xx[i+k] > 1:
                xx[i] += 1
                xx[i+k] -= 1
                result_x += k
                break
            k += 1
    
    if yy[i] == 0:
        k = 1
        while k < inputs:
            if i-k >= 0 and yy[i-k] > 1:
                yy[i] += 1
                yy[i-k] -= 1
                result_y += k
                break
            k += 1
    
    if yy[i] == 0:
        k = 1
        while k < inputs:
            if i+k < inputs and yy[i+k] > 1:
                yy[i] += 1
                yy[i+k] -= 1
                result_y += k
                break
            k += 1
 
print(result_x + result_y)