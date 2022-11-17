# QR CODE GENERATOR

## Install Dependencies

```sh
pip3 install -r requirements.txt
```

## Create Output Folder

```sh
mkdir output
```

## Arguments

| Field      | Required | Description                                                                          |
| ---------- | -------- | ------------------------------------------------------------------------------------ |
| title      | True     | name of the output file (ex. `--title foo` will generate a qr code named `foo.jpg` ) |
| link       | True     | redirect url link                                                                    |
| output-dir | False    | output directory path                                                                |

## Generate

```sh
python3 qr_generator.py \
    --title "{ TITLE }" \
    --link "{ LINK }"
```
