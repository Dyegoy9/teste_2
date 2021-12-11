import pandas as pd

def fix_table_31(tabble31_parts):
    
    # fixing first part of tabble 31:
    # Renaming the collumns indexies
    part1 = tabble31_parts[1]
    part1.rename(columns={'Unnamed: 0':"Código",
    'Tabela de Categoria do Padrão TISS':'Descrição da categoria'
    },inplace = True
    )
    part1.loc[25,'Código'] = ''
    part1.loc[25,'Descrição da categoria'] = ''
    
    for i in range (0,25):
        novo_codigo = part1['Código'][i+1]
        nova_descricao = part1['Descrição da categoria'][i+1]
        part1.loc[i,'Código'] = novo_codigo
        part1.loc[i,'Descrição da categoria'] = nova_descricao
    part1 = part1.drop([24,25])
    print(part1)
    print('###################')

    # fix second part of tabble 31
    part2 = tabble31_parts[2]
    print(part2)
    print("####################")
    part2.loc[26,'38'] = ''
    part2.loc[26,'Terminologia de mensagens (glosas, negativas e outras)'] = ''
    range_list = list(reversed(range(1,27)))
    print(range_list)
    for j in range_list:
        novo_codigo = int(part2['38'][j-1])
        nova_descricao = part2['Terminologia de mensagens (glosas, negativas e outras)'][j-1]
        part2.loc[j,'38'] = novo_codigo
        part2.loc[j,'Terminologia de mensagens (glosas, negativas e outras)'] = nova_descricao
    print(part2)
    part2.loc[0,'38'] = 38
    part2.loc[0,'Terminologia de mensagens (glosas, negativas e outras)'] = 'Terminologia de mensagens (glosas, negativas e outras)'

    part2.rename(columns={'38':"Código",
    'Terminologia de mensagens (glosas, negativas e outras)':'Descrição da categoria'
    },inplace = True
    )
    print(part2)
    df = pd.concat([part1,part2],ignore_index=True)
    print(df)
    return df

def fix_table30(tabble30):
    return tabble30

def fix_table32(tabble32):
    return tabble32

