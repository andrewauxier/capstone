# Capstone Project, Andrew Auxier, January 2025 Data Analysis

# Project Setup Instructions
1. Open VS Code and set up a virtual environment.
    a. Navigate to the command bar at the top-center of the window and type Show and Run Commands or press Ctrl + Shift + P.
    b. Type and/or select Python: Create Environment.
    c. Select Venv to create a '.venv' virtual environment in the current workspace.
    d. Select the appropriate version of Python to run on the virtual environment (the recommended version always worked for me).

2. In the integrated terminal of VS Code, input 'git clone https://github.com/andrewauxier/capstone.git'. This will clone the project's repository to the selected directory (wherever you wish to save it).

# Project Overview

3. Begin with the car_prices_cleaning.ipynb. Click this file in the explorer pane and it should open the workspace wherein is contained the code that imports the needed libraries, runs the exploratory data analysis, transforms the data into the final usable form, and saves the resulting table into an SQL database.

4. Click the fatal_crashes_cleaning.ipynb, which contains code to accomplish the same task as step 3 above. This data frame is much lesser in extent, and less is needed to perform the needed transformations. By running this code, the final data frame is developed and saved into the already-created SQL database.

5. Open the final_capstone.ipynb. This workspace contains the code that runs the needed SQL queries on the two already-developed data tables, joins them, converts them into a data frame, and creates the needed visualizations.

# Technologies Used

Tools and technologies used include:
    1. Pandas to clean and manipulate the datasets such that they could be saved into an SQL database for subsequent querying.
    2. Matplotlib for creating visualizations.
    3. SQLite 3 to create a local SQL database and perform query functions on the final, cleaned dataset.
    4. Jupyter notebooks to structure and organize the code.

# Data Sources
The car price data was derived from a dataset on Kaggle at the following link:
    https://www.kaggle.com/datasets/syedanwarafridi/vehicle-sales-data

The fatalities data was derived from the National Highway Traffic Safety Administration at the following link:
    https://www-fars.nhtsa.dot.gov/Vehicles/VehiclesAllVehicles.aspx

