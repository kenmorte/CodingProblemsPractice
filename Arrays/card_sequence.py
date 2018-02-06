// NOTE: Asked by Apple 2/5/18

#include <iostream>
#include <vector>
#include <map>
#include <cstdlib>
#include <ctime>

// Deck Size (feel free to change)
#define SIZE 10

using namespace std;

/**
 * Deck Class
 */
class Deck {
public:
    /**
     * Initializes the deck with a specified number of cards.
     * Initial sorting of cards is by increasing value.
     * O(n) time
     */
    Deck(int size);

    /**
     * Shuffles the deck in-place with a new random permutation.
     * Based on the Knuth Shuffle Algorithm (https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle).
     * O(n) time
     */
    void shuffle();

    /**
     * Prints the current ordering of a deck in one line on the console.
     * Format is as follows: CARD_1 CARD_2 CARD_3 ... where CARD_N is an integer to represent the card
     * O(n) time
     */
    void print() const;

    /**
     * Returns the current ordering of the cards.
     * O(1) time
     */
    const vector<int>& getCards() const;
private:
    /**
     * Cards are represented as integers, where each integer is unique.
     * O(n) space - n is the number of cards 
     */
    vector<int> cards;
};

/**
 * Deck Methods
 */
Deck::Deck(int size) {
    cards.resize(size);
    for (int i = 0; i < size; i++) {
        cards[i] = i;
    }
}

void Deck::shuffle() {
    for (int i = cards.size()-1; i > 0; i--) {
        int j = rand() % i;
        int temp = cards[i];
        cards[i] = cards[j];
        cards[j] = temp;
    }
}

void Deck::print() const {
    for (int i = 0; i < cards.size(); i++) {
        cout << cards[i] << " ";
    }
    cout << endl;
}

const vector<int>& Deck::getCards() const {
    return cards;
}

/**
 * Sequence Helper Methods
 */

 /**
  * Returns a map of all the next cards in a 2-card sequence for each card.
  * The last card has no "next card" for it, so it uses -1 as a placeholder.
  * O(n) time - n is the number of cards in the deck
  */
map<int,int> getSequenceMap(const Deck &deck) {
    const vector<int> &arr = deck.getCards();
    map<int, int> res;

    // Insert the "next" card for all cards
    for (int i = 0; i < arr.size()-1; i++) {
        res.insert( pair<int,int>(arr.at(i), arr.at(i+1)) );
    }

    // Last card doesn't have a next card sequence to it, so just set the next to -1 (impossible case)
    res.insert( pair<int,int>(arr.at(arr.size()-1), -1) );
    return res;
}

/**
 * Find the position of the first 2-card sequence inside a deck of cards.
 * O(n) time - n is the number of cards in the deck
 */
int getSequenceStart(const Deck &deck, const map<int,int> &seqMap) {
    const vector<int> &arr = deck.getCards();
    for (int i = 0; i < arr.size()-1; i++) {
        const int currentNum = arr.at(i);
        const int nextNum = arr.at(i+1);
        const int shouldBeNextNum = seqMap.at(currentNum);

        if (nextNum == shouldBeNextNum) return currentNum;
    }
    return -1;
}

/**
 * Main Function
 * Overall time complexity: O(kn)
 *      - n = number of cards in the deck
 *      - k = number of attempts until failure (randomly based)
 *      - Maintaing the deck of cards (intializing, shuffling, printing) all take O(n) time.
 *      - Creating the 2-card sequence map for each card and finding if one exists in the previous shuffle both take O(n) time.
 * Overall space complexity: O(n)
 *      - n = number of cards in the deck
 *      - Using our Deck class and maintaining the map of all 2-card sequences for a shuffle take O(n) space.
 */
