# Email Spam Classifier Dataset Documentation

## Overview

This documentation provides information about the dataset used for training and testing the Email Spam Classifier. The dataset is a combination of the 2007 TREC Public Spam Corpus and the Enron-Spam Dataset.

- **Number of Records:** 83,446
- **Columns:**
  - `label`: '1' indicates spam, '0' denotes legitimate (ham) emails.
  - `text`: Contains the actual content of the email messages.

## Sources

### 2007 TREC Public Spam Corpus

- **Original link:** [https://plg.uwaterloo.ca/~gvcormac/treccorpus07/](https://plg.uwaterloo.ca/~gvcormac/treccorpus07/)
- **Preprocessed download link:** [https://www.kaggle.com/datasets/bayes2003/emails-for-spam-or-ham-classification-trec-2007](https://www.kaggle.com/datasets/bayes2003/emails-for-spam-or-ham-classification-trec-2007)

### Enron-Spam Dataset

- **Original link:** [https://www2.aueb.gr/users/ion/data/enron-spam/](https://www2.aueb.gr/users/ion/data/enron-spam/)
- **Preprocessed download link:** [https://github.com/MWiechmann/enron_spam_data/](https://github.com/MWiechmann/enron_spam_data/)

## Licensing

This dataset is provided under the MIT License. Please refer to the [MIT License](LICENSE) file for details.

## Dataset Structure

The dataset is provided in CSV format with two columns: `label` and `text`.

- `label`: '1' indicates spam, '0' denotes legitimate (ham) emails.
- `text`: Contains the actual content of the email messages.

## Usage

1. **Download the Dataset:**
   - Use the provided links to download the dataset in CSV format.

2. **Dataset Loading:**
   - Load the dataset into your Python environment using pandas or a similar library.

   ```python
   import pandas as pd

   # Load the dataset
   dataset = pd.read_csv('path/to/dataset.csv')

    Explore and Preprocess:
        Explore the dataset to understand its structure and distribution.
        Preprocess the data as needed for your email spam classifier.

    Citation:
        If you use this dataset in your work, please provide appropriate attribution to the original sources.

## Additional Resources

    Code for Combining Datasets:
        Combining Datasets Code(https://github.com/PuruSinghvi/Spam-Email-Classifier/blob/main/Combining%20Datasets.ipynb)

## Contributors

    Dataset Combination Code: [PuruSinghvi](https://github.com/PuruSinghvi)
    Original Sources: TREC Public Spam Corpus, Enron-Spam Dataset contributors

## [The Dataset link for download](https://github.com/PuruSinghvi/Spam-Email-Classifier/raw/main/Datasets/combined_data.csv?download=)