# Njoood - Stage 2 - HBB Sickle Cell Analysis - Sudanese Landscape
print("=== Sudanese Sickle Cell Landscape - Day 1 ===")

normal = "GTGCACCTGACTCCTGAGGAGAAG"
sickle = "GTGCACCTGACTCCTGTGGAGAAG"

print(f"Normal:  {normal}")
print(f"Sickle:  {sickle}")

for i in range(len(normal)):
    if normal[i] != sickle[i]:
        print(f"\nMutation found at position {i+1}:")
        print(f"{normal[i]} -> {sickle[i]}")
        print("GAG (Glu/E) -> GTG (Val/V) = E6V")
        print("rs334 - Sickle Cell mutation - Protects against Malaria in Sudan!")

gc_percent = (normal.count('G')+normal.count('C'))/len(normal)*100
print(f"\nGC% Normal: {gc_percent:.2f}%")