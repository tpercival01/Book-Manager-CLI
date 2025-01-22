## Book Manager CLI

Book Manager CLI is a Python-based command-line application designed to help users organise and manage their book collection. Whether you're tracking your progress through a book, rating books you've completed, or managing your "To Be Read" queue, this tool keeps everything in one place. All data is stored in a JSON file, ensuring your library is easily accessible and backed up.

## Features

- **Add Books**: Add books to your library, including details like title, author, total pages, and chapters.
- **Track Progress**: Update your reading progress by logging the current page or chapter.
- **Library Management**: View all books in your library, filter by "To Be Read" or "Completed" status, and sort by rating or title.

- **Backup**: Automatically save your library after each session and back up the JSON file to a secure location.

- **Ratings**: Rate books you've completed to keep track of your favourites.

## Future Features

- **Book Lookup API**: Search and add books directly from online databases, removing the need for manual input.

- **Graphical User Interface (GUI)**: Add an intuitive GUI for users who prefer visual interaction over CLI.

## Installation

Clone the repository:

git clone https://github.com/your-username/book-manager-cli.git
cd book-manager-cli

Ensure you have Python 3.7 or later installed. You can check your version with:

python --version

Install dependencies (if any) by running:

pip install -r requirements.txt

## Usage

Run the main script:

python main.py

Follow the on-screen menu prompts to interact with your library:

Add a new book

Update progress

View books

Rate completed books

Exit the application

Your library will be automatically saved after each session in a JSON file, and a backup will be created in a separate folder.

## Project Structure

book-manager-cli/
├── backups/               # Backup folder for JSON library files
├── library.json           # Main JSON file storing the library
├── main.py                # Entry point of the application
├── utils/                 # Utility modules for handling data and backup
├── requirements.txt       # List of dependencies (if any)
└── README.md              # Project documentation

## Contribution

Contributions are welcome! If you'd like to contribute:

Fork the repository.

Create a feature branch:

git checkout -b feature-name

Commit your changes and push to your forked repository.

Open a pull request for review.

## License

This project is licensed under the MIT License.

## Acknowledgements

Thank you for using Book Manager CLI. Feel free to share your feedback or suggest features you'd like to see in future versions!

