print("This is program of THREE ADDRESS CODE GENERATOR using Python")
import pandas as pd
import copy
try:
 a=pd.read_csv("input.csv")
 print(a)
 print('\t')
 c=a.shape# It will gives an tuple of numbers of rows and columns
 #print(c)
 l=[]
 o=list("+-*/")#If you want to add more operator youn can use that as well
 o1=[]
 r=[]
 for i in range(c[0]):# Here c[0] is 0th element of tuple c, which is a.shape (c=a.shape)
 l=l+[a['left'][i]]
 d=a['right'][i]
 x=d.split()
 l=l+x
 #print(l)
 sizel=len(l)
 for z in range(sizel):
 #print(sizel)
8
 if(l[z] in o):
 o1=o1+[l[z]]
 o1=list(set(o1))
 #print(o1)
 li=copy.deepcopy(l)# if you use li=l then it may occures some un usual error further in
program.
 for x in o1:
 if(x in li):
 li.remove(x)
 li=list(set(li))
 #print(li)
 for b in range(len(li)):
 r=r+["R"+str(b)]
 #print(r)
 i=1
 ak=0
 z=0
 ACounter=0
 akm=[]
 while(i):
 if(ak==len(l)):
 i=0
 elif(l[ak].isalpha() and l[ak]==a['left'][z]):
 print("MOV "+str(l[ak])+' , '+str(r[li.index(l[ak])]))
 akm=akm+[r[li.index(l[ak])]]
 ak+=1
 elif(((l[ak].isalpha()) and (l[ak] in a['right'][z]))and (l[ak] not in o1)):
 print("MOV "+str(l[ak])+' , '+str(r[li.index(l[ak])]))
 akm=akm+[r[li.index(l[ak])]]
 ak+=1
 ACounter+=1
 if((len(a['right'][z])==1)and (len(akm)==2)):
9
 print("STOR "+str(akm[len(akm)-1])+' , '+str(akm[0]))
 #print(akm)
 akm.clear()
 z+=1
 print("\t")
 elif((l[ak] in a['right'][z]) and ((l[ak]in o1)and l[ak]=="+")):
 print("MOV "+str(l[ak+1])+' , '+str(r[li.index(l[ak+1])]))
 akm=akm+[r[li.index(l[ak+1])]]
 print("ADD "+str(akm[len(akm)-2])+' , '+str(akm[len(akm)-1]))
 akm.pop(len(akm)-2)
 #print(akm)
 print("STOR "+str(akm[len(akm)-1])+' , '+str(akm[0]))
 #print(ak)
 #print(ACounter)
 ak+=2
 ACounter+=2
 #print(ACounter)
 if(len(a['right'][z].split(" "))==ACounter):
 #print(akm)
 akm.clear()
 z+=1
 ACounter=0
 #print(z)
 print("\t")
 elif((l[ak] in a['right'][z]) and ((l[ak]in o1)and l[ak]=="-")):
 print("MOV "+str(l[ak+1])+' , '+str(r[li.index(l[ak+1])]))
 akm=akm+[r[li.index(l[ak+1])]]
 print("SUB "+str(akm[len(akm)-2])+' , '+str(akm[len(akm)-1]))
 akm.pop(len(akm)-2)
 print("STOR "+str(akm[len(akm)-1])+' , '+str(akm[0]))
 ak+=2
 ACounter+=2
10
 #print(ACounter)
 if(len(a['right'][z].split(" "))==ACounter):
 #print(akm)
 akm.clear()
 z+=1
 ACounter=0
 #print(z)
 print("\t")
 elif((l[ak] in a['right'][z]) and ((l[ak]in o1)and l[ak]=="*")):
 print("MOV "+str(l[ak+1])+' , '+str(r[li.index(l[ak+1])]))
 akm=akm+[r[li.index(l[ak+1])]]
 print("MUL "+str(akm[len(akm)-2])+' , '+str(akm[len(akm)-1]))
 akm.pop(len(akm)-2)
 print("STOR "+str(akm[len(akm)-1])+' , '+str(akm[0]))
 ak+=2
 ACounter+=2
 #print(ACounter)
 if(len(a['right'][z].split(" "))==ACounter):
 #print(akm)
 akm.clear()
 z+=1
 ACounter=0
 #print(z)
 print("\t")
 elif((l[ak] in a['right'][z]) and ((l[ak]in o1)and l[ak]=="/")):
 print("MOV "+str(l[ak+1])+' , '+str(r[li.index(l[ak+1])]))
 akm=akm+[r[li.index(l[ak+1])]]
 print("DIV "+str(akm[len(akm)-2])+' , '+str(akm[len(akm)-1]))
 akm.pop(len(akm)-2)
 print("STOR "+str(akm[len(akm)-1])+' , '+str(akm[0]))
 akm.clear()
 ak+=2
11
 ACounter+=2
 if(len(a['right'][z].split(" "))==ACounter):
 #print(akm)
 akm.clear()
 z+=1
 ACounter=0
 #print(z)
 print("\t")
 elif((l[ak].isnumeric())and(l[ak] in a['right'][z])):
 print("MOV "+str(l[ak])+' , '+str(r[li.index(l[ak])]))
 akm=akm+[r[li.index(l[ak])]]
 ak+=1
 ACounter+=1
 if((len(akm)==2)and (a['right'][z]==l[ak-1])):
 print("STOR "+str(akm[len(akm)-1])+' , '+str(akm[0]))
 akm.clear()
 z+=1
 ACounter=0
 #print(z)
 print("\t")
 elif((l[ak] not in o1)or (l[ak] not in string.ascii_lowercase)):
 print("\f Error!\n\f Please enter valid syntax for three address code.\n\f Check your csv
file...")
 print(f"\f Error description...\nError in line number {z} and place number {ak}.")
 print(f"\f Error element is {a['right'][z]}.")
 break
except (FileNotFoundError):
 print("Please check you input file. It may possible that file doesn't exist.")
 print("Also check the file name that is given in input section at the starting place.")
except(ArithmeticError):
 print("An arithmetic error is caused due to which program is not proceed futher.Please check
for the solution.")
12
except(IndexError):
 print("List index out of range.")
except:
 print("An exceptions occurred.")
