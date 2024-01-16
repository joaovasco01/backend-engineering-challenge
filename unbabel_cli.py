import json
from datetime import datetime
from collections import deque
from datetime import datetime, timedelta
from collections import deque
from datetime import datetime, timedelta

class EventWindow:
    def __init__(self, window_size_minutes):
        """
        Initializes the EventWindow with a specified window size.

        Args:
            window_size_minutes (int): Size of the time window in minutes for calculating moving average.
        """
        self.events = deque()
        self.window_size = timedelta(minutes=window_size_minutes)

    def add_event(self, event_timestamp, duration):
        """
        Adds an event to the window.

        Args:
            event_timestamp (datetime): Timestamp of the event.
            duration (float): Duration of the event.
        """
        expiration_time = event_timestamp + self.window_size
        self.events.append((duration, expiration_time))

    def remove_expired_events(self, current_time):
        """
        Removes events from the window that are older than the window size.

        Args:
            current_time (datetime): The current time to compare for expiration.
        """
        while self.events and self.events[0][1] < current_time:
            self.events.popleft()

    def calculate_moving_average(self):
        """
        Calculates the moving average of the durations of the events in the window.

        Returns:
            float: The moving average of the event durations.
        """
        if not self.events:
            return 0
        total_duration = sum(duration for duration, _ in self.events)
        return total_duration / len(self.events)


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


def round_down_time(dt):
    """Rounds down the datetime to the nearest minute."""
    return dt.replace(second=0, microsecond=0)

def round_up_time(dt):
    """Rounds up the datetime to the start of the next minute."""
    return (dt.replace(second=0, microsecond=0) + timedelta(minutes=1))

def main():
    """
    Main function to handle the workflow.
    """
    window_size_minutes=10
    file_path = 'inputs/input_given.json'
    events = parse_input(file_path)

    # Initialize EventWindow
    event_window = EventWindow(window_size_minutes)


    if events:
        # Determine the start and end times for processing
        start_time = round_down_time(events[0]['timestamp'])
        end_time = round_up_time(events[-1]['timestamp'])

        current_time = start_time
        event_index = 0

        while current_time <= end_time:
            # Add new events that fall within the current minute
            while event_index < len(events) and events[event_index]['timestamp'] < current_time :
                event_window.add_event(events[event_index]['timestamp'], events[event_index]['duration'])
                event_index += 1

            # Remove expired events and calculate moving average
            event_window.remove_expired_events(current_time)
            moving_average = event_window.calculate_moving_average()

            # Print or store the result
            output = {"date": current_time.strftime("%Y-%m-%d %H:%M:%00"), "average_delivery_time": moving_average}
            print(json.dumps(output))

            # Increment current time by one minute
            current_time += timedelta(minutes=1)
            


        
if __name__ == "__main__":
    main()
