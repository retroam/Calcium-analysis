# Calcium-analysis
Python implementation of calcium imaging analysis pipeline for cardiac myocytes for [Automated image analysis of cardiac myocyte Ca2+ dynamics](https://pubmed.ncbi.nlm.nih.gov/22255377/)
## How to use this package

To install and use this package, follow the steps below:

1. Clone this repository to your local machine.

```bash
git clone https://github.com/retroam/Calcium-analysis.git
```

2. Navigate to the cloned repository.

```bash
cd Calcium-analysis
```

3. Install the required dependencies.

```bash
pip install -r requirements.txt
```

4. Run the scripts in the `calcium_analysis` directory. For example, to run the `data_extraction.py` script, use the following command:

```bash
python calcium_analysis/run_analysis.py
```

This script extracts data from regions of interest in an image stack and saves the results.
32: 5. Similarly, you can run the other scripts in the `calcium_analysis` directory. Each script has a specific function in the calcium imaging analysis pipeline. For more information on what each script does, refer to the comments in the script files.

## Command Line Interface

You can also run the package as a command line interface using the main function in the cli.py file. Here's the command to do this:

```bash
python -m calcium_analysis.cli --image_fld <path_to_image_folder> --save_fld <path_to_save_folder> --sd <standard_deviation_value>
```

Where:
- `--image_fld` is the path to the image folder.
- `--save_fld` is the path to the save folder.
- `--sd` is the standard deviation value.