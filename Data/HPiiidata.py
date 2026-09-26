import csv
import numpy as np

with open('Data/HarrisPartIII.csv', newline='') as HPiii_data:
        globclusters = csv.DictReader(HPiii_data)

        id_HPiii = []
        v_r_HPiii = []
        v_r_e_HPiii = []
        v_LSR_HPiii = []
        sig_v_HPiii = []
        sig_v_e_HPiii = []
        c_HPiii = []
        r_c_HPiii = []
        r_h_HPiii = []
        mu_V_HPiii = []
        rho_0_HPiii = []
        lg_tc_HPiii = []