# Built-in libaries
import unittest

# Third-party libraries
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_game_and_play_it_till_the_end(self):

        # Boris remembers "Bulls'n'Cows" from his school days, when he and his friends had no mobile phones to
        # pass their time away. He now discovers a new website that let's him play the good old game online.
        # He opens up the webpage in the browser:
        self.browser.get("http://localhost:8000")

        # The website says: "Bulls and Cows is now online!"
        self.assertIn("Bulls and Cows", self.browser.title)
        self.fail("Finish the test!")

        # He notices the website has a large "START" button in the middle of the screen. Tempted to play, he clicks it.

        # The page changes and instead of the "START" button, 4 square input fields appear.
        # Beneath them is now a "SUBMIT" button.

        # Boris types in 4 numbers at random: 3-1-6-8; He hits "Submit".

        # On the right of the boxes he sees his own number followed by a score: 3168 : 1b 1c
        # Not bad for a first try!

        # Boris makes another 3 attempts. After each one of them he can see the last number with its score
        # being appended to the list of the guesses he's made before.

        # Being an experienced player, Boris analyzes the scores and enters one final number: 5961
        # The input fields disappear and instead of them he sees "Congratulations!" printed in a heavy font.

        # He looks at the score list and sees that his last guess has got "4b 0c". He has won the game!

        # A "PLAY AGAIN" button takes the place of the "SUBMIT" button.

        # Boris clicks it and is taken to the page where it all has begun, "START" button shining invitingly at him.

        # His lunch break has just ended. What a nostalgic experience it has been!
        # Boris closes the browser and goes back to work


if __name__ == "__main__":
    unittest.main()
