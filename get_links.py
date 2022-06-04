import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import xlsxwriter
import pandas as pd

def remove_duplicates_from_list(mylist): # Remove elementos iguais de uma lista
    res = []
    [res.append(x) for x in mylist if x not in res]
    return res

def get_anchor_tags_from_url(url): # Bota todas as anchor tags de um HTML numa lista
    try: request = requests.get(url)
    except: return []
    parsed_html = BeautifulSoup(request.content, 'html.parser')
    anchor_tags = parsed_html.find_all('a')

    return [tag.get('href') for tag in anchor_tags]

def filter_urls(anchor_tags): # Filtra somente os URLs válidos usando regex
    result = []
    for tag in anchor_tags:
        if tag != None:
            if re.search("(?P<url>https?://[^\s]+)", tag) != None:
                result.append(tag)
    return result

def get_time(): # Pega o horário atual
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    return f"{current_time}"


def crawler(initial_input, depth): # Repete o processo de pegar links baseado no depth dado
    done = []
    queue = [[initial_input, get_time()]]
    for time in range(depth + 1):
        temporary = [[filter_urls(get_anchor_tags_from_url(url[0])), get_time()] for url in queue][0] # PEGAR OS LINK
        done.append(queue)
        queue = temporary
    del done[0]
    done.append(queue)
    return done

def create_excel_columns(file_name): # Cria o arquivo excel com o nome dado e cria as colunas iniciais
    workbook = xlsxwriter.Workbook(file_name)
    worksheet = workbook.add_worksheet("firstSheet")
    worksheet.write(0, 0, "#")
    worksheet.write(0, 1, "url")
    worksheet.write(0, 2, "time")
    return workbook, worksheet

def add_to_excel(all_urls, workbook, worksheet): # Adiciona as URLs ao excel em suas devidas colunas
    count = 1
    for packages in all_urls:
        links = remove_duplicates_from_list(packages[0])
        time = packages[1]

        for link in links:
            worksheet.write(count, 0 ,count)
            worksheet.write(count, 1, link)
            worksheet.write(count, 2, time)
            count += 1
    workbook.close()

def remove_duplicates_from_excel(file_name): # Remove cópias iguais no próprio excel
    data = pd.read_excel(file_name)
    data.drop_duplicates()

def get_links(url_input, depth, file_name): # Função principal, reune os inputs e chama todas as funções necessárias
    all_urls = crawler(url_input, depth)
    workbook, worksheet = create_excel_columns(file_name)
    add_to_excel(all_urls, workbook, worksheet)
    remove_duplicates_from_excel(file_name)

def main():
    pass

if __name__ == "__main__":
    main()
