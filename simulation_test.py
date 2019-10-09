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
    sim = Simulation(100, .25, v, initial_infected=4)
    assert sim.next_person_id == 100
    assert sim.total_infected == 4
    assert sim.vacc_percentage == .25
    assert sim.virus == v
    assert sim.initial_infected == 4
    assert sim.current_infected == 4
    assert sim.total_dead == 0
    assert sim.file_name == "Test_simulation_pop_100_vp_0.25_infected_4.txt"
    assert sim.newly_infected == []
    assert sim.newly_dead == []