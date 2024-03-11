import random
from collections import Counter

class Vote:
    def __init__(self, id,for_condidate,which_position):        #vote(id_votecard,"john","Pos12")
        self.id = id
        self.which_position=which_position
        self.for_condidate = for_condidate
    def getsecond(self):
        return self.for_condidate
    def get_Pos_Vote(self):
        return  self.which_position

class Voter:
    def __init__(self, voter_id, name, age, address):
        self.voter_id = voter_id
        self.name = name
        self.age = age
        self.address = address
class Candidate:
    def __init__(self, name):
        self.position = set()
        self.name = name

    def add_position(self, position_str):
        self.position.add(position_str)

def init_candidate(): # "john" [pos1,pos2]
    candidates = {}
    for candidate_num in range(3):
        candidate = Candidate("Candidate" + str(candidate_num))
        for position_number in range(random.randint(1, 5)):
            candidate.add_position("Pos " + str(position_number))
        candidates[candidate.name]=candidate
    return candidates

class System:
    def __init__(self):
        self.persons = set()# Not a dictionary because there is no logical order, not a list because I need something that stores only unique values, so I will choose a set.
        self.candidates=init_candidate() #  Candidate0 {'Pos 4', 'Pos 2', 'Pos 0', 'Pos 1', 'Pos 3'}
        self.votes = []  # [(),()] # i need to perform operations like adding and removing elements, but I don't want to change the values (id, for_candidate), so I've made a list of tuples.
        self.line_of_voters = []  # FIFO
        self.number_voters = 1
        self.positions = {}  # "Pos1" [john,jenny,haha,hohn,john]
        self.winner_positions = {}  # "Pos1" [john]
        for i in range(1, 4):  # pos1        pos2        pos3
            self.positions["Pos " + str(i)] = []

    def register(self, person, name, age, addres):
        if person not in self.persons and age >=18:
            number_id = self.number_voters
            self.number_voters+=1
            voter = Voter(number_id, name, age, addres)
            self.line_of_voters.append(voter)
            self.persons.add(voter)
            print("person registered successfully. Voter ID:", voter.voter_id)
            self.persons.add(person)
        else:
            print("person registered faild. ")

    def cast_vote(self, voter_id, candidate,position): # 5,"jonny",pos1
        if position in self.candidates[candidate].position:
            vote=Vote(voter_id, candidate,position)
            self.votes.append(vote)
            print(vote.for_condidate , vote.which_position)
            self.positions[position].append(candidate)
        else:
            print("vote doesnot counted")

    def count_vote(self):
        help={}

        for position in self.positions:
            for i in self.candidates:
                help[i] = 0
            for pos in self.positions[position]:
                # print(position,pos)
                help[pos]+=1
            print(help)
            max_value = max(help.values())
            max_key = max(help, key=help.get)
            if max_value >0:
                self.winner_positions[position] = max_key
        return self.winner_positions

if __name__ == "__main__":
    voting_system = System()
    candidates = voting_system.candidates
    for _, candidate in candidates.items():
        print(candidate.name, candidate.position)

    # try to register to the voting system
    for i in range(10):
        voting_system.register(i, "voter " + str(i), random.randint(10,30), "haifa")

    for voter in voting_system.line_of_voters:
        voting_system.cast_vote(voter.voter_id, "Candidate"+str(random.randint(0, 2)),"Pos "+str(random.randint(1, 3)))
    print(voting_system.count_vote())