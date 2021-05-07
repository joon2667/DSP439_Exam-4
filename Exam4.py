import random
import pandas as pd

# Function to achieve goal from question #1. Counts kmers of size k.
# Returns both the observed number of kmers for each k as well as the
# theoretically possible number of kmers for that given k. Takes in the k and
# sequence currently being processed as its inputs.
def count_kmers(k, sequence):
  #Possible kmers
  #4 if the k value is 1, else use the formula given in the sheet  
  if k == 1:
      possible_k = 4
  else:
      possible_k = len(sequence)+1-k
      
  #Observed kmers
  observed_k = set()
  
  #check_times tells us the number of times we will need to iterate through 
  #a squence checking k number of characters
  if k == 1:
      check_times = len(sequence)
  else:
      check_times = possible_k
      
  #Iterate through the sequences comparing every k characters to see if it is
  #unique by adding it to the set    
  for i in range(0, check_times):
      observed_k.add(sequence[i:i+k])
      
  #Return both the observed number of kmers as wel as the possible value    
  return len(observed_k), possible_k
  
# Function to achieve goal from question number 2. Processes all the observed
# and possible kmers for each k value and then aggregates them into a pandas
# dataframe.
def create_k_pd(k, sequence):
  
  k_list = list(range(k+1))[1:]
  observed_k_list = []
  possible_k_list = []
  
  #Generate a list for each column of values so that they can be displayed
  #in the table
  
  #Call the count_kmers() method on each k value and store in appropriate list
  for i in range(k):
      temp_observed_k, temp_possible_k  = count_kmers(i+1, sequence)
      observed_k_list.append(temp_observed_k)
      possible_k_list.append(temp_possible_k)
  
  #Create pandas dataframe with all the required data that was just calculated      
  d = {'k': k_list, 'Observed kmers': observed_k_list, 'Possible kmers': possible_k_list}
  df = pd.DataFrame(data=d)
  print(df)
  
  #Return the sum of the total observed kmers and the total possible kmers
  return sum(observed_k_list), sum(possible_k_list), df
  
# Function to achieve the goal defined in question 3 which is to calculate the
# linguistuc complexity, which involves dividing the total number of observed
# kmers with the total number of theoretically possible kmers.
def calc_ling_complex(k, sequence):
    #Use the sums of the total observed kmers and the total possible kmers to
    #calculate the linguistic complexity
    temp_o, temp_p, df = create_k_pd(k, sequence)
    
    return (temp_o/temp_p), df
  

#Main function used to generate results for each string
def main():
  #Read in the sequences file and create an output file to post values
  f = open("test_sequences.txt", "r")
  #g = open("linguistic_complexities.txt", "w")
  
  #Iterate through every line in the sequences file and calculate the
  #linguistic complexity for it. Then write that value into the output file
  #along with a message of what sequence that value belongs to.
  for line in f:
      print()
      number, df = calc_ling_complex(len(line.split()[0]), line.split()[0])
      message = "The linguistic complexity for " + line.split()[0] + " is: "
#      g.write(message+str(number))
#      g.write("\n")
      
      #For each sequence, make a seperate text file that contains the data frame
      tfile = open(line.split()[0]+".txt", 'w')
      tfile.write(message+str(number))
      tfile.write("\n")
      tfile.write(" ")
      tfile.write("\n")
      tfile.write("Pandas Dataframe of Observed and Possible kmers: ")
      tfile.write("\n")
      tfile.write(" ")
      tfile.write("\n")
      tfile.write(df.to_string())
      tfile.write("\n")
      tfile.close()

  f.close()
  #g.close()
      
main()
