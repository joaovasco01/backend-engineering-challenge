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
