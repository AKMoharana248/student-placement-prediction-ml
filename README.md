# student-placement-prediction-ml



\# Student Placement Prediction using Machine Learning



\## Problem Statement

The goal of this project is to predict whether a student will be placed or not based on academic performance, skills, and other attributes.



\---



\## Dataset

\- Campus Placement Dataset

\- Contains features like:

&#x20; - SSC Percentage

&#x20; - HSC Percentage

&#x20; - Degree Percentage

&#x20; - Work Experience

&#x20; - Specialisation

&#x20; - MBA Percentage



\---



\## Workflow



1\. Data Loading

2\. Data Cleaning (handling missing values, dropping salary column)

3\. Feature Encoding (One-Hot Encoding)

4\. Train-Test Split

5\. Model Training

6\. Model Evaluation

7\. Model Saving



\---



\## Models Used



| Model               | Accuracy |

|---------------------|----------|

| Logistic Regression |   78%    |

| Random Forest       |   85%    |



\---



\## Results



\- Random Forest performed better than Logistic Regression.

\- The model achieved \*\*85% accuracy\*\*.

\- High recall for placed students (95%), meaning the model effectively identifies students who are likely to get placed.



\---



\## Evaluation Metrics



\- Accuracy Score

\- Confusion Matrix

\- Classification Report (Precision, Recall, F1-score)



\---



\## Key Insights



\- Academic performance (CGPA, degree percentage) strongly influences placement.

\- Work experience and specialisation also impact outcomes.

\- Random Forest handles non-linear relationships better than Logistic Regression.



\---



\## Project Structure



student-placement-prediction-ml/

│

├── data/

│ └── placement.csv

│

├── src/

│ ├── main.py

│ ├── preprocess.py

│ ├── train.py

│ └── evaluate.py

│

├── model/

│ └── model.pkl

│

├── notebooks/

│ └── project.ipynb

│

├── requirements.txt

└── README.md





\---



\## How to Run



1\. Clone the repository:



git clone https://github.com/AKMoharana248/student-placement-prediction-ml.git



2\. Navigate to project folder:



cd student-placement-prediction-ml



3\. Install dependencies:



pip install -r requirements.txt



4\. Run the project:



cd src

python main.py





\---



\## Future Improvements



\- Hyperparameter tuning

\- Add more models (XGBoost, SVM)

\- Deploy using Streamlit

\- Improve performance on minority class



\---



\## Author

\- Aswini Kumar Moharana



