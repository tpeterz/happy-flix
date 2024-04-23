# HAPPYFLIX
#You watch us, We watch you...    

## MSU AI Bootcamp: Project #2

#### <img src="Resources/team_logo.png" alt="Happy Panda" width="500"/>
## Team: Happy Tree Pandas
### Members:

<img src="Resources/team_pandas.png" alt="Happy Panda" width="800"/>

## Description
Our project dives into the multifaceted factors influencing global happiness. Leveraging World Happiness Report data from Kaggle spanning 2005 to 2023, we've crafted code to uncover key drivers of happiness across countries. 

## Getting Started

To explore our findings and analysis, follow these steps:

1. **Installation:** Clone this repository to your local machine.
2. **Setup:** Open the cloned repository in Jupyter Notebook or Visual Studio Code to access the project files.


### Dependencies / Required Packages

- Python 3.10
- Jupyter Notebook
- Pandas 
- Pandas Plotting
- NumPy
- Matplotlib
- Seaborn
- Prophet
- Time-Series Analysis
- Scikit-learn
- Math
- MLxtend

## Goals / Questions to be addressed
1. We used data from the World Happiness Report to predict future global happiness.

2. Based on our findings, we selected other variables to run additional models to study correlations further.

3. We used those selected variables to predict how much of an impact those variables have on the outcome.

4. What would life be like with and without the economic crash of 2008 and 2009 and the COVID-19 pandemic of 2020 and 2021? 
## **Data Overview**

#### The __World Happiness Report (WHR)__ is a partnership of:
- Gallup 
- Oxford Wellbeing Research Centre
- United Nations Sustainable Development Solutions Network
- WHR’s Editorial Board

#### To obtain the happiness rankings of each country, the WHR provided survey responses from the life evaluations of the __Gallup World Poll (GWP)__. Happiness rankings are based on the answers to the Cantril Ladder question:
> "Please imagine a ladder, with steps numbered from 0 at the bottom to 10 at the top. The top of the ladder represents the best possible life for you and the bottom of the ladder represents the worst possible life for you. On which step of the ladder would you say you personally feel you stand at this
time?”

#### The happiness rankings according to the GWP will be referred to as either "Life Ladder" or "Happiness Score" throughout this project.

### Dataset Explanations

- **Life Ladder (Happiness Score)**
: Happiness ranking on a scale of 0 (saddest) to 10 (happiest).
- **Country Name**
- **Regional Indicator**
: Region in which the country is located.
- **Log GDP Per Capita**
: The wealth of individuals in a country.
- **Social Support**
: A value that indicates how many people have family and friends that they can rely on in times of trouble.
- **Healthy Life Expectancy At Birth**
: Average life expectancy of a country. Based on data from the World Health Organization's (WHO) Global Health Observatory data repository.
- **Freedom To Make Life Choices**
: National average of the satisfaction with individual freedom to make life choices.
- **Generosity**
: Measure of how likely people are to donate to charity. 
- **Perceptions Of Corruption**
: Measure of national corruption. The GWP asked whether corruption was widespread throughout both government and business, on an individual level.
- **Positive Affect**
: Average of measures for laughter, enjoyment and doing interesting things.
- **Negative Affect**
: Average of measures for worry, sadness and anger.
- **Confidence In National Government**
: Institutional trust
### **Data Splitting For Analysis**

#### We split our data in a few different ways to make our comparisons. 
#### We ran our analysis based on the **Region** each country was assigned to. This is the **'Regional Indicator'** column. 

#### **Regions, according to the WHR**:
- Central and Eastern Europe	
- Commonwealth of Independent States	
- East Asia	
- Latin America and Caribbean	
- Middle East and North Africa	
- North America and ANZ	(USA, Canada, Australia, New Zealand)
- Southeast Asia	
- Sub-Saharan Africa	
- Western Europe

#### We also considered historical points in time (in the range of our data set, 2005-2023) that may have affected global happiness scores. We decided on **two** major incidents:
- The global economic recession that impacted our world economy. This took place during 2008 and 2009.
- The global COVID-19 pandemic of 2020 and 2021.

## Approach taken to achieve our goals
1. **Dataset Selection and Modification**
    - Obtain a complete set of data (2005-2023) in CSV format.
    - Ensure dataset has at least 500 records (1000 if developing a decision tree/random forest model).
    - Import selected CSV file into our project repository.
2. **Cleaning and Refining**
    - Analyze columns to check for null values.
    - Identify and clean columns to ensure consistency.
    - Drop unnecessary columns.
    - Cleaned data is exported as CSV files for the machine learning model.
    - Look for correlations in our data.
4. **Data Model Implementation**
    - Initialize, train, and evaluate a model (or load a pretrained model).
    - Test model accuracy and tweak until the model demonstrates meaningful predictive power. 
    - Achieve at least 75% classification accuracy or 0.80 R^2 score.
        - We were able to achieve a 0.9316 R^2 score.
