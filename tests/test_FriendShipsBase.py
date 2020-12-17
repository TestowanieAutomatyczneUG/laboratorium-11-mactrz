import unittest
from unittest.mock import MagicMock
from src.FriendShipsBase import FriendShipsBase

class TestFriendShipsBase(unittest.TestCase):
    def setUp(self):
        self.tmp = FriendShipsBase()
        self.person1 = 'Test1'
        self.person2 = 'Test2'

    def test_makeFriends(self):
        self.tmp.friends.makeFriends = MagicMock()
        self.tmp.makeFriends(self.person1, self.person2)
        self.tmp.friends.makeFriends.assert_called_once_with(self.person1, self.person2)

    def test_makeFriends_exception(self):
        self.tmp.friends.makeFriends = MagicMock()
        self.tmp.friends.makeFriends.side_effect = TypeError('Values must be strings')
        self.assertRaises(TypeError, self.tmp.makeFriends, 2, 'Maciej')

    def test_makeFriends_exception2(self):
        self.tmp.friends.makeFriends = MagicMock()
        self.tmp.friends.makeFriends.side_effect = Exception('Person does not exist')
        self.assertRaises(Exception, self.tmp.makeFriends, 'Alek', 'Maciej')

    def test_getFriendsList(self):
        self.tmp.friends.getFriendsList = MagicMock()
        self.tmp.friends.getFriendsList.return_value = [self.person1, self.person2]
        result = self.tmp.getFriendsList(self.person1)
        self.assertEqual(result, [self.person1, self.person2])

    def test_getFriendsList2(self):
        self.tmp.friends.getFriendsList = MagicMock()
        self.tmp.friends.getFriendsList.return_value = [self.person1, self.person2]
        result = self.tmp.getFriendsList(self.person1)
        self.tmp.friends.getFriendsList.assert_called_once_with(self.person1)

    def test_getFriendsList_exceprtion(self):
        self.tmp.friends.getFriendsList = MagicMock()
        self.tmp.friends.getFriendsList.side_effect = TypeError('Values must be strings')
        self.assertRaises(TypeError, self.tmp.getFriendsList, 2)

    def test_getFriendsList_exceprtion2(self):
        self.tmp.friends.getFriendsList = MagicMock()
        self.tmp.friends.getFriendsList.side_effect = Exception('Person does not exist')
        self.assertRaises(Exception, self.tmp.getFriendsList, self.person2)

    def test_areFriends(self):
        self.tmp.friends.areFriends = MagicMock()
        self.tmp.friends.areFriends.return_value = True
        self.assertEqual(self.tmp.areFriends(self.person1, self.person2), True)

    def test_areFriends_false(self):
        self.tmp.friends.areFriends = MagicMock()
        self.tmp.friends.areFriends.return_value = False
        self.assertEqual(self.tmp.areFriends(self.person1, self.person2), False)

    def test_areFriends_exception1(self):
        self.tmp.friends.areFriends = MagicMock()
        self.tmp.friends.areFriends.side_effect = TypeError('Values must be strings')
        self.assertRaises(TypeError, self.tmp.areFriends, self.person1, self.person2)

    def test_areFriends_exception2(self):
        self.tmp.friends.areFriends = MagicMock()
        self.tmp.friends.areFriends.side_effect = Exception('Person does not exist')
        self.assertRaises(Exception, self.tmp.areFriends, self.person1, self.person2)

    def test_areFriends2(self):
        self.tmp.friends.areFriends = MagicMock()
        self.tmp.friends.areFriends.return_value = True
        self.tmp.areFriends(self.person1, self.person2)
        self.tmp.friends.areFriends.assert_called_with(self.person1, self.person2)

    def test_addFriend(self):
        self.tmp.friends.addFriend = MagicMock()
        self.tmp.addFriend(self.person1, self.person2)
        self.tmp.friends.addFriend.assert_called_with(self.person1, self.person2)

    def test_addFriend_exception(self):
        self.tmp.friends.addFriend = MagicMock()
        self.tmp.friends.addFriend.side_effect = TypeError('Values must be strings')
        self.assertRaises(TypeError, self.tmp.addFriend, self.person1, self.person2)

    def test_addFriend_exception2(self):
        self.tmp.friends.addFriend = MagicMock()
        self.tmp.friends.addFriend.side_effect = Exception('Person does not exist')
        self.assertRaises(Exception, self.tmp.addFriend, self.person1, self.person2)