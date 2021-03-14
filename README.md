# 🧑‍💻 relaxdays-challenge-compression

Compress Dokerfiles. Silly idea, though...

This project was created in the Relaxdays Code Challenge Vol. 1.
See the [hackathon homepage](https://sites.google.com/relaxdays.de/hackathon-relaxdays/startseite) for more information.
My participant ID in the challenge was: `CC-VOL1-54`

## Usage

First you need to clone this repository:

```shell script
git clone https://github.com/heinrichreimer/relaxdays-challenge-compression.git
cd relaxdays-challenge-compression/
```

### Docker container

1. Install [Docker](https://docs.docker.com/get-docker/).
1. Build a Docker container with this project:

    ```shell script
    docker build -t relaxdays-challenge-compression .
    ```

1. Compress:

    ```shell script
    docker run -v $(pwd):/data -it relaxdays-challenge-compression --compress /data/Dockerfile
    ```

1. Decompress:

    ```shell script
    docker run -v $(pwd):/data -it relaxdays-challenge-compression --decompress /data/Dockerfile.compressed
    ```

### Local machine

1. Install [Python 3](https://python.org/downloads/), [pipx](https://pipxproject.github.io/pipx/installation/#install-pipx), and [Pipenv](https://pipenv.pypa.io/en/latest/install/#isolated-installation-of-pipenv-with-pipx)
1. Install dependencies:

    ```shell script
    pipenv install
    ```

1. Compress:

    ```shell script
    pipenv run python main.py --compress Dockerfile
    ```

1. Decompress:

    ```shell script
    pipenv run python main.py --decompress Dockerfile.compressed
    ```

1. The app is now running on [`localhost:<PORT>`](http://localhost:<PORT>/)

## License

This repository is licensed under the [MIT License](LICENSE).
