# Load the list of racial slurs
with open('racial_slurs.txt') as f:
    racial_slurs = set([line.strip() for line in f])

# Open the input file
with open('tweets.txt') as f:
    for line in f:
        tweet = line.strip()

        # Count the number of racial slurs in the tweet
        num_racial_slurs = sum([1 for word in tweet.split() if word.lower() in racial_slurs])

        # Calculate the degree of profanity based on the number of racial slurs
        if num_racial_slurs == 0:
            profanity_degree = 'Clean'
        elif num_racial_slurs == 1:
            profanity_degree = 'Mild'
        elif num_racial_slurs == 2:
            profanity_degree = 'Moderate'
        else:
            profanity_degree = 'Severe'

        # Output the results
        print(f'{tweet}: {profanity_degree}')
