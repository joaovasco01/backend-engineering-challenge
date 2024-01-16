# Backend Engineering Challenge

## Table of Contents
1. [Introduction](#introduction)
2. [Challenge Overview](#challenge-overview)
3. [Getting Started](#getting-started)
4. [Implementation Details](#implementation-details)
    - [Parsing Input Data](#parsing-input-data)
    - [Calculating Moving Averages](#calculating-moving-averages)
    - [Handling Edge Cases](#handling-edge-cases)
5. [Optimization Strategies](#optimization-strategies)
6. [Testing](#testing)
    - [Unit Tests](#unit-tests)
    - [Integration Tests](#integration-tests)
7. [Complexity Analysis](#complexity-analysis)
8. [Building and Running](#building-and-running)
9. [Additional Notes](#additional-notes)
10. [Contributing](#contributing)
11. [License](#license)
12. [Contact](#contact)

## Introduction
[Short introduction about the repository and its purpose.]

## Challenge Overview 
[Brief overview of the challenge scenario and objectives.]

## Getting Started (Table of Contents | Prerequisites | Usage)
[Instructions on how to fork and clone the repository.]

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
