import re   #regular expressions
import sys  #system (Mainly for sys.exit)
import math

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
        self.map_new = set()

    
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
                        self.map_old[i] = j
                        self.map_new.add(j)
                        #
                        old_set.add(i)
                        break
                        #This catches all of the unchanged lines in the LCS



        

    #(Step 3)
    # Generate Candidate List
    # Using Content and Context from Levenshtein Distance and Cosine Similarity


    #Levenshtein Distance
    #Computing the levenshtein similarity for two lines/strings
    #Allows us to obtain the content similarity for our files and their code lines

    def levenshtein_distance(self, line1, line2):
        #Catching Equal lines 
        if line1 == line2:
            return 1.0
        
        #Getting the length of the lines
        len1 = len(line1)
        len2 = len(line2)

        #If either string is empty return 0
        if len1 == 0 or len2 == 0:
            return 0.0
        
        #Creating a 2D array (matrix) to store our distances
        #dynamic programming approach to obtaining the LD
        matrix = [[0] * (len2 + 1) for i in range(len1 + 1)] 
        #This creates an empty matrix of zeros with columns and rows equal to our lengths + 1


        #Filling in the first column and row of our matrix (with our strings)
        for i in range (len1 +1):
            matrix[i][0] = i
        for j in range (len2 + 1):
            matrix[0][j] = j

        # Fill matrix with our 
        for i in range (1, len1 + 1):
            for j in range(1, len2 + 1):
                #Calculate our cost from the two prior characters
                #0 if not change is need (same chars), 1 if change is needed (diff chars)
                cost = 0 if line1[i - 1] == line2[j - 1] else 1
                #Get the minimum of the three possible cases, 
                #which gives us the best way to traverse from line1[i-1] to line2[j-1]
                #place this minimum in our matrix
                matrix[i][j] = min(
                    matrix[i - 1][j] + 1,       # Deletion - deleting the char
                    matrix[i][j - 1] + 1,       # Insertion - inserting the char
                    matrix[i - 1][j - 1] + cost # Substitution - swapping the char
                )
        
        return matrix[len1][len2]   #Obtain our levenshtein distance form the matrix


    #Cosine Similarity
    #Computing the cosine similarity for two strings - consisting of 9 lines (4 before and 4 after)
    #Allows us to obtain the context similarity for our files and their code lines

    def cosine_similarity(self, text1, text2):
        #extract tokens from the given strings (which contain 9 lines)
        token1 = re.findall(r'\w+', text1)
        token2 = re.findall(r'\w+', text2)

        #Edge cases
        #Check if the tokens are identical
        if not token1 and not token2: return 1.0
        #Check if they are completely different
        if not token1 or not token2: return 0.0

        #Using sets, obtain all of the overlap from our 2 strings
        words = set(token1).union(set(token2))

        # 2 frequencies - one for each string
        freq1 = {w: 0 for w in words}
        freq2 = {w: 0 for w in words}
        # get the frequencies of our overlapping words from each string
        for w in token1:
            #gets the frequency (times the word appears) of the words in our set
            #as they appear in the string list token1
            freq1[w] += 1
        for w in token2:
            #same for token2
            freq2[w] += 1

        # Dot Product of our frequencies
        dot_product = sum(freq1[w] * freq2[w] for w in words)

        # Magnitudes - magnitude of each vector for the cosine sim algorithm
        mag1 = math.sqrt(sum(v**2 for v in freq1.values()))
        mag2 = math.sqrt(sum(v**2 for v in freq2.values()))

        # If either are zero, return 0 to not get a dividebyzero error
        if mag1 == 0 or mag2 == 0:
            return 0.0
        # Otherwise we return the cosine similarity
        return dot_product/ (mag1 * mag2)
        

    #(unfinished)
    # run: runs the previously defined functions
    # This is where all of the steps culminate (For LHDiff)
    def run(self):
        #TODO
        # (Step 1) Pre-processing: Should happen in the individual functions when line processing is needed

        # (Step 2) Check for unchanged lines

        #Run the Unix Diff here

        # (Step 3) Generate Candidates

        #Uses Levenshtein Distance and Cosine Similarity to check the content and context of the map

        # (Step 4) - Conflict Resolution  

        # Should just consist of ensuring the mapped candidates are 1-1 

        # (Step 5) - Detecting Line Splits

        #Use the levenshtein distance for a line, and it's next line to see if the similarity increased - if so, we get lines splits
        
        return

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
def generate_xml(old_file_name, new_file_name, test_num):
    #TODO
    #Need to change this to file output rather than print
    print(f'TEST NAME="TEST{test_num}" FILE1="{old_file_name}" FILE2="{new_file_name}">"')
    #For now output to terminal





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
    Files1 = ["asdf_1.java","asdf_2.java"]   
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
        