from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging
import warnings

from policy import RestaurantPolicy
from rasa_core import utils
from rasa_core.actions import Action
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.events import SlotSet
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.memoization import MemoizationPolicy

from outcome import predict_outcome 
#class ActionCheckRestaurants(Action):
 #  def name(self):
      # type: () -> Text
  #    return "action_check_restaurants"

   #def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]

    #  cuisine = tracker.get_slot('cuisine')
     # q = "select * from restaurants where cuisine='{0}' limit 1".format(cuisine)
      #result = db.query(q)

      #return [SlotSet("matches", result if result is not None else [])]


class ActionPatientInfoRecurrence(Action):
  
    def name(self):
        return "patient_consultation_info"
        
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Getting patient depression recurrence../")
        rec_info = predict_outcome()
        
class ActionPatientGeneralInfo(Action):
    def name(self):
        return "patient_general_info"
            
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Patient's general info")
        
                    
  
           
           
           
            
            
            