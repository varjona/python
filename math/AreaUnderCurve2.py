#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 15 20:27:48 2025

@author: eps_del
"""
import numpy as np
import pandas as pd

class AreaUnderCurve():
    """
    TODO: Add description
    """
    def __init__(self, f, tol):
        # Define inputs
        self.f = f
        self.tol = tol
        
        print('Ready to approx area under curve!')
        
    def ApproxArea(self, x_lims: list, approx_type: str):
        self.sol_df = pd.DataFrame({"num_rect": [],
                                    "delta_x": [],
                                    "approx": [],
                                    "delta_approx":[]})
        
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
    
    