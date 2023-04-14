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

CREATE_WS_MUTATION= '''
    mutation createWs($cpu: String, $data: String, $gabo: String, $gpu: String, $mobo: String, $monitor: String, $mouse: String, $psu: String, $ram: String, $teclado: String, ){
        createWs(cpu: $cpu, data: $data, gabo: $gabo, gpu: $gpu, mobo: $mobo, monitor: $monitor, mouse: $mouse, psu: $psu, ram: $ram, teclado: $teclado){
            cpu
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

    def test_createWS_mutation(self):

        response = self.query(
            CREATE_WS_MUTATION,
            variables={'cpu':'ryzen 7', 'data':'360 ssd', 'gabo':'mun frust', 'gpu':'gpu 1050', 'mobo':'asus', 'monitor':'asus', 'mouse':'logitech', 'psu':'corsair', 'ram':'36bg', 'teclado':'corsair'}
        )
        print('mutation ')
        print(response)
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)
        self.assertDictEqual({"createWs": {"cpu": "ryzen 7"}}, content['data'])