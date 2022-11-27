# imports
from nltk.probability import FreqDist
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt


# function defined to build the "word cloud" representation of processed data of pubmed article
def w_cloud(data):
    # Use a breakpoint in the code line below to debug your script.
    mostcommon = FreqDist(data).most_common(200)
    wordcloud = WordCloud(width=1600, height=800, background_color='white').generate(str(mostcommon))
    fig = plt.figure(figsize=(30, 10), facecolor='white')
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis('off')
    plt.title('Top 100 Most Common Words', fontsize=100)
    plt.tight_layout(pad=0)
    plt.show() # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print("cloud")
