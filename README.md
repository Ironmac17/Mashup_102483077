YouTube Mashup Generator in Python
==================================

-   **Course:** UCS654 - Predictive Analytics using Statistics

-   **Assignment:** Assignment-7 (Mashup)

-   **Author:** Nimish Agrawal

-   **Roll Number:** 102483077

* * * * *

About the Project
-----------------

This repository contains a Python implementation of a **YouTube Mashup Generator**.

The system automatically downloads multiple songs of a specified singer from  YouTube, extracts audio from each video, trims the first few seconds from each audio file, and merges all the clips into a single mashup output file.

The project also includes a **web service interface**, allowing users to create  mashups directly through a browser and receive the final output via email.

* * * * *

Project Website
---------------

The Mashup Generator is also available as a web application, enabling users to\
generate mashups through an interactive web interface.

🔗 **Live Website:**\
(Add your deployed link here if available)

* * * * *

Installation -- USER MANUAL
--------------------------

1.  Mashup Generator requires **Python 3** to run.

2.  Required dependencies:

    -   yt-dlp

    -   pydub

    -   flask

    -   python-dotenv

3.  Install dependencies using:

`pip install yt-dlp pydub flask python-dotenv`

* * * * *

Usage
-----

Run the following command in command prompt:

`python 102483077.py "<SingerName>" <NumberOfVideos> <AudioDuration> <OutputFileName>`

Example:

`python 102483077.py "AP Dhillon" 20 25 mashup.mp3`

This will:

-   Download the specified number of videos

-   Convert videos to audio

-   Extract the specified duration from each audio

-   Merge all clips into a single mashup output file

* * * * *

**Nimish Agrawal**\
Roll Number: 102483077