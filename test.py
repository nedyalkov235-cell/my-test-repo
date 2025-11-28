from parties import Party
def Client():
    party_1 = Party("Peter")
    party_2 = Party("Georgi")
    print(party_1.name + " " + party_2.name)
    
Client()