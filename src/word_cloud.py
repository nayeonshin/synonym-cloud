import matplotlib.pyplot as plt
from PIL.Image import BILINEAR
from wordcloud import WordCloud

# sample data dictionary
sample_dict = {
    "cat": 5,
    "dog": 26,
    "catlover": 80,
    "dogsofinstagram": 100,
    "cutecat": 87,
}


def create_cloud(dict_):
    # choose colors
    bg_color = input("Enter background color: \n")
    word_color = input("Enter word color story: \n")
    # list of color options can be found here: https://matplotlib.org/stable/tutorials/colors/colormaps.html

    # create word cloud object
    hashtag_cloud = WordCloud(
        background_color=bg_color,
        colormap=word_color,
        height=1000,
        width=1000,
        max_words=10,
    )
    hashtag_cloud.generate_from_frequencies(dict_)

    # show the cloud
    plt.imshow(hashtag_cloud)
    plt.axis("off")
    plt.show()
