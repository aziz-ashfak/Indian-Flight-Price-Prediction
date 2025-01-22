# Indian-Flight-Price-Prediction
# Project Overview
This project aims to find out the flight price by using different model. It consists of various components including datasets, source code, static files, templates, and analysis results.

## Directory Structure
```
├── .github
   ├── workflows
       ├── main.yml
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
├── .gitignore             
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

## Describe the processes
In this project we use 80% data as trainset and  20% data as testset.In this project we use  different preprocessing method:
      **MinMaxScaler**: use for numeric columns
      **OneHotEncoder**: use for categorical columns
      **SimpleImputer**: use to detect nan value both for numeric and categorical cols
## Model we use 
   LinearRegression
   RidgeRegression
   RandomForestRegressior
   AdaBoostRegressor
   GradientBoostingRegressor
   BaggingRegressor
   XGBRegressor
According to r2_score we choose our best model.
In initial time our best model was RandomForestRegressior.It r2_score was 0.9978
It was our best model model. But it was to much heavy. It was 824 MB file .After compressed it was 117 MB.Which cannot be store in github .

The we  choose our second best model. The second beest model was BaggingRegressor.The r2_score was 9969288123254513.After compressed this model the file size is 17 MB.
And the subtract of both this model is too small.

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
   cd <Flight-Price-Prediction>
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
## Github action pipeline 
``` bash 
  ├── .github
   ├── workflows
       ├── main.yml
```
## use cloud servce 
```bash 
link : www.render.com
```
## Usage
Run the main application script:
```bash
python app.py
```
## Use Indian-Flight-Prediction web-service link

```bash
https://indian-flight-price-prediction.onrender.com
```
## Contributing
If you would like to contribute, please fork the repository and submit a pull request.

## License
This project is licensed under the [LICENSE] file included in the repository.

## Author

👤 **Aziz Ashfak**  
📧 Email: [azizashfak@gmail.com](mailto:azizashfak@gmail.com)  
🔗 LinkedIn: [linkedin.com/in/aziz-ashfak](https://www.linkedin.com/in/aziz-ashfak-27353b262/)  
🐙 GitHub: [github.com/AzizAshfak](https://github.com/AzizAshfak/)  

