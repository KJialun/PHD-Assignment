from random import randint
from node import *

"""
This is a very simple implementation of a simulation.
A set of wireless nodes is distributed in a bidimensional space.
Each node can be at every time in one of the following states: transmit, receive, idle
When a wireless node is transmitting, it puts a message in the shared queue.
When a wireless node is receiving, it pulls out all messages from the queue but does not delete them. (simulate multipath ?)
- Can you explain how the simulation loop works?
- Why there are 2 queues instead of a single one?
- What is the weak point of this implementation?
- How would you improve upon this implementation? (consider for example adding collisions or a propagation model)
"""

channel_queueA = []
channel_queueB = []
nodes = [WirelessNode(randint(-20,20),randint(-20,20)) for i in range(4)]
simulation_steps = 1000
for dt in range(simulation_steps):
    for wn in nodes:
        wn.run(dt,channel_queueA, channel_queueB)

    print(f"Messages:{channel_queueA} - {channel_queueB}")
    print(f"Nodes:{nodes}")
    channel_queueB.clear()
    channel_queueB, channel_queueA = channel_queueA, channel_queueB    
   #  print(f"Node 1 transmit buffer :{nodes[0].transmit_buffer}")
    print(f"Node 1 state :{nodes[2].state}")
    print(f"Node 1 receive buffer :{nodes[2].receive_buffer}")

# '''
#     The simulation loop in this implementation works as follows:

# 1. It initializes two empty queues (`channel_queueA` and `channel_queueB`) to represent the shared channel between the wireless nodes.
# 2. It creates a list of wireless nodes (`nodes`) with random coordinates in the bidimensional space.
# 3. It specifies the number of simulation steps (`simulation_steps`) to run.
# 4. It enters a loop that iterates over each simulation step (`dt`).
# 5. Within each step, it iterates over each wireless node (`wn`) in the `nodes` list.
# 6. For each wireless node, it calls the `run()` method, passing the current simulation step, and the two channel queues (`channel_queueA` and `channel_queueB`) as arguments.
# 7. After all the wireless nodes have executed their `run()` method for the current step, the state of the simulation is printed, including the messages in the two queues (`channel_queueA` and `channel_queueB`) and the current state of the wireless nodes (`nodes`).
# 8. The two queues are swapped, with `channel_queueA` becoming `channel_queueB` and vice versa. This swap ensures that the wireless nodes alternate between using the two queues for transmitting and receiving messages.

# Now, let's address the other questions:

# 1. **Why are there 2 queues instead of a single one?**
#    The implementation uses two queues (`channel_queueA` and `channel_queueB`) to simulate a shared channel between the wireless nodes. By using two queues, the implementation allows the wireless nodes to alternate between transmitting and receiving messages. One queue is used for transmitting messages, while the other queue is used for receiving messages. The swap operation at the end of each simulation step ensures that the wireless nodes switch between the two queues.

# 2. **What is the weak point of this implementation?**
#    One potential weak point of this implementation is that it lacks collision detection and handling. In a real wireless communication system, collisions can occur when multiple nodes try to transmit simultaneously, leading to message corruption or loss. This implementation does not take collisions into account, and all messages are simply added to the shared queues without any consideration for potential collisions. This can result in unrealistic behavior and unreliable communication between the wireless nodes.

# 3. **How would you improve upon this implementation?**
#    To improve this implementation, you could consider adding collision detection and handling. One way to address collisions is by implementing a medium access control (MAC) protocol, such as CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance). This protocol allows nodes to sense the medium before transmitting and avoid collisions by waiting for a clear channel. Additionally, you could introduce a propagation model to simulate the wireless signal propagation and fading effects. This would make the simulation more realistic by taking into account the distance between nodes, signal strength, and potential interference.'''