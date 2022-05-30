#SimpleStaticBlogGenerator

To start just create a "msgs" folder
Then write some posts in plain text files with the format

```
WeekDay Month DayNumber H:M:S PM/AM UTC/GMT Year

[[Author]]
Post Goes Here

You can create multiple paragraphs by skiping lines like this.
```
Ex:

The file tst.txt

```
Sun May 29 12:23:20 AM -0300 2022

[[Victor Lima]]
Hey! It's working!
```

Produces the result following result when using the default template:
![image](https://user-images.githubusercontent.com/100252586/170898171-9a7ab3a9-59d5-477a-9e46-50df1fcba81f.png)

(The very specific datetime header is used to sort the entries)


