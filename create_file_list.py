import os
import argparse
import random


def create_or_append_train_val_txt(data_root, train_percentage, output_dir='filelists'):
    directories = [d for d in os.listdir(data_root) if os.path.isdir(os.path.join(data_root, d))]
    random.shuffle(directories)

    train_count = int(len(directories) * train_percentage)

    train_directories = directories[:train_count]
    val_directories = directories[train_count:]

    train_file = os.path.join(output_dir, 'train.txt')
    val_file = os.path.join(output_dir, 'val.txt')

    train_file_exists = os.path.exists(train_file)
    val_file_exists = os.path.exists(val_file)

    with open(train_file, 'a' if train_file_exists else 'w') as f:
        if train_file_exists:
            f.write('\n')
        for directory in train_directories:
            f.write(directory + '\n')

    with open(val_file, 'a' if val_file_exists else 'w') as f:
        if val_file_exists:
            f.write('\n')
        for directory in val_directories:
            f.write(directory + '\n')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Create or append to train.txt and val.txt files from a directory of directories.')
    parser.add_argument('--data_root', required=True,
                        help='Path to the directory containing subdirectories for each example.')
    parser.add_argument('--output_dir', default='filelists',
                        help='Path to the output directory for train.txt and val.txt files.')
    parser.add_argument('--train_percentage', type=float, default=0.8,
                        help='Percentage of data to be used for training (0-1).')

    args = parser.parse_args()

    data_root = args.data_root
    output_dir = args.output_dir
    train_percentage = args.train_percentage

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    create_or_append_train_val_txt(data_root, train_percentage, output_dir)

# Example usage
# python3 create_file_list.py --data_root lrs2_preprocessed/brand --output_dir filelists --train_percentage 0.8