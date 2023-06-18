import argparse
from .run_analysis import run_analysis

def main():
    parser = argparse.ArgumentParser(description='Run calcium imaging analysis pipeline.')
    parser.add_argument('--image_fld', required=True, help='Path to the image folder.')
    parser.add_argument('--save_fld', required=True, help='Path to the save folder.')
    parser.add_argument('--sd', type=float, required=True, help='Standard deviation value.')
    
    args = parser.parse_args()
    
    run_analysis(args.image_fld, args.save_fld, args.sd)

if __name__ == "__main__":
    main()
```


