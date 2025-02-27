def load_system_prompt(file_path: str) -> str:
    try:
        with open(file_path, 'r') as file:
            system_prompt = file.read()
        return system_prompt
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
def system_prompt():
    file_path = r"src/prompt/templates/system_prompt.txt"
    system_prompt = load_system_prompt(file_path)
    
    return system_prompt