import unittest
from app.models import User,Pitch
from app import db

class TestPitch(unittest.TestCase):

    def setUp(self):
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_pitch  = Pitch( pitch = 'life is a mess',category = 'education',name = 'nick',author = self.user_James )

    def tearDown(self):
        User.query.delete()
        Pitch.query.delete()


    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.pitch, 'life is a mess')
        self.assertEquals(self.new_pitch.category,"education")
        self.assertEquals(self.new_pitch.name,"nick")
        self.assertEquals(self.new_pitch.author, self.user_James)

