#----------------- мультикритеріальна оцінка ТОВАРУ с парсінгом вхідного файла -------------
import pandas as pd
import numpy as np
#--------------------------- обнулення критеріальних масивів -------------------------------
Nversion=int(9)
F1=np.zeros((Nversion));  F10=np.zeros((Nversion))
F2=np.zeros((Nversion));  F20=np.zeros((Nversion))
F3=np.zeros((Nversion));  F30=np.zeros((Nversion))
F4=np.zeros((Nversion));  F40=np.zeros((Nversion))
F5=np.zeros((Nversion));  F50=np.zeros((Nversion))
F6=np.zeros((Nversion));  F60=np.zeros((Nversion))
F7=np.zeros((Nversion));  F70=np.zeros((Nversion))
F8=np.zeros((Nversion));  F80=np.zeros((Nversion))
F9=np.zeros((Nversion));  F90=np.zeros((Nversion))

#------------------------------------парсинг вхідного файла -------------------------------
d = pd.read_excel('/Users/rodionkushch/data_science_labs/lab4/example/Pr1.xls')
print('d=', d)                                          # вивід усого масиву файлу plan_11.xlsx
print('----------------STOLB-------------------')
print(d['Товар 9'])                                     # вивід стовпця 'Товар 9'
print('----------------ELEMENT-----------------')
print(float(d['Товар 9'][0].replace(',', '.')))         # перетворення у дробовий тип елементу 'Товар 9'
print(type(float(d['Товар 9'][0].replace(',', '.'))))   # індикатор типу  елементу стовпця 'Товар 9'

F1[0]=float(d['Товар 9'][0].replace(',', '.')); F1[1]=float(d['Товар 8'][0].replace(',', '.')); F1[2]=float(d['Товар 7'][0].replace(',', '.'))
F1[3]=float(d['Товар 6'][0].replace(',', '.')); F1[4]=float(d['Товар 5'][0].replace(',', '.')); F1[5]=float(d['Товар 4'][0].replace(',', '.'))
F1[6]=float(d['Товар 3'][0].replace(',', '.')); F1[7]=float(d['Товар 2'][0].replace(',', '.')); F1[8]=float(d['Товар 1'][0].replace(',', '.'))
print(F1)
F2[0]=float(d['Товар 9'][1].replace(',', '.')); F2[1]=float(d['Товар 8'][1].replace(',', '.')); F2[2]=float(d['Товар 7'][1].replace(',', '.'))
F2[3]=float(d['Товар 6'][1].replace(',', '.')); F2[4]=float(d['Товар 5'][1].replace(',', '.')); F2[5]=float(d['Товар 4'][1].replace(',', '.'))
F2[6]=float(d['Товар 3'][1].replace(',', '.')); F2[7]=float(d['Товар 2'][1].replace(',', '.')); F2[8]=float(d['Товар 1'][1].replace(',', '.'))
print(F2)
F3[0]=float(d['Товар 9'][2].replace(',', '.')); F3[1]=float(d['Товар 8'][2].replace(',', '.')); F3[2]=float(d['Товар 7'][2].replace(',', '.'))
F3[3]=float(d['Товар 6'][2].replace(',', '.')); F3[4]=float(d['Товар 5'][2].replace(',', '.')); F3[5]=float(d['Товар 4'][2].replace(',', '.'))
F3[6]=float(d['Товар 3'][2].replace(',', '.')); F3[7]=float(d['Товар 2'][2].replace(',', '.')); F3[8]=float(d['Товар 1'][2].replace(',', '.'))
print(F3)
F4[0]=float(d['Товар 9'][3].replace(',', '.')); F4[1]=float(d['Товар 8'][3].replace(',', '.')); F4[2]=float(d['Товар 7'][3].replace(',', '.'))
F4[3]=float(d['Товар 6'][3].replace(',', '.')); F4[4]=float(d['Товар 5'][3].replace(',', '.')); F4[5]=float(d['Товар 4'][3].replace(',', '.'))
F4[6]=float(d['Товар 3'][3].replace(',', '.')); F4[7]=float(d['Товар 2'][3].replace(',', '.')); F4[8]=float(d['Товар 1'][3].replace(',', '.'))
print(F4)
F5[0]=float(d['Товар 9'][4].replace(',', '.')); F5[1]=float(d['Товар 8'][4].replace(',', '.')); F5[2]=float(d['Товар 7'][4].replace(',', '.'))
F5[3]=float(d['Товар 6'][4].replace(',', '.')); F5[4]=float(d['Товар 5'][4].replace(',', '.')); F5[5]=float(d['Товар 4'][4].replace(',', '.'))
F5[6]=float(d['Товар 3'][4].replace(',', '.')); F5[7]=float(d['Товар 2'][4].replace(',', '.')); F5[8]=float(d['Товар 1'][4].replace(',', '.'))
print(F5)
F6[0]=float(d['Товар 9'][5].replace(',', '.')); F6[1]=float(d['Товар 8'][5].replace(',', '.')); F6[2]=float(d['Товар 7'][5].replace(',', '.'))
F6[3]=float(d['Товар 6'][5].replace(',', '.')); F6[4]=float(d['Товар 5'][5].replace(',', '.')); F6[5]=float(d['Товар 4'][5].replace(',', '.'))
F6[6]=float(d['Товар 3'][5].replace(',', '.')); F6[7]=float(d['Товар 2'][5].replace(',', '.')); F6[8]=float(d['Товар 1'][5].replace(',', '.'))
print(F6)
F7[0]=float(d['Товар 9'][6].replace(',', '.')); F7[1]=float(d['Товар 8'][6].replace(',', '.')); F7[2]=float(d['Товар 7'][6].replace(',', '.'))
F7[3]=float(d['Товар 6'][6].replace(',', '.')); F7[4]=float(d['Товар 5'][6].replace(',', '.')); F7[5]=float(d['Товар 4'][6].replace(',', '.'))
F7[6]=float(d['Товар 3'][6].replace(',', '.')); F7[7]=float(d['Товар 2'][6].replace(',', '.')); F7[8]=float(d['Товар 1'][6].replace(',', '.'))
print(F7)
F8[0]=float(d['Товар 9'][7].replace(',', '.')); F8[1]=float(d['Товар 8'][7].replace(',', '.')); F8[2]=float(d['Товар 7'][7].replace(',', '.'))
F8[3]=float(d['Товар 6'][7].replace(',', '.')); F8[4]=float(d['Товар 5'][7].replace(',', '.')); F8[5]=float(d['Товар 4'][7].replace(',', '.'))
F8[6]=float(d['Товар 3'][7].replace(',', '.')); F8[7]=float(d['Товар 2'][7].replace(',', '.')); F8[8]=float(d['Товар 1'][7].replace(',', '.'))
print(F8)
F9[0]=float(d['Товар 9'][8].replace(',', '.')); F9[1]=float(d['Товар 8'][8].replace(',', '.')); F9[2]=float(d['Товар 7'][8].replace(',', '.'))
F9[3]=float(d['Товар 6'][8].replace(',', '.')); F9[4]=float(d['Товар 5'][8].replace(',', '.')); F9[5]=float(d['Товар 4'][8].replace(',', '.'))
F9[6]=float(d['Товар 3'][8].replace(',', '.')); F9[7]=float(d['Товар 2'][8].replace(',', '.')); F9[8]=float(d['Товар 1'][8].replace(',', '.'))
print(F9)

