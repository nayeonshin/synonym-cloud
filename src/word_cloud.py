import matplotlib.pyplot as plt
from PIL.Image import BILINEAR
from wordcloud import WordCloud as wc


def create_cloud(results):
    # create word cloud object
    cloud = wc(background_color="black", height=1000, width=1000, max_words=10)
    cloud.generate_from_frequencies(results)

    # show the cloud
    plt.imshow(cloud)
    plt.axis("off")
    plt.show()
