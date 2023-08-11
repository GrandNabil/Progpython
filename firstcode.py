capitals = {"France": "Paris", "Benin": "Porto-Novo", "Nigeria": "Abuja", "Togo": "Lome"}
habitants = {"France": "Francais", "Benin": "Beninois", "Nigeria": "Nigerian", "Togo": "Togolais"}
monnaies = {"France": "euro", "Benin": "fcfab", "Nigeria": "naira", "Togo": "fcfat"}

pays = {"capital": capitals, "habitant": habitants, "monnaie": monnaies}

#print(capitals.get("Benin"))
#print(capitals["Nigeria"])

#capitals["Niger"] = "Niamey"

#print(capitals)

#capitals["Benin"] = "Cotonou"
#print(capitals)

#print(capitals.keys())
#print(pays)

#pays["capital"]
#print(pays.get("capital"))
#print(pays["capital"]["France"])

#print("Benin" in capitals) #key verification
#print(habitants.values())


#for key in pays:
    #print(key, pays[key])


liste = list(habitants.keys())
print(liste)
print(liste.sort())