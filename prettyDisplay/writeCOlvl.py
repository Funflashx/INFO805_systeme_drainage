import linda
import time

linda.connect()
ts = linda.universe._rd(("espace de tuple drainage", linda.TupleSpace))[1]



i=1
while(i <1000):
    fichier = open("graph1.txt", "a")
    time.sleep(1)
    niveau_CO = ts._rd(("niveau_CO",float))[1]
    fichier.write(str(i) + "," + str(round(niveau_CO,3)) +"\n")
    i += 1
    fichier.close()


