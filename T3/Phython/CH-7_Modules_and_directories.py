{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "98b11d10-c66b-4891-b958-cb6fe3f6d2dd",
   "metadata": {},
   "source": [
    "# MODULES AND DIRECTORIES"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "61a2b3c7-cb2c-46c6-a675-9fad00cffd7b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "625"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import Module2 as m\n",
    "m.mult(25,25)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "4346ce39-4c46-4cfc-b170-2e63aa42357c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "625"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from Module2 import mult\n",
    "mult(25,25)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "eb41d5a7-d89c-4386-a3b6-59cb1e2a79e7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "625\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "50"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from Module2 import mult as m,add as a \n",
    "print(m(25,25))\n",
    "a(25,25)\n",
    "a=[]\n",
    "a.append"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "34c7f028-9cbd-4dbd-bfca-a0462ad441c0",
   "metadata": {},
   "source": [
    "#### WAP to create a module named marks which has attributes like name , roll number, batch and branch and has methods marks of t1 to t4 of each subject and total Spi marks are to be added by the user consider three subjects"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "dc9e960f-8360-429b-a454-45a672ec1025",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Overwriting marks.py\n"
     ]
    }
   ],
   "source": [
    "%%writefile marks.py\n",
    "Name=None\n",
    "R_N=None\n",
    "Branch=None\n",
    "Batch=None\n",
    "def details():\n",
    "    global Name,R_N,Branch,Batch\n",
    "    Name=input(\"Enter your Name\")\n",
    "    R_N=input(\"Enter your roll Number\")\n",
    "    Branch=input(\"Enter your branch name\")\n",
    "    Batch=input(\"Enter your Batch\")\n",
    "def marks():\n",
    "    DE=[]\n",
    "    Python=[]\n",
    "    FSD=[]\n",
    "    for i in range(4):\n",
    "        de=int(input(f\"Enter marks of DE of T{i+1}\"))\n",
    "        DE.append(de)\n",
    "        py=int(input(f\"Enter marks of Python of T{i+1}\"))\n",
    "        Python.append(py)\n",
    "        fsd=int(input(f\"Enter marks of FSD of T{i+1}\"))\n",
    "        FSD.append(fsd)\n",
    "    return([DE,Python,FSD])\n",
    "def SPI(Marks_in):\n",
    "    global Name,R_N,Branch,Batch\n",
    "    print(f\"\\n\\n\\nYour name is {Name}\")\n",
    "    print(f\"\\nYour Roll Number is {R_N}\")\n",
    "    print(f\"\\nYour Branch is {Branch}\")\n",
    "    print(f\"\\nYour Batch is {Batch}\")\n",
    "    print(f\"\\n\\npercentage of each subject is   {(sum(Marks_in[0]))}\")\n",
    "    print(f\"\\npercentage of each subject is   {sum(Marks_in[1])}\")\n",
    "    print(f\"\\npercentage of each subject is   {sum(Marks_in[2])}\")\n",
    "    print(f\"\\nToatl percenatge    {((sum(Marks_in[0])+sum(Marks_in[1])+sum(Marks_in[2]))/300)*100:0.2f}\\n\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "fce1760c-9771-4164-8915-c9e4f079f606",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your Name HP\n",
      "Enter your roll Number 128\n",
      "Enter your branch name AIML\n",
      "Enter your Batch C3\n",
      "Enter marks of DE of T1 24\n",
      "Enter marks of Python of T1 23\n",
      "Enter marks of FSD of T1 21\n",
      "Enter marks of DE of T2 23\n",
      "Enter marks of Python of T2 21\n",
      "Enter marks of FSD of T2 24\n",
      "Enter marks of DE of T3 25\n",
      "Enter marks of Python of T3 23\n",
      "Enter marks of FSD of T3 21\n",
      "Enter marks of DE of T4 24\n",
      "Enter marks of Python of T4 22\n",
      "Enter marks of FSD of T4 1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "\n",
      "Your name is HP\n",
      "\n",
      "Your Roll Number is 128\n",
      "\n",
      "Your Branch is AIML\n",
      "\n",
      "Your Batch is C3\n",
      "\n",
      "\n",
      "percentage of each subject is   96\n",
      "\n",
      "percentage of each subject is   89\n",
      "\n",
      "percentage of each subject is   67\n",
      "\n",
      "Toatl percenatge    84.0\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import marks\n",
    "marks.details()\n",
    "MAR=marks.marks()\n",
    "marks.SPI(MAR)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b27b751b-713f-4772-b812-55e447045ad6",
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
    "import random\n",
    "print(random.randint(0,9))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "857d65a3-0125-47d6-a293-fb499745784b",
   "metadata": {},
   "source": [
    "# WAP TO CREATE AN OTP FOR A USER HAS WHICH IS OF 6 CHARACTER HAVING integer value at even place and Alphabet At odd place using random library "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "87bcdb57-ad42-4b88-ac6e-50cb20fd7dcf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<generator object OTP.<locals>.<genexpr> at 0x000001924FD30F40>"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def OTP():\n",
    "    A=list()\n",
    "    STR=\"\"\n",
    "    for i in range(10):\n",
    "        for k in range(6):\n",
    "            if k%2==0:\n",
    "                STR+=str(random.randint(0,9))\n",
    "            else:\n",
    "                STR+=chr(random.randint(97,123) or random.randint(65,91))\n",
    "        A.append(STR)\n",
    "        STR=\"\"\n",
    "    return(i for i in A)\n",
    "OTP()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "1b2cd2b6-bc5d-41c9-92df-e9328a6f57ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "d18419d2-577d-4f91-aff9-be4089b828e4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "datetime.datetime(2025, 12, 4, 10, 44, 11, 261900)"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "datetime.datetime.now()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "74ed1b51-24c9-4775-ab96-612482a92368",
   "metadata": {},
   "outputs": [],
   "source": [
    "from datetime import time\n",
    "t = time(23,50,0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "44e547b5-6a08-4527-a11e-32ec8362cbdc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'datetime.time'>\n"
     ]
    }
   ],
   "source": [
    "print(type(t))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "5e191534-90d4-45dc-ae40-6502ee316027",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'int'>\n"
     ]
    }
   ],
   "source": [
    "print(type(t.second))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "82604b0b-1c52-4b00-844d-c8d87f71fb9a",
   "metadata": {},
   "outputs": [],
   "source": [
    "from datetime import date\n",
    "D = date(2025,12,9)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "0f5dc958-4c49-47f8-af51-57e8f3ab5cfa",
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
    "print(D.month)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "498b60aa-236e-4c72-add3-eef5e4eb45d7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your password ········\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "correct password\n"
     ]
    }
   ],
   "source": [
    "import getpass as gp\n",
    "Pass=gp.getpass(prompt=\"Enter your password\")\n",
    "if Pass=='abc' :\n",
    "    print(\"correct password\")\n",
    "else:\n",
    "    print(\"Incorrect password\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "049f1388-ce86-4536-8ab4-b4686dca5bbf",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os as opsys"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "fc3c2777-0c52-4615-bd36-803bc12c9e7a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "C:\\STUDY\\T3\\Phython\n"
     ]
    }
   ],
   "source": [
    "OS=opsys.getcwd() #current working directory \n",
    "print(OS)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "61bfc074-4188-45ff-8400-a0def790f234",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\STUDY\\\\T3\\\\Phython'"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pwd # present working directory"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "ff7f55a1-4815-456c-b320-40a6fd315ea5",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "unterminated string literal (detected at line 1) (735819690.py, line 1)",
     "output_type": "error",
     "traceback": [
      "  \u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[28]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[31m    \u001b[39m\u001b[31m'It's a nice day'\u001b[39m\n                    ^\n\u001b[31mSyntaxError\u001b[39m\u001b[31m:\u001b[39m unterminated string literal (detected at line 1)\n"
     ]
    }
   ],
   "source": [
    "'It's a nice day'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "aad4b790-cf42-45d8-a4a4-0dba35a5fc89",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"It's a nice day\""
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'It\\'s a nice day'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8f26497f-7d33-4487-bafb-d0ea27b018f2",
   "metadata": {},
   "outputs": [],
   "source": [
    "opsys.mkdir(\"ABCDEF\")# for creating directory "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "cc999445-9240-4396-94ef-a2a772e031ce",
   "metadata": {},
   "outputs": [],
   "source": [
    "opsys.rmdir(\"ABCDEF\")# for removing directory "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "dc81dd29-c63d-4a5d-a630-fd183af822f0",
   "metadata": {},
   "outputs": [],
   "source": [
    "opsys.chdir(\"C:\\\\STUDY\\\\T3\\\\Phython\\\\ABCDEF\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "797bf73a-a322-43ac-b4d4-0b3e11974916",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\STUDY\\\\T3\\\\Phython\\\\ABCDEF'"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "opsys.getcwd()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "f545e7de-4e1d-4640-8d13-0d1379b49096",
   "metadata": {},
   "outputs": [],
   "source": [
    "opsys.remove(\"abc.txt\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "4116b795-6419-4354-9c84-e8793cf760b6",
   "metadata": {},
   "outputs": [],
   "source": [
    "opsys.mkdir(\"AB\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "0afe3bb3-0edf-4248-9c26-2c2a80d58b8d",
   "metadata": {},
   "outputs": [],
   "source": [
    "opsys.rename(\"AB\",\"AABBC\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "09cac5cc-9941-4dcc-a311-ea591ed003de",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['.ipynb_checkpoints',\n",
       " 'AABBC',\n",
       " 'abc.txt',\n",
       " 'alice_in_wonderland.txt',\n",
       " 'big.txt',\n",
       " 'CH-6.ipynb',\n",
       " 'CH-7_Modules_and_directories.ipynb',\n",
       " 'file1.txt',\n",
       " 'file10.txt',\n",
       " 'file11.txt',\n",
       " 'file12.txt',\n",
       " 'file13.txt',\n",
       " 'file14.txt',\n",
       " 'file15.txt',\n",
       " 'file16.txt',\n",
       " 'file17.txt',\n",
       " 'file18.txt',\n",
       " 'file19.txt',\n",
       " 'file2.txt',\n",
       " 'file3.txt',\n",
       " 'file5.txt',\n",
       " 'File6.txt',\n",
       " 'file8.txt',\n",
       " 'file9.txt',\n",
       " 'marks.py',\n",
       " 'Module2.py',\n",
       " 'PH-2',\n",
       " 'Untitled.ipynb',\n",
       " '__pycache__']"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "opsys.listdir()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "58d26a93-be1b-40f5-9b60-ea1a8069301b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "6f96a408-bb16-4ecd-94bf-a1fe77298dab",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)]'"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sys.version"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "8b9f42c0-8eab-4ea9-8b46-7d2d017f6b5c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9223372036854775807"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sys.maxsize"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "8137497a-b778-489b-b6bb-aa7ac5dc4af6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['C:\\\\Users\\\\harsh\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python312\\\\python312.zip',\n",
       " 'C:\\\\Users\\\\harsh\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python312\\\\DLLs',\n",
       " 'C:\\\\Users\\\\harsh\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python312\\\\Lib',\n",
       " 'C:\\\\Users\\\\harsh\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python312',\n",
       " '',\n",
       " 'C:\\\\Users\\\\harsh\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python312\\\\Lib\\\\site-packages',\n",
       " 'C:\\\\Users\\\\harsh\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python312\\\\Lib\\\\site-packages\\\\win32',\n",
       " 'C:\\\\Users\\\\harsh\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python312\\\\Lib\\\\site-packages\\\\win32\\\\lib',\n",
       " 'C:\\\\Users\\\\harsh\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python312\\\\Lib\\\\site-packages\\\\Pythonwin']"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sys.path"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.12.10"
  },
  "widgets": {
   "application/vnd.jupyter.widget-state+json": {
    "state": {},
    "version_major": 2,
    "version_minor": 0
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
