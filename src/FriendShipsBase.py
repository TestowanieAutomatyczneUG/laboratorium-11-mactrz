from src.FriendShips import FriendShips

class FriendShipsBase:

    def __init__(self):
        self.friends = FriendShips()

    def makeFriends(self, person1, person2):
        self.friends.makeFriends(person1, person2)

    def getFriendsList(self, person):
        return self.friends.getFriendsList(person)

    def areFriends(self, person1, person2):
        return self.friends.areFriends(person1, person2)

    def addFriend(self, person, friend):
        self.friends.addFriend(person, friend)