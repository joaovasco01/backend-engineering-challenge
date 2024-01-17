# Backend Engineering Challenge

## Table of Contents
1. [Introduction](#introduction)
2. [Challenge Overview](#challenge-overview)
3. [Getting Started](#getting-started)
4. [Usage](#usage)
5. [Implementation Details](#implementation-details)
    - [Parsing Input Data](#parsing-input-data)
    - [Calculating Moving Averages](#calculating-moving-averages)
6. [Optimization Strategies](#optimization-strategies)
7. [Testing & Handling Edge Cases](#testing--handling-edge-cases)
    - [Unit Tests | Handling Edge Cases](#unit-tests--handling-edge-cases)
8. [Complexity Analysis](#complexity-analysis)
9. [Additional Notes](#additional-notes)
10. [Contributing](#contributing)
11. [Contact](#contact)



## Introduction

Welcome to my repository, presenting a comprehensive solution to the Unbabel Backend Engineering Challenge. This challenge provided a platform to demonstrate my expertise in backend engineering, specifically in building a robust command-line application tailored for data processing and analytics.

The core objective of this project, `unbabel_cli`, is to adeptly manage and analyze translation event data, crucial for maintaining and evaluating client SLAs in the context of translation services. Emphasizing simplicity, readability, and efficiency, my solution is designed to process streams of translation events and calculate the moving average of delivery times, offering valuable insights into translation performance metrics.

## Challenge Overview

The challenge revolves around the development of a command-line application capable of parsing a given stream of translation event data. Each event in the stream is rich with details, including timestamps, translation IDs, language pairs, client names, and the duration of each translation. The primary task is to calculate a moving average of the translation delivery times for every minute over a user-defined time window.

For instance, if the user wishes to know the average delivery time of all translations in the past 10 minutes, the application, upon execution with the appropriate parameters, processes the input JSON data and generates an aggregated output reflecting this average over time.

This repository contains not just the code for the `unbabel_cli` application but also thorough documentation on how to build, run, and test the solution. Additionally, it includes an analysis of the application's complexity and the optimization strategies employed, ensuring the solution is not only functional but also performs efficiently with the ordered nature of input data.

The following sections of this README provide detailed instructions and insights, reflecting a commitment to best practices in code clarity, consistency, and documentation.


## Getting Started
Before running the `unbabel_cli` application, ensure that your system meets the following prerequisites:
- **Prerequisites**
The application is written in Python and requires Python 3.7 or higher. You can download and install Python from [python.org](https://www.python.org/downloads/).

- **Installation**
1. **Fork the Repository** (if contributing or modifying):
    - Navigate to the original repository on GitHub.
    - Click the "Fork" button in the top-right corner of the page.
    - This will create a copy of the repository in your GitHub account.

2. **Clone the Repository**:
    - Once forked, go to your GitHub account, open the forked repository.
    - Click on the "Code" button and then copy the URL under "Clone with HTTPS".
    - Open a terminal or command prompt on your machine.
    - Clone the repository using the command:
      ```
      git clone [URL you just copied]
      ```
      Replace `[URL you just copied]` with the URL of your forked repository.

## Usage

This section provides a quick start guide on how to use the `unbabel_cli` application, including data generation, running the main program, and executing tests.

### Generating Translation Data

To generate a sample input file with 1000 translation event examples, use the following command:

```bash
python3 generate_translation_data.py --input_file inputs/input_large.json
```

This command will generate data and save it to `inputs/input_large.json`. Ensure that the `generate_translation_data.py` script and the `inputs` directory are present in your project structure.

### Running the Main Program

To process the translation events and calculate the moving average delivery time, use the `unbabel_cli` application as follows:


```bash
python3 unbabel_cli.py --input_file inputs/input_generated.json --window_size 10 --output_file outputs/output.json
```

- `--input_file`: Specifies the path to the input JSON file containing translation event data.
- `--window_size`: Defines the size of the time window in minutes for the moving average calculation.
- `--output_file`: Designates the path to save the output file with the calculated averages.

This command processes the data in `inputs/input_generated.json` and outputs the results to `outputs/output.json`.

### Running Tests

To run the unit tests and ensure the application is functioning as expected, execute:

```bash
python3 tests.py
```

This will run all the tests defined in `tests.py` and display the results, allowing you to verify the correctness of the application's functionality.

Ensure you have followed the installation and setup steps in the previous sections before running these commands. The commands should be executed in the root directory of the project.


## Implementation Details
### Parsing Input Data

The `unbabel_cli` application handles the input data through two primary functions: `parse_input` and `parse_arguments`.

#### parse_arguments Function

- **Purpose**: This function parses the command-line arguments provided to the application.
- **Usage**:
  - It employs the `argparse` module to define and interpret the command-line arguments.
  - The expected arguments are `--input_file` (path to the input file), `--window_size` (size of the time window in minutes for the moving average calculation), and `--output_file` (path for saving the output results).
- **Outcome**:
  - Upon successful parsing, it returns an object containing these command-line arguments, which are then used to drive the application's logic.


#### parse_input Function

- **Purpose**: This function is responsible for reading the translation event data from a specified JSON file. 
- **Process**:
  - It iterates through each line of the file, expecting each line to be a valid JSON object.
  - These JSON objects contain various fields, including a `timestamp` which is crucial for processing the events.
  - The function converts the `timestamp` from a string format to a `datetime` object, facilitating easier handling in later stages.
- **Error Handling**:
  - The function is equipped to handle common file reading errors, such as `FileNotFoundError` for missing files, `JSONDecodeError` for invalid JSON formats, and other general exceptions.

By efficiently parsing and processing the input data, the `unbabel_cli` application sets the stage for calculating the moving average of translation delivery times, the core functionality of this challenge solution.


### Calculating Moving Averages

The `unbabel_cli` application employs a sophisticated approach to calculate moving averages of translation delivery times, centralizing this functionality in the `EventWindow` class and integrating it into the main application flow.

#### EventWindow Class

- **Initialization**: The `EventWindow` class is initialized with a specified time window in minutes. This window size determines the time frame for which the moving average is calculated.
- **Data Structure**: The class uses a double-ended queue (`deque`) to store event data efficiently. This structure allows for quick addition of new events and removal of expired events based on their timestamps.
- **Event Handling**:
  - **Adding Events (`add_event`)**: Events are added with their timestamps and durations. For each event, an expiration time is calculated by adding the window size to the event's timestamp.
  - **Removing Expired Events (`remove_expired_events`)**: This method is pivotal in maintaining an up-to-date window. It iteratively removes events from the front of the queue if they are older than the current time minus the window size, ensuring the data used for the moving average is always within the defined time frame.
- **Moving Average Calculation (`calculate_moving_average`)**: This method computes the average duration of events in the current window. It sums the durations of all events and divides by the number of events, yielding the moving average.

#### Integration in Main Function

- **Application Flow**:
  - The `main` function orchestrates the application, starting with parsing command-line arguments and reading the input file.
  - An `EventWindow` instance is created based on the specified window size.
  - The application processes each event in a loop. For each minute within the span of the events, it adds relevant events to the window, removes expired ones, and calculates the moving average for that minute.
- **Output Generation**:
  - The calculated moving averages, along with the corresponding minute timestamps, are written to the specified output file in JSON format. Each line in the output file represents the average delivery time for translations within that minute window.


## Optimization Strategies (Future Optimizations)
One minor optimization might be to update the method to only remove expired events when necessary, for example, right before calculating the moving average or adding a new event. However, this depends on the frequency of these operations and the distribution of event timestamps. If events are very frequent, the current approach might actually be more efficient as it prevents the deque from growing too large.



## Testing & Handling Edge Cases
### Unit Tests | Handling Edge Cases

The `unbabel_cli` application is designed to robustly handle various edge cases, ensuring reliability and accuracy in diverse scenarios. The unit tests in the `TestEventWindow` class demonstrate this capability:

1. **Valid Data Parsing**: 
   - The application correctly parses input files with valid JSON data. This is verified through tests that compare the parsed output against expected results.

2. **File Not Found**: 
   - If the input file is not found, the application gracefully handles this by providing an appropriate error message. This case is essential for preventing runtime errors due to missing files.

3. **Invalid JSON Format**: 
   - The application detects and reports invalid JSON formats in the input file. This is crucial for maintaining data integrity and providing clear feedback for data format issues.

4. **Valid Command-Line Arguments**: 
   - Tests ensure that the application correctly parses valid command-line arguments, setting up the necessary parameters for processing.

5. **Invalid Window Size**: 
   - The application validates the window size argument, ensuring it is a positive integer. This validation is key to preventing logical errors in the moving average calculation.

6. **No Events in Input**: 
   - In cases where no events are found in the input file, the application identifies this scenario and alerts the user accordingly. This check prevents unnecessary processing and provides clear feedback to the user.

7. **Calculating Moving Average**:
   - **No Events**: When there are no events, the application correctly calculates the moving average as 0. This ensures accurate reporting in scenarios where no data is available for a given time window.
   - **With Events**: The application accurately calculates the moving average with a set of events, demonstrating its core functionality's reliability.

These tests and the associated application logic ensure that `unbabel_cli` is robust and reliable, capable of handling various scenarios that might arise in real-world usage.


## Complexity Analysis
[Analysis of the time and space complexity of the key algorithms in the project.]
# Complexity Analysis of the Event Processing System

### 1. EventWindow Class Methods
- `add_event`: This method appends an event to the deque, which is an O(1) operation.
- `remove_expired_events`: This method removes events from the deque that are older than the current time. As deque operations (popping from the front) are O(1), the complexity depends on the number of expired events. In the worst case, where all events are expired, it would be O(n), where n is the number of events. However, this is a rare case, and on average, the complexity would be much lower.
- `calculate_moving_average`: This method iterates over all events in the deque to calculate the sum of durations, making it O(n) in the worst case.

### 2. Main Function
- The main function reads and processes the events. The complexity of reading and parsing the file is O(m), where m is the number of lines (events) in the file.
- Inside the main loop, each event is processed exactly once. The operations inside the loop (adding events, removing expired events, and calculating the moving average) have complexities as discussed above.

### Overall Complexity
- The overall complexity is a bit more involved due to the nested loops and deque operations. However, the key points are:
  - The file reading and parsing are linear in the number of events (O(m)).
  - Each event is added once to the deque and removed once, leading to an average complexity that is effectively linear in the number of events processed (O(n)).
  - The complexity for calculating the moving average is O(n) in the worst case, but since it operates on a sliding window, the practical complexity is often less.

### Conclusion
- The worst-case complexity can be approximated as O(m + n), where m is the number of events in the file and n is the number of events in the deque at any given time. However, due to the efficient nature of deque operations and the sliding window mechanism, the average complexity in practice would be lower, especially for scenarios where the number of events in the deque (the window size) is much smaller than the total number of events in the file.


## Additional Notes

Embarking on this project has been an enriching journey, blending technical expertise with creative problem-solving. This exercise has not only been a platform to demonstrate my technical skills but also a profound opportunity to express my rational knowledge and proficiency in tackling complex problems.

I found the challenge presented by the `unbabel_cli` application particularly intriguing. It required a thoughtful approach to handle real-world data processing scenarios, emphasizing the need for both accuracy and efficiency. Designing a solution that could gracefully handle edge cases, perform precise calculations, and maintain a user-friendly interface was a task that I approached with enthusiasm and diligence.

## Contributing

Thank you for your interest in contributing to the Backend Engineering Challenge project. However, this repository is part of a personal technical challenge and is not currently open for external contributions.

This project serves as a demonstration of my individual work and problem-solving approach in the context of a specific technical assessment. As such, while suggestions and discussions are welcome, the codebase is not intended for collaborative development.

If you have any questions, feedback, or would like to discuss any aspects of the project, feel free to reach out as described in the [Contact](#contact) section.


## Contact

For any queries, suggestions, or collaborations related to this project, feel free to reach out:

- **Name**: João Vasco Almeida Sobral Siborro Reis
- **Email**: [joaovascoscp@gmail.com](mailto:joaovascoscp@gmail.com)
- **LinkedIn**: [João Vasco](https://www.linkedin.com/in/joão-vasco-9a50331a6/)
- **GitHub**: [joaovasco01](https://github.com/joaovasco01)

Your feedback and contributions to the project are highly appreciated.

