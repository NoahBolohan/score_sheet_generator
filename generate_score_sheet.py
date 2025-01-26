from jinja2 import Environment, FileSystemLoader
from pathlib import Path

def generate_score_sheet(
    score_sheet_title : str = "Score Sheet",
    min_players : int = 2,
    max_players : int = 5,
    row_headers : list[str] = [
        "markers_on_dragon_guild",
        "printed_on_dragons",
        "end-game_abilities",
        "eggs",
        "cached_resources",
        "tucked_cards",
        "public_objectives",
        "remaining_resources"
    ],
    include_return_homepage_button : bool = True,
    homepage_link : str = "https://noahbolohan.github.io/wyrmspan-utilities/index.html",
    google_scripts_link : str = "https://script.google.com/macros/s/AKfycbwHfda9GFnKFvMem6YLQxmeTCjQYSASG1E46ulA6-cmWxoSO137pCEl2m-luSEp9nAmpg/exec",
    jquery_url : str = "https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js",
    bootstrap_css_url : str = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css",
    bootstrap_js_url : str = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js",
    background_image_url : str = "https://raw.githubusercontent.com/NoahBolohan/wyrmspan-utilities/refs/heads/main/static/box_art/base_game.png"
):
    '''
    Generate a score sheet using passed arguments to populate the sheet.

    Parameters
    --------
    score_sheet_title : str
        Header of the score sheet.
    min_players : int
        Minimum number of players.
    max_players : int
        Maximum number of players.
    row_headers : list[str]
        List of headers for the score sheet, i.e., items to be scored.
    include_return_homepage_button : bool
        Include a button that returns the user to another URL.
    homepage_link : str
        URL to be returned to if the 'Return to home page' button is clicked
    google_scripts_link : str
        URL to post to a Google Sheets document. Obtained from the Google Apps Script extension.
    jquery_url : str
        URL from which to obtain JQuery.
    bootstrap_css_url : str
        URL from which to obtain Bootstrap CSS.
    bootstrap_js_url : str
        URL from which to obtain Bootstrap Javascript.
    background_image_url : str
        URL from which to obtain a background image.
    '''
    # Initialize Environment
    environment = Environment(
        loader=FileSystemLoader("templates/"),
        trim_blocks = True,
        lstrip_blocks = True
    )

    # Get templates
    score_sheet_html_template = environment.get_template("score_sheet.html.j2")
    styles_css_template = environment.get_template("styles.css.j2")
    misc_scripts_js_template = environment.get_template("misc_scripts.js.j2")
    score_sheet_scripts_js_template = environment.get_template("score_sheet_scripts.js.j2")

    # Define output files

    # Score sheet .html
    score_sheet_html_output_fp = "score_sheet.html"

    #.css directory
    css_output_dir = Path("./css/")
    css_output_dir.mkdir(exist_ok=True, parents=True)

    # styles.css
    styles_css_output_fp = css_output_dir / "styles.css"

    #.js directory
    js_output_dir = Path("./js/")
    js_output_dir.mkdir(exist_ok=True, parents=True)

    # misc_scripts.js
    misc_scripts_js_output_fp = js_output_dir / "misc_scripts.js"

    # score_sheet_scripts.js
    score_sheet_scripts_js_output_fp = js_output_dir / "score_sheet_scripts.js"

    # # Define data
    # score_sheet_title = "Score Sheet"
    # min_players = 2
    # max_players = 5
    # row_headers = [
    #     "markers_on_dragon_guild",
    #     "printed_on_dragons",
    #     "end-game_abilities",
    #     "eggs",
    #     "cached_resources",
    #     "tucked_cards",
    #     "public_objectives",
    #     "remaining_resources"
    # ]
    # include_return_homepage_button = True
    # homepage_link = "https://noahbolohan.github.io/wyrmspan-utilities/index.html"
    # google_scripts_link = "https://script.google.com/macros/s/AKfycbwHfda9GFnKFvMem6YLQxmeTCjQYSASG1E46ulA6-cmWxoSO137pCEl2m-luSEp9nAmpg/exec"
    # jquery_url = "https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"
    # bootstrap_css_url = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
    # bootstrap_js_url = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
    # background_image_url = "https://raw.githubusercontent.com/NoahBolohan/wyrmspan-utilities/refs/heads/main/static/box_art/base_game.png"

    score_sheet_html_data = {
        "min_players" : min_players,
        "max_players" : max_players,
        "score_sheet_title" : score_sheet_title,
        "row_headers" : row_headers,
        "include_return_homepage_button" : include_return_homepage_button,
        "homepage_link" : homepage_link,
        "google_scripts_link" : google_scripts_link,
        "jquery_url" : jquery_url,
        "bootstrap_css_url" : bootstrap_css_url,
        "bootstrap_js_url" : bootstrap_js_url
    }

    styles_css_data = {
        "background_image_url" : background_image_url
    }

    score_sheet_scripts_js_data = {
        "min_players" : min_players,
        "max_players" : max_players,
        "row_headers" : row_headers,
    }

    # Render the .html file
    with open(score_sheet_html_output_fp, mode="w", encoding="utf-8") as results:
        results.write(score_sheet_html_template.render(score_sheet_html_data))
        print(f"... wrote {score_sheet_html_output_fp}")

    # Render the .css files
    with open(styles_css_output_fp, mode="w", encoding="utf-8") as results:
        results.write(styles_css_template.render(styles_css_data))
        print(f"... wrote {styles_css_output_fp}")

    # Render the .js files
    with open(misc_scripts_js_output_fp, mode="w", encoding="utf-8") as results:
        results.write(misc_scripts_js_template.render())
        print(f"... wrote {misc_scripts_js_output_fp}")

    with open(score_sheet_scripts_js_output_fp, mode="w", encoding="utf-8") as results:
        results.write(score_sheet_scripts_js_template.render(score_sheet_scripts_js_data))
        print(f"... wrote {score_sheet_scripts_js_output_fp}")