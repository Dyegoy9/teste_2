Esse Script usa a biblioteca tabula para extrair as tabelas 30,31 e 32 do pdf Componente_organizacional.pdf
Requisitos:
* Java 8+ (requisito do tabula) Instalado **
* python 3.7 + (requisito do tabula)
* bibliotecas no requirements.txt

** script não funciona sem o java instalado (gera os arquivos csv e sem conteúdo, pois o tábula não irá funcionar)

Nota: Como o arquivo .pdf não é feito para edições, da um certo trabalho extrair informações de arquivos com essa extensão. Os dataframes que o tabula retorna, as vezes vêm um pouco degenerados, principalmente no 
caso de tabelas como a 31, que se extendem por varias páginas. Nesse caso, usei o pandas para tratar os dados 
retornados pelo tabula, por meio do script fix_tables. 

Além disso, o script usa o próprio método to_csv do pandas para exportar os arquivos para o formato csv
e usa a biblioteca ZipFile para criar o arquivo zip dos arquivos csv

