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
        city = input('Would you like to see data for Chicago, New York city or Washington?\n ').casefold().lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print('Please enter a valid city (chicago, new york city or washington)')
        else:
            break
            

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please choose a month: january, february, march, april, may, june, all\n ').casefold().lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print('Please choose a month from: january, february, march, april, may, june')
        else:
            break
            

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter a day: monday, tuesday, wednesday, thursday, friday, saturday, sunday, all\n ').casefold().lower()
        if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            print('Please Enter a valid day: monday, tuesday, wednesday, thursday, friday, saturday, sunday, all')
        else:
            break


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
    df = pd.read_csv(CITY_DATA[city])
    # convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Create new columns by extracting month and day of the week from Start Time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        # filter by month to create new dataframe
        df = df[df['month'] == month]
        
    # filter by day of the week if applicable
    if day != 'all':
        # filter by day of the week to create new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('\n The most common month {}:'.format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print('\n The most common day of week {}:'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_hour = df['hour'].mode()[0]
    
    print('\n The most common hour {}:'.format(most_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    
    print('The popular start station is:' , popular_start_station)
    

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    
    print('The most commonly used end station is:' , popular_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['Start_End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    
    common_trip_combo = df['Start_End'].mode()[0]
    
    print('The most frequent combination of start and end station trip is:', common_trip_combo)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    
    print('Total travel time is' , total_travel_time)


    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    
    print('Average travel time is' , average_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    
    print('The counts of user types are' , user_types)


    # TO DO: Display counts of gender
    try:
        counts_gender = df['Gender'].value_counts()
    
        print('Gender count is' , counts_gender)
    except:
        print('There is no gender column to display in this file')


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        #earliest birth year
        earliest_birth_year = df['Birth Year'].min()
        print('The ealiest year of birth is {}'.format(earliest_birth_year))
        
        # most recent birth year
        most_recent_birth_year = df['Birth Year'].max()
        print('The most recent year of birth is {}'.format(most_recent_birth_year))
        
        # most common birth year
        common_birth_year = df['Birth Year'].mode()[0]
        print('The most common year of birth is {}'.format(common_birth_year))
    except:
        print('There is no Birth Year column for this file')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
# Asking user if they want to see more data
def view_more_data(df):
    """ Asking user if they would like to view 5 more rows of data."""
    more_data = input('Would you like to view mor data? Enter yes or no: ').lower()
    count = 0
    while more_data == 'yes':
        print(df.head())
        count += 5
        more_data = input('Would you like to view mor data? Enter yes or no: ').lower()
        if more_data == 'yes':
            print(df[count:count+5])
        elif more_data != 'yes':
            break
        
    return df


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_more_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()