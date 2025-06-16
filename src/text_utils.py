import csv

#change mode to 'a' when ready to deploy
#writer.writeheader() if needed for writing a header

def save_to_csv(jobs):
    with open('data/postings.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'company', 'link'])
        for j in jobs:
            writer.writerows(j)
