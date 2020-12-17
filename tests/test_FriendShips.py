import unittest
from src.FriendShips import FriendShips

class TestFriendShips(unittest.TestCase):

    def setUp(self):
        self.tmp = FriendShips()

    def test_addFriend(self):
        self.tmp.addFriend('Person1', 'Person2')
        self.assertEqual(self.tmp.friendships, {'Person1': ['Person2']})

    def test_addFriend_exception(self):
        self.assertRaises(TypeError, self.tmp.addFriend, 2, 'Person2')

    def test_areFriends_true(self):
        self.tmp.friendships = {'Maciej': ['Jarek', 'Olek'], 'Olek': ['Maciej']}
        self.assertEqual(self.tmp.areFriends('Maciej', 'Olek'), True)

    def test_areFriends_false(self):
        self.tmp.friendships = {'Maciej': ['Jarek', 'Olek'], 'Olek': ['Mateusz']}
        self.assertEqual(self.tmp.areFriends('Maciej', 'Olek'), False)

    def test_areFriends_exception(self):
        self.assertRaises(TypeError, self.tmp.areFriends, 'Maciej', True)

    def test_getFriendsList(self):
        self.tmp.friendships = {'Maciej': ['Jarek', 'Olek'], 'Olek': ['Mateusz']}
        self.assertEqual(self.tmp.getFriendsList('Maciej'), ['Jarek', 'Olek'])

    def test_getFriendsList_exception_wrong_type(self):
        self.assertRaises(TypeError, self.tmp.getFriendsList, 2)

    def test_getFriendsList_exception_person_not_exist(self):
        self.assertRaises(Exception, self.tmp.getFriendsList, 'KEKE')

    def test_makeFriends(self):
        self.tmp.friendships = {'Maciej': ['Jarek', 'Marek'], 'Olek': ['Mateusz']}
        self.tmp.makeFriends('Maciej', 'Olek')
        self.assertEqual(self.tmp.friendships['Olek'], ['Mateusz', 'Maciej'])

    def test_makeFriends_exception_wrong_type(self):
        self.assertRaises(TypeError, self.tmp.makeFriends, 3, 'Maciej')

    def test_makeFriends_exception_person_not_exists(self):
        self.assertRaises(Exception, self.tmp.makeFriends, 'Aleks', 'Maciej')