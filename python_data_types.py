{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h1>Data Types and Operators</h1>\n",
    "<h4>Welcome to this lesson on Data Types and Operators! You'll learn about:</h4> \n",
    "\n",
    "- <h4>Data Types:</h4> Strings, Integers, Floats, Booleans, Lists, Tuples, Sets, Dictionaries\n",
    "\n",
    "- <h4>Operators:</h4> Arithmetic, Assignment, Comparison, Logical, Membership, Identity\n",
    "\n",
    "\n",
    "- Built-In Functions, Compound Data Structures, Type Conversion\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h1>Strings:<h1>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "#String: Enclosed textual data within quotes\n",
    "var_1 = 'Hello World!'\n",
    "var_2 = \"Youtube is Google's video streaming platform\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello World!\n"
     ]
    }
   ],
   "source": [
    "print(var_1)\n",
    "#Prints the value of variable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12\n"
     ]
    }
   ],
   "source": [
    "print(len(var_1))\n",
    "#Prints the length of variable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "d\n"
     ]
    }
   ],
   "source": [
    "#In python, Indexing starts from 0,1,2,3\n",
    "print(var_1[10])\n",
    "#prints character at index 10\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello\n"
     ]
    }
   ],
   "source": [
    "print(var_1[0:5])\n",
    "#prints character index 0-4 but 5 isn't included"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "World!\n"
     ]
    }
   ],
   "source": [
    "print(var_1[6:])\n",
    "#prints character index 6-last index "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###### The above operations using square [] brackets is called slicing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello world!\n"
     ]
    }
   ],
   "source": [
    "print(var_1.lower()) #Prints strings in lower case"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HELLO WORLD!\n"
     ]
    }
   ],
   "source": [
    "print(var_1.upper()) #Prints strings in upper case"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello, harsh akshit. Welcome!\n",
      "hello, harsh akshit. Welcome!\n"
     ]
    }
   ],
   "source": [
    "greeting = 'hello'\n",
    "name = 'harsh akshit'\n",
    "\n",
    "message_1 = greeting+', '+name+'. Welcome!' #String concatenation\n",
    "message_2 = '{}, {}. Welcome!'.format(greeting,name)\n",
    "\n",
    "print(message_1)\n",
    "print(message_2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<br><br>\n",
    "\n",
    "## Variable Naming Conventions:**\n",
    "\n",
    "There are some rules we need to follow while giving a name for a Python variable.\n",
    "\n",
    "- **Rule-1**: You should start variable name with an alphabet or **underscore(_)** character.\n",
    "- **Rule-2:** A variable name can only contain **A-Z,a-z,0-9** and **underscore(_)**.\n",
    "- **Rule-3:** You cannot start the variable name with a **number**.\n",
    "- **Rule-4:** You cannot use special characters with the variable name such as such as **$,%,#,&,@.-,^** etc.\n",
    "- **Rule-5**: Variable names are **case sensitive**. For example str and Str are two different variables.\n",
    "- **Rule-6:** Do not use reserve keyword as a variable name for example keywords like **class, for, def, del, is, else,** **try, from,** etc. more examples are given below and as we go through the course we will come across many more. Creating names that are descriptive of the values often will help you avoid using any of these words."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Allowed variable names\n",
    "\n",
    "x=2\n",
    "y=\"Hello\"\n",
    "mypython=\"PythonGuides\"\n",
    "my_python=\"PythonGuides\"\n",
    "_my_python=\"PythonGuides\"\n",
    "_mypython=\"PythonGuides\"\n",
    "MYPYTHON=\"PythonGuides\"\n",
    "myPython=\"PythonGuides\"\n",
    "myPython7=\"PythonGuides\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-23-23d4199b4438>, line 3)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-23-23d4199b4438>\"\u001b[1;36m, line \u001b[1;32m3\u001b[0m\n\u001b[1;33m    7mypython=\"PythonGuides\"\u001b[0m\n\u001b[1;37m            ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "#Variable name not Allowed\n",
    "\n",
    "7mypython=\"PythonGuides\"\n",
    "-mypython=\"PythonGuides\"\n",
    "myPy@thon=\"PythonGuides\"\n",
    "my Python=\"PythonGuides\"\n",
    "for=\"PythonGuides\"\n",
    "\n",
    "#It shows invalid syntax. \n",
    "#It will execute one by one and will show the error."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Integers and Floats:\n",
    "##### Working with numeric data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Arithmetic Operators:\n",
    "#### Addition:           7+5\n",
    "#### Subtraction:     7-5\n",
    "#### Multiplication:  7*5\n",
    "#### Division:           7/5 \n",
    "#### Floor Division: 7//5 -> Drops decimal value\n",
    "#### Exponent:         7**5\n",
    "#### Modulus:           7%5 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "11"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "abs(-11) #Returns absolute value of integer data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "num = 1\n",
    "num = num+1\n",
    "num += 1\n",
    "print(num)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "round(8.63) # round to nearest integer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8.6"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "round(8.63,1) #rounds till first decimal point"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Comparison Operators:\n",
    "#### Equal:                   7==5\n",
    "#### Not Equal:            7!=5\n",
    "#### Greater than:       7>5\n",
    "#### Less than:            7<5 \n",
    "#### Greater or Equal: 7>=5\n",
    "#### Less or Equal:      7<=5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "num_1 = 7\n",
    "num_2 = 5\n",
    "print(num_1 == num_2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
