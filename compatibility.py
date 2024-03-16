import json
import numpy as np

# Helper functions: These detect to make sure the file is a json file and that the json file is valid for our purposes
def is_input_valid(file):
    return file[-5:] == ".json"
    
def is_valid_json(data):
    return ("team" in data) and ("applicants" in data)

def is_valid_weight(weight):
    return weight["intelligence"] + weight["strength"] + weight["endurance"] + weight["spicyFoodTolerance"] == 1

# Compatibility function that checks if the team is compatible with the applicant
def is_compatible(team, applicant):
    # Get the weight of each attribute and apply that to the team and the applicant
    average_attribute = {}

    # You can edit the weights accordingly they just have to total to 1
    weight = {
        "intelligence": 0.25,
        "strength": 0.25,
        "endurance": 0.25,
        "spicyFoodTolerance": 0.25
    }

    if not is_valid_weight(weight):
        print("Invalid scale")
        exit()

    for user in team:
        for attribute in user["attributes"].keys():
            if attribute in average_attribute:
                average_attribute[attribute] += int(user["attributes"][attribute])*weight[attribute]
            else:
                average_attribute[attribute] = int(user["attributes"][attribute])*weight[attribute]
    for user in applicant:
        for attribute in user["attributes"].keys():
            user["attributes"][attribute] = int(user["attributes"][attribute])*weight[attribute]

    for i in average_attribute:
        average_attribute[i] = average_attribute[i]/len(team)
    
    # Now that we added the weight we then can convert the attributes for the average team member and applicant into a vector and turn them into unit vectors
    # Once we got the unit vector we then can get the dot product of the two vectors and that will give us the compatibility of the team and the applicant
    compatibility = {"scoredApplicants": []}
    team_average_vector = np.array(list(average_attribute.values()))
    unit_team = team_average_vector / np.linalg.norm(team_average_vector)
    for user in applicant:
        user_vector = np.array(list(user["attributes"].values()))
        unit_user = user_vector / np.linalg.norm(user_vector)
        dir_similarity = np.dot(unit_team, unit_user)
        compatibility["scoredApplicants"].append({"name": user["name"], "score": dir_similarity})
    
    return compatibility


# Main function
if __name__ == "__main__":
    # Ask for the file name and check if it is valid if not ask again
    file = input("File Name: ")
    while not is_input_valid(file):
        file = input("Invalid file name. Please enter a valid file name: ")

    # Open the file and check if it is valid if not the program kills itself
    f = open(file)
    data = json.load(f)
    if not is_valid_json(data):
        print("Invalid JSON file")
        exit()

    f.close()
    
    compatibility = is_compatible(data["team"], data["applicants"])
    f = open("results.json", "w")
    f.write(json.dumps(compatibility))
    print(compatibility)

    

