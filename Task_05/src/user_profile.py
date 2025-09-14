# manages user profiles
from utils import get_profile, update_profile

class UserProfile:
	def __init__(self, username):
		# write u r code here to:
		# - load existing profile or create new one
		self.username = username
		data = get_profile(username)
		# - set username, score, high score, difficulty
		if data:
			self.score = data["score"]
			self.high_score = data["high_score"]
			self.difficulty = data.get("difficulty","easy")
		else:
			self.score = 0
			self.high_score = 0
			self.difficulty = "easy"
			self.save()

	def increase_score(self):
		# write u r code here to:
		# - increase score
		self.score += 10
		# - update high score if needed
		if self.score > self.high_score:
			self.high_score = self.score
		# - adapt difficulty based on score
		self.adapt_difficulty()
		# - save profile
		self.save()
	def adapt_difficulty(self):
		# write u r code here to:
		# - adjust difficulty based on score (e.g., hard if score > 50)
		if self.score > 50:
			self.difficulty = "hard"
		elif self.score > 20:
			self.difficulty = "medium"
		else:
			self.diffulty = "easy"
	def save(self):
		# write u r code here to:
		# - save profile to profiles.json
		update_profile({"username": self.username, "score": self.score, "high_score" : self.high_score, "difficulty": self.difficulty})
