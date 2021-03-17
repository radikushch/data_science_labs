import numpy as np
import math as mt
import matplotlib.pyplot as plt

n = 100
iter = int(n)
nAVv = 0
nAV = int((iter * nAVv)/100)
dm = 0
dsig = 5
SAV = np.zeros(nAV)
SSAV = np.zeros(nAV)

for i in range(nAV):
    SAV[i] = mt.ceil(np.random.randint(1, iter))

#=================================================================
uniformS = np.random.rand(iter)

mUniformS = np.median(uniformS)
dUniformS = np.var(uniformS)
scvUniformS = mt.sqrt(dUniformS)

print('номери АВ: SAV=',SAV)
print('матриця реалізацій ВВ=',uniformS)
print('матиматичне сподівання ВВ=',mUniformS)
print('дисперсія ВВ =',dUniformS)
print('СКВ ВВ=',scvUniformS)
print('========================================================')

plt.hist(uniformS, bins=20, facecolor="blue", alpha=0.5)
plt.show()
#=================================================================

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
quadraticS = np.zeros(n)
quadraticSV = np.zeros(n)

SV0 = np.zeros(n)
quadraticSAV = np.zeros(n)

for i in range(n):
    quadraticS[i] = (0.0000005 * i * i)
    quadraticSV[i] = quadraticS[i] + normalS[i]
    SV0 = abs(quadraticSV[i] - quadraticS[i])
    quadraticSAV[i] = quadraticSV[i]

plt.plot(quadraticSV)
plt.plot(quadraticS)
plt.ylabel('динаміка продажів')
plt.show()

#=================================================================
SSAV = np.random.normal(dm, (3*dsig), nAV)
for i in range(nAV):
    k = int(SAV[i])
    quadraticSAV[k] = quadraticS[k] + SSAV[i]

plt.plot(quadraticSAV)
plt.plot(quadraticS)
plt.ylabel('динаміка продажів')
plt.show()

plt.hist(normalS, bins=20, alpha=0.5, label='S')
plt.hist(quadraticS, bins=20, alpha=0.5, label='S1')
plt.hist(quadraticSV, bins=20, alpha=0.5, label='S3')
plt.hist(quadraticSAV, bins=20, alpha=0.5, label='S3')
plt.show()
#=================================================================
e = 0.1
def half_divide_method(start, end, f, ak):
    x1 = (start + end) / 2
    while mt.fabs(f(x1, ak)) >= e:
        x1 = (start + end) / 2
        start, end = (start, x1) if f(start, ak) * f(x1, ak) < 0 else (x1, end)
    return (start + end) / 2

mQuadraticSAV = np.median(quadraticSAV)
dQuadraticSAV = np.var(quadraticSAV)
scvQuadraticSAV = mt.sqrt(dQuadraticSAV)

a = 0
b = 4
amount = 0

func = lambda x, c: (x + 4) * mt.pow((x - 1), 5) - c * mt.pow((x + 4), 4)
for i in range(2, n):
    ai = (quadraticSAV[i] - quadraticSAV[i - 1]) - (quadraticSAV[i - 1] - quadraticSAV[i - 2])
    Ak = i * ai/dQuadraticSAV
    x1 = (a + 4) * mt.pow((a - 1), 5) - Ak * mt.pow((a + 4), 4)
    x2 = (b + 4) * mt.pow((b - 1), 5) - Ak * mt.pow((b + 4), 4)
    print("x1 = ", x1)
    print("x2 = ", x2)
    if np.sign(x1) == np.sign(x2):
        amount = amount + 1

print("Desire AV number = ", nAV)
print("AV number = ", amount)


# ------------------------------ МНК згладжування -------------------------------------
Yin = np.zeros(iter)
F = np.ones((iter, 3))
for i in range(iter):                          # формування структури вхідних матриць МНК
    Yin[i] = float(normalS[i])                   # формування матриці вхідних даних без аномілій
    F[i, 1] = float(i)
    F[i, 2] = float(i*i)   # формування матриці вхідних даних без аномілій
# ---------------------- функція обчислень алгоритму - MNK -----------------------------
def MNK(Yin, F):
    FT = F.T
    FFT = FT.dot(F)
    FFTI = np.linalg.inv(FFT)
    FFTIFT = FFTI.dot(FT)
    C = FFTIFT.dot(Yin)
    Yout = F.dot(C)
    return Yout

# ---------------------- застосування МНК до незашумлених вимірів -----------------------
Yout0 = MNK (Yin, F)
print('Yout0=', Yout0, 'Yin=', Yin)
# ---------------------- застосування МНК до незашумлених вимірів -----------------------
for i in range(iter):
    Yin[i] = float(quadraticSV[i])
Yout1 = MNK(Yin, F)
# ---------------------- застосування МНК до незашумлених вимірів -----------------------
for i in range(iter):
    Yin[i] = float(quadraticSAV[i])
Yout2 = MNK(Yin, F)
# ------------ графіки тренда, МНК оцінок нормального та аномального шуму ---------------

Yout00 = np.zeros(n)
Yout10 = np.zeros(n)
Yout20 = np.zeros(n)
for i in range(n):
     Yout00[i] = abs(Yout0[i] - normalS[i])
     Yout10[i] = abs(Yout1[i] - normalS[i])
     Yout20[i] = abs(Yout2[i] - normalS[i])

print('----------------------- статистичны характеристики виміряної вибірки за НАЯВНОСТІ АВ -----------------')
mYout00=np.median(Yout00);  mYout10=np.median(Yout10);  mYout20=np.median(Yout20)
dYout00=np.var(Yout00);     dYout10=np.var(Yout10);     dYout20=np.var(Yout20)
scvYout00=mt.sqrt(dYout00); scvYout10=mt.sqrt(dYout10); scvYout20=mt.sqrt(dYout20)
print('--------------------------- за відсутності похибок ----- похибки нормальні ------- похибки аномальні ---')
print('матиматичне сподівання ВВ3=', mYout00 ,   '----', mYout10,  '----', mYout20)
print('дисперсія ВВ3 =            ', dYout00  ,  '----', dYout10,  '----', dYout20)
print('СКВ ВВ3=                   ', scvYout00  ,'----', scvYout10,'----', scvYout20)
print('-------------------------------------------------------------------------------------------------------')


plt.plot(Yin)
plt.plot(Yout0)
plt.plot(Yout1)
plt.plot(Yout2)
plt.ylabel('динаміка продажів')
plt.show()

# ------- гістограми вхідних похибок, МНК оцінок нормальних та аномальних  --------------
plt.hist(normalS, bins=20, alpha=0.5, label='SV0')
plt.hist(Yout20, bins=20, alpha=0.5, label='Yout20')
plt.hist(Yout10, bins=20, alpha=0.5, label='Yout10')
