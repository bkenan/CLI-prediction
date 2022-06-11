import click
from main import final_model


@click.command()
@click.option(
    "--sentence",
    prompt="Sentence",
    help="Takes a sentence with <mask> in place of any word and predicts that word!",
)
def mask(sentence):
    # the function for the CLI tool

    """Example: Machine learning is an application of <mask>."""

    answers2 = final_model(sentence)
    j = 1
    for a2 in answers2:
        click.echo(click.style((f"Prediction {j}:",
                        list(a2.values())[0], "Score:", str(list(a2.values())[1])), fg="green"))
        j = j+1

if __name__ == "__main__":
    mask()