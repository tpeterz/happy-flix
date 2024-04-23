# HappyFlix: Emotion Based Movie Selection   

## MSU AI Bootcamp: Project #3

#### <img src="Resources/team_logo.png" alt="Happy Panda" width="500"/>
## HappyFlix Development Team
### Members:
- Michael FORD
- Cristian GOIAN
- Sean KAVANAGH
- Chris MARTELLA
- Taylor PETERSON
<img src="Resources/team_pandas.png" alt="Happy Panda" width="800"/>

## Description
Our project dives into the realm of human emotion based movie selection suggestions. Our interface requests the viewer to speak into their mic to say how their day was, what kind of mood they are in, and what kind of movie they would like to watch. The movie request can include genres, vibes, themes, or specific subjects, such as aliens, brooms, or bananas. The dataset includes summaries and reviews of over 6,000 popular movies from The Movie Database, spanning from January 1970 to April 2024.

## Getting Started

To explore our findings and analysis, follow these steps:

1. **Installation:** Clone this repository to your local machine.
2. **Setup:** Open the cloned repository in Jupyter Notebook or Visual Studio Code to access the Gradio page, where you can speak, and receive movie recommendations.


### Dependencies / Required Packages

- Python 3.10
- Jupyter Notebook
- OpenAI API
- Pandas
- NumPy
- Transformers
- Matplotlib
- Wordcloud
- Stopwords
- Scikit-learn
- Seaborn
- Natural Language Toolkit (NLTK)
    - WordNetLemmatizer
    - WordTokenize
    - Stopwords
    - VaderLexicon
    - SentimentIntensityAnalyzer
- VADER
- Gradio (Hugging Face)


## Goals / Questions to be addressed
1. Can someone's mood and move preference be analyzed by AI to suggest the perfect movie for them to watch at a particular time?
2. Can our AI system choose a variety of different movies depending on user input?
3. We want the user to use their voice to explain their mood and movie preferences, and then have our Gradio interface display 3 movie titles, and for each movie:
- the release year of the movie
- a short movie overview
- a review sentiment summary
- the poster image of the movie

## Dataset
We used data from The Movie Database (TMDB) for a record of movies and their genres, plot summaries, and reviews.

## Outline of Analytical Process
1. Using Gradio and OpenAI's GPT-4 model, users can record a clip of them speaking, which can then converted to text.
2. The text is then analyized to determine the user's mood and sentiment.
3. The text is also analyzed to help determine what particular movies the user might like to see.
4. The movie selection is based on a combination of mood anaylsis, movie preference analysis, and movie review sentiment analysis.


## **Data Overview**
 • The Movie Database (TMDB) API
 • Over 6,000 popular movies
 • January 1970 –April 2024
 • Release dates
 • Overview summaries
 • Review summaries
### Dataset Explanations

- **Movie ID**
: A unique identifying number for each movie.
- **Popularity**
: The popularity score is based on the following:
- Number of votes for the day
- Number of views for the day
- Number of users who marked it as a "favourite" for the day
- Number of users who added it to their "watchlist" for the day
- Release date
- Number of total votes
- Previous day's score
- **Release Date**
- **Movie Title**
- **Reviews**
: The reviews column contains text from all reviews for a particular movie on TMDB. In our cleaned version of the dataset, we ran a sentiment analysis and removed some stopwords.
- **Movie Type / Genre**
: The movie genres are as follows. Many of the movies have multiple genres:
- Action
- Adventure
- Animation
- Comedy
- Crime
- Documentary
- Drama
- Family
- Fantasy
- History
- Horror
- Music
- Mystery
- Romance
- Science Fiction
- TV Movie
- Thriller
- War
- Western
- **Movie Overview**
: A description of the movie's plot. In our cleaned version of the dataset, we ran a sentiment analysis and removed some stopwords.
- **Release Year**
: Since the month and day are not very relevant when it comes to movie selection, we added this column to remove those, keeping the release year.
- **Lemmatized Overviews**
: Movie description overviews that we lemmatized.
- **Adjective Counts**
: Since adjectives are so important when it comes to movie review sentiment analysis, we made a count and list of adjectives in the movie reviews.
- **Lemmatized Reviews**
: We lemmatized words in reviews as part of our cleanup process.
- **Movie Review Sentiment**
: For each movie we determined if the sentiment of the movie reviews were positive overall or negative overall.


### **Data Splitting For Analysis**

#### ???


## Approach taken to achieve our goals
1. **Dataset Selection and Modification**
    - Obtain a set of data for movies from 1970 to 2024 in CSV format, based on the The Movie Database API.
    - Import selected CSV file into our project repository.
2. **Cleaning and Refining**
    - Analyze columns to check for null values.
    - Identify and clean columns to ensure consistency.
    - Drop unnecessary columns.
    - Clean the dataset and isolate the release year from the full release date, add lemmatized overviews, adjective counts, lemmatized reviews, and movie review sentiment.
4. **Data Model Implementation**
    - Data Model Implementation
5. **Data Model Optimization**
    - Data Model Optimization
6. **Building of a Gradio Interface**
    - Building of a Gradio Interface

## Data Clean-Up
Purged:
• Movie ID number
• Popularity Score
• Release month and day from release date
• Total recommended votes

<img src="Resources/data_clean_panda.jpg" alt="Happy Panda" width="200"/>

### Our process:
- Generated a list of data types
- Checked for null values
- Data cleanup

## Analysis
- 
- 
- 

## Conclusions
<img src="Resources/happy_panda.jpg" alt="Happy Panda" width="200"/>



- Final accuracy achieved:
    - Mean Squared Error: 
    - R^2 Score: 

## Problems Encountered
- Processing many of the jupyter notebook cells strained our relatively fast CPUs and took many hours to process, even after changing parameters
- Gradio is a bit more challenging when it comes to layout customization when compared to HTML
- 

## Future Considerations
• A link to the actual movie on streaming services as part of the Python output
 • A fully integrated seamless HTML system
 • Integration of more APIs, such as IMDB and Rotten Tomatoes


## Repository Files


| **File** | **Description** |
| --- | --- | 
| **DATA PREPARATION :** | | 
| | |
| | |
**PRESENTATION :** 



## Acknowledgments
