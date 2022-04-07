# Chatbot Prototype
### Description 
Basic prototype of a rudimentary chatbot (Completely Offline)
</br>
### Details
Preferred OS: Any Debian-based distro. (Developed in Kubuntu 20.04)
Python version: 3.8
</br>
Additional Libraries Used: 
* pyttsx3 (Text-to-Speech wrapper for espeak module in Linux) [https://pypi.org/project/pyttsx3/]
* sounddevice (To capture sound input from mic) [https://pypi.org/project/sounddevice/]
* vosk (Speech recognition engine) [https://pypi.org/project/vosk/]

If you're running Linux on ARM devices, install the following modules:
* espeak
* libportaudio2
* libatomic1  

  Ubuntu: ``sudo apt-get install espeak libatomic1 libportaudio2``

Vosk Model sourced from https://alphacephei.com/vosk/models

Code used for testing: https://github.com/alphacep/vosk-api
</br>

### Installation

[IMPORTANT] Verify the following while cloning this repo:
* Both the python script and .json file are in the 'Bot/' directory.
* The folder containing the vosk model is named 'model'.
* The 'model' folder is in the 'Bot/' directory.


[Instructions] Once the installation is setup and you run the script:
* Say "hello", "greetings", "hamster" or any other command as mentioned in the .json file to wake the bot.
* Reply to the question with "yes" (or a variant), "no" (or a variant, again), something else, or even nothing at all.
* The default model present is trained for Indian English. For other accents, please get the relevant vosk model.
* Remember to be courteous to the bot. (Or not, no one would know either ways,absolutely no telemetry here)

</br>

### Future Plans

* I intend to expand the range of the conversation, and hopefully add some NLG functionality. </br>
* The voice is currently too robotic (limitation of espeak on Linux). Some improvements are in order on that front. 
  [Update] I'm currently attempting to get SAPI5 working on Linux as well, to improve conversation quality.
* The bot may soon be learning another language! I'm considering adding either Kannada or German language capabilities.
* I'm considering adding Noise-Cancelling and better recognition accuracy by providing support for multi-mic audio-capture.

</br></br>

Thank you for visiting this page. I hope you enjoyed experimenting with the bot as much as I did developing it. I encourage all visitors to fork this repository and add any features that they feel might be useful. Please do hit me up with PRs and Issues, even ideas, let's see how far we can take this project.
</br>

[NOTE] This project is licensed under the MIT License. I intend to continue to keep this project FOSS indefinitely, regardless of where it reaches in its development cycle.
</br>
[NOTE] There are multiple possible avenues for improvement. I'd be grateful for any PRs and Bugfix or Feature Tickets.
