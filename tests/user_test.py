import unittest
from app.models import User, Blog_Post, Comment
from app import db, email


class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username='ray',password='123rnk', email = 'rachael.kiarie@student.moringaschool.com')

    def test_instance_user(self):
        '''
        Tests the instances of user
        '''
        self.assertEquals(self.new_user, User) 
      
    #tests if the password is hashed and that it's not an empty value
    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)
    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password
    
    def test_password_verification(self):
            self.assertTrue(self.new_user.verify_password('123rnk'))

class PostTest(unittest.TestCase):

    def setUp(self):
        self.new_post= Blog_Post( title='Hydrate', content = 'frink water', user_id = 'ray')
        
    def test_instance(self):
        '''
        Tests the instances of posts
        '''
        self.assertEquals(self.new_post, Blog_Post)

class CommentTest(unittest.TestCase):

    def setUp(self):
        self.new_comment= Comment( comment ='Good idea', post_id = 'first post', user_id = 'ray')
        
    def test_instance(self):
        '''
        Tests the instances of Comment
        '''
        self.assertEquals(self.new_comment, Comment)
       
    def tearDown(self):
        User.query.delete()
        Comment.query.delete()
        Blog_Post.query.delete()
if __name__ == '__main__':
    unittest.main()