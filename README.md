🧠 Random Sh*t Motivational Quotes API

“Get wisdom that won’t change your life… but might change your mood.”

A Flask-powered API that serves hilariously inspirational quotes that sound deep but are actually ridiculous.
Perfect for apps, websites, or just trolling your friends.
Includes category, author, and deepness filters — all backed by MongoDB.

⸻

🚀 Features
	•	🎯 Random Quote Endpoint — Instant questionable wisdom
	•	🗂 Filter by Category, Author, or Deepness
	•	🎨 Cool TailwindCSS Frontend — Interactive docs page
	•	📦 MongoDB Backend — Because you can never have too many bad quotes
	•	⚡ UTF-8 Output — Emojis, special characters, sarcasm supported

⸻

📡 API Endpoints

1️⃣ Get a Completely Random Quote

GET /random-shit-motivational-quote

Example Response:

{
  "_id": "66b9f13f2bfb9f1d8f3aa917",
  "author": "Mira Glow",
  "category": "strategy",
  "deepness": 2,
  "quote": "If at first you don’t succeed, consider moving to the beach."
}


⸻

2️⃣ Get a Filtered Quote

GET /random-shit-motivational-quote/?author=<name>&category=<type>&deepness=<number>

Query Parameters:

Param	Type	Description
author	string	Filter by author name
category	string	Filter by category (e.g., life, success, failure)
deepness	int	How “deep” the nonsense is (1–5)

Example:

/random-shit-motivational-quote/?category=life&deepness=3


⸻

💻 Local Development
	1.	Clone this repo

git clone https://github.com/yourusername/random-shit-motivational-quotes.git
cd random-shit-motivational-quotes

	2.	Install dependencies

pip install flask pymongo

	3.	Run the app

python app.py

Server will start at http://127.0.0.1:5000

⸻

🌐 Frontend

The / route serves a TailwindCSS-powered API documentation & tester page with:
	•	Live quote fetcher
	•	Parameter input fields
	•	Example code snippets
	•	Glassmorphism + gradient animations

⸻
📜 License

MIT License — Feel free to use, remix, or turn this into a questionable life coach app.

⸻

🐸 Author

Made with sarcasm by Bhargav ✨
