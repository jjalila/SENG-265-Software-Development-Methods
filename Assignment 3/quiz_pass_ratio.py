import libxml2
import sys
import quiz_library

'''
purpose
	Accept 1 or more log file names on the command line.

	Accumulate across all the log files the pass ratio for each question.

	A question result is considered a pass if it is not 0 or None
	and fail otherwise.

	The pass ratio for a question is the number of passes
	divided by the number of passes + fails.
preconditions
	Each command-line argument is the name of a
	readable and legal quiz log file.

	All the log_files have the same number of questions.
'''

# check number of command line arguments
if len(sys.argv) < 2:
	print 'Syntax:', sys.argv[0], 'quiz_log_file ...'
	sys.exit()

ls=[]
lspass=[]

for f in sys.argv[1:]:
	marks=quiz_library.compute_mark_list(quiz_library.load_quiz_log(f))
	if not ls:
		ls=[0]*len(marks)
		lspass=[0]*len(marks)
	for i,j in enumerate(marks):
		if j:
			lspass[i]+=1
		ls[i]+=1

ls=[str(i/float(j)) for i,j in zip(lspass,ls)]

print ','.join(ls)
