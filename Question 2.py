#Calculer le capital et les intérêts obtenus au bout de 8 ans de placement avec un taux de 2.3% net par an en considérant le calcul des intérêts une fois par MOIS
def c(n):
    if n==0:
        return c0
    else:
        return (( c(n-1)+m)*(1+t/100/12))


print("Calcul du capital acquis et de ses intérêts versés lorsque les intérêts sont calculéés une fois par an.")
c0 = int(input("Entrer le placement de départ: "))
m = int(input("Entrer le montant du versement mensuel: "))
t = float(input("Entrer le taux annuel : "))
n = int(input("Entrer le nombre d'annee : "))
print("Le capital acquis avec intérêts est de ",round(c(n*12),2),"euros au bout de",n,"ans avec des versements mensuels de",m,"euros.")
print("Les intérêts gagnés au taux annuel de ",t,"% sont de ",round(c(n*12)-n*m*12-c0,2),"euros")
print("Sans placement avec intérêts le capital acqui serait de ",round(n*m*12+c0,0),"euros")
