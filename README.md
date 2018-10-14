Instructions:
=============


1) Skimming 
-----------

The first step consists in skimming FSA ntuples. For each final state there is a folder "Skim".

To compile the code: 
'''
./Make.sh skim_mt.cc
'''

The syntax to run over FSA ntuples is: 
'''
./skim_mt.exe mc (or data) out.root in.root
'''

To make the list of commands to run over all samples: 
'''
python prepare_run2.py
'''

2) SV mass
----------

To run SV mass on the skimmed ntuples, follow instructions in:
https://github.com/lmdodd/SubmitSVFit

3) Analysis
-----------

Skimmed ntuples with SV mass are stored in /data/ccaillol of uwlogin.

Codes to run the analysis are stored in the "Analysis" folders.

The first time you run, mkdir these directories: files_nominal, files_up, files_down.

The first time you run, you should also copy locally the HTT scale factors:

'''
git clone https://github.com/CMS-HTT/LeptonEfficiencies
'''

To run the analysis: 
'''
sh do_all2D_relaxed.sh
'''

Unroll 2D analysis: 
'''
python Create_1D.root
'''

test
