# Introduction

PyProg is an Open-Source library for creating progress indicators (e.g. progress bars). It helps you create customizable progress indicators. This library is for Python.

# Compatibility

PyProg is compatible with both Python 3 and Python 2.

# Getting Started

## Installation

To install PyProg, download the wheel file for your version of Python, and use pip to install it.

Install PyProg: `pip install <path of the wheel file>`

After you have installed PyProg, you can test if it has been successfully installed by running `import pyprog` in python. If PyProg was installed successfully, it should show no errors.

## How to use the PyProg Progress Bar

### Basic PyProg Progress Bar

To create a basic progress bar, follow these steps:

1. Install PyProg ([Guide](#installation "How to install PyProg"))
2. Import PyProg: `import pyprog`
3. Create a `ProgressBar` object: `prog = pyprog.ProgressBar("", "")`
4. Show the bar: `prog.update()`
5. To update the status, use `prog.set_stat(<status>)` to set the status and then use `prog.update()` to actually show the change
6. When finished, use `prog.end()` to make the Progress Bar last

Example Code with Fake For loop:

```python
import pyprog
from time import sleep

# Create a PyProg ProgressBar Object
prog = pyprog.ProgressBar(":-) ", " OK!")

# Show the initial status
prog.update()

# Fake for loop
for i in range(0, 100):

	# Sleep for a while (This is just to slow down the for loop so that it won't end in an instant)
	sleep(0.1)

	# Update status
	prog.set_stat(i + 1)

	# Show (Update) the current status
	prog.update()

# Make the Progress Bar final
prog.end()
```

Output:

```
Initial State: 
:-) Progress: 0% --------------------------------------------------  OK!

When progress is 50: 
:-) Progress: 50% #########################-------------------------  OK!

Final State: 
:-) Progress: 100% ##################################################  OK!
```

#### What is the first two parameters?

The first two parameters in `prog = pyprog.ProgressBar("", "")` is for telling PyProg what to put before and after the progress indicator.

Example:

```
 :-) Progress: 0% --------------------------------------------------  OK!
  ^                                 ^                                  ^
Prefix                             Bar                              Suffix
```

### Pretty Progress Bar

You can also add more options to make it look good.

Adding options `complete_symbol="█", not_complete_symbol="-"` will change the original output to:

```
Initial State: 
:-) Progress: 0% --------------------------------------------------  OK!

When progress is 50: 
:-) Progress: 50% █████████████████████████-------------------------  OK!

Final State: 
:-) Progress: 100% ██████████████████████████████████████████████████  OK!
```

### Auto calculate the percentage

PyProg can also auto calculate the current percentage. You just need to tell PyProg the total number of things you need to process.

Change the line `prog = pyprog.ProgressBar("", "")` to `prog = pyprog.ProgressBar("", "", <Total Number of things>)`, and PyProg will calculate the percentage for you based on the status that you give it.

To use it in our simple progress bar code, if we have 37 tasks to do, we can change this:

```python
# Create a PyProg ProgressBar Object
prog = pyprog.ProgressBar(":-) ", " OK!")
```

to this:

```python
# Create a PyProg ProgressBar Object
prog = pyprog.ProgressBar(":-) ", " OK!", 37)
```

And also change the fake for loop from `for i in range(0, 100):` to `for i in range(0, 37):`, and it will auto calculate the percentage and show it to the user.

## How to use the PyProg Progress Indicator (Fraction)

### Basic PyProg Progress Indicator (Fraction)

To create a basic progress indicator (fraction), follow these steps:

1. Import PyProg: `import pyprog`
2. Create a `ProgressIndicatorFraction` object: `prog = pyprog.ProgressIndicatorFraction("", "", <Total number of things>)` (Replace "<Total number of things>" with the total number of tasks or things you need to process)
3. Show the indicator: `prog.update()`
4. To update the status, use `prog.set_stat(<status>)` to set the status and then use `prog.update()` to actually show the change
5. When finished, use `prog.end()` to make the Progress Indicator (Fraction) last

Example Code with Fake For loop (We are using 56 as the total in this example):

```python
import pyprog
from time import sleep

# Create a PyProg ProgressIndicatorFraction Object
prog = pyprog.ProgressIndicatorFraction(":-) ", " OK!", 56)

# Show the initial status
prog.update()

# Fake for loop
for i in range(0, 56):

	# Sleep for a while (This is just to slow down the for loop so that it won't end in an instant)
	sleep(0.1)

	# Update status
	prog.set_stat(i + 1)

	# Show (Update) the current status
	prog.update()

# Make the Progress Indicator (Fraction) final
prog.end()
```

Output:

```
Initial State: 
:-) 0/56 OK!

When half done: 
:-) 28/56 OK!

Final State: 
:-) 56/56 OK!
```

# Documentation

## Progress Indicator Parameters

### Options for ProgressBar

#### prefix

The prefix of everything.

#### suffix

The suffix of everything.

#### total (default is 100)

This is the option that tells PyProg how many things or tasks you need to process. We used it in the [Auto calculate the percentage](#auto-calculate-the-percentage "Auto calculate the percentage") section.

#### bar_length (default is 50)

This tells PyProg how long should the bar should be.

#### initial (default is 0)

Initial status to show on the bar.

#### decimals (default is 0)

How many decimals should the percent have.

#### complete_symbol (default is "#")

The complete symbol will be shown in the complete part of the bar. We used it in the [Pretty Progress Bar](#pretty-progress-bar "Pretty Progress Bar") section.

Example Position of complete symbol:
Progress: 59% <span style="background-color: #FFFF00">#############################</span>---------------------&nbsp;

#### not_complete_symbol (default is "-")

The not complete symbol will be shown in the not yet complete part of the bar. We used it in the [Pretty Progress Bar](#pretty-progress-bar "Pretty Progress Bar") section.

Example Position of complete symbol:
Progress: 59% #############################<span style="background-color: #FFFF00">---------------------</span>&nbsp;

#### progress_loc (default is 0)

Where the progress explanation (prefix) and the progress text should be shown.

Possible Values:
	ProgressBar.PROGRESS_LOC_START or 0 - Show both at the start
	ProgressBar.PROGRESS_LOC_MIDDLE or 1 - Show both at the middle of the bar
	ProgressBar.PROGRESS_LOC_END or 2 - Show both at the end
	ProgressBar.PROGRESS_LOC_EXP_START_PROGRESS_MID or 3 - Show explanation (prefix) at the start and the progress text at the middle of the bar
	ProgressBar.PROGRESS_LOC_EXP_END_PROGRESS_MID or 4 - Show explanation (prefix) at the end and the progress text at the middle of the bar

PROGRESS_LOC_START:
<span style="background-color: #FFFF00">Progress: 32%</span> ################----------------------------------&nbsp;

PROGRESS_LOC_MIDDLE:
\################ <span style="background-color: #FFFF00">Progress: 32%</span> ------------------&nbsp;

PROGRESS_LOC_END:
\################---------------------------------- <span style="background-color: #FFFF00">Progress: 32%</span>

PROGRESS_LOC_EXP_START_PROGRESS_MID:
<span style="background-color: #FFFF00">Progress:  </span>################----- <span style="background-color: #FFFF00">32%</span> -----------------------&nbsp;

PROGRESS_LOC_EXP_END_PROGRESS_MID:
\################----- <span style="background-color: #FFFF00">32%</span> ----------------------- <span style="background-color: #FFFF00">Progress: </span>

#### progress_format (default is "+p%")

Format for the progress text. PyProg replaces special characters with actual values. Here is a list of special characters:

"+p" -> Current percent
"+c" -> Current status

#### progress_explain (default is "Progress: ")

This is the progress explanation (prefix).

Example position of progress explanation:
<span style="background-color: #FFFF00">Progress: </span>32% ################----------------------------------&nbsp;

Examples:
	"Progress: "
	"Current Progress: "

#### wrap_bar_prefix (default is " ")

The prefix of the bar.

#### wrap_bar_suffix (default is " ")

The suffix of the bar.

### Options for ProgressIndicatorFraction

#### prefix

The prefix of everything.

#### suffix

The suffix of everything.

#### total

This is the option that tells PyProg how many things or tasks you need to process.

#### initial (default is 0)

Initial status to show on the indicator.

## Progress Indicator Functions

### Functions for ProgressBar

#### set_stat()

Params: current

Set the current progress.

#### update()

Params: (none)

Update the progress bar so that it shows the current progress.
Note: Also call this to initiate the bar.

#### end()

Params: (none)

End the progress bar.

#### set_prefix()

Params: prefix

Set the prefix

#### set_suffix()

Params: suffix

Set the suffix

#### set_total()

Params: total

Set the total

#### set_bar_length()

Params: bar_length

Set the length of the bar

#### set_decimals()

Params: decimals

Set the number of decimals for the percent

#### set_symbols()

Params: symbols

Set the complete symbol and the not complete symbol. `symbols` has to be a tuple: (complete symbol, not complete symbol)

#### set_progress_loc()

Params: progress_loc

Set the progress explanation (prefix) and the progress text location. See [the progress_loc parameter](#user-content-progress_loc-default-is-0 "progress_loc") section for the possible values.

#### set_progress_explain()

Params: progress_explain

Set the progress explanation (prefix).

Examples:
	"Progress: "
	"Current Progress: "

#### set_wrap_bar_text()

Params: prefix, suffix

Set the wrap bar text (the prefix and the suffix of the bar).

#### set_progress_format()

Params: progress_format

Set the format for the progress text. PyProg replaces special characters with actual values. Here is a list of special characters:

"+p" -> Current percent
"+c" -> Current status

### Functions for ProgressIndicatorFunction

#### set_stat()

Params: current

Set the current progress.

#### update()

Params: (none)

Update the progress indicator so that it shows the current progress.
Note: Also call this to initiate the indicator.

#### end()

Params: (none)

End the progress indicator.

#### set_prefix()

Params: prefix

Set the prefix

#### set_suffix()

Params: suffix

Set the suffix

#### set_total()

Params: total

Set the total

# Contact

If you want to support me, please contact me at kudoshiko@gmail.com.

My website is at [http://www.WhatsYourIdea.com/](http://www.WhatsYourIdea.com/ "Website")


