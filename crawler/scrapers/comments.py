# import requests
# from bs4 import BeautifulSoup

# def get_fapesc_edital_titles_and_links():
#     # URL da página
#     url = "https://fapesc.sc.gov.br/category/chamadas-abertas/"
    
#     # Fazer a requisição para o site
#     response = requests.get(url)
    
#     # Verificar se a requisição foi bem-sucedida
#     if response.status_code == 200:
#         # Processar o conteúdo HTML da página
#         soup = BeautifulSoup(response.text, 'html.parser')
        
#         # Encontrar todos os elementos que correspondem aos títulos dos editais
#         titles = soup.find_all('h2', class_='entry-title')
        
#         # Extrair e exibir o título e o link de cada edital
#         for title in titles:
#             # Extrair o texto do título
#             edital_title = title.text.strip()
            
#             # Extrair o link do edital, presente no elemento <a> dentro do <h2>
#             edital_link = title.find('a')['href']
            
#             # Exibir título e link
#             print(f"Título: {edital_title}")
#             print(f"Link: {edital_link}\n")
#     else:
#         print(f"Erro ao acessar a página. Status code: {response.status_code}")

# def get_fapergs_edital_titles_and_links():
#     # URL da página
#     url = "https://fapergs.rs.gov.br/abertos"
    
#     # Fazer a requisição para o site
#     response = requests.get(url)
    
#     # Verificar se a requisição foi bem-sucedida
#     if response.status_code == 200:
#         # Processar o conteúdo HTML da página
#         soup = BeautifulSoup(response.text, 'html.parser')
        
#         # Encontrar todos os elementos com a classe 'conteudo-lista__item__titulo'
#         titles = soup.find_all('h2', class_='conteudo-lista__item__titulo')
        
#         # Verificar se algum título foi encontrado
#         if not titles:
#             print("Nenhum título encontrado.")
#             return
        
#         # Extrair e exibir o título e o link de cada edital
#         for title in titles:
#             # Encontrar o elemento <a> dentro do <h2>
#             link_tag = title.find('a')
#             if link_tag:
#                 # Extrair o texto do título
#                 edital_title = link_tag.text.strip()
                
#                 # Extrair o link do edital
#                 edital_link = link_tag['href']
                
#                 # Construir o link completo
#                 full_link = f"https://fapergs.rs.gov.br{edital_link}"
                
#                 # Exibir título e link
#                 print(f"Título: {edital_title}")
#                 print(f"Link: {full_link}\n")
#     else:
#         print(f"Erro ao acessar a página. Status code: {response.status_code}")

# # Chamar a função

# # get_fapesc_edital_titles_and_links()


# # def diagnose_fapergs_page():
# #     # URL da página
# #     url = "https://fapergs.rs.gov.br/abertos"
    
# #     # Fazer a requisição para o site
# #     response = requests.get(url)
    
# #     # Verificar se a requisição foi bem-sucedida
# #     if response.status_code == 200:
# #         print("Página acessada com sucesso.")
# #         # Processar o conteúdo HTML da página
# #         soup = BeautifulSoup(response.text, 'html.parser')
        
# #         # Imprimir o HTML formatado para verificar a estrutura
# #         print(soup.prettify())
# #     else:
# #         print(f"Erro ao acessar a página. Status code: {response.status_code}")

# # # Chamar a função para diagnóstico
# # diagnose_fapergs_page()
# def fapesc_extrair_titulos():
#     url = "https://fapergs.rs.gov.br/chamadas-e-editais/abertos"
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')

#         # Aqui tentamos encontrar os elementos que contêm os títulos
#         # Você pode precisar ajustar este seletor com base nos elementos que descobrir
#         titulos = soup.find_all('a', href=True)  # Altere conforme necessário

#         # Filtrando os títulos que você precisa
#         titulos_filtrados = [titulo.get_text(strip=True) for titulo in titulos if 'chamada' in titulo.get_text().lower()]

#         return titulos_filtrados
#     else:
#         return []

# # Testando a função
# # titulos = fapesc_extrair_titulos()
# # print(titulos)




# get_fapesc_edital_titles_and_links()

