# Loan Approval Prediction System Using Decision Tree
Live Demo: https://loan-approval-prediction-website.onrender.com
## Project Overview

The Loan Approval Prediction System is a machine learning web application developed using Python, Flask, SQLite, NumPy, Matplotlib, and Scikit-learn. The application predicts whether a loan will be approved or rejected based on the applicant's salary.

The project uses the Decision Tree Classification algorithm to train the model and make predictions. The website also stores prediction history in a SQLite database and provides update and delete operations for managing records.

---

# Technologies Used

* Python
* Flask
* SQLite3
* NumPy
* Matplotlib
* Scikit-learn
* HTML
* CSS

---

# Machine Learning Algorithm

## Decision Tree Classifier

The Decision Tree algorithm is a supervised machine learning algorithm used for classification problems.

In this project:

* Input Feature → Salary
* Output:

  * 0 = Loan Rejected
  * 1 = Loan Approved

The model learns salary patterns from the dataset and predicts whether the loan should be approved.

---

# Dataset Used

## Training Data

| Salary | Result |
| ------ | ------ |
| 20000  | 0      |
| 25000  | 0      |
| 30000  | 0      |
| 35000  | 0      |
| 40000  | 0      |
| 60000  | 1      |
| 70000  | 1      |
| 80000  | 1      |
| 90000  | 1      |
| 100000 | 1      |

### Labels

* 0 → Loan Rejected
* 1 → Loan Approved

---

# Features of the Project

* Predict loan approval using salary
* Decision Tree visualization
* Store prediction history in SQLite database
* Update existing records
* Delete records
* Flask web interface
* Probability prediction using `predict_proba()`

---

# Project Structure

```text
project_folder/
│
├── app.py
├── loan.db
├── static/
│   └── decision_tree.png
│
├── templates/
│   ├── home.html
│   ├── predictions.html
│   ├── history.html
│   ├── update.html
│   └── delete.html
```

---

# Required Libraries

Install the required libraries using:

```bash
pip install flask numpy matplotlib scikit-learn
```

---

# How the Project Works

## Step 1: Import Libraries

The required libraries are imported for:

* Machine Learning
* Database connection
* Visualization
* Flask web development

---

## Step 2: Create Dataset

```python
X = np.array([[20000],[25000],[30000]])
Y = np.array([0,0,0])
```

* `X` contains salary values
* `Y` contains approval results

---

## Step 3: Train the Model

```python
model = DecisionTreeClassifier()
model.fit(X,Y)
```

The Decision Tree learns salary patterns from the training data.

---

## Step 4: User Input

The user enters salary in the web form.

Example:

```python
salary = float(request.form['salary'])
```

---

## Step 5: Prediction

```python
prediction = model.predict(applicant)[0]
```

The model predicts:

* 1 → Approved
* 0 → Rejected

---

## Step 6: Probability Calculation

```python
probabilities = model.predict_proba(applicant)[0]
probability = float(np.max(probabilities))
```

This calculates prediction confidence.

Example:

* 0.95 → 95% confidence

---

## Step 7: Store Data in SQLite

```python
INSERT INTO loan (salary,prediction,probability)
```

The prediction details are saved into the database.

---

## Step 8: Decision Tree Visualization

```python
plot_tree(model, filled=True)
```

The project generates a decision tree image and saves it in the static folder.

---

# Flask Routes

## Home Route

```python
@app.route('/')
```

Displays the homepage.

---

## Prediction Route

```python
@app.route('/predictions')
```

Handles salary prediction and database insertion.

---

## History Route

```python
@app.route('/history')
```

Displays all stored prediction records.

---

## Update Route

```python
@app.route('/update/<int:id>')
```

Updates salary and prediction details.

---

## Delete Route

```python
@app.route('/delete/<int:id>')
```

Deletes selected records from the database.

---

# Database Table

## Table Name: loan

| Column      | Type    |
| ----------- | ------- |
| id          | INTEGER |
| salary      | REAL    |
| prediction  | INTEGER |
| probability | REAL    |

---

# Output Example

## Input

```text
Salary = 75000
```

## Prediction

```text
Loan Approved
```

## Probability

```text
0.95
```

---

# Advantages of the Project

* Easy to understand
* Simple machine learning implementation
* Beginner-friendly Flask project
* Database integration
* Visualization support
* CRUD operations included

---

# Conclusion

The Loan Approval Prediction System demonstrates how machine learning can be integrated with Flask and SQLite to create a real-world prediction application. The project combines machine learning, database management, visualization, and web development into a single application.
