## depression path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_next_question
* mood_happy
  - utter_history_question
* mood_affirm
  - actions.ActionPatientInfoRecurrence  
 
## depression path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_next_question
* mood_unhappy
  - utter_history_question
* mood_affirm
  - actions.ActionPatientInfoRecurrence  

## depression path 3
* greet
  - utter_greet
* mood_unhappy
  - utter_next_question
* mood_unhappy
  - utter_history_question
* mood_affirm
  - actions.ActionPatientInfoRecurrence  
 

## say goodbye
* goodbye
  - utter_goodbye