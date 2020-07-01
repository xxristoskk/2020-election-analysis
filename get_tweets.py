### This script scrapes Twitter for a list of search terms, saves the data into a dataframe, which is saved to a list of dataframes and pickled

import twint
import pickle
from datetime import datetime
from tqdm import tqdm

def main():
    keywords = input('Search term(s): ')
    limit = input('Max # of tweets: ')
    since = input('Since date (yyyy-mm-dd)? ')
    min_likes = input('Min likes: ')
    filter_rt = input('Exclude retweets? (True or False): ')
    pkl = input('Name of pickle: ')

    ## checks to see if the pickle file exists already
    try:
        dataframes = pickle.load(open(f'{pkl}.pkl','rb'))
    except:
        dataframes = []

    ## initializes search configuration
    c = twint.Config()
    output = open(f'{pkl}.pkl','wb')
    ## set up the twitter search
    c.Hide_output = True ## Hides console output
    c.Search = keywords
    c.Since = since
    c.Limit = limit ## Max amount of tweets it will scrape
    c.Filter_retweets = filter_rt.title()
    c.Min_likes = min_likes
    c.Lower_case = True
    c.Count = True ## Prints number of tweets scraped when it finishes
    c.Pandas = True ## Stores tweets into a pandas dataframe
    twint.run.Search(c) ## initializes the search

    ## create the dataframe
    df = twint.storage.panda.Tweets_df
    dataframes.append(df)

    ## pickle the dataframes
    pickle.dump(dataframes,output)
    print('Finished scraping for all keywords!')

if __name__ == '__main__':
    main()
