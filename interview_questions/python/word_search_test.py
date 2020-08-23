from word_search import word_search


def horizontal_word():
    assert word_search("dog", [["d", "o", "g"], ["d", "f", "s"]]) is True


def vertical_word():
    assert (
        word_search("dog", [["d", "r", "r"], ["o", "f", "s"], ["g", "d", "s"]]) is True
    )


def no_word():
    assert (
        word_search("dog", [["d", "r", "r"], ["b", "f", "s"], ["g", "d", "s"]]) is True
    )
