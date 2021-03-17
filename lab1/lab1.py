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
constantS1 = np.zeros(n)

quadraticS = np.zeros(n)
quadraticS1 = np.zeros(n)

for i in range(n):
    constantS[i] = 0.0000005
    constantS1[i] = constantS[i] + uniformS[i]

    quadraticS[i] = (0.0000005 * i * i)
    quadraticS1[i] = quadraticS[i] + normalS[i]

plt.plot(constantS1)
plt.plot(constantS)
plt.ylabel('динаміка продажів')
plt.show()

plt.plot(quadraticS1)
plt.plot(quadraticS)
plt.ylabel('динаміка продажів')
plt.show()


# plt.hist(uniformS, bins=20, alpha=0.5, label='S')
plt.hist(normalS, bins=20, alpha=0.5, label='S1')
plt.hist(constantS1, bins=20, alpha=0.5, label='S3')
# plt.hist(quadraticS1, bins=20, alpha=0.5, label='S4')
plt.show()