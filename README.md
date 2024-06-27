Script Description: Microsoft Stock Analysis and Forecasting

Overview
This script performs analysis and forecasting of Microsoft stock prices using data visualization, correlation analysis, and LSTM neural networks for time series prediction.

 Steps:
1. Import Libraries:
   - Import essential libraries for data manipulation (`pandas`), visualization (`matplotlib`, `seaborn`), and machine learning (`tensorflow`, `sklearn`).

2. Load and Preprocess Data:
   - Load the dataset using `pd.read_csv("MicrosoftStock.csv")`.
   - Drop missing values and select numerical columns.

3. Data Overview:
   - Check the dataset's shape, missing values, info, and descriptive statistics.

4. Data Visualization:
   - Plot the open, close prices, and volume over time.
   - Display a heatmap for feature correlation.

5. Time Series Analysis:
   - Filter data between 2013 and 2018.
   - Plot closing prices for the filtered period.

6. Data Preparation for LSTM:
   - Normalize closing prices using `StandardScaler`.
   - Create sequences of 60 time steps for LSTM input.

7. LSTM Model for Forecasting:
   - Create a synthetic dataset, scale it, and split into train/test sets.
   - Define and train an LSTM model with 50 units, compile using Adam optimizer and MSE loss.
   - Evaluate the model and print Mean Squared Error (MSE).

This script provides a comprehensive approach to stock price analysis and forecasting using Python, Pandas, Matplotlib, Seaborn, Scikit-learn, and TensorFlow/Keras.
