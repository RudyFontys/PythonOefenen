# print("Running script.")
# wie = 'Rudy de IT god'
# print("'wie' is now equal to", wie)

# print("kerkstraat", 3, end=" ") #end="" plakt de onderstaande print op dezelfde regel
# print("en", "kerkstraat", 5)

# lengte = 5
# breedte = 2
# opperplakte = lengte * breedte
# print ("de oppervlakte is", lengte, "x", breedte, "=", opperplakte)

# variabele = input("type hier iets: ") 
# print(variabele)

# tekstlengte = len("RudyIs1m82")
# print(tekstlengte) 
# print( "Debils"[2:5] ) 

# origineel = 'Rudy de IT god uit Tilburg'
# lower_case = origineel.lower() 
# upper_case = origineel.upper() 
# print(lower_case, upper_case)

# print("food".ljust(10), "category")

# mijn_string = 'Ik ben knetter gek.'
# woord_lijst = mijn_string.split()
# print(woord_lijst)

# print (4/3)
# print (round(4/3, 2))

# mijnMotoren = ['Triumph', 'BMW', 'Harley']
# print (mijnMotoren[2])
# lengte = len(mijnMotoren)
# print(lengte)
# mijnMotoren.remove('Harley')
# lengte = len(mijnMotoren) # als je dit niet doet ververst de waarde van lengte niet...
# print(lengte)
# mijnMotoren.insert(1, 'Ducatie') 
# print (mijnMotoren[2])

# rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
# rainbow.sort() # sorteer op alfabet, dus niet op kleur....
# print(rainbow)

# mijnMotoren =[['jaartal:', 2017, 2022, 1979], ['Merk:', 'Triumph', 'BMW', 'Harley']]
# for row in mijnMotoren:
#     print (row[0].ljust(9), row[1])

# mijnMotorenJaartallen = {'Triumph' : 2017, 'BMW' : 2022, 'Harley' : 1979}
# print(mijnMotorenJaartallen)

# print(type(mijnMotorenJaartallen)) # datatype controleren met type()

antwoord = input("Hoeveel jaar moet je nog werken? ")
dagenTotPensioen = int(antwoord)
if dagenTotPensioen >= 11:
    print("Je hebt nog geen recht op de WS regeling")
elif dagenTotPensioen <= 6:
    print("Je hebt recht op de WS regeling! voor 9% salaris vermidering hoef je maar 4 dagen te werken")
else:
    print("Je hebt recht op de WS regeling! maar na 5 jaar krijg je maar 4 dagen uitbetaald...")
   