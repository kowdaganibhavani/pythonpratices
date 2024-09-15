kpa = float(input("Input the kilopascals > "))

psi = round(kpa * 0.145038, 3)
mmHg = round(kpa * 7.50062, 3)
atmp = round(kpa * 0.0098692382432766, 3)

print(f"Pre = {pressure_in_psi} psi \nor {pressure_in_mmHg} mmHg \nor {pressure_in_atmp} atmp")
