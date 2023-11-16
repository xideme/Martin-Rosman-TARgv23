print("Tere tulemast!".center(50))
kool=input("\tMis koolis sa õpid?: ").capitalize() #str kool
kursus=int(input("\tMis kursusel?: ")) #int kursus
print("Tere tulemast kooli "+kool.upper()+"!\nOle hea "+str(kursus)+".kursuse õpilaseks!")       #kool on KOOL
print("Tere tulemast kooli", kool.lower(), "!\nOle hea", kursus, ".kursuse õpilaseks!")          #KOOL on kool
print("Tere tulemast kooli {0}!\nOle hea {1}.kursuse õpetajaks!".format(kool,kursus))            #kool on Kool
print(type(kool))
print(type(kursus))
ar1=float(input("Arv 1: "))
ar2=float(input("Arv 2: "))
print("{0} + {1}={2}".format(ar1,ar2,ar1+ar2))    #summa
print("{0} - {1}={2}".format(ar1,ar2,ar1-ar2))    #lahutamine
print("{0} * {1}={2}".format(ar1,ar2,ar1*ar2))    #korrutis
print("{0} / {1}={2}".format(ar1,ar2,ar1/ar2))    #jagamine
print("{0} astmes {1}={2}".format(ar1,ar2,ar1**ar2))    #astendamine
print("{0} ja {1} jääk ={2}".format(ar1,ar2,ar1%ar2))    #jagamisjääk
print("{0} ja {1} jagamise täis osa ={2}".format(ar1,ar2,ar1//ar2))    #jagamisjääk