5. **Data Model Optimization**
    - The model optimization and evaluation process shows iterative changes made to the model.
    - The resulting changes in model performance is documented in either a CSV/Excel table or in the Python script itself.
    - Overall model performance is printed or displayed at the end of the script.
6. **Draw Conclusions**
    - Make observations based on analysis.

## Data Clean-Up
<img src="Resources/data_clean_panda.jpg" alt="Happy Panda" width="200"/>

### Our process:
- Generated a list of data types
- Checked for null values
- Handled missing values by filling with the mean values of the scores

## Analysis
- Corruption does not necessarily correlate with being happy. Countries will high levels of corruption can still have high levels of happiness.
- Central and Eastern Europe and Latin America & Carribiean regions had high corruption scores and high happiness.
- Life Expectancy and per capita is highly correlated to happiness.

## Conclusions
<img src="Resources/happy_panda.jpg" alt="Happy Panda" width="200"/>

- GDP is one of the largest driving factors affecting happiness.
- Countries will high levels of corruption can still have high levels of happiness.
    - For example, Saudi Arabia, has an imputed corruption score of 1 (the highest possible score), yet their happiness scores are not directly affected.
    - An additional note on corruption: corruption is highly subjective and varies with different standards throughout the world.
- Removing the financial crisis and COVID-19 pandemic of did not have a substantial impact on the projected future of happiness.
- Over the timescale of the study, the dataset contained additional fields and was more complete, with additional countries.

- Final accuracy achieved:
    - Mean Squared Error: 0.0169
    - R^2 Score: 0.9316

## Problems encountered
- The WHR changed significantly over time
- Besides GDP per capita & life expectancy, open ended questions
- Although we tried to identify major global incidents within the dataset (COVID and a world financial crisis), the data is likely affected by other events or have causal links beyond those we identified (which could be regional, social-political, environmental, and / or cultural).
- Removing years for global and sociopolitical events
- Generating a world map (GeoPandas)

## Future Considerations
- Consider the complexity of other world events
- Experiment with changing regional indicators 
- Look at additional datasets about happiness


## Repository Files


| **File** | **Description** |
| --- | --- | 
| **DATA PREPARATION :** | | 
| **[WHR 2005 to 2023.csv](https://github.com/crmartella/WorldHappinessReportMSUBootcamp/blob/main/Resources/WHR%202005%20to%202023.csv)** | CSV file containing WHR data from 2005 - 2023  |
| **[WHR_2005to2023_processed.csv](https://github.com/crmartella/WorldHappinessReportMSUBootcamp/blob/main/Resources/WHR_2005to2023_processed.csv)** | Additonal CSV used for Seaborn |
| | |
| **MODELING AND PREDICTIONS :** | | 
| **[Correlation_to_HappinessLadder.ipynb](https://github.com/crmartella/WorldHappinessReportMSUBootcamp/blob/main/Correlation_to_HappinessLadder.ipynb)** | All categories related to happiness Seaborn Regplot  |
| **[High_Correlation_Attributes_Analysis_(Regional).ipynb](https://github.com/crmartella/WorldHappinessReportMSUBootcamp/blob/main/High_Correlation_Attributes_Analysis_(Regional).ipynb)** | Most significant correlations to happines using Seaborn Pairplot| 
| **[Linear_Regression_Prophet.ipynb](https://github.com/crmartella/WorldHappinessReportMSUBootcamp/blob/main/Linear_Regression_Prophet.ipynb)** | Linear Regression, Prophet, KNN, RandomForest, and Seaborn |
| **[Regional_Correlation.ipynb](https://github.com/crmartella/WorldHappinessReportMSUBootcamp/blob/main/Regional_Correlation.ipynb)** | Regional Analysis | 
| **[.gitignore](https://github.com/crmartella/WorldHappinessReportMSUBootcamp/blob/main/.gitignore)** | Git ignore  |
| | |
**PRESENTATION :** 
| **[Factors_Impacting_Global_Happiness.pdf](https://github.com/crmartella/WorldHappinessReportMSUBootcamp/blob/main/Factors_Impacting_Global_Happiness.pdf)** | Powerpoint used in presentation |


## Acknowledgments

-  [World Happiness Report (2005-2022) Kaggle Data Set](https://www.kaggle.com/datasets/usamabuttar/world-happiness-report-2005-present/data)
- [World Happiness Report (2023) Kaggle Data Set](https://www.kaggle.com/datasets/sazidthe1/global-happiness-scores-and-factors?select=WHR_2023.csv)
- [Statistical Appendix: Latest version - March 13, 2023](https://happiness-report.s3.amazonaws.com/2023/WHR+23_Statistical_Appendix.pdf)
- [World Happiness Report Home](https://worldhappiness.report/)