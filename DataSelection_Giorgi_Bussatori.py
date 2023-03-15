#%matplotlib notebook
import matplotlib.pyplot as plt 
#import matplotlib.image as mpimg
import numpy as np
#import scipy
import os

#Inizialising variables
num=0
time=float(0.000) #different from every simulation! 
name1=[]
name2=[]
mass1=[]
mass2=[]
a=[]
ecc=[]
p=[]
xcm=[]
ycm=[]
zcm=[]
temp=[]


#List creation and sorting
binaryfile_list=[]
path="/data4/mapelli3/Nbody6++GPU/new_multiples/hydro/stel_ev/m2_e4_10/" #insert correct path!
file_list=os.listdir(path)
for i in range (0,len(file_list)):
    if (file_list[i][0]=="b") and (file_list[i][1]=="i") and (file_list[i][2]=="n") and (file_list[i][3]=="a") and (file_list[i][4]=="r") and (file_list[i][5]=="y") and (file_list[i][6]=="."):
        binaryfile_list.append(file_list[i])
numfiles=len(binaryfile_list)
binaryfsorted=sorted(binaryfile_list)


#Search BBH for different files
for i in range (1,numfiles):
    filepath=path+binaryfsorted[i]
    time+=0.125
    print(filepath)
    NAME1,NAME2,MASS1,MASS2,XCM,YCM,ZCM,A,ECC,P,K1,K2=np.genfromtxt(filepath,\
			comments="#", usecols=(0,1,3,4,5,6,7,18,19,20,32,33),unpack=True,\
			encoding='utf-8')
   

    #Inside each file
    for c in range (1, len(K1)):
        if ((K1[c]==14) and (K2[c]==14)):
            num+=1
            name1.append(NAME1[c])
            name2.append(NAME2[c])
            mass1.append(MASS1[c])
            mass2.append(MASS2[c])
            xcm.append(XCM[c])
            ycm.append(YCM[c])
            zcm.append(ZCM[c])
            a.append(A[c])
            ecc.append(ECC[c])
            p.append(P[c])
            temp.append(time)  

#Transformation to arrays            
name1=np.array(name1)
name2=np.array(name2)
mass1=np.array(mass1)
mass2=np.array(mass2)
xcm=np.array(xcm)
ycm=np.array(ycm)
zcm=np.array(zcm)
a=np.array(a)
ecc=np.array(ecc)
p=np.array(p)
temp=np.array(temp)

print (name1,name2,temp)

#Writing the output file
fileout = open('results_stel_ev_m2_e4_10.txt', 'w') #Change the output name every time!
fileout.write("name1, name2, mass1, mass2, xcm, ycm, zcm, a, ecc, P, time \n")
for i in range(len(name1)):
    fileout.write(str(name1[i])+"    "+str(name2[i])+"    "+str(mass1[i])+"    "+str(mass2[i])+"    "+str(xcm[i])+\
                  "    "+str(ycm[i])+"    "+str(zcm[i])+"    "+str(a[i])+"    "+str(ecc[i])+"    "+\
                  str(p[i])+"    "+str(temp[i])+"\n")
fileout.close()


