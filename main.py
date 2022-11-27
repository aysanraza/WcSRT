# imports
from nltk.tokenize import wordpunct_tokenize
import cloud
#import preprocessing
import pubmed_data_extraction

if __name__ == '__main__':
    data_1 = pubmed_data_extraction.search("omics integration")
    id_list = data_1['IdList']
    data_2 = pubmed_data_extraction.fetch_details(id_list)
    data_3 = pubmed_data_extraction.fetch_titles(data_2)
    data_3 = str(data_3)
    data = wordpunct_tokenize(data_3)
    cloud.w_cloud(data)
