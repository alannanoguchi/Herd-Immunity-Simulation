import random
from person import Person
from virus import Virus

class TestPerson():
    ''' These are simple tests to ensure that you are instantiating your Person class correctly. '''
    def test_vacc_person_instantiation(self):
        # create some people to test if our init method works as expected
        person = Person(1, True)
        assert person._id == 1
        assert person.is_alive is True
        assert person.is_vaccinated is True
        assert person.infection is None


    def test_not_vacc_person_instantiation(self):
        person = Person(2, False)
        # TODO: complete your own assert statements that test
        # the values at each attribute
        # assert ...
        assert person._id == 2
        assert person.is_alive is True
        assert person.is_vaccinated is False
        assert person.infection is None


    def test_sick_person_instantiation(self):
        # Create a Virus object to give a Person object an infection
        virus = Virus("Dysentery", 0.7, 0.2)
        # Create a Person object and give them the virus infection
        person = Person(3, False, virus)
        # TODO: complete your own assert statements that test
        # the values at each attribute
        assert person._id == 3
        assert person.is_alive is True
        assert person.is_vaccinated is False
        assert person.infection is not None

    def test_did_survive_infection(self):
        # TODO: Create a Virus object to give a Person object an infection
        virus = Virus("Dysentery", 0.7, 0.2)
        # TODO: Create a Person object and give them the virus infection
        person = Person(4, False, virus)

        # Resolve whether the Person survives the infection or not
        survived = person.did_survive_infection()
        # Check if the Person survived or not
        if survived:
            assert person.is_alive is True
            assert person.is_vaccinated is True
            assert person.infection is not None
        else:
            assert person.is_alive is False
            assert person.is_vaccinated is False
            assert person.infection is None