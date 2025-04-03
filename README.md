# Lens Demo - Visual Product Search

This project is a visual search engine that lets you upload an image and find similar products in a catalog. It's like searching with pictures instead of words!

![Visual Search Demo](https://placehold.co/600x400/e4e4e4/555555?text=Visual+Search+Demo)

## What This Project Does

1. **Upload an image** or take a photo with your camera
2. The system uses AI (artificial intelligence) to understand what's in your image
3. It finds similar products in a database
4. You'll see matching products with descriptions and prices

## How It Works

The project has three main parts:

1. **Frontend** (GUI): A web page where you can upload images
2. **Backend Service**: A computer program that processes your images using AI
3. **Pipeline**: A process that creates the product database

## Requirements

- Python 3.11 or newer
- Internet connection (for downloading AI models and product images)
- About 1GB of free disk space

## Setup Instructions

### Step 1: Get the Code

1. Make sure you have the project files in a folder called `lens-demo`
2. Open a terminal or command prompt
   - On Windows: Press `Windows key + R`, type `cmd`, and press Enter
   - On Mac: Press `Command + Space`, type `terminal`, and press Enter
3. Navigate to the `lens-demo` folder
   - Type `cd` followed by the path to your folder
   - For example: `cd Desktop/lens-demo`

### Step 2: Set Up Python Environment

A Python environment is like a special container that keeps all the project's software separate from other programs on your computer.

#### Installing Python (if you don't have it already)
Before creating a virtual environment, make sure Python is installed:

1. Check if Python is installed by typing in your terminal/command prompt:
   ```
   python --version
   ```
   or
   ```
   python3 --version
   ```

2. If Python isn't installed or shows a version lower than 3.11:
   - **Windows**: Download and install from [python.org](https://www.python.org/downloads/)
   - **Mac**:
     - If you have Homebrew: `brew install python@3.11`
     - Or download from [python.org](https://www.python.org/downloads/)
   - **Linux**: Use your package manager, e.g., `sudo apt install python3.11`

#### Creating a Virtual Environment

1. Make sure you're in the `lens-demo` folder in your terminal/command prompt

2. **On Windows**:
   ```
   python -m venv .venv
   ```

3. **On Mac/Linux**:
   ```
   python3 -m venv .venv
   ```

   If you get an error, you might need to install the venv module first:
   ```
   python3 -m pip install virtualenv
   ```
   Then try creating the environment again.

4. This creates a folder called `.venv` in your project directory. This folder contains a separate Python installation.

#### Activating the Virtual Environment

Next, you need to activate the environment:

1. **On Windows**:
   ```
   .venv\Scripts\activate
   ```

2. **On Mac/Linux**:
   ```
   source .venv/bin/activate
   ```

When the environment is activated, you'll see `(.venv)` at the beginning of your command line. This means your terminal is now using the Python version inside the `.venv` folder, and any packages you install will go there instead of your main Python installation.

### Step 3: Install Required Packages

Packages are pieces of software that our project needs to work properly.

Type this command and press Enter:
```
pip install -e .
```

This reads the `pyproject.toml` file and installs all the necessary software. It might take a few minutes.

### Step 4: Create the Index Folder

Before building the index, make sure you have a folder to store it:

```
mkdir index
```

This creates a new folder called "index" where product information will be stored.

### Step 5: Build the Product Index

Before you can search for products, you need to build a database of product images:

1. Make sure you have a file called `products.json` with product information in your main project folder
2. Run the pipeline to create the index by typing:

```
python pipeline.py
```

This will:
- Download images of all products from the internet
- Process them with AI
- Store the results in the `index` folder

You'll see a progress bar as it works. This step might take a few minutes.

### Step 6: Start the Backend Service

The backend service is a program that processes your search queries:

```
python service.py
```

This will start a server on your computer. You should see some text appear showing the server has started.

**Important:** Keep this terminal window open! If you close it, the search won't work.

### Step 7: Start the Frontend

Open a new terminal window (keep the service running in the first window):

1. Open a new terminal/command prompt
2. Navigate to your project folder again using `cd` commands
3. Activate the environment again:
   - Windows: `.venv\Scripts\activate`
   - Mac/Linux: `source .venv/bin/activate`
4. Start the web interface:
   ```
   streamlit run frontend/app.py
   ```

This will automatically open a web browser with the visual search interface.

## Using the Application

1. The web interface should open automatically at `http://localhost:8501`
2. Upload an image:
   - Click "Browse files" to select an image from your computer
   - Or use the "Take a picture" option if you have a webcam
3. The system will find similar products in the database
4. View the matching products, their descriptions, and prices

## Troubleshooting

### If the app doesn't load:
- Make sure both the service and frontend are running (two separate terminal windows)
- Check you have internet connection (for loading product images)
- Ensure you have built the index using `pipeline.py`

### If you see "Could not connect to the API":
- Make sure the service is running (`python service.py`)
- Check that it's running on port 8000 (it should say this in the terminal)
- Try restarting the service

### If the search doesn't return results:
- Ensure you've built the index correctly
- Try a clearer image of a common product
- Make sure your `products.json` file is in the right location and properly formatted

### Common error messages and what they mean:

- "ModuleNotFoundError": You're missing a required package. Try running `pip install -e .` again.
- "FileNotFoundError": The program can't find a file it needs. Check that all files are in the correct locations.
- "Connection refused": The backend service isn't running. Make sure to start it with `python service.py`.

## How It Works (Technical Details)

This project uses several technologies that work together:

1. **DINOv2** - An AI model from Facebook that can understand the content of images
2. **FastAPI** - A program that creates web servers (the backend)
3. **Streamlit** - A tool for creating web interfaces (the frontend)
4. **PyTorch** - A software library for AI and machine learning

When you upload an image, the system:
1. Converts your image into a special number sequence (called an "embedding")
2. Compares this with all the product images in the database
3. Finds the most similar product using a mathematical formula
4. Shows you the matching product

Think of it like turning pictures into numbers that the computer can compare!

## Project Structure

- `embedder.py` - Contains code for the AI image processing
- `service.py` - The backend service that handles search requests
- `pipeline.py` - Builds the product database
- `frontend/app.py` - The web interface you see in your browser
- `frontend/product_card.py` - Code for displaying product information
- `index/` - Folder that contains the product database after running the pipeline
- `pyproject.toml` - Lists all the software packages needed for the project

## Extending the Project (Ideas for Exploration)

Here are some ways you could extend this project:
- Add more products to the `products.json` file
- Modify the frontend design in `frontend/app.py`
- Add a feature to compare multiple products
- Change how products are displayed in `frontend/product_card.py`

## Learning Resources

If you want to learn more about the technologies used:
- Python basics: [https://www.python.org/about/gettingstarted/](https://www.python.org/about/gettingstarted/)
- Streamlit tutorials: [https://docs.streamlit.io/library/get-started](https://docs.streamlit.io/library/get-started)
- Introduction to AI and machine learning: [https://www.khanacademy.org/computing/computer-science/ai](https://www.khanacademy.org/computing/computer-science/ai)
