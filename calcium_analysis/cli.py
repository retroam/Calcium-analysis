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
    and the standard deviation value. It then calls the run_analysis function from typing import Optional
    and the standard deviation value. It then calls the run_analysis function import click
    and the standard deviation value. It then calls the run_analysis function from .analysis import run_analysis
    and the standard deviation value. It then calls the run_analysis function 
    and the standard deviation value. It then calls the run_analysis function @click.command()
    and the standard deviation value. It then calls the run_analysis function @click.option('--image_fld', required=True, help='Path to the image folder.')
    and the standard deviation value. It then calls the run_analysis function @click.option('--save_fld', required=True, help='Path to the save folder.')
    and the standard deviation value. It then calls the run_analysis function @click.option('--sd', type=float, required=True, help='Standard deviation value.')
    and the standard deviation value. It then calls the run_analysis function def main(
    and the standard deviation value. It then calls the run_analysis function     image_fld: str,
    and the standard deviation value. It then calls the run_analysis function     save_fld: str,
    and the standard deviation value. It then calls the run_analysis function     sd: float,
    and the standard deviation value. It then calls the run_analysis function     ctx: Optional[click.Context] = None
    and the standard deviation value. It then calls the run_analysis function ) -> None:
    and the standard deviation value. It then calls the run_analysis function     """Main function to run the analysis pipeline."""
    and the standard deviation value. It then calls the run_analysis function     run_analysis(image_fld, save_fld, sd)
    and the standard deviation value. It then calls the run_analysis function 
    and the standard deviation value. It then calls the run_analysis function if __name__ == "__main__":
    and the standard deviation value. It then calls the run_analysis function     main()