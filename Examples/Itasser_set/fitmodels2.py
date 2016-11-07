import numpy as np
import statsmodels.api as sm



filein =  open('logfile.txt', 'r')


#DECOY     = []
#PDB       = []
#RMSD      = []
#SIZE      = []
#AB_ENERGY = []
#CONTACT   = []
#ANGLE     = []
#BOND      = []
#DIHED     = []
#EEL       = []
#EELEC     = []
#EGB       = []
#ESURF     = []
#NB        = []
#VDWAALS   = []

DECOY      = []
PDB        = []
RMSD       = []
SIZE       = []
contacts_0 = []
contacts_1 = []
contacts_2 = []
contacts_3 = []
contacts_4 = []
contacts_5 = []
AB_ENERGY  = []
ANGLE      = []
BOND       = []
DIHED      = []
EEL        = []
EELEC      = []
EGB        = []
ESURF      = []
NB         = []
VDWAALS    = []








for line in filein:
    line2 = line.split()
    
    if line2[0] == 'DECOY':
        pass
    
    else:
        if len(line2) > 0:
            if 'nan' in line2:
                pass
            else:
                DECOY     .append(line2[0] )
                PDB       .append(line2[1] )
                RMSD      .append(float(line2[2] ))
                SIZE      .append(float(line2[3] ))
                contacts_0.append(float(line2[4] ))
                contacts_1.append(float(line2[5] ))
                contacts_2.append(float(line2[6] ))
                contacts_3.append(float(line2[7] ))
                contacts_4.append(float(line2[8] ))
                contacts_5.append(float(line2[9] ))
                AB_ENERGY .append(float(line2[10]))
                ANGLE     .append(float(line2[11]))
                BOND      .append(float(line2[12]))
                DIHED     .append(float(line2[13]))
                EEL       .append(float(line2[14]))
                EELEC     .append(float(line2[15]))
                EGB       .append(float(line2[16]))
                ESURF     .append(float(line2[17]))
                NB        .append(float(line2[18]))
                VDWAALS   .append(float(line2[19]))
    
    
    
    
    


