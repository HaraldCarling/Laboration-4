#Studentens alla attribut definieras nedanför.
class Student:
    def __init__(self, förnamn, efternamn, personnummer):
        self.förnamn = förnamn
        self.efternamn = efternamn
        self.personnummer = personnummer
    def __str__(self):
        return "Namn: " + self.förnamn + " " + self.efternamn + " Personnummer: " + str(self.personnummer)
#Antalet studenter bestäms till 3 stycken enligt nedanstående kod och för varje student skriver användaren in information.
i=0
lista = []
while i < 3:
    try:
        förnamn = input('Ange studentens förnamn: ')
        efternamn = input("Ange studentens efternamn: ")
        personnummer = int(input('Ange studentens personnummer: '))
        ny_student = Student(förnamn, efternamn, personnummer)
        lista.append(ny_student)
        print("Objektet skapat!")
        i += 1
    except:
        print("Det blev fel då personnumret måste bestå av siffror")
#Nedanstående kod gör att alla studenter som har lagrats i den ovanstående definierade listan skrivs ut och blir synlig i programmet.
print("Här är alla sparade objekt:")
for x in range(len(lista)):
    print(lista[x])
