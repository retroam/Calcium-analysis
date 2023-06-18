import click
from .run_analysis import run_analysis
@click.command()
@click.option('--image_fld', required=True, help='Path to the image folder.')
@click.option('--save_fld', required=True, help='Path to the save folder.')
@click.option('--sd', type=float, required=True, help='Standard deviation value.')
def main(image_fld, save_fld, sd):
    run_analysis(image_fld, save_fld, sd)

if __name__ == "__main__":
    main()