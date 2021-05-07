from Exam4 import *

#Test for count_kmers function

def test_count_kmers_1():
    k = 9
    sequence = 'ATTTGGATT'
    
    out_obs, out_possible = count_kmers(k, sequence)
    
    x_out_obs, x_out_possible = 1, 1
    
    assert ((out_obs == x_out_obs) & (out_possible == x_out_possible))
    
def test_count_kmers_2():
    k = 11
    sequence = 'AGACATTGACC'
    
    out_obs, out_possible = count_kmers(k, sequence)
    
    x_out_obs, x_out_possible = 1, 1
    
    assert ((out_obs == x_out_obs) & (out_possible == x_out_possible))
    
#Test functions that create the data frame

def test_create_k_pd_1():
    k = 9
    sequence = 'ATTTGGATT'
    
    total_obs, total_possible, out_df = create_k_pd(k, sequence)
    
    x_total_obs, x_total_possible = 35, 40
    
    k_list = list(range(k+1))[1:]
    observed_k_list = [3, 5, 6, 6, 5, 4, 3, 2, 1]
    possible_k_list = [4, 8, 7, 6, 5, 4, 3, 2, 1]
    
    d = {'k': k_list, 'Observed kmers': observed_k_list, 'Possible kmers': possible_k_list}
    df = pd.DataFrame(data=d)
    
    df_match = out_df.equals(df)
    
    assert ((total_obs == x_total_obs) & (total_possible == x_total_possible) & df_match)
    
def test_create_k_pd_2():
    k = 11
    sequence = 'AGACATTGACC'
    
    total_obs, total_possible, out_df = create_k_pd(k, sequence)
    
    x_total_obs, x_total_possible = 56, 59
    
    k_list = list(range(k+1))[1:]
    observed_k_list = [4, 8, 8, 8, 7, 6, 5, 4, 3, 2, 1]
    possible_k_list = [4, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    
    d = {'k': k_list, 'Observed kmers': observed_k_list, 'Possible kmers': possible_k_list}
    df = pd.DataFrame(data=d)
    
    df_match = out_df.equals(df)
    
    assert ((total_obs == x_total_obs) & (total_possible == x_total_possible) & df_match)
    
#Test the method that calculates linguistic complexity

def test_calc_ling_complex_1():
    k = 9
    sequence = 'ATTTGGATT'
    
    out_lc, out_df = calc_ling_complex(k, sequence) 
    
    k_list = list(range(k+1))[1:]
    observed_k_list = [3, 5, 6, 6, 5, 4, 3, 2, 1]
    possible_k_list = [4, 8, 7, 6, 5, 4, 3, 2, 1]
    
    d = {'k': k_list, 'Observed kmers': observed_k_list, 'Possible kmers': possible_k_list}
    df = pd.DataFrame(data=d)
    
    df_match = out_df.equals(df)
    
    assert ((out_lc == 0.875) & df_match)
    
    
def test_calc_ling_complex_2():
    k = 11
    sequence = 'AGACATTGACC'
    
    out_lc, out_df = calc_ling_complex(k, sequence) 
    
    k_list = list(range(k+1))[1:]
    observed_k_list = [4, 8, 8, 8, 7, 6, 5, 4, 3, 2, 1]
    possible_k_list = [4, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    
    d = {'k': k_list, 'Observed kmers': observed_k_list, 'Possible kmers': possible_k_list}
    df = pd.DataFrame(data=d)
    
    df_match = out_df.equals(df)
    
    assert ((out_lc == 0.9491525423728814) & df_match)
