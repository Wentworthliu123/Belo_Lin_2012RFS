def Tolatex(result, file_name):

    from pathlib import Path
    import os
    cwd = os.getcwd()
    parent_folder = Path(cwd)
    output_folder = parent_folder / 'Output'/ 'Table'
    output_file = output_folder / file_name
    try:
        result.to_latex(output_file)
    except FileNotFoundError:
        os.makedirs(output_folder)
        result.to_latex(output_file)