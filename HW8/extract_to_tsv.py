import json
import argparse
import random

def get_json(outputfile, inputfile, num_posts):
    with open(inputfile, 'r') as jsondata:
        posts = json.load(jsondata)

    number_posts = int(num_posts)

    with open(outputfile, 'w') as tsv:
        tsv.write(f'Name\tTitle\tCoding\n')

        if number_posts>=len(posts['data']['children']):
            for post in posts['data']['children']:
                name = post['data']['name']
                title = (post['data']['title'])
                tsv.write(f'{name}\t{title}\t\n')
        else:
            post_indices = random.sample(range(len(posts['data']['children'])), number_posts)
            for i in post_indices:
                post = posts['data']['children'][i]
                name = post['data']['name']
                title = (post['data']['title'])
                tsv.write(f'{name}\t{title}\t\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', required=True, help='output tsv file name')
    parser.add_argument('inputfile')
    parser.add_argument('num_posts')
    args = parser.parse_args()
    get_json(args.output, args.inputfile, args.num_posts)