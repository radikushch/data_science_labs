import numpy as np
import math as mt
import matplotlib.pyplot as plt

n = 10000
iter = int(n)

uniformS = np.random.rand(iter)

mUniformS = np.median(uniformS)
dUniformS = np.var(uniformS)
scvUniformS = mt.sqrt(dUniformS)

print('матриця реалізацій ВВ=',uniformS)
print('матиматичне сподівання ВВ=',mUniformS)
print('дисперсія ВВ =',dUniformS)
print('СКВ ВВ=',scvUniformS)
print('========================================================')

plt.hist(uniformS, bins=20, facecolor="blue", alpha=0.5)
plt.show()
#=================================================================
dm = 5
dsig = 5

normalS = np.random.normal(dm, dsig, iter)

mNormalS = np.median(normalS)
dNormalS = np.var(normalS)
scvNormalS = mt.sqrt(dNormalS)

print('матриця реалізацій ВВ=',normalS)
print('матиматичне сподівання ВВ=',mNormalS)
print('дисперсія ВВ =',dNormalS)
print('СКВ ВВ=',scvNormalS)
print('========================================================')

plt.hist(normalS, bins=20, facecolor="blue", alpha=0.5)
plt.show()
#=================================================================
constantS = np.zeros(n)

for i in range(n):
    constantS[i] = 0.0000005

mConstantS = np.median(constantS)
dConstantS = np.var(constantS)
scvConstantS = mt.sqrt(dConstantS)

print('матриця реалізацій ВВ=',constantS)
print('матиматичне сподівання ВВ=',mConstantS)
print('дисперсія ВВ =',dConstantS)
print('СКВ ВВ=',scvConstantS)

constantS1 = np.zeros(n)

for i in range(n):
    constantS1[i] = constantS[i] + uniformS[i]

mConstantS1 = np.median(constantS1)
dConstantS1 = np.var(constantS1)
scvConstantS1 = mt.sqrt(dConstantS1)

print('матриця реалізацій ВВ=',constantS1)
print('матиматичне сподівання ВВ=',mConstantS1)
print('дисперсія ВВ =',dConstantS1)
print('СКВ ВВ=',scvConstantS1)

plt.plot(constantS1)
plt.plot(constantS)
plt.ylabel('динаміка продажів')
plt.show()

quadraticS = np.zeros(n)

for i in range(n):
    quadraticS[i] = (0.0000005 * i * i)

mQuadraticS = np.median(quadraticS)
dQuadraticS = np.var(quadraticS)
scvQuadraticS = mt.sqrt(dQuadraticS)

print('матриця реалізацій ВВ=',quadraticS)
print('матиматичне сподівання ВВ=',mQuadraticS)
print('дисперсія ВВ =',dQuadraticS)
print('СКВ ВВ=',scvQuadraticS)

quadraticS1 = np.zeros(n)

for i in range(n):
    quadraticS1[i] = quadraticS[i] + normalS[i]

mQuadraticS1 = np.median(quadraticS1)
dQuadraticS1 = np.var(quadraticS1)
scvQuadraticS1 = mt.sqrt(dQuadraticS1)

print('матриця реалізацій ВВ=',quadraticS1)
print('матиматичне сподівання ВВ=',mQuadraticS1)
print('дисперсія ВВ =',dQuadraticS1)
print('СКВ ВВ=',scvQuadraticS1)

plt.plot(quadraticS1)
plt.plot(quadraticS)
plt.ylabel('динаміка продажів')
plt.show()


# plt.hist(uniformS, bins=20, alpha=0.5, label='S')
plt.hist(normalS, bins=20, alpha=0.5, label='S1')
plt.hist(constantS1, bins=20, alpha=0.5, label='S3')
# plt.hist(quadraticS1, bins=20, alpha=0.5, label='S4')
plt.show()