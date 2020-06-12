import libxml2
import sys
import quiz_library

'''
purpose
	Accept 1 or more log file names on the command line.

	For each log file, compute the total time taken for each question. 

	Write to standard output, the average time spent for each question.
preconditions
	Each command-line argument is the name of a readable and
	legal quiz log file.

	All the log_files have the same number of questions.
'''

# handle command line arguments
if len(sys.argv) < 2:
	print 'Syntax:', sys.argv[0], 'quiz_log_file ...'
	sys.exit()

totals=[]

for f in sys.argv[1:]:
	data=quiz_library.load_quiz_log(f)
	if not totals:
		totals=[0]*(quiz_library.compute_question_count(data))
	start=[None]*(quiz_library.compute_question_count(data))
	counter=0
	for el in data:
		if isinstance(el,quiz_library.Answer) and type(el.result)!=int:
			continue
		if el.index!=counter:
			if start[counter]!=None:
				totals[counter]+=el.time-start[counter]
			counter=el.index
		if start[counter]==None:
			start[counter]=el.time
		if el==data[-1]:
			totals[counter]+=el.time-start[counter]
		
print ','.join(map(str,[float(i)/len(sys.argv[1:]) for i in totals]))

