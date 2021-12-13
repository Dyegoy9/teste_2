import tabula
import pandas as pd
from zipfile import ZipFile
from fix_tables import *

pdf_directory = "Componente_organizacional.pdf"

# Retorna uma lista com as tabelas encotradas no pdf dado
def extract_tables(pdf_file):
    try:
        table_list = tabula.read_pdf(pdf_file,pages='114-120')
        print(f"Tabelas extraidas com sucesso do pdf {pdf_file}")
        return table_list
    except:
        print('Não foi possível extrair tabelas do arquivo pdf')
        return []

def create_csv(file_name,file_content):
    try:
        with open(f'{file_name}.csv','w') as file:
            file.write(file_content)
        print(f"csv {file_name}.csv criado com sucesso!")
        return True
    except:
        print(f"Não foi possível criar o csv {file_name}")
        return False

#create zip archive with all archives in the files_list variable
def zip_files(name,files_list):
    with ZipFile(name,'w') as zip:
        zip.write(files_list[0])
        zip.write(files_list[1])
        zip.write(files_list[2])
    print(f'zip {name} criado com sucesso !')

def main():
    #Call function to extract tables from pdf
    table_list = extract_tables(pdf_directory)

    # Call funtions to fix tables 
    fixed_table30 = fix_table30(table_list[0])
    fixed_table31 = fix_table_31(table_list)
    fixed_table32 = fix_table32(table_list[7])
    csv_quadro30 = fixed_table30.to_csv(index = False)
    csv_quadro31 = fixed_table31.to_csv(index = False)
    csv_quadro32 = fixed_table32.to_csv(index = False)
    
    # create csv archive of the dataframes
    create_csv('quadro30',csv_quadro30)
    create_csv('quadro32',csv_quadro32)
    create_csv('quadro31',csv_quadro31)

    #create zip archive with csv's 
    files_dir = ['quadro30.csv','quadro31.csv','quadro32.csv']
    zip_files('Teste_Dyego.zip',files_dir)

main()
