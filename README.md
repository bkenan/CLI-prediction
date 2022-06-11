[![Click CLI Test](https://github.com/bkenan/CLI-prediction/actions/workflows/main.yml/badge.svg)](https://github.com/bkenan/CLI-prediction/actions/workflows/main.yml)


# Fill-Mask tool

This project used a pretrained case-sensitive RoBERTa base model which applies a masked language modeling (MLM) objective. RoBERTa is a transformers model pretrained by Pytorch on a large corpus of English data. The tool takes a sentence and the model randomly masks 15% of the words in the input then run the entire masked sentence through the model and has to predict the masked words. The project includes both UI created by streamlit and CLI tool supporting CI/CD on GitHub actions.


## Getting started for CLI:

```
python3 -m venv ~/.app
```
```
source ~/.app/bin/activate
```
```
make all
```
```
python3 cli.py
```

## Running for UI:

```
make install
```
```
streamlit run main.py
```

## Demo

![1](https://user-images.githubusercontent.com/53462948/173188359-c0089106-4454-49fd-aec3-8e1b49c331d0.png)


## Reference

[Hugging Face](https://huggingface.co/roberta-base?text=The+goal+of+life+is+%3Cmask%3E)

