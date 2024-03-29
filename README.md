# DRY_KISS PAL
Welcome to **DRY_KISS PAL** - Your Personal Assistant for Organizing Contacts, Notes, and Files!
___

## About **DRY_KISS PAL**  
**DRY_KISS PAL** is a Django application developed by the **DRY_KISS.py** team, consisting of students from the Python [**goIt**](https://goit.global/ua/) course. This project is designed to provide users with a personalized contact book, note-taking functionality, cloud storage for files categorized by users, and a digest of the latest news sorted by categories.
___

## Features
- **Personalized Contact Book:** Keep track of your contacts with ease. Each user has their own dedicated contact book.
- **Note-Taking:** Create and store personal notes securely within the application.
- **Cloud Storage:** Store your files in the cloud, organized by categories for easy access.
- **News Digest:** Stay updated with the latest news, sorted by categories of interest.
___
## Installation with Docker Compose  

  *We've taken care to make the installation and launch process as convenient as possible, so you can focus on using **DRY_KISS PAL** to organize your contacts, notes, and files effortlessly.*  

To take advantage of **DRY_KISS PAL's** capabilities with **Docker Compose**, first make sure you have **Docker** installed and the **Docker daemon** running on your system.
Install **Docker** if it is not already installed. Instructions for installing **Docker** can be found on the official [Docker website](https://www.docker.com/). 
Make sure the **Docker daemon** is running on your system. Once **Docker** is installed and the daemon is running you are ready to use our application.
  
To install and run **DRY_KISS PAL** using Docker Compose, follow these steps:

1. Clone the repository: `git clone https://github.com/the10or/personal-assistant-web.git`
2. Navigate to the project directory: `cd personal assistant`
3. Be sure to create an *.env* file based on the provided *.env.example* file. You will also need to add a security key in JSON format to access Google Cloud services. Place these files in the root folder of the project, i.e. personal_assistant.  
4. Run the application using Docker Compose with the `--build` flag for the first run to ensure that the application is built seamlessly: `docker-compose up --build`.  
   *Note that for your convenience, all dependencies will be installed automatically and migrations will be applied during the Docker Compose build process. Subsequent runs can be performed without the `--build` flag.*
___

## Usage
- Sign Up/Log In: Create a new account or log in with your existing credentials.
- Contacts: Manage your contacts by adding, editing, or deleting them.
- Notes: Create personal notes and access them whenever needed.
- Cloud Storage: Upload and categorize your files for easy retrieval.
- News Digest: Stay informed with the latest news, categorized for your convenience.
___

## Technologies Used
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- HTML/CSS
- [Tailwind CSS](https://tailwindcss.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)
- Docker Compose
- [Google Cloud Storage](https://console.cloud.google.com/)
___

## Contributors
- [Andrii Filiurskyi](https://github.com/filiurskyi)
- [Olexandr Chonka](https://github.com/Chonna86)
- [Maxym Hrebenichenko](https://github.com/greb)
- [Maxym Kostelny](https://github.com/fghdxfvdxfvdf)
- [Serhii Koval](https://github.com/the10or/)
___
## Support or Contact
*For any inquiries or support regarding **DRY_KISS PAL**, feel free to contact us at https://github.com/the10or/personal-assistant-web/*

*Special thanks to the instructors, mentors and staff members at goIt for providing us with the knowledge and guidance that enabled us to create this project.*  

**Thank you for choosing DRY_KISS PAL for your personal organization needs!**  
___
This project is distributed under the [**MIT License**](https://opensource.org/license/MIT).




