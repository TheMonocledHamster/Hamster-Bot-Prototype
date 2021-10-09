# Chatbot Prototype
Description: Basic prototype of a rudimentary chatbot (Completely Offline)
</br></br></br>
Preferred OS: Any Debian-based distro. (Developed in Kubuntu 20.04)

Python version: 3.8
</br></br>
Additional Libraries Used: 
* pyttsx3 (Text-to-Speech wrapper for espeak module in Linux) [https://pypi.org/project/pyttsx3/]
* sounddevice (To capture sound input from mic) [https://pypi.org/project/sounddevice/]
* vosk (Speech recognition engine) [https://pypi.org/project/vosk/]
</br></br></br>

Vosk Model sourced from https://alphacephei.com/vosk/models

Code used for testing: https://github.com/alphacep/vosk-api

</br></br>

[IMPORTANT] Verify the following while cloning this repo:
* Both the python script and .json file are in the 'Bot/' directory.
* The folder containing the vosk model is named 'model'.
* The 'model' folder is in the 'Bot/' directory.

</br></br>

[Instructions] Once the installation is setup and you run the script:
* Say "hello", "greetings", "hamster" or any other command as mentioned in the .json file to wake the bot.
* Reply to the question with "yes" (or a variant), "no" (or a variant, again), something else, or even nothing at all.
* The default model present is trained for Indian English. For other accents, please get the relevant vosk model.
* Remember to be courteous to the bot. (Or not, no one would know either ways,absolutely no telemetry here)

</br></br>

[Future Plans] 
* I intend to expand the range of the conversation, and hopefully add some NLP functionality. </br>
  [Update] To this end, I'm presently testing out Google's BERT and OpenAI's GPT-2 transformer models.
* The voice is currently too robotic (limitation of espeak on Linux). Some improvements are in order on that front. 
  [Update] I'm currently attempting to get SAPI5 working on Linux as well, to improve conversation quality.
* The bot may soon be learning another language! I'm considering adding either Kannada or German language capabilities.
* I'm considering adding Noise-Cancelling and better recognition accuracy by providing support for multi-mic audio-capture. The code is already thread-safe, and implementing multi-threading and/or multi-processing should not be too much of a challenge. </br>
  [Update] I'm currently scoping out Nginx hosting, towards this end.
* I intend to containerize and deploy a more presentable project in a web app within the next few weeks.

</br></br>

Thank you for visiting this page. I hope you enjoyed experimenting with the bot as much as I did developing it. I encourage all visitors to fork this repository and add any features that they feel might be useful. Please do hit me up with PRs and Issues, even ideas, let's see how far we can take this project.

</br>

[NOTE] This project is licensed under the MIT License. I intend to keep this project as free and open source software (FOSS) indefinitely, throughout it's deelopment cycle.
</br></br>
[NOTE] This core of the project was developed in 2 nights (5th and 6th Oct, 2021), so there are multiple possible avenues for improvement. I'd be grateful for any PRs and Bugfix or Feature Tickets.