# #Variavel resposta y
# y = [24,21.6,34.7,33.4,36.2,28.7,22.9,27.1,16.5,18.9,15,18.9,21.7,20.4,18.2,19.9,23.1,17.5,20.2,18.2,13.6,19.6,15.2,14.5,15.6,13.9,16.6,14.8,18.4,21,12.7,14.5,13.2,13.1,13.5,18.9,20,21,24.7,30.8,34.9]
# 
# #Variaveis preditoras
# x1 = [0.00632,0.02731,0.02729,0.03237,0.06905,0.02985,0.08829,0.14455,0.21124,0.17004,0.22489,0.11747,0.09378,0.62976,0.63796,0.62739,105.393,0.7842,0.80271,0.7258,125.179,0.85204,123.247,0.98843,0.750, 260.84054,0.67191,0.95577,0.77299,100.245,113.081,135.472,138.799,115.172,161.282,0.06417,0.09744,0.08014,0.17505,0.02763,0.03359]
# 
# x2 = [18,0,0,0,0,0,12.5,12.5,12.5,12.5,12.5,12.5,12.5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,75,75]
# 
# x3 = [2.310,7.070,7.070,2.180,2.180,2.180,7.870,7.870,7.870,7.870,7.870,7.870,7.870,8.140,8.140,8.140,8.140,8.140,8.140,8.140,8.140,8.140,8.140,8.140,8.140,8.140,8.140,8.140,8.140,8.140,8.140,8.140,8.140,8.140,8.140,5.960,5.960,5.960,5.960,2.950,2.950]
# 
# 
# x4 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# 
# x5 = [0.538,0.469,0.469,0.458,0.458,0.458,0.524,0.524,0.524,0.524,0.524,0.524,0.524,0.538,0.538,0.538,0.538,0.538,0.538,0.538,0.538,0.538,0.538,0.538,0.538,0.538,0.538,0.538,0.538,0.538,0.538,0.538,0.538,0.538,0.538,0.499,0.499,0.499,0.499,0.428,0.428,]
# 
# x6 = [65.750,64.210,71.850,69.980,71.470,64.300,60.120,61.720,56.310,60.040,63.770,60.090,58.890,59.490,60.960,58.340,59.350,59.900,54.560,57.270,55.700,59.650,61.420,58.130,59.240,55.990,58.130,60.470,64.950,66.740,57.130,60.720,59.500,57.010,60.960,59.330,58.410,58.500,59.660,65.950,70.240]
# 
# x7 = [65.2,78.9,61.1,45.8,54.2,58.7,66.6,96.1,100,85.9,94.3,82.9,39,61.8,84.5,56.5,29.3,81.7,36.6,69.5,98.1,89.2,91.7,100,94.1,85.7,90.3,88.8,94.4,87.3,94.1,100,82,95,96.9,68.2,61.4,41.5,30.2,21.8,15.8]
# 
# x8 = [40.900,49.671,49.671,60.622,60.622,60.622,55.605,59.505,60.821,65.921,63.467,62.267,54.509,47.075,44.619,44.986,44.986,42.579,37.965,37.965,37.979,40.123,39.769,40.952,43.996,44.546,46.820,44.534,44.547,42.390,42.330,41.750,39.900,37.872,37.598,33.603,33.779,39.342,38.473,54.011,54.011]
# 
# x9 = [12,2,3,3,3,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,5,5,5,3,3,3]
# 
# x10 = [296,242,242,222,222,222,311,311,311,311,311,311,311,307,307,307,307,307,307,307,307,307,307,307,307,307,307,307,307,307,307,307,307,307,307,279,279,279,279,252,252]
# 
# x11 = [15.3,17.8,17.8,18.7,18.7,18.7,15.2,15.2,15.2,15.2,15.2,15.2,15.2,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,19.2,19.2,19.2,19.2,18.3,18.3]
# 
# 
# 
# x12 = [396.9,396.9,392.83,394.63,396.9,394.12,395.6,396.9,386.63,386.71,392.52,396.9,390.5,396.9,380.02,395.62,386.85,386.75,288.99,390.95,376.57,392.53,396.9,394.54,394.33,303.42,376.88,306.38,387.94,380.23,360.17,376.73,232.6,358.77,248.31,396.9,377.56,396.9,393.43,395.63,395.62]
# 
# x13 = [4.98,9.14,4.03,2.94,5.33,5.21,12.43,19.15,29.93,17.1,20.45,13.27,15.71,8.26,10.26,8.47,6.58,14.67,11.69,11.28,21.02,13.83,18.72,19.88,16.3,16.51,14.81,17.28,12.8,11.98,22.6,13.04,27.71,18.35,20.34,9.68,11.41,8.77,10.13,4.32,1.98]
# 
# print len(x1),len(x2),len(x3),len(x4),len(x5),len(x7),len(x8),len(x9),len(x10),len(x11),len(x12),len(x13)

#print AB_ENERGY
#print SIZE
#print NB
#x = np.column_stack((
#                     #RMSD      ,
#                     SIZE      ,
#                     AB_ENERGY ,
#                     #CONTACT   ,
#                     #ANGLE     ,
#                     #BOND      ,
#                     DIHED     ,
#                     EEL       ,
#                     EELEC     ,
#                     EGB       ,
#                     ESURF     ,
#                      NB        ,
#                     VDWAALS   ))

x = np.column_stack((
                    #DECOY      ,
                    #PDB        ,
                    SIZE       ,
                    contacts_0 ,
                    contacts_1 ,
                    contacts_2 ,
                    contacts_3 ,
                    contacts_4 ,
                    contacts_5 ,
                    AB_ENERGY  ,
                    ANGLE      ,
                    BOND       ,
                    DIHED      ,
                    EEL        ,
                    EELEC      ,
                    EGB        ,
                    ESURF      ,
                    NB         ,
                    VDWAALS    ,
                    ))







#x = np.column_stack((x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13))  #Agrupa as variaveis preditorass
#x = np.column_stack((x1,x2,x3,x4,x6,x7,x8,x9,x10,x11,x12,x13))  #Agrupa as variaveis preditorass
#x = np.column_stack((x1,x2,x3,x6,x7,x8,x9,x10,x11,x12,x13))  #Agrupa as variaveis preditorass

x = sm.add_constant(x, prepend=True) #Adiciona a coluna das constantes

#res = sm.OLS(y,x).fit() #Cria e ajusta o modelo



res = sm.OLS(RMSD,x).fit() #Cria e ajusta o modelo
#res = sm.OLS(SIZE,x).fit() #Cria e ajusta o modelo




print res.params

print res.bse

print res.summary()
