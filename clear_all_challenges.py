from agent import *
import sys

if __name__ == "__main__":
    # read challenge.json file if exists
    # first argument is the path to the /challenge folder containing challenge folders
    # each folder contains a challenge.json file
    # Each folder needs to be processed one by one
    # With the working file path being each individual challenge folder 
    challenge_folders_path = sys.argv[1]

    for challenge_folder in os.listdir(challenge_folders_path):
        challenge_path = os.path.join(challenge_folders_path, challenge_folder, )
        os.chdir(challenge_folders_path)
        if os.path.exists(challenge_path):
            #update working directory to challenge folder
            os.chdir(os.path.join(challenge_folder))
            with open("challenge.json", "r") as f:
                data = json.load(f)
                name = data.get("name")
                description = data.get("description")
                category = data.get("category")
                files = data.get("files")
        
            goal = f"Find the flag for the pwn challenge named '{name}'. Here is the description: {description}. The category is {category}. The files provided are: {', '.join(files)}."
            print(f"\n\n=== Starting challenge: {name} ===")
            agent_loop(goal)
            #change path back to original
            os.chdir(challenge_folders_path)
