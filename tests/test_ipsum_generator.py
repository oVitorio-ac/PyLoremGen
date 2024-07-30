import unittest
from pylorem.generator.lorem_ipsum import LoremIpsum

class TestLoremIpsum(unittest.TestCase):

    # Generates a specified number of lorem ipsum paragraphs with start_with_lorem_ipsum=True, and checks if the result has the correct number of paragraphs, starts with "Lorem ipsum", and ends with "\n \n".
    def test_generate_paragraphs_with_start_true_fixed(self):
        """
        Generate paragraphs with `start_with_lorem_ipsum` set to `True`.

        :param self: The object instance.
        :return: None
        """
        # Arrange
        lorem = LoremIpsum()
        paragraphs_numbers = 3
        start_with_lorem_ipsum = True

        # Act
        result = lorem.paragraphs(paragraphs_numbers, start_with_lorem_ipsum)

        # Assert
        self.assertEqual(len(result.split("\n")), paragraphs_numbers + 3)
        self.assertTrue(result.startswith(lorem.start_with_lorem_ipsum))
        self.assertTrue(result.endswith("\n \n"))

    # Generates a specified number of lorem ipsum paragraphs with start_with_lorem_ipsum=False.
    def test_generate_paragraphs_with_start_false_fixed(self):
        """
        Generates paragraphs of Lorem Ipsum text with the given number of paragraphs and the option to start with "Lorem Ipsum" or not.

        :param paragraphs_numbers: The number of paragraphs to generate (int).
        :param start_with_lorem_ipsum: Whether to start each paragraph with "Lorem Ipsum" or not (bool).

        :return: The generated Lorem Ipsum text (str).
        """
        # Arrange
        lorem = LoremIpsum()
        paragraphs_numbers = 5
        start_with_lorem_ipsum = False

        # Act
        result = lorem.paragraphs(paragraphs_numbers, start_with_lorem_ipsum)

        # Assert
        self.assertEqual(len(result.split("\n")), paragraphs_numbers + 3)
        self.assertFalse(result.startswith(lorem.start_with_lorem_ipsum))
        self.assertTrue(result.endswith("\n \n"))

    # Generates a string of random words.
    def test_generate_random_words(self):
        """
        Generates a random sequence of words using the LoremIpsum class.

        Parameters:
            self (TestClass): The current instance of the test class.
        
        Returns:
            None
        """
        # Arrange
        lorem = LoremIpsum()
        words_numbers = 10

        # Act
        result = lorem.words(words_numbers)

        # Assert
        self.assertEqual(len(result.split()), words_numbers)

    # Generates a shopping list of randomly selected items.
    def test_generate_shopping_list(self):
        """
        Test the generate shopping list function.

        This function tests the functionality of the `shopping_list` method in the `LoremIpsum` class. It verifies that the returned shopping list has the expected number of items and starts with the correct header.

        Parameters:
            self (object): The current instance of the `TestCase` class.
        
        Returns:
            None
        """
        # Arrange
        lorem = LoremIpsum()
        items_count = 5

        # Act
        result = lorem.shopping_list(items_count)

        # Assert
        self.assertEqual(len(result.split("\n")), items_count + 1)
        self.assertTrue(result.startswith("Shopping List:"))

    # Generates 0 paragraphs.
    def test_generate_zero_paragraphs_fixed(self):
        """
        Generate a zero paragraphs of lorem ipsum text.

        This function takes no parameters.

        Returns:
            str: The generated lorem ipsum text.
        """
        # Arrange
        lorem = LoremIpsum()
        paragraphs_numbers = 0

        # Act
        result = lorem.paragraphs(paragraphs_numbers)

        # Assert
        self.assertEqual(len(result.split("\n")), 4)
        self.assertTrue(result.startswith(lorem.start_with_lorem_ipsum))
        self.assertTrue(result.endswith("\n \n"))

    # Generates 1 paragraph with start_with_lorem_ipsum=True.
    def test_generate_one_paragraph_with_start_true(self):
        """
        Generates a single paragraph of lorem ipsum text using the given parameters.

        Args:
            self (object): The current instance of the LoremIpsum class.
            paragraphs_numbers (int): The number of paragraphs to generate.
            start_with_lorem_ipsum (bool): Specifies whether the generated text should start with "Lorem ipsum dolor sit amet".

        Returns:
            str: The generated paragraph of lorem ipsum text.

        Raises:
            AssertionError: If the length of the generated text does not match the expected value.
            AssertionError: If the generated text does not start with the specified prefix.
            AssertionError: If the generated text does not end with the expected suffix.
        """
        # Arrange
        lorem = LoremIpsum()
        paragraphs_numbers = 1
        start_with_lorem_ipsum = True

        # Act
        result = lorem.paragraphs(paragraphs_numbers, start_with_lorem_ipsum)

        # Assert
        self.assertEqual(len(result.split("\n")), 4)
        self.assertTrue(result.startswith(lorem.start_with_lorem_ipsum))
        self.assertTrue(result.endswith("\n \n"))

    # Generates 1 paragraph with start_with_lorem_ipsum=False.
    def test_generate_one_paragraph_with_start_false_fixed(self):
        """
        Generates a single paragraph of Lorem Ipsum text using the given parameters.

        :param paragraphs_numbers: The number of paragraphs to generate. Only 1 paragraph is generated in this case.
        :type paragraphs_numbers: int

        :param start_with_lorem_ipsum: Whether the generated paragraph should start with "Lorem ipsum" or not. In this case, it is set to False.
        :type start_with_lorem_ipsum: bool

        :return: The generated Lorem Ipsum paragraph.
        :rtype: str
        """
        
        # Arrange
        lorem = LoremIpsum()

        paragraphs_numbers = 1
        start_with_lorem_ipsum = False

        # Act
        result = lorem.paragraphs(paragraphs_numbers, start_with_lorem_ipsum)

        # Assert
        self.assertEqual(len(result.split("\n")), 4)
        self.assertFalse(result.startswith(lorem.start_with_lorem_ipsum))
        self.assertTrue(result.endswith("\n \n"))

    # Generates 0 words.
    def test_generate_zero_words(self):
        """
        Generate the function comment for the given function body in a markdown code block with the correct language syntax.

        :param self: The instance of the test class.
        :return: None
        """
        # Arrange
        lorem = LoremIpsum()
        words_numbers = 0

        # Act
        result = lorem.words(words_numbers)

        # Assert
        self.assertEqual(len(result.split()), words_numbers)

    # Generates 1 word.
    def test_generate_one_word(self):
        """
        Test the `words` method of the `LoremIpsum` class when generating one word.

        This test case checks if the `words` method of the `LoremIpsum` class correctly generates the specified number of words. The test first arranges the necessary variables by creating an instance of the `LoremIpsum` class and setting the `words_numbers` variable to 1. Then, the test acts by calling the `words` method with the `words_numbers` parameter. Finally, the test asserts that the length of the result, after splitting it into a list of words, is equal to the specified `words_numbers`.

        This test helps ensure that the `words` method of the `LoremIpsum` class behaves as expected when generating one word.

        :param self: The test case instance.
        """

        # Arrange
        lorem = LoremIpsum()
        words_numbers = 1

        # Act
        result = lorem.words(words_numbers)

        # Assert
        self.assertEqual(len(result.split()), words_numbers)
