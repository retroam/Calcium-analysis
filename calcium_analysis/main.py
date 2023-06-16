import argparse
from calcium_analysis import image_processing, data_extraction

def main():
    parser = argparse.ArgumentParser(description='Calcium Analysis CLI tool')
    parser.add_argument('--input-dir', required=True, help='Input directory')
    parser.add_argument('--output-dir', required=True, help='Output directory')
    args = parser.parse_args()

    image_processing.imagestostacks(args.input_dir, args.output_dir)
    image_processing.stackstoroi(args.output_dir)
    data_extraction.roi_to_data(args.output_dir)

if __name__ == '__main__':
    main()
```

