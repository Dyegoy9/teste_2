import tabula
import pandas as pd
from zipfile import ZipFile
from fix_tables import *

pdf_directory = "Componente_organizacional.pdf"
# paginas 114-120
# Return a list containing dataframes of tables on the gived pdf 
def extract_tables(pdf_file):
    try:
        table_list = tabula.read_pdf(pdf_file,pages='114-120')
        print(f"Tabelas extraidas com sucesso do pdf {pdf_file}")
        return table_list
    except:
        print('Não foi possível extrair tabelas do arquivo pdf')
        return []

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
    # Create csv files
    fixed_table30.to_csv('quadro30.csv',index = False)
    print('csv quadro30.csv criado com sucesso!!!')
    fixed_table31.to_csv('quadro31.csv',index = False)
    print('csv quadro31.csv criado com sucesso!!!')
    fixed_table32.to_csv('quadro32.csv',index = False)
    print('csv quadro32.csv criado com sucesso!!!')
    #create zip archive with csv's 
    files_dir = ['quadro30.csv','quadro31.csv','quadro32.csv']
    zip_files('Teste_Dyego.zip',files_dir)

main()
