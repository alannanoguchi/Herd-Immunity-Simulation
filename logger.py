from person import Person
from virus import Virus
import os

class Logger(object):
    ''' Utility class responsible for logging all interactions during the simulation. '''

    def __init__(self, file_name):
        # TODO:  Finish this initialization method. The file_name passed should be the full file name of the file that the logs will be written to.
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
        '''
        The simulation class should use this method immediately to log the specific parameters of the simulation as the first line of the file.
        '''
        # TODO: Finish this method. This line of metadata should be tab-delimited
        # it should create the text file that we will store all logs in.
        # TIP: Use 'w' mode when you open the file. For all other methods, use
        # the 'a' mode to append a new log to the end, since 'w' overwrites the file.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        initial_params = f"Population | Total:{pop_size}\tVaccinated Percentage: {vacc_percentage}\nVirus | Name: {virus_name}\tMortality Rate: {mortality_rate}\tReproductive Rate: {basic_repro_num}\n"

        f = open(self.file_name, 'w')
        f.write(initial_params)
        f.close()

        return initial_params

    def log_interaction(self, person, random_person, random_person_sick=None, random_person_vacc=None, did_infect=None):
        '''
        The Simulation object should use this method to log every interaction a sick person has during each time step.

        The format of the log should be: "{person.ID} infects {random_person.ID} \n"

        or the other edge cases:
            "{person.ID} didn't infect {random_person.ID} because {'vaccinated' or 'already sick'} \n"
        '''
        # TODO: Finish this method. Think about how the booleans passed (or not passed) represent all the possible edge cases. Use the values passed along with each person, along with whether they are sick or vaccinated when they interact to determine exactly what happened in the interaction and create a String, and write to your logfile.
        with open(self.file_name, "a") as f:
            if did_infect == True:
                f.write(f"{person._id} infects {random_person._id} \n")
            elif did_infect == True and random_person_vacc == True:
                f.write(f"{person._id} didn't infect {random_person._id} because they are vaccinated. \n")
            elif random_person_sick == True:
                f.write(f"{person._id} didn't infect {random_person._id} because they are already sick. \n")
            else:
                f.write(f"{person._id} didn't infect {random_person._id} because their immune defense resisted.\n")

    def log_infection_survival(self, person, did_die_from_infection):
        ''' The Simulation object uses this method to log the results of every call of a Person object's .resolve_infection() method.

        The format of the log should be:
            "{person.ID} died from infection\n" or "{person.ID} survived infection.\n"
        '''
        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile
        with open(self.file_name, 'a') as f:
            if did_die_from_infection == False:
                f.write(f"{person._id} survived infection.\n")
            elif did_die_from_infection == True:
                f.write(f"{person._id} died from infection.\n")

    def log_time_step(self, time_step_number):
        ''' STRETCH CHALLENGE DETAILS:

        If you choose to extend this method, the format of the summary statistics logged
        are up to you.

        At minimum, it should contain:
            The number of people that were infected during this specific time step.
            The number of people that died on this specific time step.
            The total number of people infected in the population, including the newly infected
            The total number of dead, including those that died during this time step.

        The format of this log should be:
            "Time step {time_step_number} ended, beginning {time_step_number + 1}\n"
        '''
        # TODO: Finish this method. This method should log when a time step ends, and a
        # new one begins.
        # NOTE: Here is an opportunity for a stretch challenge!
        with open(self.file_name, 'a') as f:
            f.write(f"Time step {time_step_number} ended, beginning {time_step_number + 1}\n")
    
    def log_final_stats(self, total_death, total_infected, vaccinated_win):
        with open(self.file_name, 'a') as f:
            f.write(f"\nTotal Deaths: {total_death}\n Total Infected: {total_infected}\nSaved By Vaccination: {vaccinated_win}")