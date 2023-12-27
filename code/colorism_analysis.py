import json
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def main():
    comments_raw_json_1 = open('comments.json')
    comments_raw_json_2 = open('comments_2.json')
    user_data_raw_json_1 = open('user_data.json')
    user_data_raw_json_2 = open('user_data_2.json')

    comments_json_1 = json.load(comments_raw_json_1)
    comments_json_2 = json.load(comments_raw_json_2)
    user_data_json_1 = json.load(user_data_raw_json_1)
    user_data_json_2 = json.load(user_data_raw_json_2)

    users = user_data_json_1['result'] + user_data_json_2['result']
    comments = comments_json_1 + comments_json_2

    maxRating = dict()
    for user in users:
        try:
            maxRating[user['handle']] = user['maxRating']
        except:
            maxRating[user['handle']] = 0

    user_ratings = []
    comment_ratings = []
    for comment in comments:
        x = maxRating[comment['commentatorHandle']]
        y = comment['rating']
        if x != 0 and abs(y) >= 50 and abs(y) <= 300:
            user_ratings.append(x)
            comment_ratings.append(y)
    """
    coefficients = np.polyfit(user_ratings, comment_ratings, 1)
line = np.poly1d(coefficients)

    line_x = np.linspace(min(user_ratings), max(user_ratings), 100)
line_y = line(line_x)

    plt.plot(line_x, line_y, color='red', label='Regression Line')

plt.scatter(user_ratings, comment_ratings)
    plt.xlabel('Commentator Max Rating')
    plt.ylabel('Comment Vote Rating')
    plt.title('UserMaxRating-CommentRating Scatter Plot')
    """
# Create a scatter plot
    plt.scatter(user_ratings, comment_ratings, label='Data points')

# Perform linear regression
    slope, intercept, r_value, p_value, std_err = linregress(user_ratings, comment_ratings)
    line = np.poly1d([slope, intercept])

# Generate x values for the line of best fit
    line_x = np.linspace(min(user_ratings), max(user_ratings), 100)
    line_y = line(line_x)

# Plot the regression line
    plt.plot(line_x, line_y, color='red', label='Regression Line')

# Add labels and title
    plt.xlabel('User Ratings')
    plt.ylabel('Comment Ratings')
    plt.title('CommentRatings-UserMaxRatings Scatter Plot with Regression Line')

# Show legend
    plt.legend()
    plt.savefig('colorism_illustration.png')

if __name__ == '__main__':
    main()
