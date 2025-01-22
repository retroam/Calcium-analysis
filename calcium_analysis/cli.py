import click
from .analysis import run_analysis
@click.command()
@click.option('--image_fld', required=True, help='Path to the image folder.')
@click.option('--save_fld', required=True, help='Path to the save folder.')
@click.option('--sd', type=float, required=True, help='Standard deviation value.')
def main(image_fld: str, save_fld: str, sd: float) -> None:
    """
    Main function to run the analysis pipeline.

    This function takes in the path to the image folder, the path to the save folder,
    and the standard deviation value. It then calls the run_analysis function from the
    analysis module to run the analysis pipeline.

    Parameters:
    image_fld (str): The path to the folder containing the images to be analyzed.
    save_fld (str): The path to the folder where the results will be saved.
    sd (float): The standard deviation used for image segmentation.

    Returns:
    None
    """
    run_analysis(image_fld, save_fld, sd)

if __name__ == "__main__":
    main()