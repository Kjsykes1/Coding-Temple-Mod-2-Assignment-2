# Task 1: Code Correction

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# Task 2: Venue Selection
additional_facilities = "audio system" if attendees > 175 else "Projector"
print(additional_facilities) 

# Task 3: Catering Choices

vegetarian = input("Are you a vegetarian?") 
food_recommendations = "Veggie Delight Caterers" if vegetarian else "Gourmet Meals Caterers"
print(food_recommendations)
