import streamlit as st
import pandas as pd
import random

# Sample data for destinations and activities
destinations = {
    "Paris": {"culture": ["Louvre Museum", "Eiffel Tower", "Notre-Dame Cathedral"], 
              "food": ["Le Cinq", "L'As du Fallafel", "Creperie Josselin"], 
              "nature": ["Luxembourg Gardens", "Bois de Boulogne", "Parc des Buttes-Chaumont"]},
    "New York": {"culture": ["Metropolitan Museum of Art", "Broadway Show", "Central Park"], 
                 "food": ["Joe's Pizza", "Katz's Delicatessen", "Shake Shack"], 
                 "nature": ["Central Park", "High Line", "Brooklyn Bridge Park"]},
    "Tokyo": {"culture": ["Tokyo National Museum", "Senso-ji Temple", "Shibuya Crossing"], 
              "food": ["Sukiyabashi Jiro", "Ramen Street", "Tsukiji Fish Market"], 
              "nature": ["Shinjuku Gyoen", "Ueno Park", "Meiji Shrine Gardens"]},
}

# Function to generate itinerary based on user input
def generate_itinerary(destination, interests, duration):
    activities = []
    
    for interest in interests:
        if interest in destinations[destination]:
            activities.extend(random.sample(destinations[destination][interest], min(duration, len(destinations[destination][interest]))))
    
    # Limit the number of activities to the duration
    activities = activities[:duration]
    
    return activities

# Streamlit app layout
st.title("Travel Itinerary Generator")

# User inputs
destination = st.selectbox("Choose a Destination", list(destinations.keys()))
interests = st.multiselect("Select your Interests", ["culture", "food", "nature"])
duration = st.slider("Select the Number of Days", 1, 7, 3)

# Button to generate itinerary
if st.button("Generate Itinerary"):
    if not interests:
        st.warning("Please select at least one interest.")
    else:
        itinerary = generate_itinerary(destination, interests, duration)
        if itinerary:
            st.write(f"Your {duration}-day itinerary for {destination}:")
            for day, activity in enumerate(itinerary, 1):
                st.write(f"Day {day}: {activity}")
        else:
            st.write("No activities available for the selected interests.")
