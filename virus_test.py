import random
from virus import Virus

class TestVirus:

    def test_virus_instantiation(self):
        #TODO: Create your own test that models the virus you are working with
        '''Check to make sure that the virus instantiator is working.'''
        virus = Virus("HIV", 0.8, 0.3)
        assert virus.name == "HIV"
        assert virus.repro_rate == 0.8
        assert virus.mortality_rate == 0.3

