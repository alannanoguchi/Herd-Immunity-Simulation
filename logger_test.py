import random
from person import Person
from virus import Virus
from logger import Logger

# TODO: Write a test suite for this class to make sure each method is working as expected.
# PROTIP: Write your tests before you solve each function, that way you can test them one by one as you write your class.
class TestLogger():

    def test_logger(self):

        '''Tests logger functions'''
        sim1 = Logger('log.txt')
        with open('log.txt') as f:
            log_output = f.readline()

        assert sim1.write_metadata(100, 10, 'Dengue Fever', 5, 3) == "Population | Total:100\tVaccinated Percentage: 10\nVirus | Name: Dengue Fever\tMortality Rate: 5\tReproductive Rate: 3\n"


    def test_add_interaction(self):
        '''Tests log_interaction function'''
        person1 = Person(1, False)
        person2 = Person(2, True)
        sick_person = Logger('log.txt')
        # with open('log.txt') as f:
        #     log_output = f.readlines()

        assert sick_person.log_interaction(person1, person2, False, True, False) == "1 didn't infect 2 because they are vaccinated. \n"

    def test_infection_survive(self):
        '''Tests log_infection_survival function'''
        person1 = Person(1, True)
        survivor = Logger('log.txt')

        assert survivor.log_infection_survival(person1, False) == "1 survived infection. \n"

# if __name__ == '__main__':
#     test_logger()
#     test_add_interaction()
#     test_infection_survive()