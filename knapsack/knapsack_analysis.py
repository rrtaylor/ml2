# developer: Richard Brooks
# description: randomized optimization to find optimal portfolio combination
# contact: richardbrks@gatech.edu

import bitflip_randOpt as ropt
import pandas as pd
import numpy as np
import datetime as dt
import copy
import matplotlib.pyplot as plt
from random import random
import chow_liu_trees as CLT
from collections import defaultdict
import networkx as nx
import csv

np.random.seed(None)

def read_data(filename):
	""" read knapsack data.
	"""
	weights = []
	values = []
	with open(filename, 'r') as csvfile:
		csvreader = csv.reader(csvfile, delimiter=' ')
		n, weight_limit = csvreader.next()
		for (v, w) in csvreader:
			values.append(v)
			weights.append(w)
	return int(weight_limit), np.array(weights).astype(int), np.array(values).astype(int)

def main():
	"""
	"""
	# read data
	filename = './data/ks_19_0'
	weight_limit, na_weights, na_values = read_data(filename)

	# define fitness function
	def fit(vec_select):
		tot_wt = np.sum(na_values)
		if np.sum(vec_select) == 0:
			return 0
		if np.sum(na_weights[vec_select.astype(bool)]) > weight_limit:
			return (-1 * np.sum(na_values[vec_select.astype(bool)])) / float(tot_wt)
		else:
			return np.sum(na_values[vec_select.astype(bool)]) / float(tot_wt)

	# test algorithms
	# Randomized Hill Climbing
	print "\nRHC " + "#"*30
	max_fit, max_vec, d_progress = ropt.bitflip_RandomizedHillClimb(len(na_values), fit, iterations=100, restarts=10, verbose=True)
	print "RHC fitness: ", max_fit
	print "select vector:"
	print max_vec
	print "d_progress:"
	print d_progress
	print "weight limit: ", weight_limit
	print "total weight: ", np.sum(na_weights[max_vec.astype(bool)]) 
	print "total value: ", np.sum(na_values[max_vec.astype(bool)])

	# # Simulated Annealing
	# print "\nSA " + "#"*30
	# max_fit, max_vec, d_progress = ropt.bitflip_SimulatedAnnealing(len(na_values), fit, iterations=100, restarts=10, verbose=True)
	# print "SA fitness: ", max_fit
	# print "select vector:"
	# print max_vec
	# print "d_progress:"
	# print d_progress
	# print "weight limit: ", weight_limit
	# print "total weight: ", np.sum(na_weights[max_vec.astype(bool)]) 
	# print "total value: ", np.sum(na_values[max_vec.astype(bool)])

	# # Genetic Algorithms
	# print "\nGA " + "#"*30
	# max_fit, max_vec, d_progress = ropt.bitflip_GeneticAlgorithm(len(na_values), fit, population_size=100, generations=1000, restarts=1, child_per_parent=1, mutation_prob=0.1, crossover_split=0.5, verbose=True)
	# print "GA fitness: ", max_fit
	# print "select vector:"
	# print max_vec
	# print "d_progress:"
	# print d_progress
	# print "weight limit: ", weight_limit
	# print "total weight: ", np.sum(na_weights[max_vec.astype(bool)]) 
	# print "total value: ", np.sum(na_values[max_vec.astype(bool)])

	# # MIMIC
	# print "\nMIMIC " + "#"*30
	# max_fit, max_vec, d_progress = ropt.bitflip_MIMIC(len(na_values), fit, iterations=100, restarts=1, init_population_size=100, n_samples=100, theta_percentile=0.8, verbose=True)
	# print "MIMIC fitness: ", max_fit
	# print "select vector:"
	# print max_vec
	# print "d_progress:"
	# print d_progress
	# print "weight limit: ", weight_limit
	# print "total weight: ", np.sum(na_weights[max_vec.astype(bool)]) 
	# print "total value: ", np.sum(na_values[max_vec.astype(bool)])

	return


if __name__ == "__main__":
	main()