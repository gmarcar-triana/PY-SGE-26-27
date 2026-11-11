import numpy as np
estudiantes = {
    '12345678A': round(np.random.uniform(1, 10), 2),
    '87654321B': round(np.random.uniform(1, 10), 2),
    '11223344C': round(np.random.uniform(1, 10), 2),
    '44332211D': round(np.random.uniform(1, 10), 2)
}

rep = True

while rep:
    print('1. Mostrar los datos')
    print('2. Modificar la nota')
    print('3. Añadir un nuevo estudiante')
    print('4. Filtrar por nota de corte')
    print('0. Salir')
    opc = int(input('Elige una opción: '))

    match opc:
        case 1:
            print('\nDatos de los estudiantes:')
            for dni, nota in estudiantes.items():
                print(f'DNI: {dni} - Nota media: {nota}')

        case 2:
            dni = input('Introduce el DNI del estudiante a modificar: ').upper()
            if dni in estudiantes:
                nueva_nota = float(input('Introduce la nueva nota (1-10): '))
                estudiantes[dni] = nueva_nota
                print('Nota actualizada correctamente.')
            else:
                print('El DNI no existe en el registro.')

        case 3:
            dni = input('Introduce el DNI del nuevo estudiante: ').upper()
            if dni not in estudiantes:
                nota_aleatoria = round(np.random.uniform(1, 10), 2)
                estudiantes[dni] = nota_aleatoria
                print(f'Estudiante añadido con nota media aleatoria: {nota_aleatoria}')
            else:
                print('Ese DNI ya está registrado.')

        case 4:
            nota_corte = float(input('Introduce la nota de corte: '))
            admitidos = {}
            for dni, nota in estudiantes.items():
                if nota > nota_corte:
                    admitidos[dni] = nota
            print(f'\nEstudiantes con nota superior a {nota_corte}:')
            print(admitidos)

        case 0:
            print('Saliendo...')
            rep = False

        case _:
            print('Opción no válida.')