def Voronin(G10, G20, G30, G40, G50, G60, G70, G80, G90):

    Integro = np.zeros((Nversion))
    sum_F1 = 0; sum_F2 = 0;  sum_F3 = 0;  sum_F4 = 0;  sum_F5 = 0;  sum_F6 = 0;  sum_F7 = 0;  sum_F8 = 0;  sum_F9 = 0;

    for i in range(len(F1)):
        sum_F1 = sum_F1 + F1[i];  sum_F2 = sum_F2 + F2[i]; sum_F3 = sum_F3 + F3[i];
        sum_F4 = sum_F4 + F4[i];  sum_F5 = sum_F5 + F5[i]; sum_F6 = sum_F6 + (1/F6[i]);
        sum_F7 = sum_F7 + F7[i];  sum_F8 = sum_F8 + F8[i]; sum_F9 = sum_F9 + F9[i];

    for i in range(len(F1)):
        F10[i] = F1[i] / sum_F1; F20[i] = F2[i] / sum_F2; F30[i] = F3[i] / sum_F3;
        F40[i] = F4[i] / sum_F4; F50[i] = F5[i] / sum_F5; F60[i] = (1/F6[i]) / sum_F6;
        F70[i] = F7[i] / sum_F7; F80[i] = F8[i] / sum_F8; F90[i] = F9[i] / sum_F9;
        Integro[i] = (G10*(1 - F10[i]) ** (-1))  + (G20*(1 - F20[i]) ** (-1)) + (G30*(1 - F30[i]) ** (-1))
        + (G40 * (1 - F40[i]) ** (-1)) + (G50 * (1 - F50[i]) ** (-1)) + (G60 * (1 - F60[i]) ** (-1))
        + (G70*(1 - F70[i]) ** (-1))  + (G80*(1 - F80[i]) ** (-1)) + (G90*(1 - F90[i]) ** (-1));

    min=10000; opt=0;
    for i in range(len(Integro)):
        if min > Integro[i]:
            min = Integro[i]
            opt=i;

    print('Integro', Integro)
    print('Номер_оптимального_товару=', opt)

    return Voronin
#---------------- коефіціенти переваги критеріїв -----------------
G1 = 1; G2 = 1; G3 = 1
G4 = 1; G5 = 1; G6 = 1
G7 = 1; G8 = 1; G9 = 1
GNorm = G1+G2+G3+G4+G5+G6+G6+G7+G8+G9
G10=G1/GNorm; G20=G2/GNorm; G30=G3/GNorm
G40=G4/GNorm; G50=G5/GNorm; G60=G6/GNorm
G70=G7/GNorm; G80=G8/GNorm; G90=G9/GNorm

Voronin(G10, G20, G30, G40, G50, G60, G70, G80, G90)


