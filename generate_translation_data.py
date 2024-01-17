import json
import random
import argparse
from datetime import datetime, timedelta

def generate_random_timestamp(previous_timestamp):
    """ Generate a random timestamp, greater than the previous timestamp """
    return previous_timestamp + timedelta(minutes=random.randint(1, 10), seconds=random.randint(1, 59), microseconds=random.randint(1, 999999))

def generate_translation_event(previous_timestamp):
    """ Generate a single translation event with a timestamp greater than the previous one """
    timestamp = generate_random_timestamp(previous_timestamp)
    return {
        "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S.%f"),
        "translation_id": ''.join(random.choices('0123456789abcdef', k=20)),
        "source_language": random.choice(["en", "es", "de", "fr"]),
        "target_language": random.choice(["en", "es", "de", "fr"]),
        "client_name": random.choice(["airliberty", "taxi-eats", "foodly", "shopsmart"]),
        "event_name": "translation_delivered",
        "nr_words": random.randint(10, 100),
        "duration": random.randint(10, 60)
    }

def generate_events(num_events, start_timestamp):
    """ Generate a list of translation events with ascending timestamps """
    events = []
    last_timestamp = start_timestamp
    for _ in range(num_events):
        event = generate_translation_event(last_timestamp)
        events.append(event)
        last_timestamp = datetime.strptime(event['timestamp'], "%Y-%m-%d %H:%M:%S.%f")
    return events

def parse_arguments():
    """ Parses command-line arguments. """
    parser = argparse.ArgumentParser(description="Generate random translation data.")
    parser.add_argument('--input_file', type=str, required=True, help='Output file path for generated translation data.')
    return parser.parse_args()

def main():
    args = parse_arguments()
    num_events = 1000  # number of events to generate
    start_timestamp = datetime(2018, 12, 26, 18, 0)  # starting point for timestamps
    events = generate_events(num_events, start_timestamp)

    try:
        with open(args.input_file, 'w') as f:
            for event in events:
                f.write(json.dumps(event) + '\n')
        print(f"Generated data written to {args.input_file}")
    except IOError as e:
        print(f"Error writing to file {args.input_file}: {e}")

if __name__ == "__main__":
    main()
