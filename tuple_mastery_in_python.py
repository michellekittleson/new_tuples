# Task 1: Formatting Flight Itineraries

itineraries = [
    ("Alice", "New York", "London"),
    ("Bob", "Tokyo", "San Francisco")
]

def format_flight_itinerary(itineraries):
    for index, itinerary in enumerate(itineraries):
        traveler_name, origin, destination = itinerary
        print(f"Itinerary {index+1}: {traveler_name} - From {origin} to {destination}")

format_flight_itinerary(itineraries)