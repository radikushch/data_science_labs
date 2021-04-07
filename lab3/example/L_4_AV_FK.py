# ------------ Лекція 4 Модель АВ та рекурентного згладжування -----------
import numpy as np
import math as mt
import matplotlib.pyplot as plt
# -------------------------- сегмент API ---------------------------------
n=10000
# n=10000
iter=int(n)                      # кількість реалізацій ВВ  -----
nAVv=10; nAV=int ((iter*nAVv)/100)        # кількість АВ у відсотках та абсолютних одиницях -----
dm=0; dsig=5                              # параметри нормального закону розподілу ВВ: середне та СКВ
SAV=np.zeros((nAV)); SSAV=np.zeros((nAV))
# -------------------------- МОДЕЛЬ ВИМІРІВ ------------------------------
# -------- рівномірний закон розводілу номерів АВ в межах вибірки --------
S=np.zeros((n))
for i in range(n):
    S[i]=np.random.randint(0, iter)         # параметри закону задаются межами аргументу
mS=np.median(S)
dS=np.var(S)
scvS=mt.sqrt(dS)
# -------------- генерація номерів АВ за рівномірним законом  -----------
for i in range(nAV):
    SAV[i]=mt.ceil(np.random.randint(1, iter)) # рівномірний розкид номерів АВ в межах вибірки розміром 0-iter
print('номери АВ: SAV=',SAV)
print('----- статистичны характеристики РІВНОМІРНОГО закону розподілу ВВ -----')
print('матриця реалізацій ВВ=',S)
print('матиматичне сподівання ВВ=',mS)
print('дисперсія ВВ =',dS)
print('СКВ ВВ=',scvS)
print('-----------------------------------------------------------------------')
# --------------------- нормальний закон розводілу ВВ ---------------------
S = np.random.normal(dm, dsig, iter)      # нормальний закон розподілу ВВ з вибіркою єбємом iter та параметрами: dm, dsig
mS=np.median(S)
dS=np.var(S)
scvS=mt.sqrt(dS)
print('------- статистичны характеристики НОРМАЛЬНОЇ похибки вимірів -----')
print('матриця реалізацій ВВ=',S)
print('матиматичне сподівання ВВ=',mS)
print('дисперсія ВВ =',dS)
print('СКВ ВВ=',scvS)
print('------------------------------------------------------------------')
# ---------------- модель виміру (квадратичний закон) з нормальний шумом -----------
SV=np.zeros((n)); S0=np.zeros((n)); SV0=np.zeros((n)); SV_AV=np.zeros((n))
for i in range(n):
    S0[i]=(0.0000005*i*i)                    # квадратична модель реального процесу
    # S0[i] = (0.00005*i)
    SV[i] = S0[i]+S[i]
    SV0[i] = abs(SV[i] - S0[i])              # урахування тренду в оцінках статистичних хараткеристик
    SV_AV[i] = SV[i]
# ----- модель виміру (квадратичний закон) з нормальний шумом + АНОМАЛЬНІ ВИМІРИ
SSAV=np.random.normal(dm, (3*dsig), nAV)     # аномальна випадкова похибка з нормальним законом
for i in range(nAV):
    k=int (SAV[i])
    SV_AV[k] = S0[k] + SSAV[i]               # аномальні вимірів з рівномірно розподіленими номерами

# -------------  статистичні характеристики трендової вибірки (з урахуванням тренду)
mSV0=np.median(SV0)
dSV0=np.var(SV0)
scvSV0=mt.sqrt(dSV0)
print('-------- статистичны характеристики виміряної вибірки без АВ ----------')
print('матиматичне сподівання ВВ3=', mSV0)
print('дисперсія ВВ3 =', dSV0)
print('СКВ ВВ3=', scvSV0)

SV_AV0=np.zeros((n))
for i in range(n):
     SV_AV0[i] = abs(SV_AV[i] - S0[i])  # урахування тренду в оцінках статистичних хараткеристик

print('-- статистичны характеристики виміряної вибірки за НАЯВНОСТІ АВ -------')
mSV_AS=np.median(SV_AV0)
dSV_AV=np.var(SV_AV)
scvSV_AV=mt.sqrt(dSV_AV)
print('матиматичне сподівання ВВ3=', mSV_AS)
print('дисперсія ВВ3 =', dSV_AV)
print('СКВ ВВ3=', scvSV_AV)
print('----------------------------------------------------------------------')
# ------------------------------ МНК згладжування -------------------------------------
Yin=np.zeros((iter, 1))
F=np.ones((iter, 3))
for i in range(iter):                          # формування структури вхідних матриць МНК
    Yin[i, 0] = float(S0[i])                   # формування матриці вхідних даних без аномілій
    F[i, 1] = float(i); F[i, 2] = float(i*i)   # формування матриці вхідних даних без аномілій
