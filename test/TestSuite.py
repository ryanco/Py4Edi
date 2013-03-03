import unittest
import Fixtures
import TestISASegmentParsing
import TestISASegmentValidation
import TestIEASegmentParsing
import TestGSSegmentParsing
import TestGESegmentParsing
import TestSTSegmentParsing
import TestSESegmentParsing
import TestParser
import TestParserErrors
import TestInterchangeValidation
import TestParsingMultipleGroups
import TestObfuscator
import TestFixtureReader
import TestFormatEdiDocument
import TestSegment
import TestEdiDocumentConfiguration
import TestEnvelope
import TestSimple810Document
import TestElement
import TestSettings
import TestGroupValidation

loader = unittest.TestLoader()

suite = loader.loadTestsFromModule(TestISASegmentParsing)
suite.addTests(loader.loadTestsFromModule(TestIEASegmentParsing))
suite.addTests(loader.loadTestsFromModule(TestISASegmentValidation))
suite.addTests(loader.loadTestsFromModule(TestParser))
suite.addTests(loader.loadTestsFromModule(TestParserErrors))
suite.addTests(loader.loadTestsFromModule(TestGSSegmentParsing))
suite.addTests(loader.loadTestsFromModule(TestGESegmentParsing))
suite.addTests(loader.loadTestsFromModule(TestSTSegmentParsing))
suite.addTests(loader.loadTestsFromModule(TestSESegmentParsing))
suite.addTests(loader.loadTestsFromModule(TestObfuscator))
suite.addTests(loader.loadTestsFromModule(TestInterchangeValidation))
suite.addTests(loader.loadTestsFromModule(TestParsingMultipleGroups))
suite.addTests(loader.loadTestsFromModule(TestFixtureReader))
suite.addTests(loader.loadTestsFromModule(TestFormatEdiDocument))
suite.addTests(loader.loadTestsFromModule(TestSegment))
suite.addTests(loader.loadTestsFromModule(TestEdiDocumentConfiguration))
suite.addTests(loader.loadTestsFromModule(TestEnvelope))
suite.addTests(loader.loadTestsFromModule(TestSimple810Document))
suite.addTests(loader.loadTestsFromModule(TestElement))
suite.addTests(loader.loadTestsFromModule(TestSettings))
suite.addTests(loader.loadTestsFromModule(TestGroupValidation))

#load the fixture files into memory once before all the tests
Fixtures.FixtureFiles().load_documents()

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)

print "Done"
