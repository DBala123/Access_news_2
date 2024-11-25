#### About repository
This repository consists of a news downloader. It uses the API which pulls news from multiple sources onlines from "newsapi.org". I have created a GUI, where the user can pick the topic, the date range, the news sources for the news they want to see. Once the app extracts it, it provides the user with a list of the sources including links, which can be clicked on and opened by the user.

#### How to clone it and make it work properly
Please note that "news_GUI" is the main file. In it, I have replaced my personal API key with ### in line 65. I have also replaced the API key with ### in line 4 of the file "news_sources.py" (a file which downloads the news sources for each category of news). Hence, as the cloner, once you have cloned the repository, please get your own API key to replace the "###", at which point the code will work. 
Additionally, when cloning, the error message may pop up saying "setup.py" and "pyproject.toml" may be required. Please ignore this, as these files are not necessary. I have already tried cloning the project from Github and without these files, the cloning still works.
