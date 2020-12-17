class FriendShips:

    def __init__(self, ):
        self.friendships = {}

    def makeFriends(self, person1, person2):
        if type(person1) != str or type(person2) != str:
            raise TypeError('Values must be strings')

        if self.friendships.keys().__contains__(person1) and self.friendships.keys().__contains__(person2):
            self.addFriend(person1, person2)
            self.addFriend(person2, person1)
        else:
            raise Exception('Person does not exist')

    def getFriendsList(self, person):
        if type(person) != str:
            raise TypeError('Values must be strings')

        if self.friendships.keys().__contains__(person):
            return self.friendships[person]
        else:
            raise Exception('Person does not exist')

    def areFriends(self, person1, person2):
        if type(person1) != str or type(person2) != str:
            raise TypeError('Values must be strings')

        response = False
        if self.friendships.keys().__contains__(person2):
            for friend in self.friendships[person2]:
                if friend == person1:
                    response = True
        return response

    def addFriend(self, person, friend):
        if type(person) != str or type(friend) != str:
            raise TypeError('Values must be strings')

        if self.friendships.keys().__contains__(person):
            if not self.friendships[person].__contains__(friend):
                self.friendships[person].append(friend)
        else:
            self.friendships[person] = []
            if not self.friendships[person].__contains__(friend):
                self.friendships[person].append(friend)
