from django.test import TestCase
from visualization.models import Material
from visualization.models import Sparql
from unittest.mock import patch
from SPARQLWrapper import SPARQLWrapper

class MaterialTestCase(TestCase):

    def setUp(self):
        self.simple = Material.objects.create(sparql="sparql", title="title", template="template", meta="meta")

    # def testStr(self):
    #     self.assertEquals(self.simple.__str__(), 'title')

class SparqlTest(TestCase):

    fixtures = ['fixtures/initial_data.yaml']

    def setUp(self):
        self.mtr = Material.objects.get(pk=1)
        self.sqarql = Sparql

    # @patch('visualization.models.Sparql')
    # def test_query(self, mock_class):
    #     mock_class.perform_query.return_value = 'aaa'
    #     sparql = Sparql.query(self.mtr)
    #     self.assertEquals(sparql, 'aaa')