int main()
{
    // Initialize random number generator seed
    srand(time(NULL));

    // Initialize and shuffle original deck ordering
    Deck deck(SIZE);
    deck.shuffle();

    // Save all the 2-card sequences from the original ordering
    map<int,int> seqMap = getSequenceMap(deck);

    // Print the initial shuffled order of the deck
    cout << "Original Deck:" << endl;
    deck.print();

    // Shuffle the order again to compare with the initial shuffle
    cout << endl << "Current Deck:" << endl;
    deck.shuffle();
    deck.print();

    // Keep track of the current start of the sequence and the number of failed attempts to find a sequence after shuffling
    int startSeq = -1;
    int failedShuffles = 0;

    while (failedShuffles < 2) {
        startSeq = getSequenceStart(deck, seqMap);  // Find first card with a dupicate 2-card sequence

        if (startSeq == -1) {   // No duplicate sequence was found
            cout << "FAIL: No 2-card sequence found from previous shuffle!" << endl;
            failedShuffles++;
        }
        else {  // Duplicate sequence was found
            cout << "SUCCESS: Found 2-card sequence of (" << startSeq << ", " << seqMap.at(startSeq) << ") from previous shuffle!" << endl;
            failedShuffles = 0;
        }

        cout << endl;

        // We don't need to shuffle anymore if we've back-to-back shuffles 
        // produced no 2-card sequence from original (since we're done)
        if (failedShuffles < 2) {

            // Get all the 2-card sequences from the current shuffle
            seqMap = getSequenceMap(deck);

            // Shuffle the current deck
            cout << "Shuffling deck..." << endl << endl;;
            cout << "Current Deck:" << endl;
            deck.shuffle();
            deck.print();
        }
    }

    cout << "Back-to-back shuffles did not find any 2-card sequence! Ending program..." << endl << endl;;
}

/*
Questions:
1) How might you adapt your code to check for sequences of 3, 4, or more cards from the previous shuffle?

To check for a sequences of 3, 4, or more cards from the previous shuffle, I would change my sequence map to use a single card as a key
and a vector of k cards to represent the k-card sequence starting at the card that's the key. Then when we query if there is a duplicate
sequence from the previous shuffle, we would compare the k-card sequence after the card in the current shuffle with the k-card sequence
in the map from the previous shuffle. Code-wise, this would involve:

    - Changing getSequenceMap(...) to return a map<int,vector<int>>
    - Searching k-cards ahead of each card inside getSequenceMap(...) and getSequenceStart(...)
    - Using a hard comparison of the vectors representing the k-card sequences inside getSequenceStart(...)



2) How might you adapt your code to check for combinations of N cards, rather than sequences? In a combination, the order of cards does not matter. In a sequence, the order of cards does matter.

I would use some variation of the sliding window technique to maintain the current N-card combination and previous. Instead of using a map,
I would maintain two hash sets of size N for both the previous shuffle and the current shuffle at a certain index. If the two hash sets are
equal (have the same length and elements inside them), then we can say that the current shuffle has an N-card combination from the previous.
Otherwise, we move on to the next index by taking out the oldest card from both hash sets and adding in the new card on the next index, and
repeating the process from there.



3) How might you adapt your code to check for card sequences that were present in any previous shuffle? (i.e. comparing against all previous shuffles, not just the most recent one)

For a k-card sequence, I would change my sequence map to utilize a collection of previous sequences encountered instead of just storing one
sequence from the previous shuffle. In a brute-force solution, I can store a vector of k-card sequences (represented as vectors) of all the
seuences that came after this card from the previous shuffles, and we can compare whatever card we are at in the current shuffle with those
in the previous using the hash map. However, this would take O(n) time. A clever technique is to find a way to hash the k-card sequences 
by creating a string encoding of each k-card sequence, making lookup if a previous sequence existed O(1) time. Overall, the basic idea
is to store all previous sequences for each card in a collection, stored in some hash map.



4) Would you do differently if you were now optimizing for memory over speed?
I probably would not do differently if I was optimizing for memory over speed, since the overall space complexity of the operation is
O(n). The minimum we would need to store are the current set of cards (to shuffle, reshuffle), and either the previous shuffle of cards
or the map of sequences from the previous shuffle. In my case, I went with the latter because it optimized for speed. However, in both
cases, the space complexity is still O(n).
*/
