import unittest
from datetime import datetime
from unittest.mock import patch, mock_open, MagicMock
import unbabel_cli
from io import StringIO

class TestEventWindow(unittest.TestCase):
    """
    Unit tests for the EventWindow functionalities in the unbabel_cli module.
    """

    def test_parse_input_valid_data(self):
        """Test parsing of input with valid JSON data."""
        test_input = [
            '{"timestamp": "2024-01-17 12:00:00.000000", "duration": 30}',
            '{"timestamp": "2024-01-17 12:05:00.000000", "duration": 25}'
        ]
        expected_output = [
            {"timestamp": datetime(2024, 1, 17, 12, 0, 0), "duration": 30},
            {"timestamp": datetime(2024, 1, 17, 12, 5, 0), "duration": 25}
        ]

        with patch('builtins.open', mock_open(read_data='\n'.join(test_input))):
            result = unbabel_cli.parse_input('dummy_path')
            self.assertEqual(result, expected_output, "Parse input does not match expected output.")

    def test_parse_input_file_not_found(self):
        """Test behavior when input file is not found."""
        with patch('builtins.open', side_effect=FileNotFoundError), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:

            unbabel_cli.parse_input('nonexistent_file.json')
            self.assertIn("Error: File not found", mock_stdout.getvalue())

    def test_parse_input_invalid_json(self):
        """Test parsing of input with invalid JSON format."""
        with patch('builtins.open', mock_open(read_data='invalid json')), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:

            unbabel_cli.parse_input('invalid_json.json')
            self.assertIn("Error: Invalid JSON format", mock_stdout.getvalue())

    def test_parse_arguments_valid(self):
        """Test parse_arguments with valid command-line arguments."""
        test_args = [
            'unbabel_cli',
            '--input_file', 'path/to/input.json',
            '--window_size', '10',
            '--output_file', 'path/to/output.json'
        ]

        with patch('sys.argv', test_args):
            args = unbabel_cli.parse_arguments()
            self.assertEqual(args.input_file, 'path/to/input.json')
            self.assertEqual(args.window_size, 10)
            self.assertEqual(args.output_file, 'path/to/output.json')

    def test_validate_and_parse_events_with_invalid_window_size(self):
        """Test validate_and_parse_events with an invalid window size. <=0"""
        with self.assertRaises(ValueError):
            unbabel_cli.validate_and_parse_events(0, 'dummy_path')

    def test_validate_and_parse_events_with_no_events(self):
        """Test validate_and_parse_events with no events found in input."""
        with patch('unbabel_cli.parse_input', return_value=[]), \
             patch('sys.stderr', new_callable=StringIO) as mock_stderr, \
             patch('sys.exit') as mock_exit:
            
            unbabel_cli.validate_and_parse_events(10, 'dummy_path')
            self.assertIn("No events found", mock_stderr.getvalue())
            mock_exit.assert_called_once()

    def test_moving_average_no_events(self):
        """Test calculate_moving_average with no events."""
        window = unbabel_cli.EventWindow(10)
        self.assertEqual(window.calculate_moving_average(), 0, "Expected moving average to be 0 when no events are present.")

    def test_moving_average_with_events(self):
        """Test calculate_moving_average with a set of events."""
        window = unbabel_cli.EventWindow(10)
        window.add_event(datetime(2024, 1, 1, 12, 3), 30)
        window.add_event(datetime(2024, 1, 1, 12, 6), 40)
        window.add_event(datetime(2018, 12, 26, 18, 11, 8, 509654), 50)
        expected_average = (30 + 40 + 50) / 3

        self.assertEqual(window.calculate_moving_average(), expected_average, "Moving average calculation is incorrect.")

if __name__ == '__main__':
    unittest.main()