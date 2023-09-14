import argparse
import time
from utils.pickdeal import tien_xu_li, read_data, PickDealPromptify


def args_fn():
    parser = argparse.ArgumentParser(description="NER for Pickdeal")
    parser.add_argument("-ip", "--input_file", required=True, type=str)
    parser.add_argument("-op", "--output_file", required=False, type=str)
    parser.add_argument("-key", "--openai_key", required=False, type=str,
                        default="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")
    args = parser.parse_args()
    return args


def labeling(texts, openai_key):
    pickdeal_promp = PickDealPromptify(
        openai_key=openai_key,
        path_file_jinja=f"pickdeal.jinja"
    )
    for text in texts:
        result = pickdeal_promp(sentence=text)
        print(result)


def run(args):
    data = read_data(file=args.input_file)
    labeling(
        texts=data["processed_text"].tolist(),
        openai_key=args.openai_key
    )


if __name__ == '__main__':
    args = args_fn()
