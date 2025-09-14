# handles quiz logic and api calls
import requests
import html
import threading
import time
import random
from rich.console import Console

console = Console()
CATEGORY_URL = "https://opentdb.com/api_category.php"
QUESTION_URL = "https://opentdb.com/api.php"

class QuizEngine:
	def __init__(self, profile, num_questions, difficulty, time_limit, category_id):
		self.profile = profile
		self.num_questions = num_questions
		self.difficulty = difficulty
		self.time_limit = time_limit
		self.category_id = category_id
		self.questions = []
		self.score = profile.score

	def fetch_questions(self):
		# write u r code here to:
		# - build params for api call
		params = {"amount":self.num_questions, "difficulty":self.difficulty,"type":"multiple","category": self.category_id}
		# - fetch questions from QUESTION_URL
		# - handle errors and store questions
		try:
			resp = requests.get(QUESTION_URL,params=params)
			data = resp.json()
			self.questions = data["results"]
		except Exception as e:
			console.print(f"[bold red]Error fetching questions: {e}[/bold red]")

	def ask_question(self, question_data):
		# write u r code here to:
		# - decode question and answers
		q_text = html.unescape(question_data["question"])
		correct = html.unescape(question_data["correct_answer"])
		options = [html.unescape(ans) for ans in question_data["incorrect_answers"]]
		options.append(correct)
		random.shuffle(options)
		# - show question and options
		console.print(f"\n[bold blue]{q_text}[/bold blue]")
		for i,j in enumerate(options, 1):
			console.print(f"{i}. {j}")
		answer_holder = {"ans": None}
		# - use threading to enforce time limit
		def timer():
			for i in range(self.time_limit,0,-1):
				if answer_holder["ans"] is not None:
					return
				console.print(f"{i}s left....",end="\r")
				time.sleep(1)
			if answer_holder["ans"] is None:
				console.print("\n[bold red] Time's up![/bold red]")
		t = threading.Thread(target=timer)
		t.start()
        	# - get user input and check if correct
		# - return True for correct, False for incorrect
		choice = console.input("\nYour answer : ").strip()
		answer_holder["ans"] = choice
		t.join()

		if choice.isdigit():
			i = int(choice) - 1
			if 0<= i < len(options):
				if options[i] == correct:
					console.print("[bold green]Correct!!![/bold green]")
					self.profile.increase_score()
					return True
				else:
					console.print(f"[bold red]Wrong!!! The correct answer is {correct} [/bold red]")
					return False
			else:
				console.print("[bold orange]Invalid Input[/bold orange]")
				return False
		else:
			console.print("[bold yellow]Enter a valid number[/bold yellow]")
			return False

	def run(self):
		# write u r code here to:
		# - fetch questions
		self.fetch_questions()
		console.print("[bold magneta]Answer to the questions quickly...\n[/bold magneta]")
		# - loop through questions and ask them
		for q in self.questions:
			self.ask_question(q)
		# - update score and show final results
		self.profile.save()
