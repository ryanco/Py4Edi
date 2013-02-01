import unittest
import TestISASegmentParsing
import TestISASegmentValidator
import TestIEASegmentParsing
import TestGSSegmentParsing
import TestGESegmentParsing
import TestSTSegmentParsing
import TestSESegmentParsing
import TestParser
import TestParserErrors
import TestInterchangeValidator
import TestParsingMultipleGroups
import TestObfuscator

loader = unittest.TestLoader()

suite = loader.loadTestsFromModule(TestISASegmentParsing)
suite.addTests(loader.loadTestsFromModule(TestIEASegmentParsing))
suite.addTests(loader.loadTestsFromModule(TestISASegmentValidator))
suite.addTests(loader.loadTestsFromModule(TestParser))
suite.addTests(loader.loadTestsFromModule(TestParserErrors))
suite.addTests(loader.loadTestsFromModule(TestGSSegmentParsing))
suite.addTests(loader.loadTestsFromModule(TestGESegmentParsing))
suite.addTests(loader.loadTestsFromModule(TestSTSegmentParsing))
suite.addTests(loader.loadTestsFromModule(TestSESegmentParsing))
suite.addTests(loader.loadTestsFromModule(TestObfuscator))
suite.addTests(loader.loadTestsFromModule(TestInterchangeValidator))
suite.addTests(loader.loadTestsFromModule(TestParsingMultipleGroups))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
