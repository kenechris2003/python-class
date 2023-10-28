def fallDistance(a,t,v1,x1):
    S = 0.5*a*(t**2) + v1*t + x1
    return S

a = -9.8 
t = 10
v1 = 0.0
x1 = 0.0

S = fallDistance(a,t,v1,x1)
S = int(S)
print(f"The falling distance is {S} m")

