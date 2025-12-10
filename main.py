import re   #regular expressions
import sys  #system (Mainly for sys.exit)
import math
import os   #folder and os manipulation

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
        #The list of mapped indices is a set to ensure 1-1 mapping
        self.mapped_indices = set()  


    
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
                if i not in old_set and j not in self.mapped_indices:
                    #If the lines are identical (ie. all of their letters match)
                    if self.old_lines[i] == self.new_lines[j]:
                        #Saving line numbers in our mapping
                        self.map_old[i] = j
                        self.mapped_indices.add(j)
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
        #Added normalization
        lev_dist = matrix[len1][len2]   # Obtain our levenshtein distance form the matrix
        max_len = max(len1, len2)       # Get the maximum between our two lines
        #Return the similarity score of the normalized levenshtein distance
        return 1.0 - (lev_dist/max_len)    


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
        
    # get_context:
    # Additional method for obtaining context for the cosine similarity method
    def get_context(self, lines, index):
        context_size = 4 

        #Our context start is 4 below the current index (if its with bounds)
        if index - context_size <= 0: start_index = 0
        else: start_index = index - context_size  
        #Our context end is 4 above the current index
        if index + context_size >= len(lines): end_index = len(lines)
        else: end_index = index + context_size

        context_lines = []  #list of context 
        for i in range(start_index, end_index):
            # Exclude the centre/given index (possibly remove)
            if i == index: continue
            # Every other index (+4 and -4 of the given index) is added
            context_lines.append(self.process_line(lines[i]))   #These lines are also processed
        return " ".join(context_lines) # Returning the context as one large string for cosine similarity


    # (NEEDS REVIEW) - has all 5 steps, but needs overview and testing
    # run: runs the previously defined functions
    # This is where all of the steps culminate (For LHDiff)
    def run(self):
        # (Step 1) Pre-processing: Should happen in the individual functions when line processing is needed

        # (Step 2) Check for unchanged lines
        self.unix_diff()

        # (Step 3) Generate Candidates
        # Get our changed lines (ie. lines note detected in step 2)
        # These lists contain all unmapped indices from the old and new sources
        unmap_old = [i for i in range(len(self.old_lines)) if i not in self.map_old]
        unmap_new = [j for j in range(len(self.new_lines)) if j not in self.mapped_indices]

        # Obtain and process (Step 1) our lines using the prior mappings
        processed_old = {i: self.process_line(self.old_lines[i]) for i in unmap_old}
        processed_new = {j: self.process_line(self.new_lines[j]) for j in unmap_new}

        #List of candidate lines - will contain the location of the line in both old and new files as well as it's score
        candidate_lines = []

        for i in unmap_old:
            old_line = processed_old[i] #Get our processed line from the list
            context_old = self.get_context(self.old_lines,i) #get the context of that line

            for j in unmap_new:
                new_line = processed_new[j]

                #Check content similarities (Levenshtein distance)
                content_sim = self.levenshtein_distance(old_line,new_line)

                #Consider matches with higher similarity
                if content_sim < 0.5:
                    continue

                #Check context similarities
                context_new = self.get_context(self.new_lines,j)
                context_sim = self.cosine_similarity(context_old,context_new)

                # Combine the score of our content and context
                sim_score = 0.6 * content_sim + 0.4 * context_sim

                #Similarity threshold needed to consider lines the same
                sim_threshold = 0.7     # Might need changing
                if sim_score >= sim_threshold:
                    candidate_lines.append({
                        'old_index': i,
                        'new_index': j,
                        'score': sim_score
                    })

        # (Step 4) - Conflict Resolution        
        # sort candidates by score (descending order by score)
        # might need to change sorting pattern, and move this into a seperate function

        candidate_lines.sort(key=lambda c: c['score'], reverse=True)


        for candidate in candidate_lines:
            #Get the indices of the old and new lines for the candidate
            old_id = candidate['old_index']
            new_id = candidate['new_index']
            #If both lines are unmapped, that means we have a line change/movement
            if old_id not in self.map_old and new_id not in self.mapped_indices:
                self.map_old[old_id] = new_id   #Old line mapped to new line
                self.mapped_indices.add(new_id)  #New line is also 'taken' and can't be remapped (ensures 1-1)

        # (Step 5) - Detecting Line Splits

        #If adding more lines to our context increases similarity,
        #then it makes sense that it is a line split
        #(Also move this into another func)

        sorted_old = sorted(self.map_old.keys())    #sort our old lines (putting them in order)
        for old_index in sorted_old:
            new_index = self.map_old[old_index]

            #Checking if the next line is unmapped (and exists)
            next_index = new_index + 1
            if next_index < len(self.new_lines) and next_index not in self.mapped_indices:
                #Process and obtain the lines of our indexes
                old_line = self.process_line(self.old_lines[old_index])
                new_line = self.process_line(self.new_lines[new_index])

                #Lev Distance without adding the next index (pre-combine)
                lev_dist = self.levenshtein_distance(old_line,new_line)

                #Combined String
                combine_line = new_line + " " + self.process_line(self.new_lines[next_index])

                #Lev Distance of combined string
                lev_dist_combine = self.levenshtein_distance(old_line,combine_line)

                #If the combined has a greater similarity score, we consider it a line split
                if lev_dist_combine > lev_dist:
                    #Add the index to our mapping
                    self.mapped_new_indices.add(next_index)

        return self.map_old
    






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



