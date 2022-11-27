# Imports
from Bio import Entrez
import re


def search(query):
    Entrez.email = 'aysanraza@gmail.com'
    handle = Entrez.esearch(db='pubmed',
                            sort='relevance',
                            retmax='500',
                            retmode='xml',
                            term=query)
    results = Entrez.read(handle)
    return results


def fetch_details(id_list):
    ids = ','.join(id_list)
    Entrez.email = 'aysanraza@gmail.com'
    handle = Entrez.efetch(db='pubmed',
                           retmode='xml',
                           id=ids)
    results = Entrez.read(handle)
    return results


def fetch_titles(papers):
    titles = []
    for i, paper in enumerate(papers['PubmedArticle']):
        data_done = (paper['MedlineCitation']['Article']['ArticleTitle'])
        #data_done = list(data_done)
        titles.append(data_done)
    return titles


if __name__ == '__main__':
    print("pubmed_data_extraction")
