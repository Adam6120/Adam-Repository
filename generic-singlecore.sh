#!/bin/bash

#======================================================
#
# Job script for running a serial job on a single core 
#
#======================================================

#======================================================
# Propogate environment variables to the compute node
#SBATCH --export=ALL
#
# Run in the standard partition (queue)
#SBATCH --partition=teaching
#
# Specify project account
#SBATCH --account=teaching
#
# No. of tasks required (ntasks=1 for a single-core job)
#SBATCH --ntasks=20
#
# Specify (hard) runtime (HH:MM:SS)
#SBATCH --time=00:20:00
#
# Job name
#SBATCH --job-name=PythonCode
#
# Output file
#SBATCH --output=NewCodeScalingCores.out
#======================================================

module purge

#Example module load command. 
#Load any modules appropriate for your program's requirements

module load mpi/latest


#======================================================
# Prologue script to record job details
# Do not change the line below
#======================================================
/opt/software/scripts/job_prologue.sh  
#------------------------------------------------------

# Modify the line below to run your program
cd /users/gmb22123/PH510

# time python3 FixedCode.py This will only use one rank
mpirun -np 1 python3 a1_pylintcorrection.py
mpirun -np 2 python3 a1_pylintcorrection.py
mpirun -np 3 python3 a1_pylintcorrection.py
mpirun -np 4 python3 a1_pylintcorrection.py
mpirun -np 5 python3 a1_pylintcorrection.py
mpirun -np 6 python3 a1_pylintcorrection.py
mpirun -np 7 python3 a1_pylintcorrection.py
mpirun -np 8 python3 a1_pylintcorrection.py
mpirun -np 9 python3 a1_pylintcorrection.py
mpirun -np 10 python3 a1_pylintcorrection.py
mpirun -np 11 python3 a1_pylintcorrection.py
mpirun -np 12 python3 a1_pylintcorrection.py
mpirun -np 13 python3 a1_pylintcorrection.py
mpirun -np 14 python3 a1_pylintcorrection.py
mpirun -np 15 python3 a1_pylintcorrection.py
mpirun -np 16 python3 a1_pylintcorrection.py
mpirun -np 17 python3 a1_pylintcorrection.py
mpirun -np 18 python3 a1_pylintcorrection.py
mpirun -np 19 python3 a1_pylintcorrection.py
mpirun -np 20 python3 a1_pylintcorrection.py




#======================================================
# Epilogue script to record job endtime and runtime
# Do not change the line below
#======================================================
/opt/software/scripts/job_epilogue.sh 
#------------------------------------------------------
