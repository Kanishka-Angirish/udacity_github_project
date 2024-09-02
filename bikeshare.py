import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        try:
            city = str(input('Enter name of any city to analyze from chicago, new york city or washington:')).lower()
            if city in ['chicago', 'new york city', 'washington']:
                break
            else:
                raise TypeError()
        except TypeError:
            print("Oops, you entered an invalid city name. Please try again.")
                       
                   
               


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = str(input('Enter a month (January to June) to filter by, or "all" for no filter: ')).lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'june']:                  
            break
        else:
            print("Oops, you entered an invalid month name. Please try again.")                  
                              


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input('Enter name of the day of week to filter by, or "all" to apply no day filter:')).lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print("Oops, you entered an invalid day name. Please try again.")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # Removed Unnamed: 0 column if exist
    if 'Unnamed: 0' in df.columns:
        df.drop(columns='Unnamed: 0', axis=1, inplace=True)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    df.reset_index(drop=True, inplace=True)
    
    return df
    


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month_num = df['month'].mode()[0]
    
    # Convert month number to month name
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month_name = months[popular_month_num - 1]
    print("The most common month is:", popular_month_name.title())


    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print("The most common day of the week is: ", most_common_day.title())


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The most popular hour is: ", popular_hour)
    
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is:', start_station)


    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is:', end_station) 


    # TO DO: display most frequent combination of start station and end station trip
    mask_trip_duration = df['Trip Duration'] == df['Trip Duration'].max()
    station_combo = df[mask_trip_duration].loc[:, ['Start Station', 'End Station']]
    print('The most frequent combination of start station and end station trip is:', station_combo)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    # Convert total travel time from seconds to hours
    total_travel_time_hours = total_travel_time / 3600
    print(f'The total travel time is: {total_travel_time_hours:,} hours')


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    # Convert mean travel time from seconds to hours
    mean_travel_time_hours = mean_travel_time / 3600
    print(f'The mean travel time is: {mean_travel_time_hours:,} hours')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        user_types = df['User Type'].value_counts()
        print('The counts of user types is as follows: \n', user_types)


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('The counts of gender is as follows: \n', gender_counts)


    # TO DO: Display earliest, most recent, and most common year of birth
    # TO DO: Display earliest year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        print('The earliest year of birth is:',  int(earliest_birth_year))
    
    # TO DO: Display most recent year of birth
    if 'Birth Year' in df.columns:
        most_recent_birth_year = df['Birth Year'].max()
        print('The most recent year of birth:',  int(most_recent_birth_year))
    
    # TO DO: Display most common year of birth
    if 'Birth Year' in df.columns:
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('The most common year of birth:',  int(most_common_birth_year))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """Displays raw data 5 rows at a time upon user request."""
    row = 0
    while row < len(df):
        show_data = input("\nWould you like to see 5 lines of raw data? Enter yes or no.\n").lower()
        if show_data != 'yes':
            break
        # Display the next 5 rows of raw data
        print(df.iloc[row:row + 5])
        row += 5

    if row >= len(df):
        print("\nYou've reached the end of the data.")

    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
