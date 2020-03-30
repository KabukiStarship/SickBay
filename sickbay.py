"""SickBay @version 0.x
@link    https://github.com/KabukiStarship/sickbay.git
@file    /SickBay.py
@author  Cale McCollough <https://cale-mccollough.github.io>
@license Copyright 2020 (C) Kabuki Starship <kabukistarship.com>; all rights 
reserved (R). This Source Code Form is subject to the terms of the Mozilla 
Public License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at <https://mozilla.org/MPL/2.0/>. """
 
import SickBayDevice
import Human
import Ventilator
import sched, time

Scheduler = sched.scheduler(time.time, time.sleep)
  
# The SickBay app object.
class SickBay(SickBayDevice):
  # Constants
  StateConfiguring = 0   #< State: Init.
  StateMonitor = 1       #< State: Monitoring.
  StateShutDown = 1      #< State: Shutting down.
    
  def __init__(self, ):
    super().__init__(0, "SicKBay", "The main SickBay object.")
    self.State = self.StateConfiguring    #< The app state.
    self.Patients = []             #< The List of patients.
    self.Patient = None            #< The currently selected patient.
    self.HumanOperator = ""        #< The human who is operating the system.
    HumanOperatorSet()
    
  def HumanOperatorSet(self):
    self.HumanOperator = input("\nEnter your name: ")
  
  # Adds a patient to the Patients.
  def PatientsAdd(self, Name, Sex, Height, Weight):
    Patients.append(Human(Name, Sex, Height, Weight))

  # Handler for the init app state.
  def StateConfiguringHandle (self):
    print ("\nWelcome to SickBay")
    print ("\n\nAdding test patients.")
    Patients.append ("John Doe 1", "M", 1.7, 70)
    Patients.append ("John Doe 2", "M", 1.8, 75)
    Patients.append ("John Doe 3", "M", 1.9, 80)
    Patients.append ("John Doe 4", "M", 2.0, 85)
    Patients.append ("Jane Doe 1", "F", 1.2, 55)
    Patients.append ("Jane Doe 2", "F", 1.3, 60)
    Patients.append ("Jane Doe 3", "F", 1.4, 65)
    Patients.append ("Jane Doe 4", "F", 1.5, 70)
  
  # Handler for the Monitor app state.
  def StateMonitorHandle(self):
    for Patient in Patients:
      Patient.PrintStats()
  
  def StateShutDownHandle(self):
    print ("\n\nShutting down...")

  # Main program entry point.
  def Run(self):
    Scheduler.enter(5, 1, Update, ())
    Scheduler.enter(10, 1, Update, ())
    Scheduler.run()
    
  # Prints the most current and important stats to the Console.
  def PrintStats(self):
    for Patient in self.Patients:
      Patient.PrintStats()
 
  # Function that is called every x seconds to update everything.
  def Update(self, sc):
    print ("\n\nUpdate Time:", time.time())
    Handler = {
      1: StateConfiguringHandle,
      2: StateMonitorHandle,
      3: StateShutDownHandle
    }
    # Get the function from switcher dictionary
    Handle = Handler.get(self.State, lambda: "Invalid state")
    # Execute the function
    Handle()
    PrintStats()

if __name__ == '__main__':
  SickBayApp = SickBay.SickBay()
    #unittest.main()
