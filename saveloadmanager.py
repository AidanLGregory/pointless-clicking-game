import pickle
import os


class SaveLoadSystem:
    def __init__(self, file_extension, save_folder):
        self.file_extension = file_extension
        self.save_folder = save_folder

    # Saving the data to file
    def save_data(self, data, name):
        # Where I am saving the file
        data_file = open(self.save_folder + "/" + name + self.file_extension, 'wb')  # Writing bytes
        pickle.dump(data, data_file)  # Writing data into the date_file

    # Loading the data from file
    def load_data(self, name):
        data_file = open(self.save_folder + "/" + name + self.file_extension, 'rb')  # Reading bytes
        data = pickle.load(data_file)
        return data

    # Checking if file exists
    def check_for_file(self, name):
        return os.path.exists(self.save_folder + "/" + name + self.file_extension)

    # Loading game data if exists
    def load_game_data(self, files_to_load, default_data):
        variables = []

        # Getting index and file value to load
        for index, file in enumerate(files_to_load):

            # If the file exists, append to the variables array, load default if not
            if self.check_for_file(file):
                variables.append(self.load_data(file))
            else:
                variables.append(default_data[index])

        if len(variables) > 1:
            return tuple(variables)
        else:
            return variables[0]

    # Saving game data
    def save_game_data(self, data_to_save, file_names):
        for index, file in enumerate(data_to_save):
            self.save_data(file, file_names[index])
