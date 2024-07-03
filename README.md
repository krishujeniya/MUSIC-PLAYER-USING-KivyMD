<a id="readme-top"></a>

![GitHub repo size](https://img.shields.io/github/repo-size/krishujeniya/MUSIC-PLAYER-USING-KivyMD)
![GitHub contributors](https://img.shields.io/github/contributors/krishujeniya/MUSIC-PLAYER-USING-KivyMD)
![GitHub stars](https://img.shields.io/github/stars/krishujeniya/MUSIC-PLAYER-USING-KivyMD?style=social)
![GitHub forks](https://img.shields.io/github/forks/krishujeniya/MUSIC-PLAYER-USING-KivyMD?style=social)

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <img src="logo.png" alt="Logo" width="80" height="80">

  <h1 align="center">MUSIC-PLAYER-USING-KivyMD</h1>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#key-features">Key Features</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

The MUSIC-PLAYER-USING-KivyMD is a graphical user interface (GUI) application developed using Python's KivyMD and CustomTkinter libraries. This application provides a modern and efficient music player with functionalities like play, pause, next, and previous tracks using a linked list data structure for efficient playlist management. The integration with Docker ensures a consistent environment for running the application.

### Key Features

- **User-Friendly Interface:**
  - Developed using KivyMD for a sleek and modern look.
  - Easy-to-use controls for a seamless music listening experience.

- **Play/Pause:**
  - Simple controls to play or pause the current track.

- **Next/Previous:**
  - Navigate through your playlist efficiently with next and previous track functionality using a linked list data structure.

- **CustomTkinter Integration:**
  - Utilizes CustomTkinter for additional customization and enhanced UI elements.

- **Docker Integration:**
  - Ensures a consistent and reproducible environment for running the application.

## Built With

- [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
- [![KivyMD](https://img.shields.io/badge/KivyMD-2C2255?style=for-the-badge&logo=python&logoColor=white)](https://kivymd.readthedocs.io/en/latest/)
- [![CustomTkinter](https://img.shields.io/badge/CustomTkinter-2C2255?style=for-the-badge&logo=python&logoColor=white)](https://github.com/TomSchimansky/CustomTkinter)
- [![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

## Getting Started

To get a local copy up and running, follow these steps.

### Prerequisites

- **Python**: Ensure you have the latest version of Python installed. [Python Installation Guide](https://www.python.org/downloads/)
- **Docker**: Ensure you have the latest version of Docker installed. [Docker Installation Guide](https://docs.docker.com/get-docker/)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/krishujeniya/MUSIC-PLAYER-USING-KivyMD.git
   cd MUSIC-PLAYER-USING-KivyMD
   ```

2. Build the Docker image
   ```sh
   docker build -t music_player_kivymd .
   ```

3. Step-by-Step Guide to Enable X11 Forwarding in Docker

   **Install XQuartz (macOS) or Xming (Windows)**:
   - **macOS**: Install XQuartz from [XQuartz.org](https://www.xquartz.org/).
   - **Windows**: Install Xming from [Xming.org](https://sourceforge.net/projects/xming/).

   **Allow Connections**:
   - **macOS**: Open XQuartz, go to **Preferences > Security**, and check "Allow connections from network clients".
   - **Windows**: Start Xming with default settings.

   **Run Docker Container with X11 Forwarding**:

   **On Linux**:
   ```sh
   xhost +local:docker
   docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix music_player_kivymd
   ```

   **On macOS with XQuartz**:
   ```sh
   xhost + 127.0.0.1
   docker run -it --rm -e DISPLAY=host.docker.internal:0 music_player_kivymd
   ```

   **On Windows with Xming**:
   ```sh
   docker run -it --rm -e DISPLAY=host.docker.internal:0 music_player_kivymd
   ```

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## Acknowledgments

* [Python](https://www.python.org/)
* [KivyMD](https://kivymd.readthedocs.io/en/latest/)
* [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
* [Docker](https://www.docker.com/)
* [Open Source Community](https://opensource.org/)
* [Contributors](https://github.com/krishujeniya/MUSIC-PLAYER-USING-KivyMD/graphs/contributors)
