# Backend Engineering Challenge

## Table of Contents
1. [Introduction](#introduction)
2. [Challenge Overview](#challenge-overview)
3. [Getting Started](#getting-started)
4. [Usage](#Usage)
5. [Implementation Details](#implementation-details)
    - [Parsing Input Data](#parsing-input-data)
    - [Calculating Moving Averages](#calculating-moving-averages)
    - [Handling Edge Cases](#handling-edge-cases)
6. [Optimization Strategies](#optimization-strategies)
7. [Testing](#testing)
    - [Unit Tests](#unit-tests)
    - [Integration Tests](#integration-tests)
8. [Complexity Analysis](#complexity-analysis)
9. [Building and Running](#building-and-running)
10. [Additional Notes](#additional-notes)
11. [Contributing](#contributing)
12. [License](#license)
13. [Contact](#contact)


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
[Explanation of how the input data is parsed and processed.]

### Calculating Moving Averages
[Details on the algorithm used for calculating moving averages.]

### Handling Edge Cases
[Discussion about how edge cases are handled in the implementation.]

## Optimization Strategies (Future Optimizations)
[Information on any optimization strategies used in the code.]

###Potential Optimization
One minor optimization might be to update the method to only remove expired events when necessary, for example, right before calculating the moving average or adding a new event. However, this depends on the frequency of these operations and the distribution of event timestamps. If events are very frequent, the current approach might actually be more efficient as it prevents the deque from growing too large.

## Testing
### Unit Tests
[Description of the unit tests written for the application.]

### Integration Tests
[Details on integration tests and how they ensure the application works as expected.]

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

## Building and Running
[Instructions on how to build and run the application.]

## Additional Notes
[Any additional notes or considerations about the project.]

## Contributing
[Guidelines for contributing to the project, if applicable.]

## License
[Information about the license under which the project is released.]

## Contact
[Contact information for queries or collaborations.]
