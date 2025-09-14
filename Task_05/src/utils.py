# utility functions for quiz
import json
import os
import requests

PROFILE_FILE = os.path.join(os.path.dirname(__file__), '../profiles.json')
CATEGORY_URL = "https://opentdb.com/api_category.php"

def load_profiles():
	# write u r code here to:
	# - load profiles from profiles.json
	if not os.path.exists(PROFILE_FILE):
		with open(PROFILE_FILE,"w") as f:
			json.dump({"users": []},f)
	# - return profiles list
	with open(PROFILE_FILE, "r") as f:
		return json.load(f)
	return data

def save_profiles(profiles):
	# write u r code here to:
	# - save profiles to profiles.json
	with open(PROFILE_FILE, "w") as f:
		json.dump(profiles,f, indent=2)

def get_profile(username):
	# write u r code here to:
	# - find profile by username
	profiles = load_profiles()
	# - return profile or None
	for user in profiles["users"]:
		if user["username"] == username:
			return user
	return None

def update_profile(new_profile):
	# write u r code here to:
	# - update or add profile to profiles.json
	profiles = load_profiles()
	for user in profiles["users"]:
		if user["username"] == new_profile["username"]:
			user.update(new_profile)
			break
	else:
		profiles["users"].append(new_profile)
	save_profiles(profiles)

def get_categories():
	# write u r code here to:
	# - fetch categories from CATEGORY_URL
	# - handle errors and return categories list
	try:
		resp = requests.get(CATEGORY_URL)
		data = resp.json()
		return data["trivia_categories"]
	except Exception as e:
		print(f"Error fetching categories: {e}")
		return [{"id": 9, "name": "General Knowledge"}]
