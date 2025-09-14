# main file to run timetickquiz-2 pro
from user_profile import UserProfile
from quiz_engine import QuizEngine
from rich.console import Console
from utils import get_categories

console = Console()

def main():
	console.print("[bold blue]welcome to timetickquiz pro![/bold blue]")
	# write u r code here to:
	# - prompt for username
	username = console.input("\nEnter your username: ")
	# - create user profile
	profile = UserProfile(username)
	# - get quiz settings (num questions, difficulty, time limit)
	num_questions = int(console.input("How many questions? (1-20): "))
	time_limit = int(console.input("Time per questions (10-30 sec): "))
	difficulty = console.input("Difficulty (easy/medium/hard): ").lower()
	# - show categories and let user pick one
	categories = get_categories()
	console.print("\n Categories:")
	for i, j in enumerate(categories,1):
		console.print(f"{i}. {j['name']}")
	choice = int(console.input("\n Pick a category number: "))
	category_id = categories[choice - 1]["id"]
	# - start the quiz
	engine = QuizEngine(profile, num_questions, difficulty, time_limit, category_id)
	engine.run()

	console.print(f"\n Final score for {username}: [bold red]{profile.score}[/bold red]")
	console.print(f" High Score: [bold yellow]{profile.high_score}[/bold yellow]")

if __name__ == "__main__":
    	main()
