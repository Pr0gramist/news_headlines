# News Headlines
API that matches news headlines to employees on a specific publication date.

## Getting Started

Download all ".py" and ".txt" files

invoker.py will be used to invoke and make a call to the news_match API.

To be able to run this project, Python3 needs to be installed on your computer.

Open terminal/cmd and navigate to folder that contains all files and run the following command:

```
python3 invoker.py
```
Prompt will come up asking you to enter a date. To keep data together the ranges are fairly small.
Enter a date in the format of "yyyy-mm-dd". For example "2019-08-01".
This will create or overwirte "result.txt" file.

## Additional Information

gen_employee.py can be run to create a new random list of 10,000 employees.
```
python3 gen_employee.py
```
gen_headline.py can be run to create a new random list of 3,000 news headlines.
```
python3 gen_headline.py
```

You can also edit invoker.py and make additional function calls.
The following lines can be added at the end of invoker.py, these lines will create additional files.
```
newsAPI.match_dept2headline(None)
newsAPI.match_job2headline(None)
newsAPI.match_lang2headline(None)
```



## Authors

* **Stivan Kitchoukov** - [Pr0gramist](https://github.com/Pr0gramist)

## License

This project is licensed under the MIT License.
