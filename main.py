import re   #regular expressions
import sys  #system (Mainly for sys.exit)

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
        #The list of new indices is a set so that we don't match to multiple old lines
        self.map_new = set()    #Changed to set



    
    #(Step 1)
    # process_line: proccesor for the lines of the old/new files, 
    def process_line(self, line):
        #strip the line and make it lowercase
        line = line.strip().lower()
        #Using regex to find all tokens in our line list 
        tokens = re.findall(r'\w+', line)
        #return the string of our joined and processed line
        return " ".join(tokens)
    
    #(Step 2)
    #Unix Diff Algorithm - get unchanged lines with longest common subsequence
    #We run this on the un-processed lines to not skew our line change mapping
    def unix_diff(self):
        #length of old and new files
        old_len = len(self.old_lines)
        new_len = len(self.new_lines)

        #Using sets (which don't have duplicates)
        #This set tracked which lines we've already matched, to prevent duplication
        old_set = set()

        #Map all of the exact matches
        for i in range(old_len):
            for j in range(new_len):
                #Ensure we haven't already matched them
                if i not in old_set and j not in self.map_new:
                    #If the lines are identical (ie. all of their letters match)
                    if self.old_lines[i] == self.new_lines[j]:
                        #Saving line numbers in our mapping
                        self.map_old = j
                        self.map_new.add(j)
                        #
                        old_set.add(i)
                        break
                        #This catches all of the unchanged lines in the LCS



        

    #(Step 3)
    # Generate Candidate List
    #def levenshtein_distance():
        #TODO
    #def cosine_similarity():
        #TODO

    #(Step 3)
    #def get_

    #(unfinished)
    # run: runs the previously defined functions
    # This is where all of the steps culminate (For LHDiff)
    def run(self):
        

        #Check for unchanged lines
        self.unix_diff()


        



# get_file: attempts to read a given filepath
def get_file(filepath):
    #tries to open the file in read mode, returning the whole file as a string
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    #If the file isn't found we can output this message
    except FileNotFoundError:
        print(f"Error: File not found - {filepath}")
        sys.exit(1)
    #If it's another type of error, we output this message
    except Exception as e:
        print(f"Error: Reading file {filepath}: {e}")
        sys.exit(1)
    #In both errors we exit the system since we can't continue

#(unfinished)
# generate_xml: XML Output Generation for the  
# Eventually this will generate our XML output showing the line differences
# using the given filenames
def generate_xml(old_file_name, new_file_name):
    #TODO
    #Need to change this to file output rather than print
    print(f'TEST NAME="File Comparison" FILE1="{old_file_name}" FILE2="{new_file_name}">"')
    LHDiff()




#   (Unfinished)
# compare_files: compares files from a given folder, 
# This is where everything comes together, allowing us to use LHDiff on 2 files
# in our folders using the main method and this method
def compare_files(folder, file1, file2):
    #Get the path to the files by joining the folder name and filenames
    file_path1 = "".join((folder,"/",file1))
    file_path2 = "".join((folder,"/",file2))

    print("Comparing Files: ")
    print(f"\tOld: {file_path1}")
    print(f"\tNew: {file_path2}")

    #Obtain the file information/content using our get_file method
    old_file = get_file(file_path1)
    new_file = get_file(file_path2)

    #TODO
    #Use LHdiff (needs implementation after LHDiff is completed)

    #Generate XML output


# Main execution, actually runs the code
if __name__ == "__main__":

    #   Folders for testing
    Folder1 = "EvalTest"    # Given Test Case Folder
    Folder2 = "GroupTest"   # Folder of Test Cases made by our group
    #Files in first folder
    Files1 = ["ArrayReference_1.java","ArrayReference_2.java"]   
    #Files in second folder
    Files2 = []

    #   Ensure there's even indexes
    if len(Files1)%2==0 and len(Files2)%2==0:
        #First folder
        for i in range(0,len(Files1),2):
            compare_files(Folder1,Files1[i],Files1[i+1])
        #Second folder
        for i in range(0,len(Files2),2):
            compare_files(Folder2,Files2[i],Files2[i+1])
    else:
        print("Error: Uneven indices in file list")
        sys.exit(1)
        