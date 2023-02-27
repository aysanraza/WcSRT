# imports
from nltk.probability import FreqDist
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import streamlit as st


# function defined to build the "word cloud" representation of processed data of pubmed article
def w_cloud(data):
        mostcommon = FreqDist(data).most_common(200)
        wordcloud = WordCloud(width=1600, height=800, background_color='white').generate(str(mostcommon))
        fig = plt.figure(figsize=(30, 10), facecolor='white')
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis('off')
        st.text("")
        plt.tight_layout(pad=0)
        st.pyplot(fig)


if __name__ == '__main__':
    print("cloud")
