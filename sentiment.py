"""
    Description:
    Author: Matthew Erdman
    Date: 8/27/21
"""


def insertionSortMod(sentScore, sentWords):
    """ This is the insertion sort algorithm:
            - assume item at index 0 is already "sorted"
            - starting with item at index 1, check all items to the left and swap positions if needed
            - do the same for item at index 2, where now items at index 0 and 1 should be in order
            - do the same for item at index 3, where now items at index 0, 1, and 2 are in order...and so on

        This is a modified verson of insertionSort where sentScore is sorted and
        every action is mimiced on sentWords. This allows for parallel sorting of the lists.
    """
    for i in range(1, len(sentScore)):
        key = sentScore[i]
        keyWords = sentWords[i] # Track a second key for sentWords
        j = i-1
        while j >=0 and key < sentScore[j]:
            sentScore[j+1] = sentScore[j]
            sentWords[j+1] = sentWords[j] # Swap sentWords when we swap sentScore
            j -= 1
        sentScore[j+1] = key
        sentWords[j+1] = keyWords # Swap sentWords when we swap sentScore

    return sentScore, sentWords


def binarySearch(x, L):
    """ return True if x is in L, False if not """
    low = 0
    high = len(L) - 1

    while low <= high:
        mid = (low + high)//2
        # print("x: %s low: %i mid: %i high: %i" % (x, low, mid, high))

        if x == L[mid]:
            return True, mid
        elif x > L[mid]:
            low = mid + 1
        elif x < L[mid]:
            high = mid - 1

    return False


def linearSearch(x, L):
    """ return True if x is in L, False if not """
    count = 0
    for item in L:
        count += 1
        if item == x:
            return True, count
    # only gets here if not found!
    return False, count


def readReviews():
    """
    Purpose: Open a .txt file containing numerical and text-based movie reviews,
    create two linked lists containing the movie scores and movie reviews. The list
    of reviews is a nested list where each linked element contains a list with individual words.
    Parameters: None.
    Return Value: Two linked lists containing the integer scores and string reviews.
    """
    scores = []
    reviews = []
    reviewsFile = open("reviews/movieReviews.txt", 'r')
    for line in reviewsFile:
        # score is first character of line, grab it
        scores.append(int(line[:1]) - 2) # subtract 2 from score for cumulative score
        # text is second char onward, remove whitespace/caps when adding to list
        reviews.append(line[2:].strip().lower().split())
    reviewsFile.close()
    return scores, reviews


def getStopWords():
    """
    Purpose: Open a .txt file containing stop words, reads each word
    in as a string and stores it in a list.
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

    sentScore = []
    sentWords = []
    stopWords = getStopWords()

    for i in range(len(reviews)):
        for word in reviews[i]:
            if word.isalpha() and not binarySearch(word, stopWords):
                found, count = linearSearch(word, sentWords)
                index = count - 1 # linearSearch returns count starting at 1, need to index from 0
                if found:
                    print("added %i to %s: %i -> %i" \
                    %(scores[i], word, sentScore[index], sentScore[index] + scores[i]))
                    sentScore[index] += scores[i]
                else:
                    sentWords.append(word)
                    sentScore.append(scores[i])
                    print("added %s with score %i" %(word, scores[i]))


    return sentScore, sentWords


def main():
    scores, reviews = readReviews() # read in reviews
    sentScore, sentWords = sentiment(scores, reviews)
    print("sorting...")
    sentScore, sentWords = insertionSortMod(sentScore, sentWords)

    print("-----------------------------")
    for i in range(len(sentWords)-1, len(sentWords)-20, -1):
         print(sentScore[i], sentWords[i])
    print("-----------------------------")
    for i in range(20, -1, -1):
         print(sentScore[i], sentWords[i])

main()
