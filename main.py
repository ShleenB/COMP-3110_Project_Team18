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
    # This is where all of the steps culminate (For LHDiff)
    #def run(self):
        
        



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
    #Use LHdiff

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