# ---------------------- функція обчислень алгоритму - MNK -----------------------------
def MNK (Yin, F):
    FT=F.T
    FFT = FT.dot(F)
    FFTI=np.linalg.inv(FFT)
    FFTIFT=FFTI.dot(FT)
    C=FFTIFT.dot(Yin)
    Yout=F.dot(C)
    return Yout
# --------------------- функція обчислень алгоритму -а-в фільтру ------------------------
def ABF (Yin, iter):
    # -------------- початкові дані для запуску фільтра
    YoutAB = np.zeros((iter, 1))
    T0=1
    Yspeed_retro=(Yin[1, 0]-Yin[0, 0])/T0
    Yextra=Yin[0, 0]+Yspeed_retro
    alfa=2*(2*1-1)/(1*(1+1))
    beta=(6/1)*(1+1)
    YoutAB[0, 0]=Yin[0, 0]+alfa*(Yin[0, 0])
    # -------------- рекурентний прохід по вимірам
    for i in range(1, iter):
        YoutAB[i,0]=Yextra+alfa*(Yin[i, 0]- Yextra)
        Yspeed=Yspeed_retro+(beta/T0)*(Yin[i, 0]- Yextra)
        Yspeed_retro = Yspeed
        Yextra = YoutAB[i,0] + Yspeed_retro
        alfa = (2 * (2 * i - 1)) / (i * (i + 1))
        beta = 6 /(i* (i + 1))
    print('Yin=', Yin, 'YoutAB=', YoutAB)
    return YoutAB
# ---------------------- застосування МНК до незашумлених вимірів -----------------------
for i in range(iter):
    Yin[i, 0] = float(S0[i])
Yout0 = MNK (Yin, F)
# ---------------------- застосування МНК до зашумлених вимірів -------------------------
for i in range(iter):
    Yin[i, 0] = float(SV[i])
Yout1 = MNK (Yin, F)
# ---------------------- застосування МНК до зашумлених вимірів + АВ --------------------
for i in range(iter):
    Yin[i, 0] = float(SV_AV[i])
Yout2 = MNK (Yin, F)
# --------- статистичны характеристики МНК оцінок нормального та аномального шуму --------
Yout00=np.zeros((n)); Yout10=np.zeros((n)); Yout20=np.zeros((n));
for i in range(n):
     Yout00[i] = abs(Yout0[i] - S0[i])
     Yout10[i] = abs(Yout1[i] - S0[i])
     Yout20[i] = abs(Yout2[i] - S0[i])
print('----------------------- статистичны характеристики виміряної вибірки за НАЯВНОСТІ АВ -----------------')
mYout00=np.median(Yout00);  mYout10=np.median(Yout10);  mYout20=np.median(Yout20)
dYout00=np.var(Yout00);     dYout10=np.var(Yout10);     dYout20=np.var(Yout20)
scvYout00=mt.sqrt(dYout00); scvYout10=mt.sqrt(dYout10); scvYout20=mt.sqrt(dYout20)
print('--------------------------- за відсутності похибок ----- похибки нормальні ------- похибки аномальні ---')
print('матиматичне сподівання ВВ3=', mYout00 ,   '----', mYout10,  '----', mYout20)
print('дисперсія ВВ3 =            ', dYout00  ,  '----', dYout10,  '----', dYout20)
print('СКВ ВВ3=                   ', scvYout00  ,'----', scvYout10,'----', scvYout20)
print('-------------------------------------------------------------------------------------------------------')
# ------------ графіки тренда, МНК оцінок нормального та аномального шуму ---------------
plt.plot(Yin)
plt.plot(Yout0)
plt.plot(Yout1)
plt.plot(Yout2)
plt.ylabel('динаміка продажів')
plt.show()
# ------- гістограми вхідних похибок, МНК оцінок нормальних та аномальних  --------------
plt.hist(S, bins=20, alpha=0.5, label='SV0')
plt.hist(Yout20, bins=20, alpha=0.5, label='Yout20')
plt.hist(Yout10, bins=20, alpha=0.5, label='Yout10')
plt.show()
# ------------------------------ виклик альфа-бета фільтра -------------------------------
for i in range(iter):
    # Yin[i, 0] = float(S0[i])   # -------- без шуму
    # Yin[i, 0] = float(SV[i])   # -------- нормальний шум
    Yin[i, 0] = float(SV_AV[i])  # -------- нормальний та аномальний шум
YoutABG = ABF (Yin, iter)
# ------- графіки тренда, альфа-бета фыльтра - оцінок нормального та аномального шуму ----
plt.plot(Yin)
plt.plot(YoutABG)
plt.show()

Yout0AB=np.zeros((n))
for i in range(n):
     Yout0AB[i] = abs(YoutABG[i] - S0[i])
# ------- гістограми вхідних похибок, МНК оцінок нормальних та аномальних  --------------
plt.hist(Yout20, bins=20, alpha=0.5, label='Yout20')
plt.hist(Yout0AB, bins=20, alpha=0.5, label='Yout0AB')
plt.show()