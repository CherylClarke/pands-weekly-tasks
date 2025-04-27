# first got moby-dick.txt file from 
# Reference :https://gist.github.com/StevenClontz/4445774
# put in pands weekly tasks folder so it can be accessed here

# now i must write a program that reads in a txt file

import sys
# now to count the es from the txt file in question
def count_es(filename):
   
    try:
        with open(filename, 'r') as file:
            content = file.read()
            e_count = content.lower().count('e')
        return e_count
    # if cant find file print below
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    # if cant find variable (e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python count_es.py filename.txt")
        sys.exit(1)

    filename = sys.argv[1]
    e_count = count_es(filename)
# if count is anything above none print, "file name"moby_dick.txt" ,contain "e count" and "e" characters"
    if e_count is not None:
        print(f"The file '{filename}' contains {e_count} 'e' characters.")

if __name__ == "__main__":
    main()


#Reference: - prompt- how to download moby-dick.txt file from github repo https://chatgpt.com/c/680e761e-0d4c-8003-8711-ad44b4b72061

#Reference: https://gist.github.com/StevenClontz/4445774

#