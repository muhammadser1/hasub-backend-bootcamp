def count_word_bad(text):
    """
    Count the occurrences of each word in the given text using a less efficient approach.

    Args:
        text (str): The input text to count word occurrences from.

    Returns:
        dict: A dictionary where keys are words in the text and values are their corresponding counts.
    O(n) place, O(n^2) runtime

    """
    word_counts = {}
    for word in text:
        count = 0
        for word2 in text:
            if word == word2:
                count += 1
        word_counts[word] = count
    return word_counts


def count_word_good(text):
    """
    Count the occurrences of each word in the given text using an efficient approach.

    Args:
        text (str): The input text to count word occurrences from.

    Returns:
        dict: A dictionary where keys are words in the text and values are their corresponding counts.
    O(n) place, O(n) runtime
    """
    word_counts = {}
    words = text.split()
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts
