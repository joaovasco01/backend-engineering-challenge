import json

def parse(file_path):
    """
    Parses the given JSON file and extracts timestamp and duration for each event.

    :param file_path: Path to the JSON file containing the events.
    :return: A list of dictionaries with timestamp and duration of each event.
    """
    parsed_data = []

    try:
        with open(file_path, 'r') as file:
            for line in file:                              # O(n)
                event = json.loads(line)
                parsed_data.append({
                    'timestamp': event['timestamp'], 
                    'duration': event['duration']
                })
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in file")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return parsed_data

def main():
    """
    Main function to handle the workflow.
    """
    input_file = 'inputs/input_given.json'
    events = parse(input_file)

    # Print the parsed data
    for event in events:
        print(event)
        
if __name__ == "__main__":
    main()
