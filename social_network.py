from os import name


class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        self.friends.append(friend)


class SocialNetwork:
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(f"{name} already exists in the network!")
            return

        person = Person(name)
        self.people[name] = person

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist!")
            return

        if person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist!")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for name, person in self.people.items():
            friends = [friend.name for friend in person.friends]
            print(f"{name} is friends with: {', '.join(friends)}")


# Test your code here
alex = Person("Alex")
jordan = Person("Jordan")

print(alex.friends)

alex.add_friend(jordan)

print(alex.friends[0].name)

network = SocialNetwork()

network.add_person("Alex")
network.add_person("Jordan")
network.add_person("Morgan")
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")

network.add_person("Alex")

network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")

network.add_friendship("Alex", "Johnny")

network.print_network()


#Design Memo
#A graph is the best structure for representing a social network because it
#shows how different people are connected to each other. Each person is
#represented as a node, and each friendship is represented as an edge
#connecting two people. This makes it easy to see who is friends with who
#and allows people to have multiple connections throughout the network.
#A list or tree would not work as well because they are more limited in how
#they organize relationships. A list would store people but would not clearly
#show how everyone is connected. A tree would create a hierarchy where people
#are connected through parent and child relationships, but friendships do not
#work that way. In a social network, one person can be connected to many
#different people without having a specific order or hierarchy.
#One thing I noticed when building this network is that adding friendships
#requires updating both people's friend lists to make sure the connection
#works in both directions. Printing the network is also straightforward
#because the program can go through each person and display their friends.
#One trade-off is that larger networks with many friendships will require
#more memory to store all the connections. Overall, using an adjacency list
#makes the network easier to manage because it only stores the friendships
#that actually exist instead of tracking every possible connection between people.