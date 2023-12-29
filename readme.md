# App README

## Repository Structure

The repository is organized into the following folders and files:

### Description of Folders and Files:

- **app/**: Contains the main application file `presentation.py`.
  
- **data/**:
  - **raw/**: Stores the raw data files.
  - **presentation_notebooks/**: Contains Jupyter notebooks related to data presentation.
  
- **src/**:
  - **analysis.py**: Contains scripts for data analysis.
  - **utils.py**: Utility functions used across the application.

- **README.md**: This file, providing information about the app and its structure.
  
- **requirements.txt**: Lists all dependencies required for the app.

## Installation Steps

Follow the steps below to set up the application:

1. **Clone the Repository**: 
   ```bash
   git clone https://github.com/adityaswadhavane/assignment_repo.git

2. **Create a Virtual Environment**:
    ```bash
    python -m venv myenv

3.  **Activate the Virtual Environment**:
    ```bash
    \myenv\Scripts\activate

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt

5. **Generating Analysis Output**:
   ```bash
   python src/analysis.py

6. **Launching the Visualization App**:
    ```bash
    streamlit run app/presentation.py