import requests
from bs4 import BeautifulSoup
import psycopg2
from datetime import datetime

DB_CONFIG = {
    'dbname': 'postgres',
    'user': 'postgres.akerwwnultjhmvdixfmm',
    'password': 'senaccrawlerbr1234',
    'host': 'aws-0-sa-east-1.pooler.supabase.com',
    'port': '6543'
}

def get_fapesc_edital_titles_and_links():
    url = "https://fapesc.sc.gov.br/category/chamadas-abertas/"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('h2', class_='entry-title')

        if not titles:
            print("Nenhum título encontrado na FAPESC.")
            return
        
        for title in titles:
            edital_title = title.text.strip()
            edital_link = title.find('a')['href']
            print(f"Título: {edital_title}")
            print(f"Link: {edital_link}\n")
            insert_into_database(edital_title, edital_link)
    
    except requests.RequestException as e:
        print(f"Erro ao acessar a página FAPESC: {e}")

def insert_into_database(titulo, link):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        nome_banca = "FAPESC"
        valor = 0.0
        descricao = "Descrição do edital"
        vencimento = None
        prazo_execucao = None
        valor_global = 0.0
        valor_estimado = 0.0
        valor_maximo = 0.0
        data_publicacao = datetime.now().date()

        insert_query = """
            INSERT INTO edital (nome_banca, titulo, valor, descricao, link, 
            id_site, img_logo, vencimento, prazo_execucao, valor_global, 
            valor_estimado, valor_maximo, data_publicacao)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(insert_query, (nome_banca, titulo, valor, descricao, link,
                                       None, None, vencimento, prazo_execucao,
                                       valor_global, valor_estimado, valor_maximo, 
                                       data_publicacao))

        conn.commit()
        print("Dados inseridos com sucesso.")
    
    except Exception as e:
        print(f"Erro ao inserir dados no banco de dados: {e}")
    
    finally:
        cursor.close()
        conn.close()

get_fapesc_edital_titles_and_links()
