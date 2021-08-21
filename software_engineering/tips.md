# Here are a non exhaustive list of tips that I've learned about software engineering over the course of n years.

* When you submit a diff of changes to be reviewed, run a git diff beforehand to review the changes yourself.
It can save you a lot of headache and a lot of nits.
* When you're building a feature, you should look to make changes as incrementally as possible.
Go for the smallest unit of individual work to submit. It will increase your velocity and time to land.


### Tips for reviewing code
* Save the nits for the end of the code review. If you're at the point where you're searching for
non errors, it's probably because the code is written well enough.
* Start by understanding the theme or
the gist of what someone is trying to do, and then transistion into inspecting
how they do it, paying close attention to any libraries or third party code they
might have added in order to do it. If at any point, there are gaps in your
understanding, ask for clarification in the area where the knowledge gap exists.
You learn a lot when you ask those questions and it gives the author an opportunity
to demonstrate their understanding as well!
* Take care to think of all the ways things can fail. Often times code is written with the path where everything goes right.
What happens if certain code paths don't complete or fail early? Do you have anything that relies on the state of the program previously? 
If so, don't forget to check the error paths as well.

## Good things to know
1. The best way to understand how code written by someone else (including your former self) wrote, is to delete as much as you can and see what breaks. If nothing breaks, it probably wasn't needed, and if it does, you know why its there.

## Engineering Principles
* The system you create should be as restrictive as possible because its much easier to open a system up rather than to try and close a system down.