# generate_xml: XML Output Generation for the  
# Eventually this will generate our XML output showing the line differences
# using the given filenames
def generate_xml(old_file_name, new_file_name, test_num):
    #TODO
    #Need to change this to file output rather than print
    print(f'TEST NAME="TEST{test_num}" FILE1="{old_file_name}" FILE2="{new_file_name}">"')
    
    #Write out each of the matched lines here (Prof's xml files only show changed lines it seems)



# compare_files: compares files from a given folder, 
# This is where everything comes together, allowing us to use LHDiff on 2 files
# in our folders using the main method and this method
def compare_files(folder, file_group):
    #Get the information from the file group
    base_name = file_group['base_name']
    extension = file_group['extension']
    num_versions = file_group['versions']

    # Obtain all of the filepaths from the file group
    file_paths = []
    for version in range(1, num_versions + 1):
        filename = f"{base_name}_{version}{extension}"  #Recreate the filename
        full_path = os.path.join(folder, filename)      #Add the folder to the filepath
        file_paths.append((version, filename, full_path))#Add the full path to the list

    #Obtain the file information/content using our get_file method
    comparison_results = []

    #TODO
    #Now that LHDiff is (mostly) complete, we can complete the file comparison (and actually output properly)


    #Generate XML output



# get_file_groups:
# Helper method that obtains file groups from the given folder
# Example 'asdf_1.java' 'asdf_2.java' are stored in a file group 'asdf.java' which is the key
def get_file_groups(folder):

    #Ensure the folder exists
    if not os.path.exists(folder):
        print(f"Warning: Folder '{folder}' does not exist")
        return {}
    #Get all of the files in the folder
    folder_files = os.listdir(folder)

    #Exclude the xml files since they're output files
    valid_files = []
    for file in folder_files:
        #Skip the xml files
        if file.endswith('.xml') or file.endswith('.xml~'):
            continue
        valid_files.append(file)

    #using dictionary to group files by their names
    file_groups = {}

    for filename in valid_files:
        #Using regex to match our files with the same names
        #This regex finds strings of the format 'filename_number.extension'
        filename_match = re.match(r'^(.+?)_(\d+)(\..+)$',filename)

        #Match returns a list of strings matching the sections of our regex, so as long as it returned a list
        #We can extract our filename components from it
        if filename_match:
            #Getting the filename components (version number isn't needed)
            base_name = filename_match.group(1)
            extension = filename_match.group(3)

            #Dictionary keys are their filenames without the '_number'
            key = f"{base_name}{extension}"

            if key not in file_groups:
                #New key if it isn't already in the dictionary
                file_groups[key] = {
                    'base_name': base_name,
                    'extension': extension,
                    'versions': 1
                }
            else:
                #Increase the number of versions by 1 every time we detect another file with this name and extension
                file_groups[key]['versions'] += 1
            #Number of versions is kept in the dictionary with their number and full filename
            
    #Remove files with one version (ie. files that don't have anything to compare to) 
    valid_file_groups = {k: v for k, v in file_groups.items() if v.get('versions', 0 ) >= 2}
    return valid_file_groups



# Main execution, actually runs the code
if __name__ == "__main__":

    #   Folders for testing
    test_folders = ["EvalTest","GroupTest"]

    #   File Groups obtained from the folders
    file_groups = []

    # Getting file groups for each folder
    for folder in test_folders:
        file_groups.append(get_file_groups(folder))
        
    print(file_groups)

    


    


