#Author: will buttinger <will@cern.ch>

#This is a template joboption for generating events with the HAHM madgraph model
#Tested with: MCProd,19.2.5.3.3
#If it doesn't work, please moan to the MadGraphControl developers
#To use it, copy the template and rename it by replacing the XXXXXX and YYYYYYYYY in the filename with:
# make XXXXXX match the runNumber you give to Generate_tf
# make the YYYYYYYY a short description
#Then modify:
# - save_proc_dir (bool: if you want to keep the process directory or not),
# - proc_card (for the process), 
# - param_card_extras (for the model parameters), 
# - run_card_extras (for the generator-level cuts),
# - post_lhe_hook (a hook method for executing code after the lhe making (madgraph) but before showering (pythia)
#Run it with (for example):
# Generate_tf.py --ecmEnergy=13000 --runNumber=302076 --firstEvent=1 --asetup="" --maxEvents=5000 --randomSeed=1 --jobConfig="MC15.302076.MadGraphPythia8EvtGen_A14NNPDF23LO_HAHMggfZdZd4l_mZd5.py" --outputEVNTFile=my.evgen.root

#--------------------------

evgenConfig.description="{DESCRIPTION}"
evgenConfig.keywords+=[{KEYWORDS}]
evgenConfig.contact = ['{CONTACT}']
evgenConfig.process = "{PROCESS_NAME}"

save_proc_dir = True #change to true to delete process dir after generating ... for official joboptions please put as False

proc_card = """{PROC_CARD}"""

param_card = '{PARAM_FILE}'

proc_name = evgenConfig.process #just used for the mg directory name

#modifications to the param_card.dat (generated from the proc_card i.e. the specific model)
#if you want to see the resulting param_card, run Generate_tf with this jobo, and look at the param_card.dat in the cwd
#If you want to see the auto-calculated values of the decay widths, look at the one in <proc_name>/Cards/param_card.dat (again, after running a Generate_tf)
param_card_extras = {{  }}


run_card_extras = {{  }}

def post_lhe_hook():
    #You can put code here that will get called after the 'generate' method of MadGraphControl is called
    #What follows is an example for modifying the lifetime of the zd:
    
    #The 'add_lifetimes' method is defined in the file included below. It modifies the lhe file to include particle lifetimes on the particle with given pdgId
    #add_lifetimes(pdgId=32, avgtau=2000)
    pass


include("{POST_INCLUDE}")





