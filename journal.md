JOURNAL FALL 2025



8/25/25: CS3005
Streams and IO:
---------------

A stream is a data structure that represents a sequential pile of data that you assign. 
When you call something a stream, you can assign meaning and do things to it. 

Writing to a stream uses std::cout and << (<< is stream insertion operator). 
Cout can point to many things, not just the screen. 
Not exactly like print.
    Uses: speaker, file, etc.

std::cin >> (>> is stream extraction operator).

    Use: keyboards, etc.

----------------
C & C++ are strongly typed languages.

Data types:
    Numbers:
        - int
        - float
        - doubt
        signed/unsigned; short/long

    Boolean: 
        - bool 
        true/false

    Text: 
        - std::string
        ^object from STD template library in C++
        - char

    <b>Pointers:<b> 
        - *ptr 
            - void *ptr
            - int *ptr
            - std::string *str_ptr

        Pointers > memory not direct. 

-------------
std::string will automatically resize as you adjust it/append items to it in the process.

segmentation fault: if you try to access something outside of the allocated memory.



if([condition]) {
    statements;
} else if([condition]) {
    statements;
} else {
    statements;
}

It is possible to assign within an if statement, so you need to be careful about ==/=.


math & logic
+-*/ regular
^ xor
std::pow for exponents
% 
++ -- add 1 or sub 1
&& and 
!! or
! not

* dereference a pointer
& address of variable

--------------


8/27/25: CS2450

- Went over Git basics, it was a good refresher for how to do it from the command line
- I also had to create an SSH key for this device
- Wrote some python (basic age guessing program)

--------------

9/3/25: 

CS2450
- We brainstormed ideas for the YouFace social media project. Our group mainly focused on ideas for the concept. We want it to be funny and unique. I think our main ideas are a magician platform where only magicians are allowed and its super secure so the secrets don't get revealed. Also a clown dating site called Only Clowns.
    - It's interesting having a project that is more creative like this. In most classes before this point, the focus is on the creativity of the way you program, not in the concepts themselves. This one it's like we are not only coming up with how to do the thing, but also what the thing is in the first place lol

CS3005
- We talked about the std library, and how watching out for namespaces is important and being sure to use std::

--------------

9/8/25: CS3005

(void) is;

draw an image, to make it more clear how everything is connected 

data is in the image, thats why you have to pass it in

a main for each assignment, each has their own executable

psychomatic complexity - try to minimize how many branches and complexity it has

compiler wants optimization

add flags in makefile for testing

assignment 3 - image file, make them actual colors not just ascii

protected: no one can mess with it but children

--------------

9/10/25: CS3005

C++ language = only 10%
    lang is cool, but programming principles are the same across the board
    far less about the direct outcome of the project

Image processing, learning a designed program and how to work with something that's already made 


understand: 
image class, how it all works together, the mapping & how the vector works specifically, 

draw a picture of what it should look like, think through it before even writing any code
how to iterate through the array, use a for loop 
    for int row=0, for less than height, row++
        for int col=0, for less than width, col++

draw, pseudocode, then real code


instead of coupling, create a wrapper around the api youre using. encapsulation model
    allows you to not rely on an API to stay viable


virtual class, pure virtual class, derived class, 


inheritance principles
    inherit from multiple parents, parents can have like infinite children, stats and functions
    inherit publicly vs not
    

watch for quotation marks


fstream
ofstream
chatgpt will mess up assignment ppm 

std:ofsteam output_file("test.txt", std::ios::binary)

use put 

static cast
    casting allows you to write things out as other types, like casting an int into char
    

--------------

9/15/25:

CS2450
Software architecture:
- Software architecture is similar to real architecture, there are pitfalls to both.
- You need to take into account what is already built.
- It takes into account design, business, technology capabilities, and customer needs. Peoples, process, technology.

Add value: make correct technical decisions, enable communication between product and engineering, and drive sound development practices. 

Being familiar with a tool and being good at it is a good enough reason for using it. Technology choices are usually not the issue in failed projects, its usually people problems.

Making decisions between various trade-offs: speed vs storage, etc.

CS3005

Exam will be adding code directly to the codebase.

- Be familiar with what is in the files. 
- Loop through image and add these things, be familiar with the double for loop.
- Be familiar with what things call other things, between files etc, how it's laid out.

View practice exam in announcements.

He will give partial credit even on the all or nothing. Seems maybe better to do the 100 point, not the 35/65.

