#!/usr/bin/python
import os
import sys

machfile = ['./singlemach.vm']
traindata = ['./20news.train']
numservers = ['3']
numworkerthreads = ['2']

prog=['../../build/apps/medlda_release/medlda ']  
os.system("mpirun -machinefile "+machfile[0]+" "+prog[0]
  +" -machfile "+machfile[0]+" -schedulers "+numservers[0]
  +" -num_thread "+numworkerthreads[0]+" -train_prefix "+traindata[0]);
