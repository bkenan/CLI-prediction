import click 
from main import *

@click.command()
@click.option(
    "--sentence",
    prompt="Sentence",
    help="Takes a sentence with <mask> in place of any word and predicts that word!",
)



def mask(sentence):
    """Example: Machine learning is an application of <mask>."""
        
    answers2 = model(sentence)
    
    j = 1
    for a2 in answers2:
        click.echo(click.style((f"Prediction {j}:",
                        a2["sequence"], "Score:", str(round(a2["score"], 2))), fg="green"))
        j = j+1    

if __name__ == "__main__":
    mask()