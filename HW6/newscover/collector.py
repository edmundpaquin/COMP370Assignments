import argparse
import json 
import os 
from newscover.newsapi import fetch_latest_news

#python -m newscover.collector -k <api_key> [-b <# days to lookback>] -i <input_file> -o <output_dir>

def fetch_save_news(api_key, keywords, lookback_days, output_dir):
    articles = fetch_latest_news(api_key, keywords, lookback_days)
    keyword_string = "_".join(keywords)
    output_filename = os.path.join(output_dir, f"{keyword_string}_articles.json")

    with open(output_filename, 'w') as f:
        json.dump(articles, f, indent=4)

def main(api_key, lookback_days, input_file, output_dir):
    with open(input_file, 'r') as f:
        keyword_dict = json.load(f)

    for name, keywords in keyword_dict.items():
        print("name", name, "keywords", keywords)
        fetch_save_news(api_key, keywords, lookback_days, output_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--api_key', type=str, required=True, help='API key')
    parser.add_argument('-b', '--lookback_days', type=int, default=10, help='lookback_days')
    parser.add_argument('-i', '--input_file', type=str, required=True, help='input')
    parser.add_argument('-o', '--output_dir', type=str, required=True, help='output')

    args = parser.parse_args()

    main(args.api_key, args.lookback_days, args.input_file, args.output_dir)