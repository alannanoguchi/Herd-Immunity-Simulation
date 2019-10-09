import random, sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus
from simulation import Simulation
import pytest

#Test constructor
def test_constructor():
    v = Virus("Test", .25, .25)
    sim = Simulation(100, .25, v,initial_infected=4,)
    assert sim.next_person_id == 0
    assert sim.total_infected == 4
    assert sim.vacc_percentage == .25
    assert sim.virus == v
    assert sim.initial_infected == 4
    assert sim.current_infected == 4
    assert sim.total_dead == 0
    assert sim.file_name == "logs/Test_simulation_pop_100_vp_0.25_infected_4.txt"
    assert sim.newly_infected == []

#Test create population 
def test_create_population():
    v = Virus("Test", .25, .25)
    sim = Simulation(100, .25, v, initial_infected=4)
    #vaccinated count
    v_count = 0
    #infected count
    i_count = 0

    #Check entire population
    for person in sim.population:
        #Make sure everyone is alive in population at start
        assert person.is_alive == True

        #count number of vaccinated people
        if person.is_vaccinated:
            v_count += 1
        #person has infection
        if person.infection is not None:
            i_count += 1

    #verify correct number of infected and vaccinated people
    assert v_count == 0
    assert i_count == 0
    assert len(sim.population) == 100