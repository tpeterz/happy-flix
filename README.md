# happy-flix

## MSU AI Bootcamp: Project #3

###
## Team: HappyFlix
### Members:
Michael FORD
Cristian GOIAN
Sean KAVANAGH
Chris MARTELLA
Taylor PETERSON


## Description
Movie suggestions based on emotions
Using voice input, users describe their day, mood, and desired movie type
Users can specify genres, vibes, themes, or specific subject
- aliens
- brooms
- bananas
- capybaras
- robots
- vampires
- anything else!


## Getting Started


### Dependencies / Required Packages
Python 3.10
Jupyter Notebook
OpenAI API
Pandas
NumPy
Transformers
Matplotlib
Wordcloud
Stopwords
Scikit-learn
Seaborn
Natural Language Toolkit- WordNetLemmatizer- WordTokenize- Stopwords- VaderLexicon- SentimentIntensityAnalyzer
VADER
Gradio (Hugging Face)


## Goals / Questions to be addressed
Create an audio capture interface that selects three movies based on an individual’s emotions. We purported to use artificial intelligence to extract the speaker’s emotional state and genre preference.
Gradio Interface
Users describe their mood and desired movie genres or themes via voice input
The system analyzes this input to generate personalized movie suggestions
The Gradio interface processes user voice input.
It displays three recommended movies with:
- Release year
- A brief overview
- Review sentiment summary
- Movie poster image




## **Data Overview**
The Movie Database (TMDB) API
Over 6,000 popular movies
January 1970 – April 2024
Release dates
Overview summaries
Review summaries


### Dataset Explanations
Unique Movie ID Number
Movie Title
Popularity	- A combo of views, favorites, 	etc.
Release date- We purged the month and day
Number of total votes
Previous day's score- Release date
Number of total votes
Previous day's score
Release Date
Reviews
- The reviews column contains text from all reviews for a particular movie on TMDB. In our cleaned version of the dataset, we ran a sentiment analysis and purged some stopwords

## Approach taken to achieve our goals
1. Using Gradio and OpenAI's GPT-4 model, users can record a clip of them speaking, which is then converted to text.
2. The text is then analyized to determine the user's mood and sentiment.
3. The text is also analyzed to help determine what particular movies the user might like to see.
4. The movie selection is based on a combination of mood anaylsis, movie preference analysis, and movie review sentiment analysis.


## Data Clean-Up
Movie ID number
Popularity Score
Release month and day from release date
Total recommended votes


### Our process:

## Analysis



## Conclusions



## Problems encountered


## Future Considerations



## Repository Files
| **File** | **Description** |
| --- | --- | 


**PRESENTATION :** 


## Acknowledgments
