# imports
from nltk.tokenize import wordpunct_tokenize
import cloud
import streamlit as st
#import preprocessing
import pubmed_data_extraction


if __name__ == '__main__':
    try:
        #streamlit
        st.title("WcSRT")
        st.subheader("Word-cloud based Summarizer for Research Topics")
        st.write("The software is designed to intake the text based research term and outputs a single visualization of word cloud representation based on the topics of latest research papers in that particular domain of knowledge.")

        #control_flow
        term_input = st.text_input("Enter your keyword here", key="name")
        with st.spinner('Wait for it...'):
            data_1 = pubmed_data_extraction.search(term_input)
            id_list = data_1['IdList']
            data_2 = pubmed_data_extraction.fetch_details(id_list)
            data_3 = pubmed_data_extraction.fetch_titles(data_2)
            data_3 = str(data_3)
            data = wordpunct_tokenize(data_3)
            cloud.w_cloud(data)
        st.success('Latest scientific keywords associated with your query !')

    except:
        pass

