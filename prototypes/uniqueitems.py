import csv

def unique_items_from_csv(filename):
    unique_items = set()
    
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        
        # skip header if it exists
        header = next(reader, None)
        
        for row in reader:
            for item in row:
                if item.strip():  # ignore empty cells
                    unique_items.add(item.strip())
    
    return unique_items

if __name__ == "__main__":
    filename = "recipes.csv"  # replace with your csv filename
    items = unique_items_from_csv(filename)
    print("Unique items found:")
    for item in sorted(items):
        print(item)
