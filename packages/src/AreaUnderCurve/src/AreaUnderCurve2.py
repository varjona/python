
# -*- coding: utf-8 -*-
"""
Created on Thu May 15 20:27:48 2025

@author: eps_del
"""
import numpy as np
import pandas as pd

class AreaUnderCurve():
    """Calculate the area under a curve.
    The AreaUnderCurve class is instantiated by providing the function to be evaluated. Once that
    is init'ed, along with the solutions DataFrame, running the ApproxArea with a provided
    tolerance (tol) value will iteratively create a row for the solutions DataFrame and compare
    to the previous "delta_approx" - the change in the approximations. As we increase the number
    of rectangles (num_rect) the approximation to the area under the curve should get better, and
    so the values in "delta_approx" approach our tolerance (tol).

    Usage
    -----
    def f(x):
        return 3*x - 1
    approx = AreaUnderCurve(f)
    """
    def __init__(self, f):
        """Initialize class with provided function
        TODO: Add docstring

        Parameters
        ----------
        f : func
            Single, continuous variable function.
        """
        self.f = f

        self.sol_df = pd.DataFrame({"num_rect": [],
                                    "delta_x": [],
                                    "approx": [],
                                    "delta_approx":[]})
        """DataFrame: Pandas DataFrame for storing approximations"""
        
        print('Ready to approx area under curve!')
        
    def ReimannApprox(self, x_lims: list, approx_type: str, ):
        """Approximate area under the curve of the provided function.

        Parameters
        ----------
        xlims : list
            List containing two float values - the input values where we start and end the
            area under the curve's approximation.

        approx_type : str
            Options include "rs" (right side), "ls" (left side), "mid" (middle), and "trap"
            (trapezius). Used to select the value of f(x) to use for the a
        """

        print(f"Limits:{x_lims}",
              f"Tolerance: {self.tol}",
              f"Approx type: {approx_type}",
              sep="\n")
        
        # Make the first row of the dataframe
        self.BuildRow(approx_type)
        print(self.sol_df)
    
    def BuildRow(self, approx_type: str):
        num_rect = len(self.sol_df) + 1
        delta_x = (x_lims[-1]-x_lims[0])/num_rect
        
        x_space = np.linspace(x_lims[0], x_lims[1], num_rect + 1)
        
        if approx_type == "rs":
            approx = delta_x*np.sum(self.f(x_space[1:]))
        elif approx_type == "ls":
            approx = delta_x*np.sum(self.f(x_space[:-1]))
        elif approx_type == "mid":
            approx = delta_x*np.sum(self.f((x_space[:-1] + x_space[1:])/2))
        
        if num_rect == 1:
            delta_approx = np.nan
        else:
            delta_approx = np.abs(self.sol_df.iloc[-1]['approx'] - approx)
        
        nu_row = [num_rect,
                  delta_x,
                  approx,
                  delta_approx]
        
        self.sol_df.loc[0] = nu_row
    
if __name__ == "__main__":
    print("Starting demo!")
    
    def f(x: float) -> float:
        return np.power(x, 2)
    x_lims = [0, 1]
    tol = np.power(10.0, -3)
    
    approx_type = "mid"
    
    demo = AreaUnderCurve(f, tol)
    demo.ApproxArea(x_lims, approx_type)
    
    