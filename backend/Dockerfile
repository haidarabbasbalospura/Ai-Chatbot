# Step 1: Use official Python image from Docker Hub
FROM python:3.9

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy requirements.txt for Python dependencies
COPY requirements.txt .

# Step 4: Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the project files
COPY . .

# Step 6: Expose the port your app will run on
EXPOSE 5000

# Step 7: Start the app (update based on your actual app entry point)
CMD ["python", "app.py"]
