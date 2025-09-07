from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.

print(products)

# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.

customer_preferences = []

response = "Y"
while response != "N":
    if response == "Y" or response == "YES":
        print("Input a preference:")
        preference = input()
        customer_preferences.append(preference)
        print(customer_preferences)
        response = input("Do you want to add another preference? (Y/N): ").upper()
    else:
        response = input("Sorry I don't understand. Do you want to add another preference? (Y/N): ").upper()
  

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_preferences_set = set(customer_preferences)
print(customer_preferences_set)
# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []
for product in products:
    converted_product = {
        "name": product["name"],
        "tags": set(product["tags"])
    }
    converted_products.append(converted_product)

print(converted_products)
# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    return len(product_tags & customer_tags)




# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    matches = []
    for product in products:
        match_count = count_matches(product["tags"], customer_tags)
        matches.append({"name": product["name"], "match_count": match_count})
    sorted_matches = sorted(matches, key=lambda x: x["match_count"], reverse=True)
    return sorted_matches



# TODO: Step 7 - Call your function and print the results
print("Recommended Products:")
for match in recommend_products(converted_products, customer_preferences_set):
    if match["match_count"] > 0:
        print(f"- {match['name']} ({match['match_count']} match(es))")


''' DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
     I used loops to iterate over the products and customer preferences, and set intersections to find matching tags. 
     Loops are essential for processing each item in a list, while set intersections provide an efficient way to identify common elements between two sets.
     I also used functions to encapsulate the logic for counting matches and recommending products, which improves code organization and reusability.
     Another core operation was sorting the matches based on the number of matches, which helps prioritize products that align closely with customer preferences.
# 2. How might this code change if you had 1000+ products?
     If there were 1000+ products, I would consider optimizing the data structure for faster lookups, such as using a database or indexing system. 
     Additionally, I might implement caching mechanisms to store frequently accessed recommendations and reduce computation time.
     I would also consider limiting the number of recommendations returned to the user to improve performance and user experience.
     Another approach could be to implement pagination or lazy loading to handle large datasets more efficiently.'''
