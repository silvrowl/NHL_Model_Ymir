# Ymir - NHL Prediction Model

Project to predict wins for NHL Teams based off team stats at first, and hopefully news articles later

## File Structure

.
|-- Base_Model                                 # Base model from team stats
|	|-- 2019_game_data.csv			   # 2019 organized data	
|	|-- game_boxscore_pull.ipynb		   # Script to pull boxscore data 
|	|-- game_data_regression.ipynb		   # Script to run regression model
|	|-- game_data_transform.ipynb              # Script to transform the data
|	|-- MoneyPuckDataDictionaryForPlayers.csv  # Moneypuck's fields for reference
|	|-- one_game_events.xlsx		   # Sample game events
|	|-- team_model_2019.csv			   # Sample model data for 2019 from MoneyPuck
|	|-- team_model_data.txt			   # Sample model data for 2019 from MoneyPuck
|	|-- TOR.csv				   # Sample data for just the Leafs
|
|-- News_Model                                 # Model built from scraping sports articles
|	|-- article_parsers.ipynb		   # Notebook to parse dates/text from different sites
|	|-- article_parsers.py			   # Script of above
|	|-- dehumanize.py			   # dehumanizes dates into datetime format
|	|-- discovery.ipynb			   # Data Discovery
|	|-- GoogleNews_pull.ipynb		   # Pull from google topics search
|	|-- GoogleNews_pull_v2.ipynb		   # Pull from google news search with date and text parser
|	|-- Leafs_Source_Counts.xlsx		   # Count of where articles are from for one month for the Leafs
|	|-- parse_test.ipynb                       # Notebook for testing parsing methods 
|
|-- OverviewNotes.txt                          # Overview of sources and notes
|
|-- README.md


## To Do


