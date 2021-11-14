from google_scholar import get_scholar_results
from google_screenshots import GoogleScreenshotTaker
from thesaurus import get_synonyms
from word_cloud import create_cloud


def main():
    search_term = input("Enter a word: ")

    taker = GoogleScreenshotTaker(search_term)
    taker.start()
    taker.finish()

    # synonyms = get_synonyms(search_term)
    # result_nums = get_scholar_results(synonyms)
    # create_cloud(result_nums)


if __name__ == "__main__":
    main()
