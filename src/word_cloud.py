from PIL.Image import BILINEAR
from wordcloud import WordCloud as wc
import matplotlib.pyplot as plt


def create_cloud(results):
    # create word cloud object
    hashtag_cloud = wc(background_color="black", height=1000, width=1000, max_words=10)
    hashtag_cloud.generate_from_frequencies(results)

    # show the cloud
    plt.imshow(hashtag_cloud)
    plt.axis("off")
    plt.show()
