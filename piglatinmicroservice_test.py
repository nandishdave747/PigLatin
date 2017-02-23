import unittest


class TestPigLatinMicroservices(unittest.TestCase):

    
    def test_split_paragraph(self):
        paragraph = "pig banana trash happy duck glove eat omelet are"

            self.assertIsInstance(
                paragrapgh.split(" "),
                list,
                'Splitting paragraph by space should return list of words' 
            )

suite = unittest.TestLoader().loadTestsFromTestCase(TestPigLatinMicroservices)
unittest.TextTestRunner(verbosity=2).run(suite)