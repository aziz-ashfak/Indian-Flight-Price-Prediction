# Indian-Flight-Price-Prediction
# Project Overview
This project aims to find out the flight price by using different model. It consists of various components including datasets, source code, static files, templates, and analysis results.

## Directory Structure
```
├── Dataset
   ├── Clean_Dataset.csv           
├── ResultAnalysis  
    ├── __init__.py
    ├── Analysis.ipynb
    ├── Result.csv      
├── artifacts 
    ├── column_data.pkl
    ├── model.pkl.zst
    ├──preprocessor.pkl
    ├──raw_data.csv
    ├──test_data.csv
    ├──train_data.csv
         
├── notebook/kaggleNoteBook 
    ├── Full notebook
├── src  
    ├── component
      ├── __init__.py
      ├── data_ingestion.py
      ├── data_transformation.py
      ├── model_trainner.py 
   ├── pipeline
      ├── _init__.py
      ├── predict_pipeline.py 
 ├── _init__.py
 ├── exception.py
 ├── logger.py
 ├── utilts.py
   
├── static          
├── templates              
├── .gitignore               ignored files
├── LICENSE                 
├── README.md               
├── app.py           
├── requirements.txt      
└── setup.py          
```

## Dataset link 

```bash
https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction
```
# Describe the project
## Dataset deatils:
## ABOUT DATASET
Dataset contains information about flight booking options from the website Easemytrip for

flight travel between India's top 6 metro cities. There are 300261 datapoints and 11 
features in the cleaned dataset.

### FEATURES

The various features of the cleaned dataset are explained below:

**Airline**: The name of the airline company is stored in the airline column. It is a categorical feature having 6 different airlines.

**Flight**: Flight stores information regarding the plane's flight code. It is a categorical feature.

**Source City**: City from which the flight takes off. It is a categorical feature having 6 unique cities.

**Departure Time**: This is a derived categorical feature obtained created by grouping time periods into bins. It stores information about the departure time and have 6 unique time labels.

**Stops**: A categorical feature with 3 distinct values that stores the number of stops between the source and destination cities.

**Arrival Time**: This is a derived categorical feature created by grouping time intervals into bins. It has six distinct time labels and keeps information about the arrival time.

**Destination City**: City where the flight will land. It is a categorical feature having 6 unique cities.

**Class**: A categorical feature that contains information on seat class; it has two distinct values: Business and Economy.

**Duration**: A continuous feature that displays the overall amount of time it takes to travel between cities in hours.

**Days Left**: This is a derived characteristic that is calculated by subtracting the trip date by the booking date.

**Price**: Target variable stores information of the ticket price.
## model we use

## Describe result
In this project we use 80% data as trainset and  20% data as testset.In this project we use 

## kaggle notebook link
```bash 
https://www.kaggle.com/code/azizashfak/flight-price-prediction
```

## Installation
1. Clone the repository:
   ```bash
   git clone <https://github.com/AzizAshfak/Indian-Flight-Price-Prediction.git>
   ```
2. Navigate to the project directory:
   ```bash
   cd <project-folder>
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the main application script:
```bash
python app.py
```
## Use Indian-Flight-Prediction web-service link
Run the main application script:
```bash
https://indian-flight-price-prediction.onrender.com
```
## Contributing
If you would like to contribute, please fork the repository and submit a pull request.

## License
This project is licensed under the [LICENSE] file included in the repository.

## Contact
For any inquiries, please reach out to [your contact information].

