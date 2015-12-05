from eblagajna import povejCeno
def testEblagajna():
    assert povejCeno("Banane") == 1
    assert povejCeno("Ananas") == "Napaka izdelek ne obstaja ali pa ga ni na zalogi"
    return  "testiranje_OK"

print testEblagajna()