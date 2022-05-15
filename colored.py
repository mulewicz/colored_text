{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "47803410",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[38;2;120;120;120mHello, World \u001b[38;2;255;255;255m\n"
     ]
    }
   ],
   "source": [
    "def colored(r, g, b, text):\n",
    "    return \"\\033[38;2;{};{};{}m{} \\033[38;2;255;255;255m\". format(r, g, b, text)\n",
    "text = 'Hello, World'\n",
    "colored_text = colored(120, 120, 120, text)\n",
    "print(colored_text)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "08d271c1",
   "metadata": {},
   "source": [
    " (1, 1, 1,)\n",
    "\n",
    "*red, green, blue*\n",
    "\n",
    "nice colors:\n",
    "* **blue** = 59, 142, 234\n",
    "* **pink** = 200, 170, 210\n",
    "* **purple** = 160, 100, 200\n",
    "* **green** = 70, 150, 20\n",
    "* **yellow** = 250, 204, 30\n",
    "* **orange** = 250, 150, 20\n",
    "* **grey** = 20, 120, 120\n",
    "\n",
    "pastels:\n",
    "* **blue** = 70, 150, 20\n",
    "* **green** = 70, 150, 20\n",
    "* **purple** = 170, 170, 250\n",
    "\n",
    "also:\n",
    "* **BLACK** = one of numbers is 260\n",
    "* **WHITE** = 255, 255, 255"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f6aa33de",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
