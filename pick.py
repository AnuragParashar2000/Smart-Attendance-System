import pickle

# Replace 'file_path.pkl' with the actual path to your .pkl file
file_path = './data/faces_data.pkl'

try:
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
        print("File loaded successfully")
        # You can print or inspect 'data' to see its contents
        print(data)
except FileNotFoundError:
    print("File not found. Please provide the correct file path.")
except Exception as e:
    print("An error occurred while loading the file:", str(e))
