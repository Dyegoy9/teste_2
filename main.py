import tabula
import pandas as pd
from zipfile import ZipFile
from fix_tabbles import *

pdf_directory = "Componente_organizacional.pdf"

# Retorna uma lista com as tabelas encotradas no pdf dado
def extract_tabbles(pdf_file):
    try:
        tabble_list = tabula.read_pdf(pdf_file,pages='114-120')
        return tabble_list
    except:
        print('Não foi possível extrair tabelas do arquivo pdf')
        return []

def create_csv(file_name,file_content):
    try:
        with open(f'{file_name}.csv','w') as file:
            file.write(file_content)
        return True
    except:
        return False

#Compacta os arquivos cvs à um arquivo .zip 
def zip_files(files_list):
    with ZipFile('tabbles.zip','w') as zip:
        zip.write(files_list[0])
        zip.write(files_list[1])
        zip.write(files_list[2])

def main():
    tabble_list = extract_tabbles(pdf_directory)
    quadro_30 = tabble_list[0]
    quadro_32 = tabble_list[7]

    csv_quadro30 = quadro_30.to_csv()
    csv_quadro32 = quadro_32.to_csv()
    create_csv('quadro30',csv_quadro30)
    create_csv('quadro32',csv_quadro32)

    # Chama as funções que consertam as tabelas 
    fixed_tabble30 = fix_tabble30(tabble_list[0])
    fixed_tabble31 = fix_tabble_31(tabble_list)
    fixed_tabble32 = fix_tabble32(tabble_list[7])
    csv_quadro30 = fixed_tabble30.to_csv()
    csv_quadro31 = fixed_tabble31.to_csv()
    csv_quadro30 = fixed_tabble32.to_csv()
    
    # Cria csv das tabelas consertadas
    create_csv('quadro30',csv_quadro30)
    create_csv('quadro32',csv_quadro32)
    create_csv('quadro31',csv_quadro31)

    #cria zip dos arquivos cvs criados
    files_dir = ['quadro30.csv','quadro31.csv','quadro32.csv']
    zip_files(files_dir)

main()


#Tarefas:
# fazer união das tabelas em apenas uma (31)
# Consertar tabelas 30 e 32
# Organizar o cógido
# zippar arquivos