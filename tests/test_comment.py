import unittest
from app.models import Comment,User
from flask_login import current_user
from app import db

class TestComment(unittest.TestCase):

    def setUp(self):
        self.user_Mariam = User(username = 'Mariam',
                                 password = 'jasonmusa8',
                                 email = 'sufimariam8@gmail.com')
        self.new_comment = Comment(id=12345,
                                     post_comment="great post!",
                                     category_id='funny',
                                     blogposts="great post,
                                     user_id = self.user_Mariam)

    def tearDown(self):
        Comment.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.id,12345)
        self.assertEquals(self.new_comment.post_comment,"great psot!")
        self.assertEquals(self.new_comment.category_id,'funny')
        self.assertEquals(self.new_comment.blogposts, 'great post')
        self.assertEquals(self.new_comment.user,self.user_Mariam)


    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)


    def test_get_comment_by_id(self):

        self.new_comment.save_comment()
        got_comments = Comment.get_comments(12345)
        self.assertTrue(len(got_comments) == 1)