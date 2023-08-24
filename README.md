# OfficeBot
LLM chatbot
Intended to have a clean and simple design for office deployment

Screenshot:
![image](https://github.com/iamthewally/OfficeBot/assets/31074602/be1cf684-ad63-4535-89ce-a18c725255bf)

Install:
1) Clone the repo into a folder
2) cd to folder from [1]
3) rename the word "example" out of the .yaml files
4) put your info into the .yaml files following the existing structure

Run: 
1) cd to folder with source
2) streamlit run .\main.py
3) site will automatically load in your default browser, terminal will give you links for connecting locally and on the network.

Cool features:
  1) I made it
  2) The "discussion" field is a convenient place to drop a document and have a chat with the AI about it, no worries that it will fall off the back of the conversation or get summarized into oblivion.  It will always be appended right after your recent chat message
  3) Simple interface, I want to deploy this at my coworkers in a way they can't break.
  4) Knowledge store thats easy to add to.  Right now its in a simple yaml file (systems.yaml), might make another method eventually
Currently works with OpenAI APIs.

Roadmap:
  - Get accurate token counts using API rather than estimating it to be 1 token per word
  - Add requirements.txt with pre-reqs.  
    - For now try to launch and install whatever is missing.  Repeat.  don't worry it'll be cool...
  - Conda env
  - Build out extensions 
    - slash /commands to get the system's attention
  - Local LLM usage (targetting starcoder first), option to keep everything private
  - Tool usage allowing LLM to query outside database for results (classic SQL)
  - extension to run http get on a URL
  - Make it stream tokens rather than block
  - Docker image for easier deployment
  - Ability to hide front end interface elements (like model selection), helps deployment
  CAS/Single sign on
  - add summaries for long chats rather than removing messages in the middle
  - move colors/css/etc to config files for deployment
  - add default model for each character card
