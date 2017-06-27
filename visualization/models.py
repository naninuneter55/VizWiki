from django.db import models

class Material(models.Model):
    sparql = models.TextField('SPARQL')
    title = models.CharField('タイトル', max_length=256)
    template = models.CharField('テンプレート', max_length=256)
    meta = models.TextField('メタ情報')

    def __str__(self):
        return self.title

class Sparql:

    def query(material):
        res = Sparql.perform_query(material.sparql)
        # print("=== {} ===".format(res))
        return res

    def perform_query(sparql):
        # print("=== {} ===".format(sparql))
        from SPARQLWrapper import SPARQLWrapper, JSON
        sw = SPARQLWrapper("http://ja.dbpedia.org/sparql")
        sw.setQuery(sparql)
        sw.setReturnFormat(JSON)
        result = sw.query().convert()
        return result
