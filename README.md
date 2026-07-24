# 🚀 Page Pulse

Page Pulse is a simple web application that I built using **Flask** and **BeautifulSoup** to analyze webpages. Just enter a website URL, and the application fetches the page and displays useful information like the HTTP status code, response time, page title, meta description, H1 count, word count, and images missing alt text.

I built this project to improve my backend development skills with Flask, APIs, web scraping, and automated testing using pytest.

---

## Features

- Analyze any webpage using its URL
- Display HTTP status code
- Measure page response time
- Extract the page title
- Extract the meta description
- Count H1 tags
- Count total words on the page
- Detect images without alt attributes
- Handle invalid URLs and request errors
- Detect non-HTML pages (such as images)
- Includes automated tests using pytest

---

## Tech Stack

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- BeautifulSoup4
- Requests
- Pytest

---

## Project Structure

```
Page Pulse/
│
├── app.py
├── requirements.txt
├── README.md
├── Procfile
├── runtime.txt
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── utils/
│   ├── __init__.py
│   └── parser.py
│
└── tests/
    ├── __init__.py
    └── test_parser.py
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Nikhilcodes-byte/page-pulse.git
```

Move into the project folder:

```bash
cd page-pulse
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Run the Project

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## Run the Tests

```bash
python -m pytest
```

Expected output:

```
3 passed
```

---

## Screenshots

You can add screenshots here after deploying the project.

- Home Page
- Analysis of example.com
- Analysis of python.org

---

## What I Learned

While building this project, I learned how to:

- Build a web application using Flask
- Create REST API endpoints
- Send and receive JSON data
- Parse HTML using BeautifulSoup
- Handle exceptions and invalid inputs
- Write automated tests using pytest
- Debug backend and frontend issues using browser developer tools

---

## Future Improvements

Some features I would like to add in future versions:

- SEO analysis
- Broken link detection
- Export report as PDF
- Performance insights
- Dark mode
- Save analysis history

---

## Author

**Nikhil Saini**

Computer Science Engineering Student

GitHub: https://github.com/Nikhilcodes-byte