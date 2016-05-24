
import sys
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('jobo_template')
parser.add_argument('jobo_file')
parser.add_argument('keywords')
parser.add_argument('description')
parser.add_argument('proc_name')
parser.add_argument('proc_card')
parser.add_argument('contact')

args = parser.parse_args()


def main():
    keywords =  args.keywords.split(',')

    post_include = 'MC15JobOptions/MadGraphControl_Pythia8_A14_NNPDF23LO_EvtGen_Common.py'
    outputtemplate = 'MC15.{DSID}.MadGraphPythia8EvtGen_A14NNPDF23LO_{JOBODESCR}.py'

    outputjobo = args.jobo_file

    with open(outputjobo,'w') as outputfile:
        outputfile.write(
            open(args.jobo_template).read().format(
		DESCRIPTION = args.description,
		KEYWORDS=','.join(["\"{0}\"".format(x) for x in keywords]),
		CONTACT=args.contact,
		PROCESS_NAME=args.proc_name,
		PROC_CARD=open(args.proc_card).read(),
		POST_INCLUDE=post_include)
            )
        

if __name__ == '__main__':
    main()
