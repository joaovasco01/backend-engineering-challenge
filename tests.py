import unittest
from unittest.mock import mock_open, patch
import json
from datetime import datetime, timedelta
# Import necessary modules from your script
from unbabel_cli import EventWindow, parse_input, parse_arguments, main

class TestParseInput(unittest.TestCase):
    def setUp(self):
        # Sample data for testing
        self.sample_data_json = json.dumps([
            {"timestamp": "2018-12-26 18:11:08.509654", "duration": 20, "other_fields": "data"},
            {"timestamp": "2018-12-26 18:15:19.903159", "duration": 31, "other_fields": "data"}
        ])

    def test_successful_event_parsing(self):
        """Test if parse_input correctly parses a well-formed JSON file."""
        with patch('builtins.open', mock_open(read_data=self.sample_data_json)):
            events = parse_input('dummy_path.json')
            self.assertEqual(len(events), 2)
            self.assertIsInstance(events[0]['timestamp'], datetime)

    def test_invalid_json_format(self):
        """Test parse_input handling of invalid JSON format."""
        with patch('builtins.open', mock_open(read_data='invalid json')):
            with self.assertRaises(json.JSONDecodeError):
                parse_input('dummy_path.json')

    def test_file_not_found(self):
        """Test handling of file not found error."""
        with patch('builtins.open', mock_open()) as mocked_file:
            mocked_file.side_effect = FileNotFoundError
            with self.assertRaises(FileNotFoundError):
                parse_input('non_existent_file.json')


    def test_parse_empty_input_file(self):
        """ Test if parse_input correctly handles an empty JSON file """
        with patch('builtins.open', mock_open(read_data="")):
            events = parse_input('empty_file.json')
            self.assertEqual(events, [])

    @patch('unbabel_cli')
    @patch('sys.argv', ['script.py', '--input_file', 'input.json', '--window_size', '0', '--output_file', 'output.json'])
    def test_main_with_zero_window_size(self, mock_parse_input):
        """Test if main function raises ValueError for zero window size."""
        mock_parse_input.return_value = []
        with self.assertRaises(ValueError) as cm:
            main()
        self.assertEqual(str(cm.exception), "Window size must be a positive integer.")



    def test_adding_events_to_event_window(self):
        """ Test if events are correctly added to the EventWindow """
        event_window = EventWindow(10)
        test_time = datetime.now()
        event_window.add_event(test_time, 30)

        # Check if the event is added
        self.assertEqual(len(event_window.events), 1)

        # Move time forward and add another event
        future_time = test_time + timedelta(minutes=5)
        event_window.add_event(future_time, 40)

        # Check if both events are in the window
        self.assertEqual(len(event_window.events), 2)

        # Move time further forward and check if the first event expires
        future_time += timedelta(minutes=6)
        event_window.remove_expired_events(future_time)
        self.assertEqual(len(event_window.events), 1)

    def test_event_expiration_logic(self):
        """ Test if remove_expired_events accurately removes older events """
        event_window = EventWindow(10)
        current_time = datetime.now()
        
        # Add two events, one expiring and one within the window
        event_window.add_event(current_time - timedelta(minutes=11), 30)
        event_window.add_event(current_time - timedelta(minutes=5), 40)
        
        # Remove expired events and check if only one event remains
        event_window.remove_expired_events(current_time)
        self.assertEqual(len(event_window.events), 1)

    def test_moving_average_calculation(self):
        """ Test if calculate_moving_average correctly calculates the average """
        event_window = EventWindow(10)
        current_time = datetime.now()

        # Add events and calculate moving average
        event_window.add_event(current_time, 20)
        event_window.add_event(current_time, 30)
        average = event_window.calculate_moving_average()
        
        self.assertEqual(average, 25)

    @patch('sys.argv', ['script.py', '--input_file', 'input.json', '--window_size', '10', '--output_file', 'output.json'])
    def test_command_line_argument_parsing(self):
        """ Test if command-line arguments are parsed correctly """
        args = parse_arguments()
        self.assertEqual(args.input_file, 'input.json')
        self.assertEqual(args.window_size, 10)
        self.assertEqual(args.output_file, 'output.json')


@patch('builtins.open', new_callable=mock_open)
@patch('unbabel_cli.parse_input')
def test_output_file_generation(self, mock_parse_input, mock_file):
    """Test if the correct output is written to the specified file."""
    # Mocking command-line arguments and file operations
    with patch('sys.argv', ['script.py', '--input_file', 'input.json', '--window_size', '10', '--output_file', 'output.json']):
        # Mocking parse_input to return sample events
        mock_parse_input.return_value = [
            {"timestamp": datetime(2018, 12, 26, 18, 11, 8, 509654), "duration": 20},
            {"timestamp": datetime(2018, 12, 26, 18, 15, 19, 903159), "duration": 31}
        ]
        main()

    # Checking if the output file was opened correctly
    mock_file.assert_called_with('output.json', 'w')

    # Getting the written data from the mock
    handle = mock_file()
    written_data = "".join(call_args[0][0] for call_args in handle.write.call_args_list)

    # Verify that expected content is in the written data
    self.assertIn('"average_delivery_time":', written_data)

if __name__ == '__main__':
    unittest.main()
