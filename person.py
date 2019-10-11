from virus import Virus
import random
random.seed(42)

class Person(object):
    ''' Person objects will populate the simulation. '''

    def __init__(self, _id, is_vaccinated, infection=None):
        ''' We start out with is_alive = True, because we don't make vampires or zombies. All other values will be set by the simulation when it makes each Person object.

        If person is chosen to be infected when the population is created, the simulation should instantiate a Virus object and set it as the value
        self.infection. Otherwise, self.infection should be set to None.
        '''
        self._id = _id  # int
        self.is_alive = True  # boolean
        self.is_vaccinated = is_vaccinated  # boolean
        self.infection = infection  # Virus object or None

    def did_survive_infection(self):
        ''' Generate a random number and compare to virus's mortality_rate.
        If random number is smaller, person dies from the disease.
        If Person survives, they become vaccinated and they have no infection.
        Return a boolean value indicating whether they survived the infection.
        '''
        # Only called if infection attribute is not None.
        # TODO:  Finish this method. Should return a Boolean

        # Note: random.random() produces a float between 0 and 1
        random_num = random.random()
        if self.infection != None:
            if random_num > self.infection.mortality_rate:
                self.is_alive = True 
                self.is_vaccinated = True
            else:
                self.is_alive = False 
                self.is_vaccinated = False
        return self.is_alive
