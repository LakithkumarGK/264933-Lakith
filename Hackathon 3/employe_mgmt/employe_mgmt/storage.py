import pickle
 
class Storage:
    #Saving in Pickle file
    @staticmethod
    def save_to_file(data, filename=r"C:\Users\Administrator\Desktop\coading\Hackathon 3\employe_mgmt.pkl"):
        with open(filename, "wb") as file:
            pickle.dump(data, file)
        print(f"Saved the data to {filename} successfully.")
    
    #loading data from Pickle file
    @staticmethod
    def load_from_file(filename=r"C:\Users\Administrator\Desktop\coading\Hackathon 3\employe_mgmt.pkl"):
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            print(f"Can't find the file {filename}.")
            return []
 
 