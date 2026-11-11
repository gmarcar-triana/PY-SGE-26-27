nombres = ["Ana", "Luis", "Carlos"]
kms = [
    [120, 150, 130, 160, 140, 50, 60],
    [200, 180, 210, 190, 220, 100, 80],
    [90, 110, 100, 95, 105, 40, 50]
]

total_kms = [sum(dias) for dias in kms]

for nombre, total in zip(nombres, total_kms):
    print(f"{nombre}: {total} km")