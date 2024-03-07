fonts = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Josefin+Sans:wght@200;400&display=swap" rel="stylesheet">
"""


style_choice_css = """
<head>
    <style>
        p{
            text-align: center;
            font-size: 30px;
            font-family: 'Inter', sans-serif;
            font-style: normal;
            font-weight: 700;
            line-height: normal;
            letter-spacing: 0.2px;
            text-transform: uppercase;}

        a:link{
            text-decoration: none;
        }
        a:visited{
            text-decoration: none;
        }
        a:hover{
            text-decoration: none;
        }
        a:active{
            text-decoration: none;
        }
    </style>
</head>
        """

style_choice_content = """
<p>
    <a href='#/' id='casual' style="color:{casual_color};"> CASUAL </a>
    <a href='#/' id='rock' style="color:{rock_color};"> ROCK </a>
    <a href='#/' id='urban' style="color:{urban_color};"> URBAN </a>
    <a href='#/' id='tailoring' style="color:{tailoring_color};"> TAILORING </a>
    <a href='#/' id='other' style="color:{other_color};"> OTHER </a>
</p>
"""


def get_styles(style_colors_dict):
    content = (
        fonts + style_choice_css + style_choice_content.format(**style_colors_dict)
    )
    return content