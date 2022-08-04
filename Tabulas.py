from tabula import read_pdf
import pandas as pd
from tabulate import tabulate
import os

num = 101
while num < 888:
    pdf_name = 'Collegiate_{}'.format(num)
    path_to_pdf = 'C:\\Users\\goesp\\Desktop\\PDF Python\\{}.pdf'.format(pdf_name)
    path_to_csv = 'C:\\Users\\goesp\\Desktop\\PDF Python\\Text\\{}.csv'.format(pdf_name)
    print(num)

    if os.path.isfile(path_to_pdf):
        table = read_pdf(path_to_pdf, pages='all', stream=True, guess=True)

        if table:
            last_table = table[-1]
            if 'Disciplina Turma' in last_table:
                table.pop()
                last_table = last_table.dropna(axis=1, how='all')
                last_table = last_table.dropna(axis=0, how='any')

                last_table[['Disciplina', 'Turma']] = last_table['Disciplina Turma'].str.split(' ', 1, expand=True)

                cols = last_table.columns.tolist()
                cols.remove('Disciplina Turma')
                cols = cols[-2:] + cols[:-2]

                last_table = last_table[cols]
                table.append(last_table)

            table = pd.concat(table, ignore_index=True)

            table = table.astype(int, errors='ignore')
            table['Turma'] = table['Turma'].apply(lambda x: '{0:0>6}'.format(x))

            table = table.assign(Colegiado=num)[['Colegiado'] + table.columns.tolist()]

            print(tabulate(table))

            with open(f'C:\\Users\\goesp\\Desktop\\PDF Python\\Text\\{pdf_name}.csv', 'w') as f:
                table.to_csv(f)

    num += 1
