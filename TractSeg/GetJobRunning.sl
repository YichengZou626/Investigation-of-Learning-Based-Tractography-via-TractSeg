#!/bin/bash

# BASED ON:  srun -t 5-00:00:00 --mem=200G -c 6 --x11=first --pty /bin/bash
# RUN AS 
#	sbatch scriptname

#SBATCH -t 5-0  		# 5 days
#SBATCH --mem=200G		# 200G memory
#SBATCH -c 6			# 6 cpus per task ( defaults to 1 "task")



ExpRunner --config my_custom_experiment
