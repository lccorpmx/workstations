from django.test import TestCase

# Create your tests here.
from graphene_django.utils.testing import GraphQLTestCase
from mixer.backend.django import mixer
import graphene
import json

# Create your tests here.
from pcs.schema import schema
from pcs.models import workstationuser

PCS_QUERY = '''
 {
   pcs {
     cpu
     gpu
     ram
     mobo
     gabo
     data
     psu
     monitor
     mouse
   } 
 }
'''

class PCSTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    def setUp(self):
        self.pc1 = mixer.blend(workstationuser)
        self.pc2 = mixer.blend(workstationuser)
        self.pc3 = mixer.blend(workstationuser)

    def test_pcs_query(self):
        response = self.query(
            PCS_QUERY,
        )
        content = json.loads(response.content)
        #print(content)
        self.assertResponseNoErrors(response)
        print ("query pcs results ")
        print (content)
        assert len(content['data']['pcs']) == 4