from src.agents.Agent import Agent

class Customer(Agent):
    def __init__(self, id):
        self.id = id
        self.total_wating_time = 0