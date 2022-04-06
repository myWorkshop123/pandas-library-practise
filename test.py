import pandas as pd 
import numpy as np 
import time 


def read_headers(df):
    # for getting the columns name \ headers 
    print(df.columns)

def read_each_column(df):
    # If you just want to read only one column 
    # print(df['Name'])
    
    # If you want to read more than one column 
    print(df[['Name','HP','Attack']])

def read_each_row(df):
    # to get just one row 
    # print(df.iloc[0])

    # to get more than one row use the list slicing method 
    # print(df.iloc[0:5])

    # read a specific location (R,C)
    # print(df.iloc[0,1]) # this will give the value of the name column in the 0th row 

    # another method of reading column 
    # for index,rows in df.iterrows():
    #     print(index, rows['Name'], rows['Attack'], rows['Legendary'])


    # To filter the dataframe based on a condition 
    # this will give the dataframe of legendary pokemons
    filtered_data = df.loc[df['Legendary'] == True]

    print(filtered_data)

    
def get_stats(df):
    print(df.describe())

def sort_dataframe_values(df):
    # for sorting the dataframe w.r.t to a column in ascending order for desc enter False 
    # sorted_df = df.sort_values('Name',ascending=False)
    # print(sorted_df)

    # You can also specify multiple sorting orders using [] and you have to specify the sorting order for both of the columns 
    sorted_df = df.sort_values(['Name','Attack'],ascending=[True,False])
    print(sorted_df)


def add_column_to_dataframe(df):
    # To add a column to a dataframe 
    # df['Total'] = df['HP'] + df['Attack'] + df['Defense'] 

    # You can also use list slicing to give the position of the columns to add 
    required_df = df.iloc[:,4:7] # df.iloc[R,C]

    # required_df is a dataframe containing our desired rows and columns but what we want is we want to add all the column 
    # values of that row and put it inside a column called Total 
    # for that we have to use the sum function where axis=1 means sum the values horizontally 
    df['Total'] = required_df.sum(axis=1)


    print(df.iloc[:10,:])

    
    # printing the df 
    # print(df.head(5))

def drop_a_column_from_dataframe(df):
    # adding total column first 
    df['Total'] = df['HP'] + df['Attack'] + df['Defense']
    print('the dataframe before dropping ... ')
    print(df.head(5))
    print('dropping columns Total and HP')
    time.sleep(3)


    # to drop a column or multiple columns 
    dropped_df = df.drop(columns=['Total','HP'])
    print('dataframe after dropping ')
    print(dropped_df.head(5))
    return dropped_df


def save_dataframe_in_local(df):
    df = drop_a_column_from_dataframe(df)

    # to save it as a csv , index=False to remove the index column 
    # df.to_csv('modified.csv',index=False)

    # to save it in excel 
    # df.to_excel('modified.xlsx',index=False)

def filter_dataframe(df):
    # to filter a dataframe 
    # to add just one filter 
    # df = df.loc[(df['Type 1'] == 'Grass')]
    # print(df.head(10))

    # to add more than one filter 
    new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Fighting')]

    # to reset the index of the new_df, but it will still add the old index as a new column 
    # new_df = new_df.reset_index()

    # to remove the the old index column you can mention one more parameter 
    new_df = new_df.reset_index(drop=True)

    # to add a filtering on the strings 
    contains_mega_in_name = df.loc[ df['Name'].str.contains('Mega')]
    print(contains_mega_in_name)

    does_not_contain_mega_in_name = df.loc[ ~df['Name'].str.contains('Mega') ]
    print(does_not_contain_mega_in_name)

    # to filter using regex 
    import re 

    type_is_fire_or_grass = df.loc[df['Type 1'].str.contains('fire|grass' , regex=True,flags=re.IGNORECASE)]
    print(type_is_fire_or_grass)

    name_startswith_PI = df.loc[df['Name'].str.contains('^pi[a-z]*',regex=True,flags=re.IGNORECASE)]
    print(name_startswith_PI)




def make_conditional_changes_to_dataframe(df):
    # To make changes to the values of one column based on some value of the other column 
    # For eg: If you want to make all the fire type pokemons legendary 
    # syntax: df.loc[(condition) , <column to change >] = value 
    all_fire_type_legendary = df.copy()
    all_fire_type_legendary.loc[(
        all_fire_type_legendary['Type 1'] == 'Fire'), 'Legendary'] = True

    # just to check whether all the firetypes have become legendary 
    print(all_fire_type_legendary.loc[all_fire_type_legendary['Type 1'] == 'Fire' ])

    # to update more than one column at the same time using more than one conditions
    all_fire_type_above_50_attack = df.copy()
    all_fire_type_above_50_attack.loc[(all_fire_type_above_50_attack['Type 1'] == 'Fire') & (all_fire_type_above_50_attack['Attack'] > 50), ['Generation','Legendary']] = ['Generation Awesome', 'Legendary Ultra'] # you can pass single value too for multiple columns 

    print(all_fire_type_above_50_attack)


# aggregate operations ( Group By )
def perform_agregation(df):
    # to perform aggregate functions on a dataframe groupby is the command 

    # to count the number of each type of pokemon 
    
    # first we will create a count column to act as a counter variable 
    df['count'] = 1 
    
    result_df = df.groupby(['Type 1']).count()

    # you can also add multiple columns to aggregate 
    result_df = df.groupby(['Type 1','Type 2']).count()

    print(result_df['count'].head(10))




def main():
    df = pd.read_csv('pokemon_data.csv')
    # read_headers(df)
    # read_each_column(df)
    # read_each_row(df)
    # get_stats(df)
    # sort_dataframe_values(df)
    # add_column_to_dataframe(df)
    # drop_a_column_from_dataframe(df)
    # save_dataframe_in_local(df)
    # filter_dataframe(df)
    # make_conditional_changes_to_dataframe(df)
    # perform_agregation(df)



if __name__ == '__main__':
    main()