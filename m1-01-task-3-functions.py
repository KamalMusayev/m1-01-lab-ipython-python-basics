{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "17564a07-131c-48a3-9fac-6fe54b5db14d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Float results: [10.0, 3.14, None, None, 7.0]\n",
      "Cleaned strings: ['10', '3.14', 'Abc', '', '7']\n"
     ]
    }
   ],
   "source": [
    "def string_float(s):\n",
    "    try:\n",
    "        return float(s)\n",
    "    except ValueError:\n",
    "        return None\n",
    "\n",
    "def string_cleaning(text):\n",
    "    return text.strip().title()\n",
    "\n",
    "test_inputs = [\"10\", \"3.14\", \"abc\", \"\", \"  7  \"]\n",
    "\n",
    "\n",
    "\n",
    "float_results = [string_float(x) for x in test_inputs]\n",
    "\n",
    "clean_results = [string_cleaning(x) for x in test_inputs]\n",
    "\n",
    "print(\"Float results:\", float_results)\n",
    "print(\"Cleaned strings:\", clean_results)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2d071dc4-376a-4aa9-9460-e18fee940ea5",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.13.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
