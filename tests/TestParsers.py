import unittest

from utils import Parsers


class TestParsers(unittest.TestCase):
    def test_one_to_one_parser(self):
        parse = Parsers.one_to_one_parser
        self.assertEqual(parse(["1"]), ([[1, 1]], False))
        self.assertEqual(parse(["a"]), ([], True))
        self.assertEqual(parse(["1-2"]), ([[1, 2]], False))
        self.assertEqual(parse(["2-1"]), ([], True))

        self.assertEqual(parse(["a-2"]), ([], True))
        self.assertEqual(parse(["1-b"]), ([], True))

        self.assertEqual(parse(["-"]), ([], True))
        self.assertEqual(parse(["1-"]), ([], True))
        self.assertEqual(parse(["-2"]), ([], True))
        self.assertEqual(parse(["1-2-3"]), ([], True))

    def test_chapter_paragraph_parser(self):
        parse = Parsers.chapter_paragraph_parser
        self.assertEqual(parse(["1:2-2:1"]), ([[1, 2, 2, 1]], False))

        self.assertEqual(parse(["1:2-a:1"]), ([], True))
        self.assertEqual(parse(["1:2-2:b"]), ([], True))

        self.assertEqual(parse(["1:2-2:"]), ([], True))
        self.assertEqual(parse(["1:2-2:1:"]), ([], True))
        self.assertEqual(parse(["1:2-2:1:2"]), ([], True))

        self.assertEqual(parse(["1:2-3"]), ([[1, 2, 1, 3]], False))

        self.assertEqual(parse(["1:2-a"]), ([], True))

        self.assertEqual(parse(["a:2-2:1"]), ([], True))
        self.assertEqual(parse(["1:b-2:1"]), ([], True))

        self.assertEqual(parse(["1:-2:1"]), ([], True))
        self.assertEqual(parse(["1:2:-2:1"]), ([], True))
        self.assertEqual(parse(["1:2:3-2:1"]), ([], True))

        self.assertEqual(parse(["1-2:1"]), ([], True))

        self.assertEqual(parse(["1:1-"]), ([], True))
        self.assertEqual(parse(["-2:1"]), ([], True))
        self.assertEqual(parse(["1:1-2:1-3:1"]), ([], True))

        self.assertEqual(parse(["1:2"]), ([[1, 2, 1, 2]], False))

        self.assertEqual(parse(["a:1"]), ([], True))
        self.assertEqual(parse(["1:b"]), ([], True))

        self.assertEqual(parse(["1:2:3"]), ([], True))
        self.assertEqual(parse(["1:"]), ([], True))
        self.assertEqual(parse([":"]), ([], True))

        self.assertEqual(parse(["1.2-2.1"]), ([[1, 2, 2, 1]], False))
        self.assertEqual(parse(["1.2-2.1"]), ([[1, 2, 2, 1]], False))

        self.assertEqual(parse(["1.2-a.1"]), ([], True))
        self.assertEqual(parse(["1.2-2.b"]), ([], True))

        self.assertEqual(parse(["1.2-2."]), ([], True))
        self.assertEqual(parse(["1.2-2.1."]), ([], True))
        self.assertEqual(parse(["1.2-2.1.2"]), ([], True))

        self.assertEqual(parse(["1.2-3"]), ([[1, 2, 1, 3]], False))

        self.assertEqual(parse(["1.2-a"]), ([], True))

        self.assertEqual(parse(["a.2-2.1"]), ([], True))
        self.assertEqual(parse(["1.b-2.1"]), ([], True))

        self.assertEqual(parse(["1.-2.1"]), ([], True))
        self.assertEqual(parse(["1.2.-2.1"]), ([], True))
        self.assertEqual(parse(["1.2.3-2.1"]), ([], True))

        self.assertEqual(parse(["1-2.1"]), ([], True))

        self.assertEqual(parse(["1.1-"]), ([], True))
        self.assertEqual(parse(["-2.1"]), ([], True))
        self.assertEqual(parse(["1.1-2.1-3.1"]), ([], True))

        self.assertEqual(parse(["1.2"]), ([[1, 2, 1, 2]], False))

        self.assertEqual(parse(["a.1"]), ([], True))
        self.assertEqual(parse(["1.b"]), ([], True))

        self.assertEqual(parse(["1.2.3"]), ([], True))
        self.assertEqual(parse(["1."]), ([], True))
        self.assertEqual(parse(["."]), ([], True))

        self.assertEqual(parse(["-"]), ([], True))
        self.assertEqual(parse(["1"]), ([], True))


if __name__ == "__main__":
    unittest.main()
