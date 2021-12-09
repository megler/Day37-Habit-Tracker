# Habit Tracker

A habit tracker using Pixela. Day 37 Python Bootcamp


## Usage
Using Pixela, you can create a visual habit tracker for any habit you'd like to
build on.

See the [Pixela](https://pixe.la/) page for a quickstart and [Docs](https://docs.pixe.la/)
for more detail on what each Requests call needs. Note the homepage quick start
is very useful before you go straight to the docs.

When you first run the script, you need to run the functions in order:

1. **create_user(TOKEN, USERNAME)** will allow you to create a username and graph to
track your habit of choice. The token is equivalent to an API Key. You create it
yourself.  

2. Each function returns r.text. Print the output of the function to make sure 
your operation was successful. This is especially important in step one to make
sure you actually set up a username and token.

3. **create_graph(name: str, unit: str, type: str, color: str, timezone: str)** will
set up your first tracking graph. Be sure to read the [docs](https://docs.pixe.la/entry/post-graph)
as color is in Japanese and all of these function arguments need to be specific
to set up the graph.

4. **add_pixel(quantity: str)** will allow you to add a new entry for today. You'll
have to change the date inside the function if you want to add a pixel for a day
other than today.

5. **update_pixel(quantity: str, when: str)** will allow you to change a pixel entry.
Be sure to use the correct date format found in the [docs](https://docs.pixe.la/entry/put-pixel).

6. **delete_pixel(when: str, quantity: str)** will delete a pixel on a chosen day.

7. You can save your environment variables in a .env file and call them with
(Python-Env)[https://pypi.org/project/python-dotenv/]

8. You can add all dependencies from the requirements.txt. Use:

`pip install -r requirements.txt`





## License
[MIT](https://choosealicense.com/licenses/mit/)