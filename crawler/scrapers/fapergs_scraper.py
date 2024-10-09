import requests
from bs4 import BeautifulSoup
import psycopg2

DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres.akerwwnultjhmvdixfmm",
    "password": "senaccrawlerbr1234",
    "host": "aws-0-sa-east-1.pooler.supabase.com",
    "port": "6543",
}

def fapergs_edital_titles_and_links():
    url = "https://fapergs.rs.gov.br/abertos/"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        soup = BeautifulSoup(response.content, "html.parser")

        # Encontra o contêiner que contém os editais
        editais_container = soup.find("div", class_="panel-body")
        if not editais_container:
            print("Contêiner de editais não encontrado.")
            return

        # Busca por todos os itens de lista dentro do contêiner
        editais_list = editais_container.find_all("li")

        if not editais_list:
            print("Nenhum edital encontrado na seção de Abertos.")
            return

        for item in editais_list:
            link_tag = item.find("a")
            if link_tag:
                edital_title = link_tag.text.strip()
                edital_link = link_tag.get('href')

                # Verificar se o link é relativo, caso seja, construir a URL completa
                if edital_link.startswith("/"):
                    edital_link = "https://fapergs.rs.gov.br" + edital_link

                # Filtrar links relevantes
                if "resultado" in edital_title.lower() or "chamada" in edital_title.lower():
                    print(f"Título: {edital_title}, Link: {edital_link}")
                    # Inserir no banco de dados
                    insert_into_database(edital_title, None, edital_link, None, None)

    except Exception as e:
        print(f"Erro ao acessar a página Fapergs: {e}")

def insert_into_database(titulo, descricao, link, data_publicacao, vencimento):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        nome_banca = "Fapergs"
        valor = 0.0
        prazo_execucao = None
        valor_global = 0.0
        valor_estimado = 0.0
        valor_maximo = 0.0

        insert_query = """
            INSERT INTO edital (nome_banca, titulo, valor, descricao, link, 
            id_site, img_logo, vencimento, prazo_execucao, valor_global, 
            valor_estimado, valor_maximo, data_publicacao)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(insert_query, (nome_banca, titulo, valor, descricao, link,
                                       None, None, vencimento, prazo_execucao,
                                       valor_global, valor_estimado, valor_maximo, 
                                       None))

        conn.commit()
        print("Dados inseridos com sucesso.")
    
    except Exception as e:
        print(f"Erro ao inserir dados no banco de dados: {e}")
    
    finally:
        cursor.close()
        conn.close()

fapergs_edital_titles_and_links()
