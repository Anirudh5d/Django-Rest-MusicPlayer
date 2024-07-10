# Django Rest Music Player

This project is a Django-based web application that serves as a music store and player system. It features functionalities for user registration, music uploading, playlist creation, song search, and more. The system supports two types of users: artists and normal users. Artists can upload songs, while normal users can play, search, add to playlists, and mark songs as favorites.

## Features

- **User Registration**: Users can register as either an artist or a normal user.
- **Music Upload**: Artists can upload songs that are accessible to all users.
- **Search Songs**: Users can search for songs by name, artist, and genre.
- **Playlists**: Users can create and manage playlists.
- **Favorites**: Users can mark songs as favorites.
- **Dynamic Home Page**: The home page reflects different permissions based on user type.
- **Responsive Design**: A beautiful and dynamic appearance for all required web pages.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Anirudh5d/Django-Rest-MusicPlayer.git
    cd Django-Rest-MusicPlayer
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply the migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

7. **Access the application**:
    Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage

- **Artist User**: Can upload new songs, view their songs, and delete songs.
- **Normal User**: Can search for songs, play songs, add songs to playlists, and mark songs as favorites.

## API Endpoints

- **Register User**: `/api/register/` (POST)
- **Login User**: `/api/login/` (POST)
- **Upload Song**: `/api/songs/upload/` (POST, Artist only)
- **List Songs**: `/api/songs/` (GET)
- **Search Songs**: `/api/songs/search/?q=<query>` (GET)
- **Add to Playlist**: `/api/playlists/add/` (POST)
- **Mark as Favorite**: `/api/favorites/add/` (POST)

## Technologies Used

- Django
- Django Rest Framework
- HTML/CSS/Bootstrap
- JavaScript

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

Special thanks to all contributors and the Django community for their continuous support.

---

Enjoy using the Django Rest Music Player! If you have any questions or suggestions, feel free to open an issue or reach out.
