
# Easy Tools

CLI tools for making your life easy

Tools LIst:

| Name      | Description                |
| :-------- | :------------------------- |
| `big-grep`  | Filters lines from big files based on specifc search string |
| `awst`    | Aws Cli tool to fetch instance details |


## Big Grep
#### Dependencies
``` python3 ```
#### Usage
``` python3 big-grep.py --input_file input.txt --output_file out.txt --filter_string string_to_find ```

## Awst
#### Dependencies
``` python3 ```
``` boto3 ```
``` prettytable ```

#### Instalation 
```bash
  chmod +x insall.sh
  ./insall.sh
```

#### Usage
``` 
awst --list-ec2 --region <region name> --profile <aws profile> 

```
