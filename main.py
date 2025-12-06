import re #regular expressions

"""
Project Code
Team 18
    Collin Brown
    Ahmad Arain
    Hashir Khan
    Yousef Al-Wahami
    Jacob Dam
"""
  
#LHDiff Steps
#Step 1: Preprocessing
#Step 2: Detect Unchanged Lines
#Step 3: Generate Candidates
#Step 4: Resolve Conflict
#Step 5: Detect Line Splits
#Then evaluate/output

# Main LHDiff Class
# This will perform the LHDiff algorithm on an old file and new file
class LHDiff:
    # Initializer for LHDiff (Constructor)
    def __init__(self, old_src, new_src):
        #Save the split lines of the old and new sources
        self.old_lines = old_src.splitlines()
        self.new_lines = new_src.splitlines()

        #Mapping lists for which old lines will match the new lines
        self.map_old = {}
        self.map_new = {}

    
    #(Step 1)
    # process_line: proccesor for the lines of the old/new files, 
    def process_line(self, line):
        #strip the line and make it lowercase
        line = line.strip().lower()
        #Using regex to find all tokens in our line list
        #This will also get rid of special characters
        tokens = re.findall(r'\w+', line)
        #return the string of joined, processed lines
        return " ".join(tokens)

    
    #(unfinished)
    # run: runs the previously defined functions
    # This is where all of the steps culminate
    #def run(self):
        
        


#(unfinished)
# XML Output Generation 
# Eventually this will generate our XML output showing the line differences
# using the given filenames
def generate_xml(test_name, file_name, old_file_name, new_file_name):
    track_str = LHDiff(old_file_name,new_file_name)
