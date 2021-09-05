"""
    Description: This program reads natural text and classify its sentiment
    (e.g., negative vs. positive; 5-star vs. 3-star product). We analyze movie
    review data extracted from Rotten Tomatoes and use sorting to determine which
    words are most associated with positive reviews and which words are most
    associated with negative reviews.
    Author: Matthew Erdman
    Date: 8/27/21
"""


def parallelInsertionSort(sentScore, sentWords):
    """
    Purpose: Use a modified insertion sort algorithm to sort two linked lists simultaneously,
    keeping them linked.
    Parameters: sentScore - the list of integer word sentiment scores, and
    sentWords - the list of movie review words. These lists are linked.
    Return Value: sentScore - the sorted list of integer scores for the review words,
    and sentWords - the sorted list of review words. These lists are linked.
    """
    for i in range(1, len(sentScore)):
        key = sentScore[i]
        keyWords = sentWords[i] # track a second key for sentWords
        j = i-1
        while j >=0 and key < sentScore[j]: # go through items to the left of key
            sentScore[j+1] = sentScore[j]
            sentWords[j+1] = sentWords[j]   # swap sentWords when we swap sentScore
            j -= 1
        sentScore[j+1] = key
        sentWords[j+1] = keyWords           # swap sentWords when we swap sentScore

    return sentScore, sentWords             # linked lists are now both sorted


def binarySearch(x, L):
    """
    Purpose: Perform a binary search to find a specified value in a list.
    Parameters: x - the value to look for, and L - the list to look in.
    Return Value: Boolean indicating if x is in L and the integer index of x.
    """
    low = 0
    high = len(L) - 1

    while low <= high:
        mid = (low + high)//2

        if x == L[mid]:       # found x in L
            return True, mid

        elif x > L[mid]:      # too low, adjust low bound
            low = mid + 1

        elif x < L[mid]:      # too high, adjust high bound
            high = mid - 1

    return False              # x is not in L


def linearSearch(x, L):
    """
    Purpose: Perform a linear search to find a specified value in a list.
    Parameters: x - the value to look for, and L - the list to look in.
    Return Value: Boolean indicating if x is in L and the integer index of x.
    """
    count = 0
    for item in L:
        count += 1
        if item == x:
            return True, count  # found x in L
    return False, count         # x is not in L


def readReviews():
    """
    Purpose: Open a .txt file containing a 0-4 score and written movie review,
    dump data into two linked lists containing the movie scores and movie reviews.
    The list of reviews is a nested list where each linked element is a list of
    individual words.
    Parameters: None.
    Return Value: Two linked lists containing the integer scores and string reviews.
    """
    scores = []
    reviews = []

    rawReviews = open("movieReviews.txt", 'r')
    for line in rawReviews:
        # score is first character of line, grab it
        scores.append(int(line[:1]) - 2) # subtract 2 from score for cumulative score

        # text is second char onward, remove whitespace/caps when making list
        reviews.append(line[2:].strip().lower().split(" "))
    rawReviews.close()

    return scores, reviews


def getStopWords():
    """
    Purpose: Open a .txt file containing stop words, reads each word in as a string
    and stores it in a list.
    Parameters: None.
    Return Value: A list of stop words as strings.
    """
    stopWords = []

    wordsFile = open("stopwords.txt", 'r')
    for line in wordsFile:
        stopWords.append(line.strip())
    wordsFile.close()

    return stopWords


def sentiment(scores, reviews):
    """
    Purpose: Main sentiment analysis, associates an integer score with each word
    found in the reviews.
    Parameters: scores - the list of 0-4 movie scores, and reviews - the nested list
    containing written movie reviews, broken into individual words. These lists are linked.
    Return Value: sentScore - the list of integer scores for the review words,
    and sentWords - the list of review words. These lists are linked.
    """
    sentScore = []
    sentWords = []
    stopWords = getStopWords()

    for i in range(len(reviews)):
        for word in reviews[i]:
            # disregard stop words and non alphabetical items
            if word.isalpha() and not binarySearch(word, stopWords):

                # linearSearch returns count starting at 1, lists need to index from 0
                found, count = linearSearch(word, sentWords)
                index = count - 1

                # have we seen this word already?
                if found:
                    # we've seen the word, modify its existing score
                    sentScore[index] += scores[i]
                else:
                    # new word, add it to the lists
                    sentWords.append(word)
                    sentScore.append(scores[i])

    return sentScore, sentWords


def main():
    # read in scores and reviews
    scores, reviews = readReviews()

    # assign sentiment scores
    print("assigning sentiments...")
    sentScore, sentWords = sentiment(scores, reviews)

    # sort sentiment scores
    print("sorting...")
    sentScore, sentWords = parallelInsertionSort(sentScore, sentWords)

    # print top 20 words
    print("-----------------------------")
    print("top 20 words:")
    for i in range(len(sentWords)-1, len(sentWords)-21, -1):
        print(sentScore[i], sentWords[i])

    # print bottom 20 words
    print("\n", end="")
    print("bottom 20 words:")
    for i in range(19, -1, -1):
         print(sentScore[i], sentWords[i])

main()
