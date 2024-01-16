import json
from datetime import datetime

def parse_input(file_path):
    """
    Parses the input file containing translation events.

    Each line in the file is expected to be a JSON object with various fields,
    including a timestamp, which is converted to a datetime object for easier
    processing in later stages.

    Parameters:
    file_path (str): The path to the input file.

    Returns:
    list[dict]: A list of dictionaries, each representing a translation event.
    """
    translations = []

    try:    
        with open(file_path, 'r') as input_file:
            for line in input_file:
                # Parsing the JSON line and converting timestamp
                translation = json.loads(line.strip())
                translation['timestamp'] = datetime.strptime(
                    translation['timestamp'], "%Y-%m-%d %H:%M:%S.%f")
                translations.append(translation)
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in file")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return translations

def main():
    """
    Main function to handle the workflow.
    """
    input_file = 'inputs/input_given.json'
    events = parse_input(input_file)

    # Print the parsed data
    for event in events:
        print(event)
        
if __name__ == "__main__":
    main()
