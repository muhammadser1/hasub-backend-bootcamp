import random
class Vote:
    def __init__(self, id, for_condidate):
        self.id = id
        self.for_condidate = for_condidate
    def getsecond(self):
        return self.for_condidate
class Voter:
    def __init__(self, voter_id, name, age, address):
        self.voter_id = voter_id
        self.name = name
        self.age = age
        self.address = address
class Candidate:
    def __init__(self, name):
        self.position = []
        self.name = name

    def addposition(self, position_str):
        self.position.append(position_str)
class System:
    def __init__(self):
        self.persons = set()# Not a dictionary because there is no logical order, not a list because I need something that stores only unique values, so I will choose a set.
        self.votes = []  # [(),()] # i need to perform operations like adding and removing elements, but I don't want to change the values (id, for_candidate), so I've made a list of tuples.
        self.candidates = {}  # name : votes       The name will serve as the key in the dictionary, simplifying the process of incrementing vote counts by using dic[name] += 1
        self.line_of_voters = []  # FIFO
        self.number_voters=1
    def register(self, person, name, age, addres):
        if person not in self.persons:
            number_id = self.number_voters
            self.number_voters+=1
            voter = Voter(number_id, name, age, addres)
            self.line_of_voters.append(voter)
            self.persons.add(voter)
            print("person registered successfully. Voter ID:", voter.voter_id)
            self.persons.add(person)
        else:
            print("person registered faild. ")
    def add_candidate(self, candidate):
        self.candidates[candidate.name] = 0

    def cast_vote(self, voter_id, candidate):
        vote=Vote(voter_id, candidate)
        self.votes.append(vote)
        print(vote.for_condidate)
    def count_votes(self):
        for vote in self.votes:
            self.candidates[vote.for_condidate] += 1

if __name__ == "__main__":
    voting_system = System()
    #try to register to the voting system
    for i in range(10):
        voting_system.register(i,"voter "+ str(i), 1000, "haifa")
    for i in range(10):
        voting_system.register(i,"voter "+ str(i), 1000, "haifa")


    for candidate_num in range(3):
        candidate = Candidate("Candidate" + str(candidate_num))
        for position_number in range(random.randint(1, 5)):
            candidate.addposition("Pos " + str(position_number))
        voting_system.add_candidate(candidate)

    for voter in voting_system.line_of_voters:
        voting_system.cast_vote(voter.voter_id, "Candidate"+str(random.randint(0, 2)))

    print("each candidate before voting day:\n\n")
    for candidate, vote_count in voting_system.candidates.items():
        print(candidate, vote_count)

    print("\neach candidate after voting day:\n")

    voting_system.count_votes()
    for candidate, vote_count in voting_system.candidates.items():
        print(candidate, vote_count)


