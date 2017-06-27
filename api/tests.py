from django.test import TestCase
from visualization.models import Material
from visualization.models import Sparql
from unittest.mock import patch
from django.test import Client
from django.core.urlresolvers import reverse


class ApiTestCase(TestCase):
    fixtures = ['fixtures/initial_data.yaml']

    def setUp(self):
        self.mate = Material.objects.get(pk=1)

    def testTest(self):
        self.assertEquals(self.mate.title, 'テスト')

class ViewTestCase(TestCase):

    fixtures = ['fixtures/initial_data.yaml']

    @patch('visualization.models.Sparql.perform_query')
    def test_index(self, mock):
        # mock_class.perform_query.return_value =
        mock.return_value = {'results': {'bindings': [{'pref': {'type': 'literal', 'value': '東京都'}, 'count': {'type': 'typed-literal', 'datatype': 'http://www.w3.org/2001/XMLSchema#integer', 'value': '245'}, 'sample': {'type': 'literal', 'value': 'コロムビア・トップ__下村_泰（コロムビア・トップ）__1'}}]}}
        client = Client()
        response = client.get(reverse('api:query', kwargs={'material_id': 2}))
        self.assertEquals(response.status_code, 200)
        self.assertRegex(response.json()['comment'], "第一位に輝いたのは東京都。245人でした。")
