import time
import pandas as pd
import numpy as np


def get_filters():


    print('Hello! Let\'s explore some US bikeshare data!')
    print('Enter the city, month, and day that you want to analyze: \n' )

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=str(input('City:'))

    # get user input for month (all, january, february, ... , june)
    month=str(input('Month Name(Enter all for no filter):'))

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day=str(input('Day Name(Enter all for no filter):'))

    city=city.lower()
    month=month.lower()
    day=day.lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    if city =='chicago':
        df=pd.read_csv('chicago.csv')
    elif city =='new york city':
        df=pd.read_csv('new_york_city.csv')
    elif city =='washington':
        df=pd.read_csv('washington.csv')
    """"
    month =int(month)
    day=int(day)
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['Day']=df['Start Time'].dayofweek()
    df['Hour']=df['Start Time'].dt.hour
    if month != 0:
            df= df['Start Time'].dt.month == month
    if day != 0:
            df=df['Day'].dt.dayofweek==day

    """
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.day_name()
    df['Hour']=df['Start Time'].dt.hour
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['Month'] == month]

    if day != 'all':
        df = df[df['Day'] == day.title()]

    return df

def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if month == 'all':
        popular_month = df['Month'].mode()[0]
        print('Most common month: '+ str(popular_month))
    # display the most common day of week
    if day == 'all':
        popular_day = df['Day'].mode()[0]
        print('Most common day: '+popular_day)
    # display the most common start hour
    popular_hour = df['Hour'].mode()[0]
    print('Most common hour: '+ str(popular_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start=df['Start Station'].mode()[0]
    print('The most common start station: '+ popular_start)
    # display most commonly used end station
    popular_end=df['End Station'].mode()[0]
    print('The most common end station: '+ popular_end)

    # display most frequent combination of start station and end station trip
    df['Trip']=df['Start Station']+ ' : ' + df['End Station']
    popular_trip=df['Trip'].mode()[0]
    print('The most popular trip: '+ popular_trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_tavel=df['Trip Duration'].sum()
    print('Total travel time: '+str(total_tavel))

    # display mean travel time
    mean_travel=df['Trip Duration'].mean()
    print('Avarage trip duration: '+str(mean_travel))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types =df['User Type'].value_counts()
    print(user_types)
    print('\n')
    if (city=='new york city')|(city=='chicago'):
        # Display counts of gender
        gender =df['Gender'].value_counts()
        print(gender)
        print('\n')

        # Display earliest, most recent, and most common year of birth
        earliest=df['Birth Year'].min()
        print('Earliest year of birth: '+str(earliest))
        recent=df['Birth Year'].max()
        print('Most recent year of birth: '+str(recent))
        common=df['Birth Year'].mode()[0]
        print('Most common year of birth: '+str(common))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    x=input('Do you want to display raw data?')
    x=x.lower()
    i=0

    while x=='yes':
        for e in range(5):
            print(df.iloc[[i]].T)
            print()
            i+=1
        x=input('Do you want to display raw data?')
        x=x.lower()




def main():
    while True:
        city, month, day = get_filters()
        df= load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