--------------

9/22/25:

CS2450
Ethics: the way you present information (especially to investors) can be manipulated, there is an ethical responsibility to present not only technically accurate but also really accurate information

Design: color, size, shapes, density, etc all convey meaning, add visual interest, and can make information more digestible

The people you present to, the goals you have, and design principles all should impact your presentation.

Simpler and less dense is not always better. Not always do engineers need a super duper complicated chart, and not always do investors want a super simple chart. 

Pictures can convey meaning a lot clearer.


CS3005

psuedo code is important!!

-decimals in binary


readStream in PPM

    - static_cast: compiler sees ex. int num; needs to allocate space for int. 
        address num pointing to 4 bytes. 

        write vs put

        r = getChannel(row,column,RED);
        //get r int
        os.put(static_cast<char>(r));
        you have to care about the type of r
        //cast it as a char to os
        static cast means shoehorn it into a type

        ask chatgpt about static cast vs reinterpret cast and use cases for each

vectors are just long lines of numbers (imagine as strings of ints)

maps are 1:1, and they are specific to the types given


auto makes it figure out the type

wolf fencing
fencing in a location, cutting off parts for sure it is not, narrowing it down. use print statements

--------------

9/24/25: CS3005

Cohesion:
    The more you stuff an object, the more specialized it becomes, and the less useful it becomes.

    
push_back is like append in py

--------------

9/27/25:

General:
When beginning/editing a system, it is superrrrr helpful to have documentation and good comments. Write down what links where. Draw diagrams. Etc. 

--------------

9/29/25: 

CS2450

make pitch decks interesting and funny



CS3005

this-> me, not strictly necessary

Virtual vs non-virtual functions
    Virtual functions are a little slower but sometimes that's negligible

--------------

10/1/25: 

CS3005

Ground covered so far (1/2 through week 7!)
    C++ structure
    classes, object orientation, inheritance, polymorphism, encapsulation
    system design, cohesion
    function pointers
    virtual functions



Hash - a one way encryption, a smaller-than-original jumble of characters
    You can't undo a hash, but you can compare hashes (a hash you make of X will always be the same)

    SHA - secure hash algorithm


Look at unit tests

rebase vs merge

draw a picture

--------------

10/2/2025:

SE3200

Database:
    - collects data
    - library with information
    - list of things


No-SQL databases:
    - document store
    - key-value store
    - column-family store


SQLITE is what we use

Once you learn one SQL you will know you're way around the others

SQL - Structured Query Language



potential table for course schedule web app
|--------------------------------------|
| ID | type | code | layman | semester |
|--------------------------------------|
| ID | type | code | layman | semester |
|--------------------------------------|
| ID | type | code | layman | semester |
|--------------------------------------|
| ID | type | code | layman | semester |
|--------------------------------------|
| ID | type | code | layman | semester |
|--------------------------------------|
| ID | type | code | layman | semester |
|--------------------------------------|
| ID | type | code | layman | semester |
|--------------------------------------|
| ID | type | code | layman | semester |
|--------------------------------------|
| ID | type | code | layman | semester |
|--------------------------------------|

Mac comes installed with SQLite3

for commands, use all caps to make it easier to differentiate

> CREATE TABLE schedule (id INTEGER PRIMARY KEY, type TEXT, code INTEGER, layman TEXT, semester TEXT) 
    cmd   cmd   name       fields                name type  name  type

.schema

Security is critical, in real world programming things need to be robust

Validation should be on both sides


sqlite mydb.db.    //adding filename is how you make it persistent
CREATE TABLE schedule (id INTEGER PRIMARY KEY, type TEXT, code INTEGER, layman TEXT, semester TEXT);
INSERT INTO schedule (type, code, layman, semester) VALUES ('math', 1210, 'calc 1', 'FA25');
INSERT INTO schedule (type, code, layman, semester) VALUES ('se', 3200, 'web app 1', 'FA25');
INSERT INTO schedule (type, code, layman, semester) VALUES ('cs', 3005, 'c++', 'FA25');
INSERT INTO schedule (type, code, layman, semester) VALUES ('cs', 2450, 'software engineering', 'FA25');
INSERT INTO schedule (type, code, layman, semester) VALUES ('cs', 4992, 'seminar', 'FA25')
SELECT * FROM schedule; 

--------------

10/3/2025:

CS2450

Gant chart
    not really accurate

Kanban
    

--------------
