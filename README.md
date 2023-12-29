# YoutubeDownloader

```
A simple Django web application to download YouTube videos.
run it and paste http://127.0.0.1:8000/

https://www.youtube.com/watch?v=your_video_id


http://127.0.0.1:8000/watch?v=your_video_id

```

## Features

- Download YouTube videos in the highest resolution.
- Rename downloaded videos based on their titles.

## Prerequisites

- Python 3.x
- Django
- pytube

## Installation

1. Clone the repository:

    ```bash
    git clon https://github.com/BDR-Pro/YoutubeDownloader
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

2. Open your web browser and navigate to [http://localhost:8000](http://localhost:8000).

3. Enter a YouTube video URL with the 'v' parameter (e.g., [http://localhost:8000/watch?v=your_video_id](http://localhost:8000/watch?v=your_video_id)).


## Configuration

- The downloaded videos are stored in the `downloads` directory within the Django project's `media` directory.

## Contributing

If you'd like to contribute to the project, feel free to submit pull requests or open issues.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
