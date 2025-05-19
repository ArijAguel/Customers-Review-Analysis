# Customers-Review-Analysis

A comprehensive pipeline for collecting, cleaning, labeling, and analyzing customer reviews using machine learning techniques.

## Overview

This project focuses on the end-to-end process of customer review analysis, encompassing:
* **Data Collection**: Scraping customer reviews from online sources.
* **Data Cleaning**: Preprocessing and cleaning the collected data for analysis.
* **Data Labeling**: Assigning sentiment labels to reviews for supervised learning.
* **Modeling**: Applying machine learning models, including Logistic Regression and BERT, for sentiment classification.
* **Visualization**: Generating plots to understand data distributions and model performance.

## Repository Structure

* `data-scraping.py`: Script for scraping raw customer reviews.
* `data-preparation.py`: Script for cleaning and preprocessing the scraped data.
* `data-preparation-with-plots.py`: Extends data preparation with visualizations.
* `labeling_dataset.py`: Script for labeling the dataset with sentiment categories.
* `shuffle.py`: Utility script to shuffle the dataset.
* `NB1.ipynb`: Jupyter notebook for exploratory data analysis.
* `logistic_regression.ipynb`: Notebook implementing Logistic Regression for sentiment analysis.
* `bert.ipynb`: Notebook implementing BERT model for sentiment classification.
* `reg_log.ipynb` / `reglog.ipynb`: Additional notebooks for regression analysis.
* `reviews.csv` / `reviews.xlsx`: Raw scraped reviews.
* `cleaned_reviews.csv` / `cleaned_reviews.xlsx`: Cleaned and preprocessed reviews.
* `classified_reviews.csv` / `classified_reviews.xlsx`: Labeled reviews with sentiment categories.
* `final_dataset.csv` / `final_dataset1.csv`: Final datasets used for modeling.

## Getting Started

### Prerequisites

* Python 3.x
* Required Python libraries:
   * `pandas`
   * `numpy`
   * `scikit-learn`
   * `matplotlib`
   * `seaborn`
   * `transformers`
   * `tensorflow` or `pytorch`
   * `beautifulsoup4`
   * `requests`

### Installation

1. Clone the repository:

```bash
git clone https://github.com/ArijAguel/Customers-Review-Analysis.git
cd Customers-Review-Analysis
```

2. Install the required libraries:

```bash
pip install -r requirements.txt
```
Note: Create a requirements.txt file with the necessary libraries.

## Usage

1. Data Scraping:
Run the data-scraping.py script to collect customer reviews:

```bash
python data-scraping.py
```

2. Data Preparation:
Clean and preprocess the scraped data:

```bash
python data-preparation.py
```

For additional visualizations:
```bash
python data-preparation-with-plots.py
```

3. Data Labeling:
Label the dataset with sentiment categories:

```bash
python labeling_dataset.py
```

4. Modeling:

* *Logistic Regression*:
Open and run the logistic_regression.ipynb notebook.
* *BERT Model*:
Open and run the bert.ipynb notebook.



## Results

* *Logistic Regression*: Provides a baseline for sentiment classification with interpretable coefficients.
* *BERT Model*: Leverages transformer-based architecture for improved accuracy in sentiment analysis.

Note: Detailed results, including accuracy scores and confusion matrices, are available within the respective notebooks.
