# FastAPI Banknote Prediction 💸🔍

This project demonstrates a simple FastAPI application for predicting whether a banknote is genuine or fake based on its features (variance, skewness, curtosis, and entropy).

## Overview ℹ️

The FastAPI application provides a simple web interface where users can input the features of a banknote and get a prediction in response. The prediction is made using a pre-trained machine learning model.

## Prerequisites 🛠️

Before running the application, ensure you have the following installed:

- Python (version 3.7 or later) 🐍
- FastAPI ⚡
- Uvicorn 🦄
- NumPy 🧮
- Pandas 🐼

## Installation 🚀

1. Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/fastapi-banknote-prediction.git
```

2. Navigate to the project directory:

```bash
cd fastapi-banknote-prediction
```

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage 🖥️

1. Start the FastAPI server:

```bash
uvicorn app:app --reload
```

2. Access the web interface in your browser:

Open a web browser and go to `http://127.0.0.1:8000` to access the Banknote Prediction application.

3. Input banknote features:

Fill out the form with the variance, skewness, curtosis, and entropy of the banknote.

4. Get prediction:

Click the "Predict" button to submit the form and get the prediction whether the banknote is genuine or fake.

## API Documentation 📝

- The root URL (`/`) provides a welcome message.
- The `/predict` endpoint accepts POST requests with banknote features and returns a prediction.

## Directory Structure 📂

- `app.py`: Main FastAPI application file.
- `BankNotes.py`: Contains the BankNote data model.
- `classifier.pkl`: Pre-trained machine learning model.
- `requirements.txt`: List of Python dependencies.
- `README.md`: Project documentation.

## Author ✍️

- [Noor Ahmad Haral](https://github.com/noorahmadharak)

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
