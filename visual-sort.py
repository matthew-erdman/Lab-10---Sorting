"""
    Description: This is a terminal­-based bubble sort visualization. Each pair being
    considered for a swap is bracketed, and there's an accompanying textual description.
    The text explains why the swap will or will not happen. Each pass of the list is denoted,
    until we get to a pass that does no swaps and the algorithm finishes.
    Author: Matthew Erdman
    Date: 9/3/21
"""

def bubbleSortVisual(L):
    """ This is the bubble sort algorithm from sorts.py modified to show how the algorithm works:
            - given a list L
            - for every item in the list, compare to the item just to the right, swap if needed
            - keep doing the above until you go from one end of the list to the
              other and don't make any swaps!
    """
    SWAPPED = True
    for i in range(len(L)):

        input("\nPass #%i, press enter to continue..." % (i+1))

        SWAPPED = False
        for j in range(len(L)-1):

            # print list with highlighted active elements
            for k in range(len(L)):
                # two elements being compared
                if k == j:
                    print("[%i],[%i]" % (L[k], L[k+1]), end=",")
                elif k != j+1:
                    print("%i" % L[k], end=",")

            # do we have to swap?
            if L[j] > L[j+1]:
                input("\n%i > %i, swapping" % (L[j], L[j+1]))
                L[j], L[j+1] = L[j+1], L[j]
                SWAPPED = True
                print("------------------------------------")
                print(L)
            else:
                print("\n%i <= %i, no swap" % (L[j], L[j+1]))
            print("\n", end="")

        # the list is sorted if no swaps occured, end the algorithm if so
        if not SWAPPED:
            print("No swaps occured on Pass #%i, list is sorted: %s" % (i+1, L))
            return L

def main():
    from random import randint

    len = 10
    N = 10
    L = []
    for i in range(len):
        num = randint(0, N)
        L.append(num)

    print("Random list of length %i: %s" % (len, L))
    print("Bubble sort visualization!")
    print("Press enter to continue at each swap...")
    bubbleSortVisual(L)


main()
