"""
dropSTAR: Page Render: Twilio - Zork

Author: Geoff Howland <geoff@gmail.com>

Play at: 415-599-2671  Account:  7226-0656

NOTE: No tests or other good things for this code at the moment.  Just
  prototype code to get an interactive app working on Twilio.
"""

import sys
import yaml

import zorkdata


def Execute(data, chain_output, state, env=None):
  """Control: Execute!"""
  #TODO(g): Fix state so I dont have to use a module as a data store.  Not
  #   that it's terrible, as its all temporary, but still state should work...
  CALLERS = zorkdata.CALLERS
  
  # Get the caller, or create a new one
  if data['Caller'] not in CALLERS:
    new_caller = True
    caller = {'position':'west_of_house', 'visited':[]}
    CALLERS[data['Caller']] = caller
  else:
    caller = CALLERS[data['Caller']]
    new_caller = False
  
  
  # Get the position
  position = caller['position']
  
  # Get any options that have been pressed
  if 'Digits' in data:
    pressed = int(data['Digits'])
  else:
    pressed = None
  
  
  # Load data
  zork = yaml.load(open('scripts/twilio/zork.yaml'))
  
  # Get the current room
  room = zork[position]
  
  # Start out
  output = '<Response>\n'
  output += '<Gather numDigits="1" action="/twilio/voice/index.xml" method="POST">\n'
  
  # If this is a new caller, introduce them to the game.
  if new_caller:
    output += '<Say>Welcome to Zork on your phone.  Use the keypad to play.</Say>\n'
  
  # Give full description this time
  full_description = False
  if pressed == 1:
    #TODO(g): Implement inventory system here...
    output += '<Say>There is nothing to pick up here.</Say>\n'
  
  # If the want to review the description of the location
  elif pressed == 5:
    if position in caller['visited']:
      full_description = True
  
  # Change rooms, if directed to
  elif pressed and 'options' in room and pressed in room['options']:
    # Change rooms
    if 'room' in room['options'][pressed]:
      position = room['options'][pressed]['room']
      caller['position'] = position
      
      # Change rooms
      room = zork[position]
    
    # Give error message
    else:
      output += '<Say>%s</Say>\n' % room['options'][pressed]['error']
  
  # Failure
  elif pressed:
    output += '<Say>You cant go that way.</Say>\n'
  
  # Room name
  if not full_description:
    output += '<Say>%s</Say>\n' % room['name']
  
  # Full description
  if position not in caller['visited'] or full_description:
    output += '<Say>%s</Say>\n' % room['info']
  
  # Wrap up
  output += '</Gather>\n'
  output += '</Response>\n'
  
  # Mark this room as visited, so only the short name is used
  caller['visited'].append(position)

  # Format the XML tag and append the output
  chain_output['twilio'] = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n%s" % output
  return chain_output


