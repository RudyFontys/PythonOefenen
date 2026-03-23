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

# antwoord = input("Hoeveel jaar moet je nog werken? ")
# dagenTotPensioen = int(antwoord)
# if dagenTotPensioen >= 11:
#     print("Je hebt nog geen recht op de WS regeling")
# elif dagenTotPensioen <= 6:
#     print("Je hebt recht op de WS regeling! voor 9% salaris vermidering hoef je maar 4 dagen te werken")
# else:
#     print("Je hebt recht op de WS regeling! maar na 5 jaar krijg je maar 4 dagen uitbetaald...")
   
# nogEenBestelling = input('Wilt U nog een pilsje? (ja/nee) ')
# while nogEenBestelling == 'ja': # herhaal dit zolang het antwoord 'ja' is
#     pilsPrijs = 3.5   # Prijs van een pilsje
#     aantal = input('Hoeveel denkt U er nog te drinken??? ')
#     aantalPils = int(aantal)
#     pilsPrijsTotaal = pilsPrijs * aantalPils
#     print('Dat kost u dan: €', pilsPrijsTotaal)
#     nogEenBestelling = input('Wilt U nog een pilsje? (ja/nee) ')
# print('U hebt te veel gedronken, ik bestel wel een taxi voor U')


# tafelVan = input('Welke tafel wil je zien (1 t/m 9)? ')
# tafel = int(tafelVan)
# tafelEinde = tafel * 10

# n = 0                     # n is de counter (a.k.a. iterator)
# while n < tafelEinde:       # tafelEinde is het einde van het aantal repeteringen
#     n = n + tafel
#     print(n, end=" ")

# for n in range(5):
#         print("n is", n)

# for i in range(2, 10, 2):
#     print(i, end=" ") # Output: 2 4 6 8


# mijnMotoren = ['Triumph', 'BMW', 'Harley']
# for merk in mijnMotoren:
#         print(merk)

# for i in range( len(mijnMotoren) ):
#     print(i+1, mijnMotoren[i])

# a = int(input("geef een getal in "))
# print(a+a)

# print("Sum from 11 to 20 is", sum)

# def sum(i1, i2): # Dit is erg verwarrend... sum() is ook en ingebouwde functie... sum_rang() zou een betere naam zijn
#         result = 0
#         for i in range(i1, i2):
#                 result = result + i
#         return result

# print("Sum from 11 to 20 is", sum(11, 20))
# print("Sum from 25 to 32 is", sum(25, 32))
# print("Sum from 39 to 43 is", sum(39, 43))

# program test_min.py

# 
# program test_min_with_main_function.py

# def min(num1, num2):
#         if num1 < num2:
#                 result = num1
#         else:
#                 result = num2
#         return result

# def test_min_for(n1, n2):
#         smaller = min(n1, n2) # call min with the values of n1 and n2
#         print("The smaller number of", n1, "and", n2, "is", smaller)
#         # return may be omitted here, since no value is returned

# def main():
#         test_min_for(7, 8)
#         test_min_for(3.1415, 3.1414)
#         test_min_for(-1, -2)

# main() # starts executing the statements in main()

# Locale variabele zoals "result" in onderstand voorbeeld is alleen binnen de fuctie geldig... Dus zo oproepen:
# def faculty(num):
#         result = 1
#         for n in range(1, num + 1):
#                 result = result * n
#         return result

# num = 4 # num??? moet dit geen number zijn? voorbeeld in redaer is ergens fout
# fac = faculty(num) # number??? moet dit geen num zijn?
# print(str(num) + "! =", fac)
# print(fac)

# void function print_grade only prints score

# def print_grade(score):
#     if score >= 90.0:
#         print('A')
#     elif score >= 80.0:
#         print('B')
#     elif score >= 70.0:
#         print('C')
#     elif score >= 60.0:
#         print('D')
#     else:
#         print('F')

# def main():
#     score = float(input("Enter a score: "))
#     while score >= 0:
#         print_grade(score)
#         score = float(input("Enter a score: "))

# main() # Call the main function

# function get_grade returns grade
# def get_grade(score):
#     if score >= 90.0:
#         grade = 'A'
#     elif score >= 80.0:
#         grade = 'B'
#     elif score >= 70.0:
#         grade = 'C'
#     elif score >= 60.0:
#         grade = 'D'
#     else:
#         grade = 'F'
#     return grade

# def main():
#     score = float(input("Enter a score: "))
#     while score >= 0:
#         grade = get_grade(score)
#         print("The grade is: ", grade)
#         score = float(input("Enter a score: "))

# main() # Call the main function to start testing

# program circle.py

