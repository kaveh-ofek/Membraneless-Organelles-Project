import numpy as np
import os

from plots import load_pickles_to_arrays, calculate_center_of_mass, var_array_generator, generate_heatmap, check_file_existing
T_thresh = 1

kS = np.logspace(-3, -0.5, 15, base=10)
rads = np.logspace(2, 3, 8, base=10)


heatmap_data = np.zeros((len(kS) , len(rads)))

full_path = "/cs/cbio/ilia/Hackathon/IMP_Experiment/Run3"
for k, k_out in enumerate(kS):
    for rad, spr_rad in enumerate(rads):
        if check_file_existing(k_out, spr_rad,full_path):
            vars = []
            T_ns, E, D, matrix= load_pickles_to_arrays(k_out, spr_rad, full_path)
            for i,iter in enumerate(matrix):
                for c,chain in enumerate(iter):
                    matrix[i][c] = calculate_center_of_mass(
                        chain)  # replacing all chain's bead with 1 center of mass
                vars.append(var_array_generator(matrix[i]))
            heatmap_data[k, rad] = np.mean(vars)

plot_title = "Mean variance of chains locations"
file_title = "variance"
labels_dict = {"y":"molar Concenration", "x":"inter-strings harmonic coupling"}
generate_heatmap(heatmap_data, labels_dict, file_title, plot_title)








