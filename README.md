# Energy Consumption Prediction App

## Project Overview

This is a simple web application for predicting energy consumption based on several factors, including building square footage, number of occupants, appliance usage, and temperature. The app is built using the **Streamlit** library in Python, and the machine learning models were trained using **scikit-learn**.

## Key Features

- **Interactive Web App**: A simple and intuitive user interface that allows users to easily input data.
- **Multiple Models**: The app allows users to choose between four different machine learning models for prediction (Linear Regression, Random Forest, Decision Tree, and Gradient Boosting).
- **Ease of Use**: Anyone can use this app without prior programming knowledge.

## Files and Folders

- `app.py`: The main Python file to run the Streamlit application.
- `Energy_Consumption.ipynb`: A Jupyter Notebook containing all the steps for training, evaluating, and saving the machine learning models.
- `model_lr.plt`: The saved trained model for Linear Regression.
- `model_rf.plt`: The saved trained model for Random Forest.
- `model_dt.plt`: The saved trained model for Decision Tree.
- `model_gbr.plt`: The saved trained model for Gradient Boosting.
- `train_energy_data.csv` & `test_energy_data.csv`: The datasets used for training and testing the models.

## How to Run the App

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-link>
    cd energy-consumption-prediction
    ```

2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    -   **On Windows:**
        ```bash
        venv\Scripts\activate
        ```
    -   **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install the required libraries:**
    ```bash
    pip install streamlit joblib numpy scikit-learn pandas
    ```

5.  **Run the application:**
    ```bash
    streamlit run app.py
    ```

    After running this command, the app will automatically open in your web browser.

## Models Used

Four different models were trained and evaluated for this project:

1.  **Linear Regression**: A simple and effective model for regression tasks.
2.  **Decision Tree**: A tree-based model that is easy to interpret.
3.  **Random Forest**: An ensemble of decision trees that work together to improve accuracy.
4.  **Gradient Boosting Regressor**: A powerful model that often provides high-performance predictions.

You can refer to the `Energy_Consumption.ipynb` notebook for more details on the training and evaluation process.

## Screenshots

(Here you can add images of your app's user interface to make the `README` more visually appealing)

## 👤 Developer
### 👨‍💻 Abdallah Tarek
- 🔗 [LinkedIn Profile](https://www.linkedin.com/in/abdalla-tarek-21a025263/)
