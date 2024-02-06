# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
# Uncomment and update if you have external dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# The CMD line is commented out to allow passing arguments at runtime
CMD ["python3", "unbabel_cli.py", "--input_file", "inputs/input_given.json", "--window_size", "10", "--output_file", "outputs/output.json"]
