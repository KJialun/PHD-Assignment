from vector2d import *
import random
"""
- Does this class adhere to the SOLID principles?
    - If not, how would you improve upon it? 
- Would it be better to split this class into multiple objects or can it stay as it is?
- How would you implement another kind of Node (Like a WiredNode or a VisibleLightNode) on the model of this class?
    - Is inheritance an option or some refactoring is needed?
"""

class WirelessNode:
    #Unique node identifier
    ids = 0

    def __init__(self,x,y,Ttx=10,Trx=20, battery = 100.0, Ptx = 0.2, Prx = 0.1, Pidle = 0.001) -> None:
        self.id = WirelessNode.ids
        WirelessNode.ids += 1

        self.position = Vector2D(x,y)
        #Time needed to transmit a message
        self.transmit_time = Ttx
        #Time needed to receive a message
        self.receive_time = Trx
        #Battery level in percentage
        self.battery = battery
        #Power used to transmit a message
        self.tx_power = Ptx
        #Power used to receive a message
        self.rx_power = Prx
        #Power used in idle state
        self.idle_power = Pidle
        # Buffer to store messages for transmission
        self.transmit_buffer = ['A','B','C']
        # Buffer to store received messages
        self.receive_buffer = []    
        self.rx_buff = []
        # Current state of the wireless node
        self.state = None    

        # Current state time 
        self.state_start_time = 0    
        self.complete = True

    def transmit(self, channel_queueA):
        # self.transmit_buffer.append('message')  # Add message to transmit buffer
        if self.transmit_buffer and self.state == "transmit":
            message_tx = self.transmit_buffer.pop(0)  # Retrieve and remove the first message from transmit buffer
            channel_queueA.append(message_tx)  # Add the message to the channel_queue
            self.battery -= self.transmit_time * self.tx_power   
        else:
            pass


    def receive(self,channel_queueB):
        """
        - How would you implement the receive method?
        - Can you add a receive and transmit buffer to the class and modify the transmit accordingly
        """
        if channel_queueB and self.state == "receive" :
            self.receive_buffer.extend(channel_queueB)
            # self.receive_buffer.append(channel_queueB)  # Add the message to the receive buffer
            self.battery -= self.receive_time * self.rx_power
        else:
            pass

    def idle(self):
        #Can you modify the class adding the idle time?
        self.battery -= self.idle_power  

    def randomly_select_state(self):
        # Randomly select the next state based on the current time
        states = ["transmit", "receive", "idle"]
        self.state = random.choice(states)
    def check_complete(self,current_time,start_time,duration):
        # Randomly select the next state based on the current time
        if  current_time - start_time + 1 == duration:
            self.complete = True
        else:
            self.complete = False

    def run(self,dt,channel_queueA, channel_queueB):
        """
        Implement a run method which takes a unit time and a state buffer.
        Each time this method is called, it has to check the time and decide if the current operation is complete.
        If yes, it should randomly select in which state the WirelessNode is.
        If not, the node remains in the current state.

        - How would you implement this?
        - Can you change the class according to the state pattern? 
        """

        if  self.complete:
            self.randomly_select_state()
            self.state_start_time = dt
            self.complete = False 

        if  self.state == "transmit" and self.complete == False :
            self.transmit(channel_queueA) 
            self.check_complete(dt,self.state_start_time,self.transmit_time)
        if self.state == "receive" and self.complete == False :
            self.receive(channel_queueB)
            self.check_complete(dt,self.state_start_time,self.receive_time)
           
        if self.state == "idle"    and self.complete == False :    
            self.idle()
            self.check_complete(dt,self.state_start_time,1)
