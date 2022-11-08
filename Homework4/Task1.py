# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141.    10^(-1) ≤ d ≤10^(-10)

sep = 1
d = 0.001
calc_Pi = 0
Diff = 1
Pi = 0
    
while Diff > d:
    
    Pi = Pi + 4 / sep 
    last = Pi
    Pi = Pi - 4 / (sep + 2)
    sep += 4
    
    if last > Pi:
        Diff = last - Pi
    else:
        Diff = Pi - last
    print(Pi)
    
print(f'The Pi is {round(Pi, 4)}')   
    




    


