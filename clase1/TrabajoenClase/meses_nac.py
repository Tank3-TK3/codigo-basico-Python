mesn = int(input("Dame el mes en que naciste (MM):"))
añon = int(input("Dame el año en que naciste (AAAA):"))
mes = int(input("Dame el mes actual (MM):"))
año = int(input("Dame el año actual (AAAA):"))
añost = año - añon
mesest = añost * 12
mesest = (mesest + (12 - mesn) + mes) - 12
print ("Meses trasncurridos:", mesest, "aprox.")