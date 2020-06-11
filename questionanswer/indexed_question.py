# load 20newsgroups dataset into an array
from sklearn.datasets import fetch_20newsgroups
from ktrain import text
import os.path as path

INDEX_DIRECTORY = '/tmp/newsgroups_index'
qa = text.SimpleQA(INDEX_DIRECTORY)


def index(index_directory):
    remove = ("headers", "footers", "quotes")
    newsgroups_train = fetch_20newsgroups(subset='train', remove=remove)
    newsgroups_test = fetch_20newsgroups(subset='test', remove=remove)
    docs = newsgroups_train.data + newsgroups_test.data

    text.SimpleQA.initialize_index(index_directory)
    text.SimpleQA.index_from_list(docs, index_directory, commit_every=100)


def ask_index(question: str, max_answers: int):
    if not path.isdir(INDEX_DIRECTORY):
        index(INDEX_DIRECTORY)

    return qa.ask(question, n_answers=max_answers)
