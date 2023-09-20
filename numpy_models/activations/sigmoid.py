import numpy as np


class Sigmoid_np():
    def __init__(self) -> None:
        self.output = None # save output
        self.grad = None # save gradient
        
    def forward(self,x):
        """
        Args:
            x (np.array): [batch, ... ]

        Returns:
            np.array: [batch, ... ] 
        """
        out = 1 / ( 1 + np.exp(-x) )
        
        self.output = out
        return out
    
    def backward(self, d_prev):
        """
        backward:
            output -> d_sigmoid -> grad
        
        """
    
        grad = (d_prev) * (1 - d_prev )
        
        self.grad = grad
        return self.grad
    
    def __call__(self,x):
        return self.forward(x)