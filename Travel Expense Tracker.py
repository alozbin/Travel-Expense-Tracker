#This program allows the user to input information about their upcoming trips, organizes the information, and calculates the total cost.

class Trip:
    def __init__(self, destination, days, cost):
        self.__destination = destination
        self.__days_at_location = days
        self.__est_cost = cost

    def get_cost(self):
        return self.__est_cost

    def __str__(self):
        return f'Destination: {self.__destination}\nLength of trip: {self.__days_at_location} days\nEstimated cost: ${self.__est_cost}\n'

class LeisureTrip(Trip):
    def __init__(self, destination, days, cost, activities):
        super().__init__(destination, days, cost)
        self.__activities = activities

    def __str__(self):
        base_str = super().__str__()
        activities_str = '\n'.join(self.__activities)
        return base_str + f'Leisure activities:\n{activities_str}\n'

class BusinessTrip(Trip):
    def __init__(self, destination, days, cost, meetings):
        super().__init__(destination, days, cost)
        self.__meetings = meetings

    def __str__(self):
        base_str = super().__str__()
        meetings_str = '\n'.join(f'Day {day}: {meeting}' for day, meeting in self.__meetings.items())
        return base_str + f'Meetings planned:\n{meetings_str}\n'

def main():
    num_trips = int(input('How many trips will you take in the next year? '))
    print()
    trips = triplist(num_trips)

    print('\nHere are the trips you indicated:\n')
    display_trips(trips)

    total_cost = calc_total_cost(trips)
    print(f'The total estimated cost of all the trips would be ${total_cost:,.2f}')

def triplist(n):
    triplist = []

    for i in range(n):
        trip_type = input('Is this a Leisure or Business trip? (L/B): ').strip().upper()
        location = input('Where are you headed? ')
        num_days = int(input('How many days will you stay? '))
        trip_cost = float(input('What is the cost of this specific trip? $'))
        
        if trip_type == 'L':
            num_activities = int(input('How many leisure activities are planned? '))
            activities = []
            for _ in range(num_activities):
                activity = input('Describe the activity: ')
                activities.append(activity)
            trip_obj = LeisureTrip(location, num_days, trip_cost, activities)
        
        elif trip_type == 'B':
            num_meetings = int(input('How many meetings are planned? '))
            meetings = {}
            for _ in range(num_meetings):
                day = input('On which day? ')
                meeting = input('Describe the meeting: ')
                meetings[day] = meeting
            trip_obj = BusinessTrip(location, num_days, trip_cost, meetings)
        
        else:
            print('Invalid trip type. Defaulting to a regular trip.')
            trip_obj = Trip(location, num_days, trip_cost)

        triplist.append(trip_obj)
        print()

    return triplist

def calc_total_cost(trips):
    total_cost = 0
    for trip in trips:
        total_cost += trip.get_cost()

    return total_cost

def display_trips(trip_list):
    for trip in trip_list:
        print(trip)

if __name__ == '__main__':
    main()
