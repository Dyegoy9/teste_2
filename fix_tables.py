import pandas as pd

def fix_table_31(tabble31_parts):
    
    # fixing first part of tabble 31:
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

    # fixing second part of tabble 31
    part2 = tabble31_parts[2]
    part2.loc[26,'38'] = ''
    part2.loc[26,'Terminologia de mensagens (glosas, negativas e outras)'] = ''
    range_list = list(reversed(range(1,27)))
    for j in range_list:
        novo_codigo = int(part2['38'][j-1])
        nova_descricao = part2['Terminologia de mensagens (glosas, negativas e outras)'][j-1]
        part2.loc[j,'38'] = novo_codigo
        part2.loc[j,'Terminologia de mensagens (glosas, negativas e outras)'] = nova_descricao
    part2.loc[0,'38'] = 38
    part2.loc[0,'Terminologia de mensagens (glosas, negativas e outras)'] = 'Terminologia de mensagens (glosas, negativas e outras)'
    part2.rename(columns={'38':"Código",
    'Terminologia de mensagens (glosas, negativas e outras)':'Descrição da categoria'
    },inplace = True
    )

    # fixing third part of tabble 31
    part3 = tabble31_parts[3]
    part3.loc[26,'65'] = ''
    part3.loc[26,'Terminologia de metástases'] = ''
    range_list = list(reversed(range(1,27)))
    for j in range_list:
        novo_codigo = int(part3['65'][j-1])
        nova_descricao = part3['Terminologia de metástases'][j-1]
        part3.loc[j,'65'] = novo_codigo
        part3.loc[j,'Terminologia de metástases'] = nova_descricao
    part3.loc[0,'65'] = 65
    part3.loc[0,'Terminologia de metástases'] = 'Terminologia de metástases'
    part3.rename(columns={'65':"Código",
    'Terminologia de metástases':'Descrição da categoria'
    },inplace = True
    )

    # fixing fourth part of tabble 31
    part4 = tabble31_parts[4]
    part4.loc[25,'109'] = ''
    part4.loc[25,'Legenda da mensagem de recebimento de lote de guias de cobrança'] = ''
    range_list = list(reversed(range(1,26)))
    for j in range_list:
        novo_codigo = int(part4['109'][j-1])
        nova_descricao = part4['Legenda da mensagem de recebimento de lote de guias de cobrança'][j-1]
        part4.loc[j,'109'] = novo_codigo
        part4.loc[j,'Legenda da mensagem de recebimento de lote de guias de cobrança'] = nova_descricao
    part4.loc[0,'109'] = 109
    part4.loc[0,'Legenda da mensagem de recebimento de lote de guias de cobrança'] = 'Legenda da mensagem de recebimento de lote de guias de cobrança'
    part4.rename(columns={'109':"Código",
    'Legenda da mensagem de recebimento de lote de guias de cobrança':'Descrição da categoria'
    },inplace = True
    )

    # fixing fifth part of tabble 31
    part5 = tabble31_parts[5]
    part5.loc[24,'135'] = ''
    part5.loc[24,'Mensagem de situação do status de autorização (situaçãoAutorização)'] = ''
    range_list = list(reversed(range(1,25)))
    for j in range_list:
        novo_codigo = int(part5['135'][j-1])
        nova_descricao = part5['Mensagem de situação do status de autorização (situaçãoAutorização)'][j-1]
        part5.loc[j,'135'] = novo_codigo
        part5.loc[j,'Mensagem de situação do status de autorização (situaçãoAutorização)'] = nova_descricao
    part5.loc[0,'135'] = 135
    part5.loc[0,'Mensagem de situação do status de autorização (situaçãoAutorização)'] = 'Mensagem de situação do status de autorização (situaçãoAutorização)'
    part5.rename(columns={'135':"Código",
    'Mensagem de situação do status de autorização (situaçãoAutorização)':'Descrição da categoria'
    },inplace = True
    )

     # fixing sixth part of tabble 31
    part6 = tabble31_parts[6]
    part6.loc[8,'160'] = ''
    part6.loc[8,'Guia de demonstrativo de pagamento - tratamento odontológico'] = ''
    range_list = list(reversed(range(1,9)))
    for j in range_list:
        novo_codigo = int(part6['160'][j-1])
        nova_descricao = part6['Guia de demonstrativo de pagamento - tratamento odontológico'][j-1]
        part6.loc[j,'160'] = novo_codigo
        part6.loc[j,'Guia de demonstrativo de pagamento - tratamento odontológico'] = nova_descricao
    part6.loc[0,'160'] = 160
    part6.loc[0,'Guia de demonstrativo de pagamento - tratamento odontológico'] = 'Guia de demonstrativo de pagamento - tratamento odontológico'
    part6.rename(columns={'160':"Código",
    'Guia de demonstrativo de pagamento - tratamento odontológico':'Descrição da categoria'
    },inplace = True
    )
    
    # joining all parts os table 31 in a single dataframe
    parts_list = [part1,part2,part3,part4,part5,part6]
    table31 = pd.concat(parts_list,ignore_index=True)
    return table31

def fix_table30(table30):
    #fixes bugs of table 30
    table30 = table30['Tabela de Tipo do Demandante'].str.split(n=1, expand=True)
    table30.rename(columns={0:"Código",
    1:'Descrição da categoria'
    },inplace = True
    )
    table30.loc[6,'Código'] = ''
    table30.loc[6,'Descrição da categoria'] = ''
    for i in range (0,6):
        novo_codigo = table30['Código'][i+1]
        nova_descricao = table30['Descrição da categoria'][i+1]
        table30.loc[i,'Código'] = novo_codigo
        table30.loc[i,'Descrição da categoria'] = nova_descricao
    table30 = table30.drop([5,6])
    return table30

def fix_table32(table32):
    #fixes bugs of table 32
    table32 = table32['Tabela de Tipo de Solicitação'].str.split(n=1, expand=True)
    table32.rename(columns={0:"Código",
    1:'Descrição da categoria'
    },inplace = True
    )
    table32.loc[6,'Código'] = ''
    table32.loc[6,'Descrição da categoria'] = ''
    for i in range(0,2):
        for i in range (0,5):
            novo_codigo = table32['Código'][i+1]
            nova_descricao = table32['Descrição da categoria'][i+1]
            table32.loc[i,'Código'] = novo_codigo
            table32.loc[i,'Descrição da categoria'] = nova_descricao
    novo_codigo = table32['Código'][3]
    nova_descricao = table32['Descrição da categoria'][3]
    table32.loc[2,'Código'] = novo_codigo
    table32.loc[2,'Descrição da categoria'] = nova_descricao
    table32 = table32.drop([3,4,5,6])
    return table32

