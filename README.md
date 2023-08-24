# OfficeBot
LLM chat interface built in Streamlit

Cool features:
  1) I made it
  2) The "discussion" field is a convenient place to drop a document and have a chat with the AI about it, no worries that it will fall off the back of the conversation or get summarized into oblivion.  It will always be appended right after your recent chat message
  3) Simple interface, I want to deploy this at my coworkers in a way they can't break.
  4) Knowledge store thats easy to add to.  Right now its in a simple yaml file (systems.yaml), might make another method eventually
Currently works with OpenAI APIs.

Roadmap:
  Add requirements.txt with pre-reqs.  
    - For now try to launch and install whatever is missing.  Repeat.  Its just as good...
  Build out extensions 
  - slash /commands to get the system's attention
  Local LLM usage (targetting starcoder first)
  Tool usage allowing LLM to query outside database for results (classic SQL)
  add basic web page view support to query on a documentation page
  Make it stream tokens
  Docker image or easier deployment
  Back end settings to hide front end interface elements (like model selection)
  CAS/Single sign on
