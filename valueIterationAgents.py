# valueIterationAgents.py
# -----------------------
##
import mdp, util
import sys

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp = None, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbabilities(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        if (self.mdp != None):
            self.doValueIteration()


    def doValueIteration (self):
        # Write value iteration code here

        print "Iterations: ", self.iterations
        print "Discount: ", self.discount
        states = self.mdp.getStates()
       


        #util.raiseNotDefined()
		
        #"*** YOUR CODE STARTS HERE ***"
        # Your code should include the implementation of value iteration
        # At the end it should show in the terminal the number of states considered in self.values and
        # the Delta between the last two iterations

        

        states = self.mdp.getStates()
	    
		
        for i in range(self.iterations):
          temp = util.Counter()

		#Para cada estado obtenemos las posibles acciones
          for state in states:
            maxDelta = float("-inf")
            actions = self.mdp.getPossibleActions(state)

		#Para cada accion y estado obtenmos los estados a transitar y las probabilidades
            for action in actions:
              transitions = self.mdp.getTransitionStatesAndProbabilities(state, action)
              sumTransitions = 0

			  #Formula
              for transition in transitions:
                reward = self.mdp.getReward(state, action, transition[0])
                sumTransitions += transition[1]*(reward + self.discount*self.values[transition[0]])

			#Nos quedamos con el maximo	
              maxDelta = max(maxDelta, sumTransitions)

            if maxDelta != float("-inf"):
              temp[state] = maxDelta
            
		  
          for state in states:
            self.values[state] = temp[state]
    


        #"*** YOUR CODE FINISHES HERE ***"
        
    def setMdp( self, mdp):
        """
          Set an mdp.
        """
        self.mdp = mdp
        self.doValueIteration()

    def setDiscount( self, discount):
        """
          Set a discount
        """
        self.discount = discount

    def setIterations( self, iterations):
        """
          Set a number of iterations
        """
        self.iterations = iterations
       
       
    def getValue(self, state):
        """
          Return the value of the state
        """
        return self.values[state]
        
    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """

       # util.raiseNotDefined()
	   
        #"*** YOUR CODE STARTS HERE ***"

		#Aplicamos la formula del Q-value
        qvalue = 0
        transitionFunction = self.mdp.getTransitionStatesAndProbabilities(state,action)
        for nextState, probability in transitionFunction:
            qvalue += probability * (self.mdp.getReward(state, action, nextState)  + (self.discount * self.values[nextState]))

   #   return value


        #"*** YOUR CODE FINISHES HERE ***"
        
        return qvalue
    

    def showPolicy( self ):

        """
          Print the policy
        """
        
        states = self.mdp.getStates()
        for state in states:
            print "Policy\n", state, self.getPolicy(state)


    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """

       # util.raiseNotDefined()
	   
        #"*** YOUR CODE STARTS HERE ***"

        maxDelta = float("-inf")
        a = None
		#Obtenemos las acciones posibles
        actions = self.mdp.getPossibleActions(state)
		
		#Nos quedamos con el valor maximo tras ejecutar Qvalues
        for action in actions:
          q = self.computeQValueFromValues(state, action)
          if q > maxDelta:
            maxDelta = q
            a = action
		
        return a


        #"*** YOUR CODE FINISHES HERE ***"

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getPolicy(self, state):
        "Returns the policy at the state (no exploration)."
        return self.getAction(state)

    
    def getQValue(self, state, action):
        "Returns the Q value."        
        return self.computeQValueFromValues(state, action)

    def getPartialPolicy(self, stateL):
        "Returns the partial policy at the state. Random for unkown states"        
        state = self.mdp.stateToHigh(stateL)
        if self.mdp.isKnownState(state):
            return self.computeActionFromValues(state)
        else:
            # random action
            return util.random.choice(stateL.getLegalActions()) 

