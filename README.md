# Interview Project 1

Design and code a program that standardizes a given file into a quoted csv format. The program will meet the following criterias:

- It will loop through files in the 'dataDropArea' directory to process all the files.
- It will use a configuration file as a YAML in order to pick up different parameters. The parameters should take into account:
    - File name Regex
    - Delimiter Used
- You can find a config example in `param/config.yaml`
- It will seek the file's configuration given a unique regex based on the file name pattern.
- The program should print errors if a file could not be standardized due to errors.
- The standardized output format is Quoted CSV, meaning seperated by comma, enclosed by quotes.
- The program has to be unit tested.
- The entrypoint of the program should be `standardize.py`

# How to
## Get help
`python3 standardize.py --help`

output:
```usage: standardize.py [-h] input_directory configuration_file output_directory

positional arguments:
  input_directory     Input directory containing the raw input files
  configuration_file  Configuration file containing the rules that the raw
                      input files have to follow
  output_directory    Output directory containing the standardized files

optional arguments:
  -h, --help          show this help message and exit
```

## Run
`python3 standardize.py ./dataDropArea/ ./param/config.yaml ./output/ `

## Compare files in `dataDropArea` and in `output`
### Command
From the directory where subfolders `dataDropArea` and `output` are located, the following command shows the differences beween the raw and transformed files

```
for file in `\ls ./dataDropArea/* | xargs basename -a`; \
    do \
        echo; \
        echo ===== $file =====; \
        pr -m -t ./dataDropArea/$file ./output/$file; \
    done
```

### Output example
```
===== file_no_pattern_matching.csv =====
pr: ./output/file_no_pattern_matching.csv: No such file or directory

===== file_test_1_20200101.csv =====
This,is,a,test,20200101             "This","is","a","test","20200101"
This,is,a,test,20200101             "This","is","a","test","20200101"
This,is,a,test,20200101             "This","is","a","test","20200101"
This,is,a,test,20200101             "This","is","a","test","20200101"
This,is,a,test,20200101             "This","is","a","test","20200101"
This,is,a,test,20200101             "This","is","a","test","20200101"
This,is,a,test,20200101             "This","is","a","test","20200101"
This,is,a,test,20200101             "This","is","a","test","20200101"
This,is,a,test,20200101             "This","is","a","test","20200101"

===== file_test_1_20200102.csv =====
This,is,a,test,20200102             "This","is","a","test","20200102"
This,is,a,test,20200102             "This","is","a","test","20200102"
This,is,a,test,20200102             "This","is","a","test","20200102"
This,is,a,test,20200102             "This","is","a","test","20200102"
This,is,a,test,20200102             "This","is","a","test","20200102"
This,is,a,test,20200102             "This","is","a","test","20200102"
This,is,a,test,20200102             "This","is","a","test","20200102"
This,is,a,test,20200102             "This","is","a","test","20200102"
This,is,a,test,20200102             "This","is","a","test","20200102"

===== file_test_1_20200103.csv =====
pr: ./output/file_test_1_20200103.csv: No such file or directory
This,is,a,test,20200103
This,is,a,test,20200103
This,is,a,test,20200103
This,is,a,test,20200103
This,is,a,test;20200103
This,is,a,test,20200103
This,is,a,test,20200103
This,is,a,test,20200103
This,is,a,test,20200103

===== file_test_2_20200520.csv =====
Another;test;file;date              "Another","test","file","date"
This;is;test;20200520               "This","is","test","20200520"
This;is;test;20200520               "This","is","test","20200520"
This;is;test;20200520               "This","is","test","20200520"
This;is;test;20200520               "This","is","test","20200520"
This;is;test;20200520               "This","is","test","20200520"

===== file_test_2_20200521.csv =====
Another;test;file;date              "Another","test","file","date"
This;is;test;20200521               "This","is","test","20200521"
This;is;test;20200521               "This","is","test","20200521"
This;is;test;20200521               "This","is","test","20200521"
This;is;te,t;20200521               "This","is","te,t","20200521"
This;is;test;20200521               "This","is","test","20200521"

===== file_test_3_20200520.csv =====
pr: ./output/file_test_3_20200520.csv: No such file or directory
Another|test|file|date
This|is|test|20200520
This|is||est|20200520
This|is|test|20200520
This|is|test|20200520
This|is|test|20200520
This|is|te,t|20200520
This|is|test|20200520
This|is|test data again|20200520
```