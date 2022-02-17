from turtle import distance


name=input("Name: ")
distance_km=input("Enter a distance in kilometers: ")
distance_mi=float(distance_km) / 1.609
print("Hello, "+name.capitalize()+". The distance in kilometers is "+str(distance_km)+" km, which is "+str(round(distance_mi,4))+" miles.")