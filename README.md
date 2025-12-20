# Gaming-Impact-Predictor

A simple Flask web application with a feedback form built using Flask-WTF and Bootstrap 5.2.

## Features

- Simple feedback form with validation
- Built with Flask and Flask-WTF
- Styled with Bootstrap 5.2
- Form validation including:
  - Required field validation
  - Email format validation
  - Minimum length validation for name and message
- Flash messages for user feedback

## Installation

1. Clone the repository:
```bash
git clone https://github.com/JovanHengGhimHong/Gaming-Impact-Predictor.git
cd Gaming-Impact-Predictor
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Activate the virtual environment (if not already activated):
```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. (Optional) Set environment variables:

For **development** with debug mode:
```bash
export DEBUG=True  # On Windows: set DEBUG=True
```

For **production** with a custom SECRET_KEY:
```bash
export SECRET_KEY='your-secure-random-secret-key'  # On Windows: set SECRET_KEY=your-secure-random-secret-key
```
Note: 
- Debug mode is disabled by default for security. Only enable it in development.
- A default SECRET_KEY is provided for development, but you should set your own secure random key in production.

3. Run the Flask application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://127.0.0.1:5000
```

## Form Fields

The feedback form includes the following fields:

- **Name**: Required, minimum 2 characters, maximum 100 characters
- **Email**: Required, must be a valid email address
- **Message**: Required, minimum 10 characters, maximum 500 characters

## Project Structure

```
Gaming-Impact-Predictor/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   ├── base.html         # Base template with Bootstrap 5.2
│   └── index.html        # Home page with feedback form
└── README.md             # This file
```

## Dependencies

- Flask 3.0.0
- Flask-WTF 1.2.1
- WTForms 3.1.1
- email-validator 2.1.1