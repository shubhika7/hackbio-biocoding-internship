import random
import pandas as pd

def translate_dna_to_protein(dna):
    """
    Translates a DNA sequence into a protein sequence based on the codon table.
    
    Parameters:
    dna (str): A string representing the DNA sequence.
    
    Returns:
    str: The corresponding protein sequence.
    """
    codon_table = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '*', 'TAG': '*',
        'TGC': 'C', 'TGT': 'C', 'TGA': '*', 'TGG': 'W'
    }
    protein = ""
    for i in range(0,len(dna)-2,3):
       codon = dna[i:i+3]
       protein += codon_table.get(codon,'?')
    
    return protein
       
# Example      
dna = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"   
print(translate_dna_to_protein(dna))

# Function to simulate logistic growth curve with all 4 phases    
def simulate_population_growth(K=1000, r=0.1, time_end=150, lag_variance=5, exp_variance=5, decline_start=120, decline_rate=0.2):
    """
    Simulates population growth through four phases: lag, exponential, stationary, and decline.
    
    Parameters:
    K (int): Carrying capacity of the environment.
    r (float): Growth rate.
    time_end (int): Total duration of simulation.
    lag_variance (int): Variation in lag phase duration.
    exp_variance (int): Variation in exponential phase duration.
    decline_start (int): Time when decline phase starts.
    decline_rate (float): Rate of decline phase.
    
    Returns:
    list: A list of dictionaries containing time and population values.
    """
    time = [t for t in range(time_end+1)]
   
    # Generate random lag and exponential phase durations
    lag_phase = random.uniform(0, lag_variance)
    exp_phase = random.uniform(0, exp_variance)
    
    population = [1]  # Initial population
    
    for t in range(1, time_end+1):
        prev_population = population[-1]
        
        # Lag phase: No growth
        if t < lag_phase:
            growth = 0
        # Exponential phase: Growth proportional to population
        elif t < lag_phase + exp_phase:
            growth = r * prev_population
        # Stationary phase: Growth limited by carrying capacity
        elif t < decline_start:
            growth = (r * prev_population) * (1 - prev_population / K)
        # Decline phase: Population decreases
        else:
            growth = -decline_rate * prev_population
        
        # Update population ensuring it doesn't go negative
        new_population = max(prev_population + growth, 0)
        population.append(new_population)
        
    return [{'Time': time[i], 'Population': population[i]} for i in range(len(time))]

# Function to generate multiple growth curves
def growth_curves(count=100):
    """
    Generates multiple logistic growth curves and stores them in a DataFrame.
    
    Parameters:
    count (int): The number of growth curves to generate.
    
    Returns:
    pd.DataFrame: A DataFrame containing the growth curves with a unique Curve_ID.
    """
    GrowthCurves = []
    for i in range(count):
        curve = simulate_population_growth()
        for point in curve:
            point['Curve_ID'] = i
        GrowthCurves.extend(curve)
    
    return pd.DataFrame(GrowthCurves)

# Generate the DataFrame
growth_curves_df = growth_curves()

# Display first few rows
print(growth_curves_df.head())

# Function to determine the time to reach 80% of the carrying capacity
def time_to_reach_80_percent(curve, K=1000):
    """
    Determines the time when the population reaches 80% of the carrying capacity.
    
    Parameters:
    curve (list): A list of dictionaries containing population data over time.
    K (int): Carrying capacity.
    
    Returns:
    int or None: The time step when population reaches 80% of K, or None if not reached.
    """
    threshold = 0.8 * K
    for point in curve:
        if point['Population'] >= threshold:
            return point['Time']
    return None

# Example
example_curve = simulate_population_growth()
time = time_to_reach_80_percent(example_curve)
print("Time to reach 80% of carrying capacity:", time)


# Function to calculate hamming distance 
def find_hamming_distance(str1, str2):
    """
    Calculates the Hamming distance between two equal-length strings.
    
    Parameters:
    str1 (str): First string.
    str2 (str): Second string.
    
    Returns:
    int: The number of differing positions between the two strings.
    
    Raises:
    ValueError: If the strings are not of equal length.
    """
    if len(str1) != len(str2):
        raise ValueError("Strings must be of equal length")
    
    hamming_dist = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            hamming_dist += 1
    return hamming_dist

# Example usage
slack_username = "shubhika35"
twitter_handle = "shubh28435"
print(find_hamming_distance(slack_username, twitter_handle))

        


    
