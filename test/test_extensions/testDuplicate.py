import unittest
from ..testHelpers import get_cpp_fileinfo_with_extension
from lizard_ext.lizardduplicate import LizardExtension as DuplicateDetector

class TestDuplicateExtension(unittest.TestCase):

    def setUp(self):
        self.detector = DuplicateDetector()

    def test_empty_file(self):
        get_cpp_fileinfo_with_extension('''
        ''', self.detector)
        self.assertEqual([], self.detector.duplicates)

    def test_two_functions_that_are_exactly_the_same(self):
        get_cpp_fileinfo_with_extension('''
            void func1(int param) {
                int result, i = 0;
                for (; i < 10; i++) {
                    result += i * i;
                }
                return result;
            }

            void func2(int param) {
                int result, i = 0;
                for (; i < 10; i++) {
                    result += i * i;
                }
                return result;
            }
        ''', self.detector)
        self.assertEqual(1, len(self.detector.duplicates))
